
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q03_growth_potential
from inspect import getfullargspec


print(q03_growth_potential())


class Test_fifa_plot(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q03_growth_potential).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

