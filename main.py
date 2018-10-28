from TicTacToe3D import TicTacToe3D
from easyAI import TT, SSS, DUAL
from Player import AI_Player, Human_Player
from Negamax import Negamax

ai_algo     =   Negamax(2)
ai_algo2    =   SSS(1)
ai_algo3    =   DUAL(2)

TicTacToe3D(3, (3,3,3), [Human_Player(),AI_Player(ai_algo)]).play()