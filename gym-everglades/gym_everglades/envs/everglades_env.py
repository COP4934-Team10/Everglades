import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.spaces import Tuple, Discrete, Box

import everglades_server.server as server

import numpy as np
import pdb
import json

class EvergladesEnv(gym.Env):

    def __init__(self):
        # Game parameters
        self.num_turns = 150
        self.num_units = 100
        self.num_groups = 12
        self.num_nodes = 11
        self.num_actions_per_turn = 7
        self.unit_classes = ['controller', 'striker', 'tank']

        # Define the action space
        self.action_space = Tuple((Discrete(self.num_groups), Discrete(self.num_nodes + 1)) * self.num_actions_per_turn)

        # Define the state space
        self.observation_space = self._build_observation_space()

        return

    def step(self, actions):

        scores, status = self.game.game_turn(actions)
        observations = self._build_observations()

        reward = {i:0 for i in self.players}
        done = 0 
        if status != 0:
            done = 1
            if scores[0] != scores[1]:
                reward[0] = 1 if scores[0] > scores[1] else -1
                reward[1] = reward[0] * -1 # flip the sign
            # else reward is 0 for a tie
            print(scores)
        # end status done check
        print(status)

        # return state, reward, done, info
        return observations, reward, done, {}

    def reset(self, **kwargs):
    # kwargs is allowed. https://github.com/openai/gym/blob/master/gym/core.py
        # Get Players
        self.players = kwargs.get('players')
        config_dir = kwargs.get('config_dir')
        map_file = kwargs.get('map_file')
        unit_file = kwargs.get('unit_file')
        group_file = kwargs.get('group_file')
        output_dir = kwargs.get('output_dir')
        player_names = kwargs.get('pnames')
        self.debug = kwargs.get('debug',False)

        # Input validation
        assert( len(self.players) == 2 ), 'Must have exactly two players' # for now
        self.pks = self.players.keys()
        self.sorted_pks = sorted(self.pks)
        self.player_dat = {}
        for i in self.pks:
            self.player_dat[i] = {}
            
            # The commented code below can be used to allow the individual agents to specify their
            # unit configurations if the agent specifies a dictionary with group number as key
            # and an array of tuples as values. The tuples consist of ('UnitType', count). The
            # format would be:
            # self.unit_configs = {1: [('Striker', 5), ('Tank', 3)], 2:........}
            # Just make sure to comment out the code from the json file load unil the
            # Initialize game call. Also, uncomment the _build_groups function, which
            # provides a default configuration if the agent does not specify one.

            # Check if agent provided unit configuration and, if so, use it.
            ## If not, use default.
            #if hasattr(self.players[i], 'unit_config'):
            #    self.player_dat[i]['unit_config'] = self.players[i].unit_config
            #else:
            #    self.player_dat[i]['unit_config'] = self._build_groups(i)

            # Load in groups from json configuration file
            with open(group_file) as fid:
                group_dat = json.load(fid)
            
            # Dict to hold unit configurations for player with the gid as the key
            self.player_dat[i]['unit_config'] = {}

            # Loop through each group in the file
            for gid, group in enumerate(group_dat['groups']):
                # A list to hold (unitType, count) tuples for each group
                unitsInGroup = []
                
                # Loop through each unit type and add to list
                for unitType in group['units']:
                    pair = (unitType['Type'], unitType['Count'])
                    unitsInGroup.append(pair)
                # Add the group to the player's unit configuration
                self.player_dat[i]['unit_config'][gid] = unitsInGroup

        # Initialize game
        self.game = server.EvergladesGame(
                config_dir = config_dir,
                map_file = map_file,
                unit_file = unit_file,
                output_dir = output_dir,
                pnames = player_names,
                debug = self.debug
        )
        
        # Initialize players with selected groups
        self.game.game_init(self.player_dat)

        # Get first game state
        observations = self._build_observations()
        #pdb.set_trace()

        return observations

    def render(self, mode='human'):
        pass

    def close(self):
        pass

    def _build_observation_space(self):
        group_low = np.array([1, 0, 0, 0, 0])  # node loc, class, avg health, in transit, num units rem
        group_high = np.array([self.num_nodes, len(self.unit_classes), 100, 1, self.num_units])

        group_state_low = np.tile(group_low, self.num_groups)
        group_state_high = np.tile(group_high, self.num_groups)

        control_point_portion_low = np.array([0, 0, -100, -1])  # is fortress, is watchtower, percent controlled, num opp units
        control_point_portion_high = np.array([1, 1, 100, self.num_units])

        control_point_state_low = np.tile(control_point_portion_low, self.num_nodes)
        control_point_state_high = np.tile(control_point_portion_high, self.num_nodes)

        observation_space = Box(
            low=np.concatenate([[1], control_point_state_low, group_state_low]),
            high=np.concatenate([[self.num_turns + 1], control_point_state_high, group_state_high])
        )
        #pdb.set_trace()

        return observation_space


    #def _build_groups(self, player_num):
    #    unit_configs = {}

    #    num_units_per_group = int(self.num_units / self.num_groups)
    #    for i in range(self.num_groups):
    #        unit_type = self.unit_classes[i % len(self.unit_classes)]
    #        if i == self.num_groups - 1:
    #            unit_configs[i] = [(unit_type, self.num_units - sum([c[0][1] for c in unit_configs.values()]))]
    #        else:
    #            unit_configs[i] = [(unit_type, num_units_per_group)]
    #    return unit_configs

    def _build_observations(self):
        observations = {}

        for player in self.players:
            board_state = self.game.board_state(player)
            player_state = self.game.player_state(player)

            state = np.zeros(board_state.shape[0] + player_state.shape[0] - 1)
            state[0:board_state.shape[0]] = board_state
            state[board_state.shape[0]:] = player_state[1:]

            observations[player] = state

        return observations

# end class EvergladesEnv

if __name__ == '__main__':
    test_env = EvergladesEnv()
