# TicTacToe3D

This project aims to be a simple console game, where there are tested a few AI algorithms from the easyAI library and trying to implement a Reinforcement Learning algorithm (DQN). The user can select the board size(in 3 dimensions) and the difficulty of its opponent.

The "standard" AI algorithms are: Negamax with alpha/beta prunning, SSS and Dual.
The RLagent is trained only on a 1x3x3 board.

## Dependencies

In order to be able to run the game, you should have installed the following libraries: [keras][keras link], [easyAI][easyai link], [numpy][numpy link].
> pip install easyai, keras, numpy

If you would like to draw the graphs you should also install matplotlib.
> pip3 install matplotlib

## How to run

If you want to play, configure `PlayTicTacToe.py` with the desired AI player,  and run it.

If you want to train the RL agent, please check : `./models/ReinforcementAgentTrainer.py.`
This training script will train the network using the algorithms from easyAI. The agent script randmly selects the opponent, its difficulty and the number of the player.

## Disclaimer

The RL agent is just a naive implementation and also my first attempt in that domain. Any constructive feedback is welcomed.


[keras link]: http://www.keras.io
[easyai link]: https://github.com/Zulko/easyAI
[numpy link]: http://www.numpy.org/
[matplotlib link]: https://matplotlib.org/
