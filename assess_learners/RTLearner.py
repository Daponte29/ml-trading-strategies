"""Randomized decision tree learner for regression."""

import random

import numpy as np


class RTLearner(object):
    """A random-tree regressor using random split feature selection."""

    def __init__(self, leaf_size=1, verbose=False):
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.tree = None

    def author(self):
        return "ndaponte3"

    def study_group(self):
        return "ndaponte3"

    def add_evidence(self, data_x, data_y):
        """Train the learner with features and labels."""
        data = np.hstack((data_x, data_y.reshape(-1, 1)))
        self.tree = self._build_tree(data)

    def _build_tree(self, data):
        data_y = data[:, -1]
        if data.shape[0] <= self.leaf_size or len(data.shape) == 1:
            return np.array([["leaf", np.mean(data_y), -1, -1]])
        if np.all(data_y == data_y[0]):
            return np.array([["leaf", data_y[0], -1, -1]])

        best_i = random.randint(0, data.shape[1] - 2)
        split_val = np.median(data[:, best_i])
        if split_val == np.max(data[:, best_i]):
            return np.array([["leaf", np.mean(data_y), -1, -1]])

        left_tree = self._build_tree(data[data[:, best_i] <= split_val])
        right_tree = self._build_tree(data[data[:, best_i] > split_val])
        root = np.array([[best_i, split_val, 1, left_tree.shape[0] + 1]])
        return np.vstack((np.vstack((root, left_tree)), right_tree))

    def query(self, points):
        """Predict values for each row in points."""
        results = []
        tree = self.tree
        for i in range(points.shape[0]):
            node = 0
            while tree[node, 0] != "leaf":
                index = int(float(tree[node, 0]))
                split_val = float(tree[node, 1])
                if points[i, index] <= split_val:
                    node += int(float(tree[node, 2]))
                else:
                    node += int(float(tree[node, 3]))
            results.append(float(tree[node, 1]))
        return np.array(results)
