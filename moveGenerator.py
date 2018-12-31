from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player
import numpy as np

#==================================== GENERATE CUBE ======================================
def generateCube(xLines, yLines, zLines):
    cube = np.zeros((xLines, yLines, zLines), dtype='int')
    index = 1
    for xAxis in range(xLines):
        for yAxis in range(yLines):
            for zAxis in range(zLines):
                cube[xAxis][yAxis][zAxis] = index
                index += 1
    return cube

#==================================== GENERATE LIST ======================================
def generateLoseList(boardSize, winningInRow):
    '''
    Generate the lose move for a 3d TicTacToe game
    
    Arguments:
        boardSize {(int,int,int)} -- the size on x,y and z axis
        winningInRow {int} -- the number of marks required to win
    '''
    assert boardSize[0] >= 1, 'xLines can not be less than 3'
    assert boardSize[1] >= 1, 'yLines can not be less than 3'
    assert boardSize[2] >= 1, 'zLines can not be less than 1'
    xLines = boardSize[0]
    yLines = boardSize[1]
    zLines = boardSize[2]

    cube = generateCube(xLines, yLines, zLines)
    moves = []

    #z axis
    for j in range(yLines):
        for k in range(zLines):
            for i in range(xLines - winningInRow +1):
                aux = []
                for o in range(winningInRow):
                    aux.append(cube[i+o][j][k])
                moves.append(aux)
    #x axis
    for i in range(xLines):
        for j in range(yLines):
            for k in range(zLines - winningInRow +1):
                moves.append(cube[i][j][k:k+winningInRow].tolist())

    #y axis
    for i in range(xLines):
        for k in range(zLines):
            for j in range(yLines - winningInRow +1):
                aux = []
                for o in range(winningInRow):
                    aux.append(cube[i][j+o][k])
                moves.append(aux) 

    
    
    #xy axis right
    for i in range(xLines):
        for j in range(yLines- winningInRow +1):
            for k in range(zLines- winningInRow +1):
                    aux = []
                    for o in range(winningInRow):
                        aux.append(cube[i][j+o][k+o])
                    moves.append(aux) 

    #xy axisleft
    for i in range(xLines):
        for j in range(yLines-winningInRow+1):
            for k in range(winningInRow-1, zLines):
                aux = []
                for o in range(winningInRow):
                    aux.append(cube[i][j+o][k-o])
                moves.append(aux) 

    #xz axis right
    for j in range(yLines):
        for k in range(zLines- winningInRow +1):
            for i in range(xLines- winningInRow +1):
                    aux = []
                    for o in range(winningInRow):
                        aux.append(cube[i+o][j][k+o])
                    moves.append(aux) 

    #xz axis left
    for j in range(yLines):
        for i in range(xLines - winningInRow +1 ):
            for k in range(winningInRow -1, zLines):
                    aux = []
                    for o in range(winningInRow):
                        aux.append(cube[i+o][j][k-o])
                    moves.append(aux)

    #yz axis right
    for k in range(zLines):
        for j in range(yLines- winningInRow +1):
            for i in range(xLines- winningInRow +1):
                    aux = []
                    for o in range(winningInRow):
                        aux.append(cube[i+o][j+o][k])
                    moves.append(aux)

    #yz axis rightfor k in range(zLines):
        for i in range(xLines- winningInRow +1):
            for j in range(winningInRow - 1, yLines):
                    aux = []
                    for o in range(winningInRow):
                        aux.append(cube[i+o][j-o][k])
                    moves.append(aux)
    
    assert len(moves) != 0, 'There are no possible winning moves. please check winningInRow'
    return moves
