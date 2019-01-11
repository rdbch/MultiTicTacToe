# script used for playing a TicTacToe game.


from aiAlgos.RLAgent     import     RLAgent
from game.Player         import     Human_Player, AI_Player
from game.TicTacToe3D    import     TicTacToe3D 
from aiAlgos.Negamax     import     NegamaxRand
from easyAI              import     DUAL, SSS, Negamax



# classical algos /easyAi
steps       =   4                                               #the number of steps AI thinks in advance
algos       =   [   DUAL(steps),                                #0 
                    Negamax(steps),                             #1
                    NegamaxRand(steps),                         #2 - when states are equal, choose randomly from them
                    SSS(steps),                                 #3
                    RLAgent('./models/mix3/train_49500.h5')     #4 - trained on a (1,3,3) board
                    ]

#select choice from above
choice      =   4 
aiAlgo      =   algos[choice]

#=================================== PLAYERS =========================================
pl1     =   AI_Player(aiAlgo)
pl2     =   Human_Player()

#=================================== GAME ============================================
env     =   TicTacToe3D(3, (1,3,3), [pl1, pl2], 4)
env.play()
