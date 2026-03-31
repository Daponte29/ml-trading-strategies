
#Libraries/API/Imports
import numpy as np
import LinRegLearner as lrl
import BagLearner as bl
#/////////////////////
#IMPORTANT NOTE: Summer 2024 Course Ratake Student Resubmission


class InsaneLearner(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.learners = []
        for i in range(20):
            self.learners.append(bl.BagLearner(learner=lrl.LinRegLearner, kwargs={}, bags=20, boost=False, verbose=False))
    def author(self):  

    def study_group(self):
       return 'ndaponte3'
   
    
        
    def add_evidence(self, data_x, data_y):
        for learner in self.learners:
            learner.add_evidence(data_x, data_y)

    def query(self, points):
        results = []
        for learner in self.learners:
            result = learner.query(points)
            results.append(result)
        results = np.mean(np.array(results), axis=0)
        return results
