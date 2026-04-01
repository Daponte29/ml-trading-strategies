# Q-Learning Robot

## Overview
This project implements a tabular Q-Learning agent with optional Dyna-Q updates.
The learner is designed for grid/world navigation tasks and demonstrates reinforcement learning fundamentals:
- state-action value learning
- epsilon-greedy exploration with decay
- model-based hallucinated updates (Dyna)

## Key Files
- `QLearner.py`: Q-learning and Dyna-Q implementation
- `tests/testqlearner.py`: evaluation script
- `testworlds/`: environment definitions
- `tests/grade_robot_qlearning.py`: system validation harness

## Skills Demonstrated
- Reinforcement learning from scratch
- Exploration vs exploitation strategy
- Transition-model-based acceleration (Dyna-Q)

## Run
```bash
python tests/testqlearner.py
```
