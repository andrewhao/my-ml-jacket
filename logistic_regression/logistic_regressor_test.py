import unittest
import pandas as pd
from logistic_regression.logistic_regressor import MyLogisticRegression


class LogisticRegressorTestCase(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv('./data2.csv')
        self.subject = MyLogisticRegression()

    def test_init(self):
        self.assertIsInstance(self.subject, MyLogisticRegression)

    def test_fit(self):
        self.assertEqual(self.subject.fit(), self.subject)

    def test_predict(self):
        self.assertEqual(self.subject.predict(), [])
