"""Deterministic decision tree learner for regression."""

import numpy as np
import numpy.ma as ma


class DTLearner(object):
    """A simple correlation-based decision tree regressor."""

    def __init__(self, leaf_size=1, verbose=False):
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.tree_structure = None

    def author(self):
        return "ndaponte3"

    def study_group(self):
        return "ndaponte3"

    def add_evidence(self, x, y):
        """Train the tree using feature matrix x and target vector y."""
        data = np.hstack((x, y.reshape(-1, 1)))
        self.tree_structure = self._build_tree(data)

    def _build_tree(self, data):
        y_vals = data[:, -1]

        if data.shape[0] <= self.leaf_size or len(data.shape) == 1:
            return np.array([["leaf", np.mean(y_vals), -1, -1]])
        if np.all(y_vals == y_vals[0]):
            return np.array([["leaf", y_vals[0], -1, -1]])

        best_feature = 0
        max_corr = -1
        for feature_idx in range(data.shape[1] - 1):
            corr = ma.corrcoef(
                ma.masked_invalid(data[:, feature_idx]),
                ma.masked_invalid(y_vals),
            )[0, 1]
            corr = abs(corr)
            if corr > max_corr:
                max_corr = corr
                best_feature = feature_idx

        split_value = np.median(data[:, best_feature])
        if split_value == np.max(data[:, best_feature]):
            return np.array([["leaf", np.mean(y_vals), -1, -1]])

        left_tree = self._build_tree(data[data[:, best_feature] <= split_value])
        right_tree = self._build_tree(data[data[:, best_feature] > split_value])
        root = np.array([[best_feature, split_value, 1, left_tree.shape[0] + 1]])
        return np.vstack((np.vstack((root, left_tree)), right_tree))

    def query(self, points):
        """Predict values for rows in points by traversing the learned tree."""
        predictions = []
        tree = self.tree_structure

        for point in points:
            node = 0
            while tree[node, 0] != "leaf":
                feature_idx = int(float(tree[node, 0]))
                split_value = float(tree[node, 1])
                if point[feature_idx] <= split_value:
                    node += int(float(tree[node, 2]))
                else:
                    node += int(float(tree[node, 3]))
            predictions.append(float(tree[node, 1]))

        return np.array(predictions)

