# EvgGroup
**This is the class of a group of units.**

## Variables
|Type               |Variable               |Description                                                                                |
|-------------------|-----------------------|-------------------------------------------------------------------------------------------|
|*int*              |**groupID**            |The identification number for the group.                                                   |
|*int*              |**mapGroupID**         |A cumulative group identification for outputting the initial number of groups on the map.  |
|*int*              |**mapUnitID**          |A cumulative unit identification for outputting the initial number of units on the map.    |
|*int*              |**location**           |The node where the group is located.                                                       |
|*bool*             |**ready**              |This indicates if the group is ready to move.                                              |
|*bool*             |**moving**             |This indicates if the group is currently moving.                                           |
|*bool*             |**destroyed**          |This indicates if the group has been destroyed.                                            |
|*int*              |**distance_remaining** |The remaining distance the group must travel to reach the destination node.                |
|*int*              |**travel_destination** |The node to which the group is traveling.                                                  |
|*list\<EvgUnit>*   |**units**              |The list of units contained in the group.                                                  |
|*int*              |**pathIndex**          |This property is never referenced.                                                         |
