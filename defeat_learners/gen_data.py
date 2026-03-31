""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
template for generating data to fool learners (c) 2016 Tucker Balch  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Nicholas Daponte  		  	   		 	   			  		 			 	 	 		 		 	
IMPORTANT NOTE: Course Retake Submission		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import math  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
# this function should return a dataset (X and Y) that will work  		  	   		 	   			  		 			 	 	 		 		 	
# better for linear regression than decision trees  		  	   		 	   			  		 			 	 	 		 		 	
def best_4_lin_reg(seed=1489683273):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		 	   			  		 			 	 	 		 		 	
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		 	   			  		 			 	 	 		 		 	
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param seed: The random seed for your data generation.  		  	   		 	   			  		 			 	 	 		 		 	
    :type seed: int  		  	   		 	   			  		 			 	 	 		 		 	
    :return: Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: numpy.ndarray  		  	   		 	   			  		 			 	 	 		 		 	
    """  
    # Set the random seed for reproducibility
    np.random.seed(seed)	
    #features
    num_rows, num_features = 700	, 10 
    #Random numbers 1 to 10 for features	 
    x = np.random.uniform(1, 10, size=(num_rows, num_features))
    
    #Make target/label with a clear linear relationship
    coef = np.random.uniform(1, 5, size=(num_features))
    noise = np.random.normal(0,3,num_rows)
    y = np.dot(x, coef)  + noise
    
    #class example just for reference------		 	   			  		 			 	 	 		 		 	
    # np.random.seed(seed)  		  	   		 	   			  		 			 	 	 		 		 	
    # x = np.zeros((100, 2))  		  	   		 	   			  		 			 	 	 		 		 	
    # y = np.random.random(size=(100,)) * 200 - 100  		  	   		 	   			  		 			 	 	 		 		 	
    # Here's is an example of creating a Y from randomly generated  		  	   		 	   			  		 			 	 	 		 		 	
    # X with multiple columns  		  	   		 	   			  		 			 	 	 		 		 	
    # y = x[:,0] + np.sin(x[:,1]) + x[:,2]**2 + x[:,3]**3  		  	   		 	   			  		 			 	 	 		 		 	
    return x, y  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def best_4_dt(seed=1489683273):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		 	   			  		 			 	 	 		 		 	
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		 	   			  		 			 	 	 		 		 	
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param seed: The random seed for your data generation.  		  	   		 	   			  		 			 	 	 		 		 	
    :type seed: int  		  	   		 	   			  		 			 	 	 		 		 	
    :return: Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: numpy.ndarray  		  	   		 	   			  		 			 	 	 		 		 	
    """
    np.random.seed(seed)
    num_rows, num_features = 700	, 10
    
 
    #Random numbers 1 to 10 for features	 
    x = np.random.uniform(1, 10, size=(num_rows, num_features))
    coef = np.random.uniform(1, 5, size=(num_features))
    noise = np.random.normal(0,3,num_rows)
    #Non linear relationship to target better suited for DT than LR
    y = (coef[0] * x[:, 0] ** 3 * x[:, 1] ** 2 + 
               coef[1] * x[:, 0] ** 2 * x[:, 1] + 
               coef[2] * x[:, 0] * x[:, 1] ** 2 + 
               coef[3] * x[:, 0] * x[:, 1] + 
               coef[4] * x[:, 0] + 
               coef[5] * x[:, 1]) + noise
    #Class example just for reference 		  	   		 	   			  		 			 	 	 		 		 	
    # np.random.seed(seed)  		  	   		 	   			  		 			 	 	 		 		 	
    # x = np.zeros((100, 2))  		  	   		 	   			  		 			 	 	 		 		 	
    # y = np.random.random(size=(100,)) * 200 - 100  		  	   		 	   			  		 			 	 	 		 		 	
    return x, y  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def author():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The GT username of the student  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: str  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    return "ndaponte3"  # Change this to your user ID
def study_group():
   return 'ndaponte3'  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    print("they call me Tim.") 
    # Test best_4_lin_reg function	  	   		 	   			  		 			 	 	 		 		 	
