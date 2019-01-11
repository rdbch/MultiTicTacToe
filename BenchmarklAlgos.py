from enum               import     Enum
from easyAI             import     SSS, DUAL, Negamax
from aiAlgos.Negamax    import     NegamaxRand
from aiAlgos.RLAgent    import     RLAgent
from game.Player        import     AI_Player, Human_Player
from game.TicTacToe3D   import     TicTacToe3D
from keras              import     models

import pickle
import keras
#==================================== ENUM CLASS TYPE ====================================
class Strategy(Enum):
    OFFENSIVE   =   0
    DEFFENSIVE  =   1
    NORMAL      =   2
    NOT_WIN     =   3

#==================================== PARAMETERS =========================================
timeNo      =   20                                # the no of times the test should run
player1Win  =   0                                       

pl1No       =   "negamax"
pl2No       =   "rlAgent"

pl1Steps    =   4                                   # the number of steps each algo thinks in advanced
pl2Steps    =   4

rlAgent     =   RLAgent('./models/mix3/train_49500.h5')

aiAlgosPl1  =   {"negamax"          :   Negamax(pl1Steps), 
                    "dual"          :   DUAL(pl1Steps), 
                    "sss"           :   SSS(pl1Steps), 
                    "negamaxRand"   :   NegamaxRand(pl1Steps), 
                    "rlAgent"       :   rlAgent
                }

aiAlgosPl2  =   {"negamax"          :   Negamax(pl2Steps), 
                    "dual"          :   DUAL(pl2Steps), 
                    "sss"           :   SSS(pl2Steps), 
                    "negamaxRand"   :   NegamaxRand(pl2Steps), 
                    "rlAgent"       :   rlAgent
                }
resultList  =   []
strategy    =   Strategy.NORMAL                     # scoring method
strategyVal =   strategy.value

for i in ["rlAgent", "negamaxRand", 'dual', 'sss', 'negamax']:
    for j in ["negamaxRand", 'dual', 'sss', 'negamax']:
        pl1         =   aiAlgosPl1[i]                   # player 1 algo
        pl2         =   aiAlgosPl2[j]                   # player 2 algo


        #==================================== SAVING DATA ========================================
        strategyStr =   str(strategy).split('.')[1]
        pl1Str      =   i
        pl2Str      =   j
        
        #print opponents
        print(pl1Str)
        print(pl2Str)
    
        saveName    = "savedSessions/" + strategyStr + "_"
        saveName    +=  pl1Str + str(pl1Steps) + "__" + pl2Str + str(pl2Steps) + '_' + str(timeNo) + ".p"

        #==================================== GAME LOOP ==========================================
        with open(saveName, "wb") as f:
            player1Win = 0            
            for no in range(timeNo):

                res = TicTacToe3D(3, (1,3,3), [AI_Player(pl1), AI_Player(pl2)], strategyVal).play(verbose = False)[-1].nplayer
                if res == 2:
                    player1Win += 1
                    res = 1
                else:
                    res = 2
                pickle.dump(res,f)      

            f.close()

        print("Player 1 won,",pl1Str, player1Win/timeNo*100,"%")
        resultList.append([pl1Str, pl2Str, player1Win/timeNo*100])

with open("finalRes2.res", "wb") as f:
    pickle.dump(resultList, f)
    f.close()