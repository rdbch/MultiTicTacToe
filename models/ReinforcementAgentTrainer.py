# Script used for training the RL agent. It randoply trains the agent as both, 1st player,
# and second player. Also, it randomly introduces random moves. It uses multiple algorithms 
# to train against. It saves the model every
# 500 episodes. 
#
# Note: this RL agent is not as good as you think. A way better combination would bve an 
# AlphaGo like approach

import gym
import copy
import keras
import random
import numpy as np

from keras.models import Sequential
from keras.layers import InputLayer, Dense, Dropout

from game.TicTacToe3D   import TicTacToe3D
from game.Player        import AI_Player, Human_Player
from easyAI             import DUAL, SSS, Negamax
from aiAlgos.Negamax    import NegamaxRand

#=================================== MODEL DEFINITION ====================================
model = Sequential()
model.add( Dense(10,     activation = 'relu', input_dim = 9))
model.add( Dense(100,    activation = 'relu') )
model.add( Dense(100,    activation = 'relu') )
model.add( Dense(9,      activation = 'linear') )

model.compile(loss='mse', optimizer='adam', metrics=['mae'])

# model = keras.models.load_model('./models/mix/train_49500.h5')
#=================================== PARAMETERS ==========================================

env             =   TicTacToe3D(3, (1,3,3), [Human_Player(),Human_Player() ], 4)
num_episodes    =   100000
y               =   0.95
rlFirst         =   True
decay           =   0.9999
aiAlgos         =   [SSS(5), NegamaxRand(4), NegamaxRand(2), Negamax(2)]

#=================================== TRAINING LOOP =======================================
print('Start training')
for i in range(num_episodes):

    #reset the environment
    state       =   env.reset()                         
    done        =   False                       

    #get the training conditions
    rlFirst         =   random.choice([True,False])  
    trainAlgo       =   random.choice(aiAlgos)                         
    trainPlayer     =   AI_Player(trainAlgo)

    y *= decay                                          #it learn slower after many iterations
    
    #=================================== GAME LOOP =======================================
    #play a game until it is finished
    while not done:

        # opponent move
        if not rlFirst:
            if random.random() > 0.1:
                trainMove           =   trainPlayer.ask_move(env)
            else:
                trainMove = random.choice(env.possible_moves())

            newState,_,done,_   =   env.step(trainMove)
            state               =   newState

            #debug message once every 500 episodes
            if done:
                if i % 500 == 0:
                    print('EasyAI ended')
                break
        

        normalizedState =   np.array(copy.deepcopy(state))/2
        pred            =   model.predict([[normalizedState]])

        # get the best possible move
        for imoves in range(9):
            predPos = np.argmax(pred) + 1
            if predPos in env.possible_moves():
                break
            pred[0][predPos-1] = -0.1

        # make the step with the predicted move
        newState, reward, done, _   =   env.step(predPos)
        normalizedNewState          =   np.array(copy.deepcopy(newState))/2
        
        # compute label for training
        target                      =   reward + y * np.max(model.predict([[normalizedNewState]]))
        targetVec                   =   model.predict([[normalizedState]])
        targetVec[0][predPos-1]     =   target
        
        # train the model
        model.fit([[normalizedState]], targetVec, epochs=1, verbose=0)
        
        #debug message
        if done:
            if i % 500 == 0:
                print('RL has ended')
            break

        state =   newState

        # opponent move
        if rlFirst:
            if random.random() > 0.1:
                trainMove   =     trainPlayer.ask_move(env)
            else:
                trainMove   =     random.choice(env.possible_moves())

            newState,_,done,_   =   env.step(trainMove)
        
        state =   newState

    #debug message    
    if i % 500 == 0:
        print("Episode {} of {} , rlFirst {}".format(i, num_episodes, rlFirst))
        print(state)

        #save the model
        keras.models.save_model(model, './mix3/train_'+str(i)+'.h5') 
