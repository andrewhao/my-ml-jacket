import unittest
import pandas as pd
from logistic_regression.logistic_regressor import MyLogisticRegression


class LogisticRegressorTestCase(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv('./data2.csv')

    def test_init(self):
        subject = MyLogisticRegression()
        self.assertIsInstance(subject, MyLogisticRegression)

    def test_fit(self):
        subject = MyLogisticRegression()
        self.assertEqual(subject.fit(), subject)

    