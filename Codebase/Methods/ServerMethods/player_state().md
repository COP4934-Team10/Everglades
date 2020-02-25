# player_state()
This returns the state of a player's groups.

## Syntax
```python
player_state(int player_num)
```

## Returns
A numpy array. The first index is the turn number followed by five indices repeating
for each group the player has in the game. The indices are:

|Index          |Description                                            |
|---------------|-------------------------------------------------------|
|0              |Integer: The turn number.                              |
|index % 5 = 1  |Integer: The group's location as a node number.        |
|index % 5 = 2  |Integer: A number corresponding to the type of unit.   |
|index % 5 = 3  |Float: The average group health [0:100].               |
|index % 5 = 4  |Boolean: Whether the group is currently moving.        |
|index % 5 = 0  |Integer: The number of units alive in the group.       |

## Parameters
|Parameter      |Description        |
|---------------|-------------------|
|**player_num** |The player's key.  |