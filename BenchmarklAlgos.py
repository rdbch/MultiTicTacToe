from enum        import     Enum
from easyAI      import     SSS, DUAL, Negamax
from Negamax     import     NegamaxRand
from Player      import     AI_Player, Human_Player
from TicTacToe3D import     TicTacToe3D
import pickle


#==================================== ENUM CLASS TYPE ====================================
class Strategy(Enum):
    OFFENSIVE   =   0
    DEFFENSIVE  =   1
    NORMAL      =   2
    NOT_WIN     =   3

#==================================== PARAMETERS =========================================
timeNo      =   10                                 # the no of times the test should run
player1Win  =   0                                       

pl1Steps    =   2                                   # the number of steps each algo thinks in advanced
pl2Steps    =   5

pl1         =   NegamaxRand(pl1Steps)               # player 1 algo
pl2         =   DUAL(pl2Steps)                      # player 2 algo

strategy    =   Strategy.NORMAL                     # scoring method
strategyVal =   strategy.value

#==================================== SAVING DATA ========================================
strategyStr =   str(strategy).split('.')[1]
pl1Str      =   str(pl1).split(' ')[0].split('.')[1]
pl2Str      =   str(pl2).split(' ')[0].split('.')[3]

saveName    = "savedSessions/" + strategyStr + "_"
saveName    +=  pl1Str + str(pl1Steps) + "_" + pl2Str + str(pl2Steps) + '_' + str(timeNo) + ".p"

print(pl1Str, pl2Str)
print(strategyStr)

#==================================== GAME LOOP ==========================================
with open(saveName, "wb") as f:
    for i in range(timeNo):
        res = TicTacToe3D(3, (3,3,3), [AI_Player(pl1), AI_Player(pl2)], strategyVal).play(verbose = False)[-1].nplayer
        if res == 2:
            player1Win += 1
            res = 1
        else:
            res = 2
        pickle.dump(res,f)      

        #debug step, sows where you are

        print("Interm step:", i)

    f.close()

print("Player 1 won:", player1Win/timeNo*100,"%")