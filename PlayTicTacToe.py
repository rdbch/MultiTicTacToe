import keras
import numpy as np

from Player         import  Human_Player, AI_Player
from TicTacToe3D    import  TicTacToe3D 

humanPlayer = Human_Player()
model   =   keras.models.load_model('./models/mix2/train_17500.h5')
env     =   TicTacToe3D(3, (1,3,3), [humanPlayer, humanPlayer], 4)
done    =   False
state   =   env.reset()
rlFirst =   True
#=================================== MAIN LOOP ========================================
while not done:
    
    if not rlFirst:
        env.show()
        playerMove = humanPlayer.ask_move(env)

        newState,_,done,_   =   env.step(playerMove)
        state               =   newState

        if done:
            print('Player ended')
            break
    
    pred    =   model.predict([[state]])

    # get the best possible move
    while True:
        predPos = np.argmax(pred) + 1
        if predPos in env.possible_moves():
            break
        pred[0][predPos-1] = -1
  
    newState, reward, done, _ = env.step(predPos)
    state =   newState

    if done:
            print('RL ended')
            break
            
    if rlFirst:
        
    
        env.show()
        playerMove = humanPlayer.ask_move(env)

        newState,_,done,_   =   env.step(playerMove)
        state               =   newState


        if done:
            print('Player ended')
            break