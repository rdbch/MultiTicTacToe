# Script used to generate that resulted from the test phase

import pickle
import numpy as np
import matplotlib.pyplot as plt

#load data
with open("finalRes.res", "rb") as f:
    results = pickle.load(f)

# create plot
n_groups    =   len(results)

fig, ax     =   plt.subplots()
index       =   np.arange(4 )
bar_width   =   0.4
opacity     =   0.8

winProcs    =   []
algoStrs    =   []

#=================================== LOOP FOR GEN ========================================
# for each algorithm as first player plot against others

for i in range(0,4,1):
    winProcs = []
    algoStrs = []

    #construct the resulted string
    for result in results[4*i:4*i+4]:
        [algo1Str, algo2Str, winProc] = result
        winProcs.append(winProc)
        algoStrs.append(algo2Str)

    pl2Procs = (np.array(winProcs) - 100) * -1

    #plot player 1
    rects1 = plt.bar(index, winProcs, bar_width,
                    alpha = opacity,
                    color = 'b',
                    label = algo1Str)

    #plot player 2
    rects2 = plt.bar(index + bar_width, pl2Procs, bar_width,
                    alpha = opacity,
                    color = 'g',
                    label = 'Player2')

    #plot labels and axis     
    plt.xticks(index + bar_width, algoStrs)
    plt.xlabel('Algorithms')
    plt.ylabel('Scores')
    plt.title('Scores by algo')
    plt.legend()
    
    plt.show()

    # save plot
    plt.savefig(algo1Str + ".png")
