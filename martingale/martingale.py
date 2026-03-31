""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""Assess a betting strategy.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Tucker Balch (replace with your name)  		  	   		 	   			  		 			 	 	 		 		 	

*** IMPORTANT!!! Previous Summer 2024 Student Retaking Course and Resubmitting Work		  	   		 	   			  		 			 	 	 		 		 	
"""  
#Libraries	////////////////////////   		 	   			  		 			 	 	 		 		 	
import numpy as np
import matplotlib.pyplot as plt
#///////////////////////////////////


def author():
    return 'ndaponte3'

def study_group():
    return 'None'

def gtid():
    return 903357453

def get_spin_result(win_prob):
    return np.random.random() <= win_prob # if falls within probability range then a WIN if over the range then LOSS

def simulator(win_prob, has_bankroll, bankroll):
    result_array = np.zeros(1001)
    episode_winnings = 0
    count = 0

    while episode_winnings < 80 and count < 1001:
        won = False
        bet_amount = 1
        while not won and count < 1001:
            result_array[count] = episode_winnings
            count += 1
            won = get_spin_result(win_prob)
            if won:
                episode_winnings += bet_amount
                
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2

                if has_bankroll:
                    if episode_winnings == -bankroll:
                        result_array[count:] = episode_winnings
                        return result_array
                    if episode_winnings - bet_amount < -bankroll:
                        bet_amount = bankroll + episode_winnings
        if episode_winnings >= 80:  # Stop if winnings reach or exceed 80 #Maybe dont need this condition?
            break                        
    if count < 1001:
        result_array[count:] = episode_winnings # Fill Forward the winnings when reaching 80 or above

    return result_array # Return the episode results

def exp1_figure1(win_prob):
   
    
    plt.axis([0, 300, -256, 100])
    plt.title("10 Episodes Infinite bankroll")
    plt.xlabel("Number of Spins")
    plt.ylabel("Total Winnings $USD")

    for _ in range(10):
        curr_episode = simulator(win_prob, False, None)
        plt.plot(curr_episode)

    plt.savefig("figure1.png")
    plt.clf()

def exp1_figure2_and_figure3(win_prob):
    result_array = np.zeros((1000, 1001))
    for index in range(1000):
        curr_episode = simulator(win_prob, False, None)
        result_array[index] = curr_episode

    mean_array = np.mean(result_array, axis=0)
    std = np.std(result_array, axis=0, ddof=0)
    mean_plus_array = mean_array + std
    mean_minus_array = mean_array - std

    plt.axis([0, 300, -256, 100])
    plt.title(" 1000 Episodes Infinite bankroll")
    plt.xlabel("Number of Spins")
    plt.ylabel("Total Winnings $USD")
    plt.plot(mean_array, label="mean")
    plt.plot(mean_plus_array, label="mean+std")
    plt.plot(mean_minus_array, label="mean-std")
    plt.legend()
    plt.savefig("figure2.png")
    plt.clf()

    median_array = np.median(result_array, axis=0)
    median_plus_array = median_array + std
    median_minus_array = median_array - std

    plt.axis([0, 300, -256, 100])
    plt.title("Medians of 1000 Episodes Infinite bankroll")
    plt.xlabel("Number of Spins")
    plt.ylabel("Total Winnings $USD")
    plt.plot(median_array, label="median")
    plt.plot(median_plus_array, label="median+std")
    plt.plot(median_minus_array, label="median-std")
    plt.legend()
    plt.savefig("figure3.png")
    plt.clf()

def exp2_figure4_and_figure5(win_prob, bank_roll):
    result_array = np.zeros((1000, 1001))
    for index in range(1000):
        curr_episode = simulator(win_prob, True, bank_roll)
        result_array[index] = curr_episode

    mean_array = np.mean(result_array, axis=0)
    std = np.std(result_array, axis=0, ddof=0)
    mean_plus_array = mean_array + std
    mean_minus_array = mean_array - std

    plt.axis([0, 300, -256, 100])
    plt.title("Means of 1000 Episodes with $" + str(bank_roll) + " bankroll")
    plt.xlabel("Number of Spins")
    plt.ylabel("Total Winnings")
    plt.plot(mean_array, label="mean")
    plt.plot(mean_plus_array, label="mean+std")
    plt.plot(mean_minus_array, label="mean-std")
    plt.legend()
    plt.savefig("figure4.png")
    plt.clf()

    median_array = np.median(result_array, axis=0)
    median_plus_array = median_array + std
    median_minus_array = median_array - std

    plt.axis([0, 300, -256, 100])
    plt.title("Medians of 1000 Episodes with $" + str(bank_roll) + " bankroll")
    plt.xlabel("Number of Spins")
    plt.ylabel("Total Winnings")
    plt.plot(median_array, label="median")
    plt.plot(median_plus_array, label="median+std")
    plt.plot(median_minus_array, label="median-std")
    plt.legend()
    plt.savefig("figure5.png")
    plt.clf()

def save_results_to_file():
    with open("p1_results.txt", "w") as file:
        file.write("Experiment Results\n")
        file.write("===================\n")
        file.write(f"Author: {author()}\n")
        file.write(f"GTID: {gtid()}\n")
        file.write(f"Study Group: {study_group()}\n")
        file.write("\n")
        file.write("Figures:\n")
        file.write("Figure 1: 10 Episodes w/ infinite bankroll\n")
        file.write("Figure 2: means of 1000 Episodes infinite bankroll\n")
        file.write("Figure 3: medians of 1000 Episodes infinite bankroll\n")
        file.write("Figure 4: means of 1000 Episodes $256 bankroll\n")
        file.write("Figure 5: medians of 1000 Episodes $256 bankroll\n")
        

def test_code():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Method to test your code  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    win_prob = 18 / 38  # probability of winning on black due to Dr. Balch's Stradegy  		  	   		 	   			  		 			 	 	 		 		 	
    np.random.seed(gtid())  # do this only once  reproducibility		  	   		 	   			  		 			 	 	 		 		 	
    #print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	   			  		 			 	 	 		 		 	
    # add your code here to implement the experiments  
    bank_roll = 256
    exp1_figure1(win_prob)
    exp1_figure2_and_figure3(win_prob)
    exp2_figure4_and_figure5(win_prob, bank_roll)
    
    save_results_to_file()

if __name__ == "__main__":
    test_code()
