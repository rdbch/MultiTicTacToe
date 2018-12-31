import gym
import keras
import random
import numpy as np
import copy

from keras.models import Sequential
from keras.layers import InputLayer, Dense, Dropout

from TicTacToe3D  import TicTacToe3D
from Player       import AI_Player, Human_Player
from easyAI       import DUAL, SSS, Negamax
from Negamax      import NegamaxRand

#=================================== MODEL DEFINITION ====================================
model = Sequential()
model.add( Dense(10,     activation = 'sigmoid', input_dim = 9))
model.add( Dense(100,    activation = 'sigmoid') )
model.add( Dense(9,      activation = 'softmax') )

model.compile(loss='mse', optimizer='adam', metrics=['mae'])

# model = keras.models.load_model('./models/mix/train_49500.h5')
#=================================== PARAMETERS ==========================================

env             =   TicTacToe3D(3, (1,3,3), [Human_Player(),Human_Player() ], 4)
num_episodes    =   300000
y               =   0.95
rlFirst         =   True
decay           =   0.9999
aiAlgos         =   [SSS(5), NegamaxRand(4), NegamaxRand(2), Negamax(2)]
#=================================== TRAINING LOOP =======================================
print('Start training')
for i in range(num_episodes):
    rlFirst     =   random.choice([True,False])  
    state       =   env.reset()
    done        =   False
    trainAlgo       =   random.choice(aiAlgos)                         
    trainPlayer     =   AI_Player(trainAlgo)
    y *= decay
    #=================================== GAME LOOP =======================================
    while not done:
        if not rlFirst:
            # opponent move
            if random.random() > 0.1:
                trainMove           =   trainPlayer.ask_move(env)
            else:
                trainMove = random.choice(env.possible_moves())

            newState,_,done,_   =   env.step(trainMove)
            state               =   newState

            if done:
                if i % 500 == 0:
                    print('EasyAI ended')
                break
        
        normalizedState = np.array(copy.deepcopy(state))/2
        pred    =   model.predict([[normalizedState]])

        # get the best possible move
        while True:
            predPos = np.argmax(pred) + 1
            if predPos in env.possible_moves():
                break
            pred[0][predPos-1] = -1

        # make the step with the predicted move
        newState, reward, done, _ = env.step(predPos)
        
        # compute label for training
        target                      =   max(0, min(1, y * reward + np.max(model.predict([[normalizedState]])))) 
        targetVec                   =   model.predict([[normalizedState]])
        targetVec[0][predPos-1]     =   target
        
        # train the model
        model.fit([[normalizedState]], targetVec, epochs=1, verbose=0)
        
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

    
    if i % 500 == 0:
        print("Episode {} of {} , rlFirst {}".format(i, num_episodes, rlFirst))
        print(state)
        #save the model
        keras.models.save_model(model, './models/mix2/train_'+str(i)+'.h5') 
