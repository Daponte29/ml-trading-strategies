""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
Test a learner.  (c) 2015 Tucker Balch  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
#Libraries/////////////////   			  	   		 	   			  		 			 	 	 		 		 	
import math  		  	   		 	   			  		 			 	 	 		 		 	
import sys  		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np  	
import matplotlib.pyplot as plt	  

import LinRegLearner as lrl 	   		 	   			  		 			 	 	 		 		 	
import DTLearner as dt  
import RTLearner as rt
import BagLearner as bl
import InsaneLearner as it
#//////////////////////////
#IMPORTANT NOTE: Summer 2024 Course Ratake Resubmission

if __name__ == "__main__":
 	  	   		 	   			  		 			 	 	 		 		 	
    if len(sys.argv) != 2:
        print("Usage: python testlearner.py <filename>")
        sys.exit(1)
    file = sys.argv[1]
 
    with open(file) as inf:
        data = []
        for line in inf:
            try: 
                values = list(map(float,line.strip().split(",")[1:]))
                data.append(values)
            except ValueError:
                #skip line if float conversion fails
                continue
    
            
       
    
        
    # Read in raw data Istanbul test dataread
    #data = np.genfromtxt("Data/Istanbul.csv", delimiter=',', skip_header=1, usecols=range(1, 10))  # Assuming there are 10 columns in total

    
    #convert to numpy array
    data = np.array(data)
    # Shuffle the data
    np.random.seed(42)  # For reproducibility
    shuffled_indices = np.random.permutation(data.shape[0])
    
    # Compute how much of the data is training and testing
    train_rows = int(0.6 * data.shape[0])
    
    # Split the indices into training and testing
    train_indices = shuffled_indices[:train_rows]
    test_indices = shuffled_indices[train_rows:]
    
    # Separate out training and testing data using the shuffled indices
    train_x = data[train_indices, :-1]
    train_y = data[train_indices, -1]
    test_x = data[test_indices, :-1]
    test_y = data[test_indices, -1]
    
    print(f"Train X shape: {train_x.shape}")
    print(f"Train Y shape: {train_y.shape}")
    print(f"Test X shape: {test_x.shape}")
    print(f"Test Y shape: {test_y.shape}")
    
    
    
    ### Experiment 1: DTLearner
    rmse_in_sample = []
    rmse_out_sample = []
    for i in range(1, 21):
        # create a learner and train it
        learner = dt.DTLearner(leaf_size=i, verbose=False)
        learner.add_evidence(train_x, train_y)
        # evaluate in sample
        pred_y = learner.query(train_x)
        rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
        rmse_in_sample.append(rmse)
        # evaluate out of sample
        pred_y2 = learner.query(test_x)
        rmse2 = math.sqrt(((test_y - pred_y2) ** 2).sum() / test_y.shape[0])
        rmse_out_sample.append(rmse2)
      # plotting the figure
    plt.plot(rmse_in_sample, color='blue')
    plt.plot(rmse_out_sample, color='orange')
    plt.title("RMSE vs Leaf Size for DTLearner")
    plt.xlabel("Leaf Size")
    plt.xlim(1, 20)
    plt.ylabel("RMSE")
    plt.ylim(0, 0.01)
    plt.legend(["In-Sample", "Out-Sample"], loc="best")
    # plt.show()
    plt.savefig("Q1_new_alternative_metrics.png")
    plt.close("all")

    
    
    
    
    ### Experiment 2: BagLearner: 15 bags leaf size 1-20
    rmse_in_sample = []
    rmse_out_sample = []
    for i in range(1, 21):
        # create a learner and train it
        learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": i}, bags=15, boost=False, verbose=False)
        learner.add_evidence(train_x, train_y)
        # evaluate in sample
        pred_y = learner.query(train_x)
        rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
        rmse_in_sample.append(rmse)
        # evaluate out of sample
        pred_y2 = learner.query(test_x)
        rmse2 = math.sqrt(((test_y - pred_y2) ** 2).sum() / test_y.shape[0])
        rmse_out_sample.append(rmse2)
    # plotting the figure
    plt.plot(rmse_in_sample)
    plt.plot(rmse_out_sample)
    plt.title("RMSE vs Leaf Size for BagLearner with 15 Bags")
    plt.xlabel("Leaf Size")
    plt.xlim(1, 20)
    plt.ylabel("RMSE")
    plt.ylim(0, 0.01)
    plt.legend(["In-Sample", "Out-Sample"])
    plt.savefig("Q2_new_alternative_metrics.png")
    plt.close("all")
    #plt.show()
    
    
  
    
    
  #Experiment 3: 
    male_dt = []
    male_rt = []
    mdape_dt = []
    mdape_rt = []
    
    for i in range(1, 21):
        # create a DTlearner and train it
        learner = dt.DTLearner(leaf_size=i, verbose=False)
        learner.add_evidence(train_x, train_y)
        # create a RTlearner and train it
        learner2 = rt.RTLearner(leaf_size=i, verbose=False)
        learner2.add_evidence(train_x, train_y)
        # evaluate DTlearner in sample
        pred_y = learner.query(train_x)
        male = np.mean(np.abs(np.log1p(train_y) - np.log1p(pred_y)))
        male_dt.append(male)
        mdape = np.median(np.abs((train_y - pred_y) / train_y))
        mdape_dt.append(mdape)
        # evaluate RTlearner in sample
        pred_y2 = learner2.query(train_x)
        male2 = np.mean(np.abs(np.log1p(train_y) - np.log1p(pred_y2)))
        male_rt.append(male2)
        mdape2 = np.median(np.abs((train_y - pred_y2) / train_y))
        mdape_rt.append(mdape2)
    
    # plotting the figures
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(male_dt)
    plt.plot(male_rt)
    plt.title("MALE for Training DTLearner vs RTLearner")
    plt.xlabel("Leaf Size")
    plt.xlim(1, 20)
    plt.ylabel("MALE")
    plt.legend(["DTLearner", "RTLearner"])
    
    plt.subplot(1, 2, 2)
    plt.plot(mdape_dt)
    plt.plot(mdape_rt)
    plt.title("MdAPE for Training DTLearner vs RTLearner")
    plt.xlabel("Leaf Size")
    plt.xlim(1, 20)
    plt.ylabel("MdAPE")
    plt.legend(["DTLearner", "RTLearner"])
    
    plt.tight_layout()
    #plt.show()
    plt.savefig("Q3_new_alternative_metrics.png")
    plt.close("all")
    
    
    
    
    
    
    # # Create a learner and train it
    # learner = dtl.DTLearner(leaf_size=5, verbose=True)  # create a DTLearner
    # learner.add_evidence(train_x, train_y)  # train it
    # print(learner.author())
    
    # # Evaluate in sample
    # pred_y = learner.query(train_x)  # get the predictions
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    # print("\nIn sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=train_y)
    # print(f"corr: {c[0,1]}")
    
    # # Evaluate out of sample
    # pred_y = learner.query(test_x)  # get the predictions
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    # print("\nOut of sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=test_y)
    # print(f"corr: {c[0,1]}")
