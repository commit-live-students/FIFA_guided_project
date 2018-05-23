# Regression Plot


## Write a function `q07_plot_regression_chart` that:
- Works on calling previous function (`q06_regression`) value.
- Overlays the scatter plot between Independent(X) and dependent variable(Y) used in linear regression model with 
line plot of Independent variable(X) and predicted values(y_pred).


### Parameters
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| x_l | int | compulsory | | Get or set the x limits of the current axes. |
| x_h |int | compulsory | | Get or set the x limits of the current axes. |
| y_l | int | compulsory | | Get or set the y limits of the current axes. |
| y_h | int | compulsory | | Get or set the y limits of the current axes. |
| c | String | compulsory | | Colour of the scatter plot data points |
| X | numpy.ndarray | default | | Feature Variable |
| y | numpy.ndarray | default | | Target Variable |
| y_pred | numpy.ndarray | default | | Prediction values |


### Returns

| Return | dtype | description |
| --- | --- | --- |
|var1 | numpy.ndarray |Independent variable  |
|var2 |numpy.ndarray | Dependent variable |
|var3| numpy.ndarray | Predicted values |
|var4 | numpy.ndarray | Coefficient value computed by model  |
|var5 | numpy.float64 | Mean absolute error |
|var6 | numpy.float64 | R-squared |


For plot image reference you can go through the link below:-

https://github.com/commit-live-students/FIFA_guided_project/blob/master/images/q07_plot_regression_chart.png
