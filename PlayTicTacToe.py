from aiAlgos.RLAgent     import      RLAgent
from game.Player         import      Human_Player, AI_Player
from game.TicTacToe3D    import      TicTacToe3D 

# only usable for a (1,3,3) board
aiAlgo      =   RLAgent('./models/mix2/train_17500.h5')

#=================================== PLAYERS =========================================
pl1     =   AI_Player(aiAlgo)
pl2     =   Human_Player()

#=================================== GAME ============================================
env     =   TicTacToe3D(3, (1,3,3), [pl1, pl2], 4)
env.play()
