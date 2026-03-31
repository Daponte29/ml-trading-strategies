"""Stacked bagged linear regression learner."""

import numpy as np
import LinRegLearner as lrl
import BagLearner as bl


class InsaneLearner(object):
    """An ensemble of bagging learners, each wrapping linear regression."""

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.learners = [
            bl.BagLearner(
                learner=lrl.LinRegLearner,
                kwargs={},
                bags=20,
                boost=False,
                verbose=False,
            )
            for _ in range(20)
        ]

    def add_evidence(self, data_x, data_y):
        for learner in self.learners:
            learner.add_evidence(data_x, data_y)

    def query(self, points):
        predictions = np.array([learner.query(points) for learner in self.learners])
        return np.mean(predictions, axis=0)

    def author(self):
        return "ndaponte3"

    def study_group(self):
        return "ndaponte3"
