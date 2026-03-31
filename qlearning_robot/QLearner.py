""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
Template for implementing QLearner  (c) 2015 Tucker Balch  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Tucker Balch (replace with your name)  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
#Libraries///////////  		  	   		 	   			  		 			 	 	 		 		 	
import random as rand  
import numpy as np 		  	   		 	   			  		 			 	 	 		 		 	
#///////////////////		  	   		 	   			  		 			 	 	 		 		 	
	  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
class QLearner(object):
     		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    This is a Q learner object.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param num_states: The number of states to consider.  		  	   		 	   			  		 			 	 	 		 		 	
    :type num_states: int  		  	   		 	   			  		 			 	 	 		 		 	
    :param num_actions: The number of actions available..  		  	   		 	   			  		 			 	 	 		 		 	
    :type num_actions: int  		  	   		 	   			  		 			 	 	 		 		 	
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.  		  	   		 	   			  		 			 	 	 		 		 	
    :type alpha: float  		  	   		 	   			  		 			 	 	 		 		 	
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.  		  	   		 	   			  		 			 	 	 		 		 	
    :type gamma: float  		  	   		 	   			  		 			 	 	 		 		 	
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.  		  	   		 	   			  		 			 	 	 		 		 	
    :type rar: float  		  	   		 	   			  		 			 	 	 		 		 	
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.  		  	   		 	   			  		 			 	 	 		 		 	
    :type radr: float  		  	   		 	   			  		 			 	 	 		 		 	
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.  		  	   		 	   			  		 			 	 	 		 		 	
    :type dyna: int  		  	   		 	   			  		 			 	 	 		 		 	
    :param verbose: If â€œverboseâ€ is True, your code can print out information for debugging.  		  	   		 	   			  		 			 	 	 		 		 	
    :type verbose: bool  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    def __init__( 
         		  	   		 	   			  		 			 	 	 		 		 	
        self,  		  	   		 	   			  		 			 	 	 		 		 	
        num_states=100,  		  	   		 	   			  		 			 	 	 		 		 	
        num_actions=4,  		  	   		 	   			  		 			 	 	 		 		 	
        alpha=0.2,  		  	   		 	   			  		 			 	 	 		 		 	
        gamma=0.9,  		  	   		 	   			  		 			 	 	 		 		 	
        rar=0.5,  		  	   		 	   			  		 			 	 	 		 		 	
        radr=0.99,  		  	   		 	   			  		 			 	 	 		 		 	
        dyna=0,  		  	   		 	   			  		 			 	 	 		 		 	
        verbose=False,  		  	   		 	   			  		 			 	 	 		 		 	
    ):  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        Constructor method  		  	   		 	   			  		 			 	 	 		 		 	
        """  		  	   		 	   			  		 			 	 	 		 		 	
        self.num_states = num_states  		  	   		 	   			  		 			 	 	 		 		 	
        self.num_actions = num_actions  		  	   		 	   			  		 			 	 	 		 		 	
        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna  
        self.verbose = verbose
        self.s = 0
        self.a = 0
        self.Q_table = np.zeros((num_states,num_actions))

        ''' Initialize Q Table '''
        self.verbose = verbose
        self.Tc = np.zeros((num_states, num_actions, num_states)) + 0.0000001
        self.T = np.zeros((num_states, num_actions, num_states))	  
        self.R = np.zeros((num_states, num_actions))   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    def querysetstate(self, s):
        """
        Update the current state without updating the Q-table.
        
        :param s: The new state.
        :type s: int
        :return: The selected action.
        :rtype: int
        """
        self.s = s
        action = rand.randint(0, self.num_actions - 1)
        
        if self.verbose:
            print(f"s = {s}, a = {action}")
        
        return action 		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    def query(self, s_prime, r):
        """
        Update the Q-table and return an action.
        
        :param s_prime: The new state.
        :param r: The reward.
        :return: The selected action.
        :rtype: int
        """
        # Update Q-table using Q-learning update rule
        self.Q_table[self.s, self.a] = (1 - self.alpha) * self.Q_table[self.s, self.a] + self.alpha * (r + self.gamma * np.amax(self.Q_table[s_prime]))
    
        random = np.random.random()
        
        # Update model (Tc, T, R) based on observed state-action-next_state transitions
        self.Tc[self.s, self.a, s_prime] += 1
        self.R[self.s, self.a] = (1 - self.alpha) * self.R[self.s, self.a] + self.alpha * r
    
        # Perform Dyna-Q updates
        for i in range(self.dyna):
            s_dyna = rand.randint(0, self.num_states - 1)
            a_dyna = rand.randint(0, self.num_actions - 1)
            s_prime_dyna = np.argmax(self.Tc[s_dyna, a_dyna])
            r_dyna = self.R[s_dyna, a_dyna]
            self.Q_table[s_dyna, a_dyna] = (1 - self.alpha) * self.Q_table[s_dyna, a_dyna] + self.alpha * (r_dyna + self.gamma * np.amax(self.Q_table[s_prime_dyna]))
    
        # Choose action based on exploration-exploitation trade-off
        if random >= self.rar:
            action = np.argmax(self.Q_table[s_prime])
        else:
            action = rand.randint(0, self.num_actions - 1)
    
        self.a = action
        self.s = s_prime
        self.rar *= self.radr
    
        if self.verbose:
            print(f"State {s_prime}, selected action: {action}, reward: {r}")
    
        return action

	


	  	   		 	   			  		 			 	 	 		 		 	
    def author(self):
    def study_group(self):
       return 'ndaponte3'  


		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    print("Remember Q from Star Trek? Well, this isn't him")  		  	   		 	   			  		 			 	 	 		 		 	
