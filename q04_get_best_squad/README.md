# Finding Best Squad


## Write a function `q04_get_best_squad` that:
- Takes in the list of positions for which the best squad is to be known.
- Works on calling previous function (`q02_Convert`) value.
- Splits the Data points in column named as `Preferred Positions` and rename it to as `Preferred Position`.
- Iterates over positions and finds out maximum value of the column `Overall` along with its `Preferred Position` and name of the player.


### Parameters
- list: list of positions for which the best squad is to be known

### Returns
- DataFrame with columns named as 'Position', 'Player' and 'Overall'. `dtype: DataFrame`
 