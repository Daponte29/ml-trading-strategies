#Libraries///////////////////
import numpy as np
import numpy.ma as ma
#///////////////////////////
#IMPORTANT NOTE: Summer 2024 Course Ratake Student Resubmission



class DTLearner(object):

    def __init__(self, leaf_size=1, verbose=False):
        self.leaf_size = leaf_size
        self.verbose = verbose

    def author(self):  
        return 'ndaponte3'
    
    def study_group(self):
        return 'ndaponte3'

    def add_evidence(self, X, y):
        data_combined = np.hstack((X, y.reshape(-1, 1)))
        self.tree_structure = self.build_tree(data_combined)

    def build_tree(self, data_combined):
        y_vals = data_combined[:, -1]
        if data_combined.shape[0] <= self.leaf_size or len(data_combined.shape) == 1:
            return np.array([['leaf', np.mean(y_vals), -1, -1]])
        elif np.all(y_vals == data_combined[0, -1]):
            return np.array([['leaf', data_combined[0, -1], -1, -1]])
        else:
            best_feature = 0
            max_correlation = -1
            for feature_idx in range(data_combined.shape[1] - 1):
                correlation = ma.corrcoef(ma.masked_invalid(data_combined[:, feature_idx]), 
                                          ma.masked_invalid(y_vals))[0, 1]
                correlation = abs(correlation)
                if correlation > max_correlation:
                    max_correlation = correlation
                    best_feature = feature_idx

            split_value = np.median(data_combined[:, best_feature], axis=0)
            if split_value == max(data_combined[:, best_feature]):
                return np.array([['leaf', np.mean(y_vals), -1, -1]])

            left_subtree = self.build_tree(data_combined[data_combined[:, best_feature] <= split_value])
            right_subtree = self.build_tree(data_combined[data_combined[:, best_feature] > split_value])
            root_node = np.array([[best_feature, split_value, 1, left_subtree.shape[0] + 1]])
            return np.vstack((np.vstack((root_node, left_subtree)), right_subtree))

    def query(self, data_points):
        predictions = []
        root_node = self.tree_structure
        for point in data_points:
            current_node = 0
            while root_node[current_node, 0] != 'leaf':
                feature_index = root_node[current_node, 0]
                split_value = root_node[current_node, 1]
                if point[int(float(feature_index))] <= float(split_value):
                    current_node += int(float(root_node[current_node, 2]))
                else:
                    current_node += int(float(root_node[current_node, 3]))
            prediction = root_node[current_node, 1]
            predictions.append(float(prediction))
        return np.array(predictions)

