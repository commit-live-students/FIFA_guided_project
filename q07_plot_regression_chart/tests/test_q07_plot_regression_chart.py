
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q07_plot_regression_chart
from inspect import getfullargspec
from q06_regression.build import q06_regression

X, y, y_pred, a, b, c = q06_regression()

q07_plot_regression_chart(40, 100, 0, 130, 'black', X, y, y_pred)


class Test_fifa_plot(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q07_plot_regression_chart).args
        self.assertEqual(len(arg), 8, "Expected argument(s) %d, Given %d" % (8, len(arg)))

