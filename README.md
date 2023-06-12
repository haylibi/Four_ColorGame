# Four_ColorGame
Implementation of algorithms for the game FourColor

## Introduction
This project was built using python 3.7.2.
The report was built using LaTeX

## How to run?
Executing the file "run.py" in the folder "src" executes the software as intended.
1. Execute the file "run.py" in the folder "src"
1. To test Minimax, call the function "jogo(depth)" with "depth" as the value you which to test the algorithm with.
1. Alpha Beta, call the function "jogo_alpha_beta(depth)" with "depth" as the value you which to test the algorithm with.
1. Monte Carlo Tree Search, call the function "jogo_monte()".
1. After the previous 4 steps, you'll be asked if you want to be the first player. Answering with "N" or "n" means you won't be the first player, anything else you'll be the first one. The machine plays with "O". Afterwards, you just have to write the number of the column you which to play
NOTE: If you want to interupt the game, just write "stop" during your turn


## Dependecies
This software was tested using Python 3.7.2, and requires only two default packages:
1. time
2. path
3. random

## Algorithms defined
* Min-Max
* Alpha–beta pruning
* Monte Carlo tree search


## Tests
The examples used in our report can be found in the folder "Tests"


## Post Scriptum

If you want to check what a specific algorithm returns for a given state, please execute: 
1. minimax_3(L,X,max depth,depth) - where L is the state, X the player who's playing ('X' or 'O'), max depth the limit for the depth search, depth which depth to start with; (there are 3 minimax: minimax; minimax_2; minimax_3)
1. alphabeta(state,X,alpha,beta,depth,max depth)- Where state is the state,  X the player who's playing ('X' or 'O'), alpha minus inf, beta infinity, depth which depth to start with, max depth the limit for the depth search
1. monte carlo(node,X)- Where node is the state  X the player who's playing ('X' or 'O').
