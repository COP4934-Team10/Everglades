# EvgMapNode
**This is the class of the nodes that make up the Everglades map.**

## Variables
|Type                       |Variable           |Description                                                                                                                                        |
|---------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|*int*                      |**ID**             |The identification number of the node.                                                                                                             |
|*float*                    |**radius**         |The radius of the node.                                                                                                                            |
|*list\<string>*            |**resource**       |A list of the resources for the node. It contains ‘OBSERVE’ for watchtower, ‘DEFENSE’ for fortress, and an empty list for a node with no resources.|
|*int*                      |**defense**        |The defense value for the node.                                                                                                                    |
|*int*                      |**controlPoints**  |The amount of points a player receives for controlling the node.                                                                                   |
|*int*                      |**teamStart**      |Indicates the node is a team’s home base. It is 0 for player 0, 1 for player 1, and -1 for all neutral nodes.                                      |
|*int*                      |**controlledBy**   |Indicates which player controls the node. It uses the same integer values as teamStart.                                                            |
|*int*                      |**controlState**   |This is the percentage that the node is under control.                                                                                             |
|*list\<EvgNodeConnections>*|**connections**    |The list of tuples containing valid connections from this node and the respective distances.                                                       |
|*list\<int>*               |**connection_idxs**|The list of valid connections from this node.                                                                                                      |
|*dict*                     |**groups**         |The key is the player number (0 or 1) and the value is a list of group IDs for groups located at this node.                                        |
