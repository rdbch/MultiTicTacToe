from Negam import Negamax
from TicTacToe3D import TicTacToe3D
from easyAI import TT, SSS, DUAL
from Player import AI_Player, Human_Player

ai_algo = Negamax(3)
ai_algo2 = SSS(4)
ai_algo3 = DUAL(3)
TicTacToe3D(4, (2,4,4), [AI_Player(ai_algo),AI_Player(ai_algo2)]).play()