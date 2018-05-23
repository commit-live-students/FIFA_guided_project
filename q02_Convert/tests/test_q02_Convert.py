import os
import sys
import pandas as pd


sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_Convert
from inspect import getfullargspec

data = q02_Convert()


class Test_fifa_setup(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q02_Convert).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_convert_df_return_instance(self):
        self.assertIsInstance(data, pd.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_convert_df_return_shape(self):
        self.assertEqual(data.shape, (17981, 11),
                         "The Expected return shape does not match with the given return shape")

    def test_convert_value(self):
        self.assertEqual(data['Value (M)'][1], 105.0,
                         "The Expected return value does not match with the given return value")

    def test_convert_wage(self):
        self.assertEqual(data['Wage (M)'][1], 565.0,
                         "The Expected return value does not match with the given return value")

