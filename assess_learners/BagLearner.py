"""Bootstrap aggregation learner."""

import numpy as np


class BagLearner(object):
    """Train multiple base learners on bootstrap samples and average predictions."""

    def __init__(self, learner, kwargs, bags, boost=False, verbose=False):
        self.bags = bags
        self.boost = boost
        self.verbose = verbose
        self.learners = [learner(**kwargs) for _ in range(bags)]

    def author(self):
        return "ndaponte3"

    def study_group(self):
        return "ndaponte3"

    def add_evidence(self, data_x, data_y):
        """Fit each bag on a bootstrap sample of the training set."""
        rows = data_x.shape[0]
        for learner in self.learners:
            sample_idx = np.random.choice(rows, size=rows, replace=True)
            learner.add_evidence(data_x[sample_idx], data_y[sample_idx])

    def query(self, points):
        """Average predictions across all bags."""
        predictions = [learner.query(points) for learner in self.learners]
        return np.mean(np.asarray(predictions), axis=0)
