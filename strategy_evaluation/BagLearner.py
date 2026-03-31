import numpy as np
from scipy import stats

class BagLearner(object):
    def __init__(self, learner, kwargs={"leaf_size": 1}, bags=20, boost=False, verbose=False):
        self.learner = learner
        self.learner_list = []
        self.bags = bags
        self.boost = boost
        self.verbose = verbose
        
        # Initialize learners
        for _ in range(bags):
            self.learner_list.append(learner(**kwargs))

    def add_evidence(self, dataX, dataY):
        train_rows = dataX.shape[0]
        
        for learner in self.learner_list:
            # Generate a bootstrap sample
            indices = np.random.randint(0, train_rows, train_rows)
            newX = dataX[indices]
            newY = dataY[indices]
            
            learner.add_evidence(newX, newY)

    def query(self, points):
        predictions = []
        
        for learner in self.learner_list:
            predictions.append(learner.query(points))
        
        # Convert to numpy array for mode calculation
        predictions_array = np.array(predictions)
        # Find the most common prediction
        res, _ = stats.mode(predictions_array, axis=0)
        
        return res.flatten()

    def author(self):

    def study_group(self):
        return 'ndaponte3'
