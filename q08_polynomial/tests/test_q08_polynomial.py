import os
import sys
import numpy

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q08_polynomial
from inspect import getfullargspec

coef, mean_error, r2score, X_test, y_test, y_prediction,= q08_polynomial()


class Test_fifa_plot(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q08_polynomial).args
        self.assertEqual(len(arg), 0, "Expected argument(s) %d, Given %d" % (0, len(arg)))

    def test_coefficent_instance(self):
        self.assertIsInstance(coef, numpy.ndarray,
                              "The Expected return type does not match with the given return type")

    def test_mean_error_instance(self):
        self.assertIsInstance(mean_error, numpy.float64,
                              "The Expected return type does not match with the given return type")

    def test_r2score_instance(self):
        self.assertIsInstance(r2score, numpy.float64,
                              "The Expected return type does not match with the given return type")
    def test_training_features_instance(self):
        self.assertIsInstance(X_test, numpy.ndarray,
                              "The Expected return type does not match with the given return type")

    def test_training_label_instance(self):
        self.assertIsInstance(y_test, numpy.ndarray,
                              "The Expected return type does not match with the given return type")

    def test_prediction_instance(self):
        self.assertIsInstance(y_prediction, numpy.ndarray,
                              "The Expected return type does not match with the given return type")
