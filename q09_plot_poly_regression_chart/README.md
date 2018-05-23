# Polynomial Regression Plot


## Write a function `q09_plot_poly_regression_chart` that :
- Works on calling previous function (`q02_Convert`) value and makes use of the dataframe it returns.
- Splits the Data points in column named as `Preferred Positions` and rename it to as `Preferred Position`.
- Maps a dictionary given below to the column created above as `Preferred Positions`.
- Calls up the function `q07_plot_regression_chart` and takes the input dependent , independent and predicted values returned
by `q08_polynomial` function.


- Below is the given dictionary:
color_dict = {'ST': 'red', 'CF': 'red', 'LW': 'red', 'RW': 'red',
                  'LM': 'blue', 'RM': 'blue', 'CM': 'blue', 'CAM': 'blue', 'CDM': 'blue',
                  'LB': 'green', 'RB': 'green', 'CB': 'green', 'LWB': 'green', 'RWB': 'green',
                  'GK': 'purple'}



### Parameters
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| X | numpy.ndarray | default | | Feature variable value returned by previous function (q08_polynomial) |
| y | numpy.ndarray | default | | Target Variable value returned by previous function (q08_polynomial) |
| y_pred | numpy.ndarray | default | | Prediction values value returned by previous function (q08_polynomial) |


### Returns

This function returns the plot


For plot image reference you can go through the link below:-
https://github.com/commit-live-students/FIFA_guided_project/blob/master/images/q09_plot_poly_regression_chart.png
