
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q09_plot_poly_regression_chart
from inspect import getfullargspec


q09_plot_poly_regression_chart()


class Test_fifa_setup(TestCase):
    def test_fifa_to_df_args(self):
        arg = getfullargspec(q09_plot_poly_regression_chart).args
        self.assertEqual(len(arg), 3, "Expected argument(s) %d, Given %d" % (3, len(arg)))

