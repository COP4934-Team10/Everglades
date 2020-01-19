import os
import numpy as np
import time
import json

class random_actions:
    def __init__(self, action_space, player_num, map_name):
        self.action_space = action_space
        self.num_groups = 12
        
        with open('/everglades/config/' + map_name) as fid:
            self.map_dat = json.load(fid)

        self.nodes_array = []
        for i, in_node in enumerate(self.map_dat['nodes']):
            self.nodes_array.append(in_node['ID'])

        self.num_nodes = len(self.map_dat['nodes'])
        self.num_actions = action_space

        self.shape = (self.num_actions, 2)

    def get_action(self, obs):
        #print('!!!!!!! Observation !!!!!!!!')
        #print(obs)
        #print(obs[0])
        #for i in range(45,101,5):
        #    print(obs[i:i+5])
        #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        action = np.zeros(self.shape)
        action[:, 0] = np.random.choice(self.num_groups, self.num_actions, replace=False)
        action[:, 1] = np.random.choice(self.nodes_array, self.num_actions, replace=False)
        #print(action)
        return action


