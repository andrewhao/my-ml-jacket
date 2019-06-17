from math import exp, e as E, log


def sigmoid(z):
    return 1.0 / float(1.0 + exp(-z))


def cost_function(x, y, theta):
    return y * log(hypothesis(x, theta), E) + \
           (1 - y) * log(1 - hypothesis(x, theta), E)


def derivative_cost_function():
    return


def hypothesis(x, theta):
    return sigmoid(theta * x)


class MyLogisticRegression:
    def __init__(self, max_iter=1000):
        self.max_iter = max_iter

    def fit(self):
        return self

    def predict(self):
        return []

    def score(self):
        return
