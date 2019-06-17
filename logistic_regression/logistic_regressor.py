from cmath import exp


def sigmoid(z):
    return 1.0 / float(1.0 + exp(-z))


class MyLogisticRegression:
    def __init__(self, max_iter=1000):
        self.max_iter = max_iter

    def fit(self):
        return

    def predict(self):
        return

    def score(self):
        return

