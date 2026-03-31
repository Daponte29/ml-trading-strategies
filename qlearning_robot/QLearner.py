"""Tabular Q-Learning implementation with optional Dyna-Q updates."""

import random
import numpy as np


class QLearner(object):
    """A basic Q-learner supporting epsilon-greedy exploration and Dyna-Q."""

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
        self.q_table = np.zeros((num_states, num_actions))

        # Dyna model statistics.
        self.tc = np.full((num_states, num_actions, num_states), 1e-7)
        self.r_model = np.zeros((num_states, num_actions))

    def querysetstate(self, s):
        """Set state without updating values and return chosen action."""
        self.s = s
        if random.random() < self.rar:
            action = random.randint(0, self.num_actions - 1)
        else:
            action = int(np.argmax(self.q_table[s]))
        self.a = action

        if self.verbose:
            print(f"s={s}, a={action}")

        return action

    def query(self, s_prime, r):
        """Update Q-table from transition and return next action."""
        best_next = np.max(self.q_table[s_prime])
        self.q_table[self.s, self.a] = (
            (1 - self.alpha) * self.q_table[self.s, self.a]
            + self.alpha * (r + self.gamma * best_next)
        )

        # Update transition/reward model for Dyna simulation.
        self.tc[self.s, self.a, s_prime] += 1
        self.r_model[self.s, self.a] = (
            (1 - self.alpha) * self.r_model[self.s, self.a] + self.alpha * r
        )

        for _ in range(self.dyna):
            s_sim = random.randint(0, self.num_states - 1)
            a_sim = random.randint(0, self.num_actions - 1)
            s_prime_sim = int(np.argmax(self.tc[s_sim, a_sim]))
            r_sim = self.r_model[s_sim, a_sim]

            best_sim = np.max(self.q_table[s_prime_sim])
            self.q_table[s_sim, a_sim] = (
                (1 - self.alpha) * self.q_table[s_sim, a_sim]
                + self.alpha * (r_sim + self.gamma * best_sim)
            )

        if random.random() < self.rar:
            action = random.randint(0, self.num_actions - 1)
        else:
            action = int(np.argmax(self.q_table[s_prime]))

        self.rar *= self.radr
        self.s = s_prime
        self.a = action

        if self.verbose:
            print(f"s={s_prime}, a={action}, r={r}")

        return action

    def author(self):
        return "ndaponte3"

    def study_group(self):
        return "ndaponte3"


if __name__ == "__main__":
    print("QLearner module")
