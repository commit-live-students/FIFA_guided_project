# Introducing Polynomial function to linear regression


## Write a function `q08_polynomial` that:
- Works on calling previous function (`q02_Convert`) value and makes use of the dataframe it returns.
- Assigns Independent variable as `Overall`and dependent variable as `Value (M)` and reshapes the dimension of values to (-1,1)
- Fit transforms the data using function `PolynomialFeatures` with degree as 2.
- Fits the linear regression model on previously created polynomial function and predicts the dependent variable.

### Parameters
- This Function takes nothing as input parameter.

### Returns

| Return | dtype | description |
| --- | --- | --- |
|var1 | numpy.ndarray | Coefficient value computed by model  |
|var2 | numpy.float64 | Mean absolute error |
|var3 | numpy.float64 | R-squared |
|var4 | numpy.ndarray |Independent variable  |
|var5 | numpy.ndarray | Dependent variable |
|var6| numpy.ndarray | Predicted values |

 