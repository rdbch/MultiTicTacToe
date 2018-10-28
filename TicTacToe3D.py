import random
import numpy            as  np
import moveGenerator    as  mg

from twoPlayerGame         import  TwoPlayersGame
from easyAI         import  SSS, AI_Player
from Negamax        import  Negamax
from Player  import  Human_Player


class TicTacToe3D( TwoPlayersGame ):
    def __init__(self,winningInRow, boardSize, players):
        
        self.players    =   players
        self.nplayer    =   2
        
        self.lose_move  =   mg.generateLoseList(boardSize,winningInRow)
       
        self.winningInRow = winningInRow
        
        self.boardSize  =   boardSize
        self.boardLen   =   boardSize[0] * boardSize[1] * boardSize[2]
        self.board      =   [0 for i in range(self.boardLen)]

    def possible_moves(self):
        lst = [i+1 for i,e in enumerate(self.board) if e==0]
        # random.shuffle(lst)
        return lst
    
    def make_move(self, move):
        self.board[int(move)-1] = self.nplayer

    def unmake_move(self, move): # optional method (speeds up the AI)
        self.board[int(move)-1] = 0
    
    def lose(self):
        """ Has the opponent "three in line ?" """
        for move in self.lose_move:
            if self.board[move[0]-1] == self.board[move[1]-1] == self.board[move[2]-1] == self.nopponent :
                return True
        return False

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()
        
    def show(self):
        index = 0
        for i in range(self.boardSize[0]):
            for j in range(self.boardSize[1]):
                for k in range(self.boardSize[2]):
                    if self.board[index] == 0:
                        print('.', end = ' ')
                    elif self.board[index] == 1:
                        print('X', end = ' ')
                    else:
                        print('O', end = ' ')
                    index += 1
                print()
            print('')
        
    def scoring(self):
        return -100 if self.lose() else 0
    


    