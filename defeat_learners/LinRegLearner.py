""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
#IMPORTANT NOTE: Course Retake Submission		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
class LinRegLearner(object):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    This is a Linear Regression Learner. It is implemented correctly.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param verbose: If â€œverboseâ€ is True, your code can print out information for debugging.  		  	   		 	   			  		 			 	 	 		 		 	
        If verbose = False your code should not generate ANY output.  		  	   		 	   			  		 			 	 	 		 		 	
    :type verbose: bool  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    def __init__(self, verbose=False):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Constructor method  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        pass  # move along, these aren't the drones you're looking for  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    def author(self):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        :return: The GT username of the student  		  	   		 	   			  		 			 	 	 		 		 	
        :rtype: str  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
    def study_group(self):
       return 'ndaponte3'  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 

	   			  		 			 	 	 		 		 	
    def add_evidence(self, data_x, data_y):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Add training data to learner  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        :param data_x: A set of feature values used to train the learner  		  	   		 	   			  		 			 	 	 		 		 	
        :type data_x: numpy.ndarray  		  	   		 	   			  		 			 	 	 		 		 	
        :param data_y: The value we are attempting to predict given the X data  		  	   		 	   			  		 			 	 	 		 		 	
        :type data_y: numpy.ndarray  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        # slap on 1s column so linear regression finds a constant term  		  	   		 	   			  		 			 	 	 		 		 	
        new_data_x = np.ones([data_x.shape[0], data_x.shape[1] + 1])  		  	   		 	   			  		 			 	 	 		 		 	
        new_data_x[:, 0 : data_x.shape[1]] = data_x  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        # build and save the model  		  	   		 	   			  		 			 	 	 		 		 	
        self.model_coefs, residuals, rank, s = np.linalg.lstsq(  		  	   		 	   			  		 			 	 	 		 		 	
            new_data_x, data_y, rcond=None  		  	   		 	   			  		 			 	 	 		 		 	
        )  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    def query(self, points):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Estimate a set of test points given the model we built.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		 	   			  		 			 	 	 		 		 	
        :type points: numpy.ndarray  		  	   		 	   			  		 			 	 	 		 		 	
        :return: The predicted result of the input data according to the trained model  		  	   		 	   			  		 			 	 	 		 		 	
        :rtype: numpy.ndarray  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        return (self.model_coefs[:-1] * points).sum(axis=1) + self.model_coefs[  		  	   		 	   			  		 			 	 	 		 		 	
            -1  		  	   		 	   			  		 			 	 	 		 		 	
        ]  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    print("the secret clue is 'zzyzx'")  		  	   		 	   			  		 			 	 	 		 		 	
