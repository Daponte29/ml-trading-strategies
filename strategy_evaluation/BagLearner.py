"""Bootstrap aggregation learner used by StrategyLearner."""

import numpy as np
from scipy import stats


class BagLearner(object):
    def __init__(self, learner, kwargs=None, bags=20, boost=False, verbose=False):
        if kwargs is None:
            kwargs = {"leaf_size": 1}
        self.bags = bags
        self.boost = boost
        self.verbose = verbose
        self.learners = [learner(**kwargs) for _ in range(bags)]

    def add_evidence(self, dataX, dataY):
        rows = dataX.shape[0]
        for learner in self.learners:
            idx = np.random.randint(0, rows, rows)
            learner.add_evidence(dataX[idx], dataY[idx])

    def query(self, points):
        preds = np.array([learner.query(points) for learner in self.learners])
        mode_vals, _ = stats.mode(preds, axis=0)
        return mode_vals.flatten()

    def author(self):
        return "ndaponte3"

    def study_group(self):
        return "ndaponte3"
