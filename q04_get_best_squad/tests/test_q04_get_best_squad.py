
import os
import sys
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q04_get_best_squad
from inspect import getfullargspec


# 4-3-3
squad_433 = ['GK', 'LB', 'CB', 'CB', 'RB', 'LM', 'CDM', 'RM', 'LW', 'ST', 'RW']

dataframe = q04_get_best_squad(squad_433)


class Test_fifa_setup(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q04_get_best_squad).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_data_to_df_return_instance(self):
        self.assertIsInstance(dataframe, pd.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(dataframe.shape, (11, 3),
                         "The Expected return shape does not match with the given return shape")
