
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q05_feature_correlation
from inspect import getfullargspec


q05_feature_correlation()


class Test_fifa_plot(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q05_feature_correlation).args
        self.assertEqual(len(arg), 0, "Expected argument(s) %d, Given %d" % (0, len(arg)))

