"""Random tree learner used by strategy evaluation bagging."""

import numpy as np


class RTLearner(object):
    def __init__(self, leaf_size=1, verbose=False):
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.tree = None

    def _build_tree(self, data):
        if data.shape[0] <= self.leaf_size:
            return np.array([["leaf", np.mean(data[:, -1]), -1, -1]], dtype=object)

        split_feature = np.random.randint(data.shape[1] - 1)
        if np.all(data[:, split_feature] == data[0, split_feature]):
            return np.array([["leaf", np.mean(data[:, -1]), -1, -1]], dtype=object)

        split_value = np.median(data[:, split_feature])
        left_mask = data[:, split_feature] <= split_value
        right_mask = data[:, split_feature] > split_value

        if not left_mask.any() or not right_mask.any():
            return np.array([["leaf", np.mean(data[:, -1]), -1, -1]], dtype=object)

        left_tree = self._build_tree(data[left_mask])
        right_tree = self._build_tree(data[right_mask])
        root = np.array([[split_feature, split_value, 1, left_tree.shape[0] + 1]], dtype=object)
        return np.vstack((root, left_tree, right_tree))

    def add_evidence(self, data_x, data_y):
        data = np.column_stack((data_x, data_y))
        self.tree = self._build_tree(data)

    def query(self, points):
        preds = []
        for point in points:
            row = 0
            while self.tree[row, 0] != "leaf":
                feature = int(self.tree[row, 0])
                split_val = float(self.tree[row, 1])
                if point[feature] <= split_val:
                    row += int(self.tree[row, 2])
                else:
                    row += int(self.tree[row, 3])
            preds.append(float(self.tree[row, 1]))
        return np.array(preds)

    def author(self):
        return "ndaponte3"

    def study_group(self):
        return "ndaponte3"
