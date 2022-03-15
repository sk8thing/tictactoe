# Description
Tic-tac-toe game written in Python3 using the pygame library and minimax algorithm.
## Running the game
Make sure you have installed the [pygame](https://pypi.org/project/pygame/) library
```
pip3 install pygame
```
To run the game simply do
```
python3 main.py
```
## Controls
LMB - move to position\
R - restart the game when ended
## The minimax algorithm
In turn based games each player desires to pick the move that gives them an advantage. 
Each available move has a value associated with it, therefore there is a player that is maximizing and one that is minimizing. 
The algorithm goes back and forth between the two players, where the maximizing player is trying to pick the move with the maximum score, but the score for each available move is determined by the minimizing player trying to pick the move with the minimum score. 
This repeats until there's no more available moves or once an end state is reached.
## Screenshots
![1](https://user-images.githubusercontent.com/101511232/158174032-ffcdc33d-a247-4b2e-9d12-331b94a80c84.png)
![2](https://user-images.githubusercontent.com/101511232/158176036-fe998bd0-39e5-4c7a-b779-96cb5233d521.png)
![3](https://user-images.githubusercontent.com/101511232/158176621-af133b1f-6efc-4dbf-b91a-5a0b5efcc45f.png)