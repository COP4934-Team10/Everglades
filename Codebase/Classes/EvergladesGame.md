# EvergladesGame
**This class contains the logic of the Everglades game.**

## Variables
|Type                       |Variable               |Description                                                                                                                                            |
|---------------------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|  
|*vectorize*                |**_vec_convert_node**  |Vectorized version of _convert_node function.                                                                                                          |
|*int*                      |**current_turn**       |The current turn in the game.                                                                                                                          |
|*string*                   |**dat_dir**            |Folder name containing that game instance’s telemetry files.                                                                                           |
|*bool*                     |**debug**              |This flag allows the masking of fog of war for debugging purposes.                                                                                     |
|*EvgMap*                   |**evgMap**             |This is an instance of the Everglades map.                                                                                                             |
|*list\<int>*               |**focus**              |List of group IDs on which to focus.                                                                                                                   |
|*int*                      |**fort_bonus**         |Fortress defense multiplier.                                                                                                                           |
|*Map*                      |**map_dat**            |This contains the map data read from the configuration file.                                                                                           |
|*ndarray\<int>*            |**map_key1**           |Length is the number of map nodes. Array sorted by index of evgMap node and populated by node IDs.                                                     |
|*ndarray\<int>*            |**map_key2**           |Length is the number of map nodes. Array sorted by node ID and populated by indices of evgMap nodes.                                                   |
|*dict*                     |**output**             |Key is name of telemetry file. Value is the data for that telemetry file. Also contains a header.                                                      |
|*string*                   |**output_dir**         |The destination directory for telemetry output.                                                                                                        |
|*list\<int>*               |**p1_node_map**        |Array of node IDs from player 1 perspective.                                                                                                           |
|*dict*                     |**player_names**       |This contains the names of the agent modules.                                                                                                          |
|*dict*                     |**players**            |The key is the player key (0 or 1). The value is an instance of EvgPlayer.                                                                             |
|*dict*                     |**team_starts**        |Contains team’s starting nodes, pulled from map_dat, which got it from the map json file. 0 = player 1 start, 1 = player 2 start, -1 = neutral nodes.  |
|*int*                      |**total_groups**       |Total amount of groups in the game.                                                                                                                    |
|*int*                      |**total_units**        |Total amount of units in the game.                                                                                                                     |
|*Units*                    |**unit_dat**           |Read Unit data from .json file. Contains the types and stats of the units (health, damage, speed, etc.).                                               |
|*dict*                     |**unit_ids**           |Key is int uid, the order that the types were processed, starting at 0. Value is unit_type.                                                            |
|*dict*                     |**unit_names**         |Key is unit_type. Value is int uid, the order that the types were processed, starting at 0.                                                            |
|*list\<EvgUnitDefinition>* |**unit_types**         |List of each type of unit with respective stats as retrieved from the .json file.                                                                      |
|*int*                      |**watch_bonus**        |Watchtower vision bonus.                                                                                                                               |





## Methods
[_convert_node()](../Methods/_convert_node().md)  
[board_init()](../Methods/board_init().md)  
[board_state()](../Methods/board_state().md)  
[build_knowledge_output()](../Methods/build_knowledge_output().md)  
[capture()](../Methods/capture().md)  
[combat()](../Methods/combat().md)  
[debug_state()](../Methods/debug_state().md)  
[game_end()](../Methods/game_end().md)  
[game_init()](../Methods/game_init().md)  
[game_turn()](../Methods/game_turn().md)  
[movement()](../Methods/movement().md)  
[output_init()](../Methods/output_init().md)  
[player_state()](../Methods/player_state().md)  
[unitTypes_init()](../Methods/unitTypes_init().md)  
[write_output()](../Methods/write_output().md)  
