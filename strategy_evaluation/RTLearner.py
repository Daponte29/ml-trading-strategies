import numpy as np

class RTLearner(object):
    def __init__(self, leaf_size, verbose=False):
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.learner = np.array([])

    def build_tree(self, data):
        # If the data has less than or equal to the leaf size, return a leaf
        if data.shape[0] <= self.leaf_size:
            return np.array([['leaf', np.mean(data[:, -1]), '-1', '-1']])
        
        # Select random attribute for splitting
        X_attr = np.random.randint(data.shape[1] - 1)

        # If all values in the selected attribute are the same, return a leaf
        if np.all(data[:, X_attr] == data[0, X_attr]):
            return np.array([['leaf', np.mean(data[:, -1]), '-1', '-1']])

        # Sort data based on the selected attribute
        data = data[np.argsort(data[:, X_attr])]
        splitVal = np.median(data[:, X_attr])

        # If max value equals the split value, return a leaf
        if np.max(data[:, X_attr]) == splitVal:
            return np.array([['leaf', np.mean(data[:, -1]), '-1', '-1']])

        # Build left and right sub-trees
        leftTree = self.build_tree(data[data[:, X_attr] <= splitVal])
        rightTree = self.build_tree(data[data[:, X_attr] > splitVal])
        
        # Root of the tree
        root = [X_attr, splitVal, '1', str(leftTree.shape[0] + 1)]
        tree = np.vstack((root, leftTree, rightTree))
        
        return tree

    def add_evidence(self, Xtrain, Ytrain):
        data = np.concatenate((Xtrain, Ytrain[:, None]), axis=1)
        self.learner = self.build_tree(data)

    def query(self, trainX):
        predY = np.array([])
        for data in trainX:
            row = 0
            while self.learner[row][0] != 'leaf':
                X_attr = int(float(self.learner[row][0]))
                splitVal = float(self.learner[row][1])
                if float(data[X_attr]) <= splitVal:
                    row = row + int(float(self.learner[row][2]))
                else:
                    row = row + int(float(self.learner[row][3]))
            if self.learner[row][0] == 'leaf':
                predY = np.append(predY, float(self.learner[row][1]))
        return predY

    def author(self):

    def study_group(self):
        return 'ndaponte3'
