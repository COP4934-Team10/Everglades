# EvergladesEnv
**This class contains the OpenAI Gym and is the Everglades environment.**

## Variables
|Type               |Variable                   |                       Description                                 |
|-------------------|---------------------------|-------------------------------------------------------------------|
|*Tuple*            |**action_space**           |This defines the range of actions an agent may take.               |
|*bool*             |**debug**                  |This flag allows the masking of fog of war for debugging purposes. |
|*EvergladesGame*   |**game**                   |This is an instance of the Everglades game.                        |
|*int*              |**num_actions_per_turn**   |The number of actions a player may take per turn.                  |
|*int*              |**num_groups**             |The number of groups per player.                                   |
|*int*              |**num_nodes**              |The number of nodes in the map.                                    |
|*int*              |**num_turns**              |The number of turns in a game.                                     |
|*int*              |**num_units**              |The total number of units per player.                              |
|*Box*              |**observation_space**      |This defines the boundaries of observation.                        |
|*list<dict_keys>*  |**pks**                    |The list of keys for the player dictionary.                        |
|*dict*             |**player_dat**             |This contains the unit groups for each player.                     |
|*dict*             |**players**                |This contains an instance of the agent class for each player.      |
|*list<dict_keys>*  |**sorted_pks**             |The sorted list of keys for the player dictionary.                 |
|*list*             |**unit_classes**           |The types of units in the game.                                    |

## Methods
[**_build_groups()**](../Methods/_build_groups().md)  
[**_build_observations()**](../Methods/_build_observations().md)  
[**_build_observation_space()**](../Methods/_build_observation_space().md)  
[**close()**](../Methods/close().md)  
[**render()**](../Methods/render().md)  
[**reset()**](../Methods/reset().md)  
[**step()**](../Methods/step().md)  