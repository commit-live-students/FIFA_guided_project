# Data Pre-processing

After loading the required data into structured format next step is to cleanse the data according to the needs
which can be later on fed to the model. This assignment helps you to achieve that particular task.

## Write a function `q02_Convert` that:

- Removes the symbol K, €, M from the column named as `Value` and `Wage`.
- Renames columns to `Value (M)` and `Wage (M)`.
- Changes their data-type to float64.

### Parameters
- data: dataframe created with the help of previous function

### Returns
- DataFrame with necessary operations applied. `dtype: DataFrame`
 