import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score


from q02_Convert.build import q02_Convert

dataset = q02_Convert()


def q08_polynomial():
    "write your solution here"
   
