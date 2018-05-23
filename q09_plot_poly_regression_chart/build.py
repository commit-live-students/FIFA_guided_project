import os
import sys

import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q08_polynomial.build import q08_polynomial
from q07_plot_regression_chart.build import q07_plot_regression_chart
from q02_Convert.build import q02_Convert

dataset = q02_Convert()
a, b, c1, X_2, y_2, y_2_pred = q08_polynomial()


def q09_plot_poly_regression_chart(X_2=X_2, y_2=y_2, y_2_pred=y_2_pred):
    "Write your solution here"
