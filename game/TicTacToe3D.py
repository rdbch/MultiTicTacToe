import random
import numpy                as  np
import game.MoveGenerator   as  mg

from game.TwoPlayerGame     import  TwoPlayersGame

from gym import Env

class TicTacToe3D( TwoPlayersGame, Env ):
    '''A class that implements the rules of a tick tack toe game. It enherits the easyAI
    class (due to my project for university) and the Env class from openAI gym.

    '''

#==================================== CONSTRUCTOR ========================================
    def __init__(self,winningInRow, boardSize, players, scoringType):
        '''Constructor of the TiTacToe3D game. Here the basic rules are deffinied
        
        Arguments:
            winningInRow {int} -- the number of conssecutive boxes required to win
            boardSize {[int,int,int]} -- a tuple with 3 elements for board size
            players {Player} -- the player
            scoringType {int} -- the coring type
        '''
        self.verbose = False
        self.players    =   players
        self.nplayer    =   1
        
        self.lose_move  =   mg.generateLoseList(boardSize,winningInRow)
       
        self.winningInRow = winningInRow
        
        self.boardSize  =   boardSize
        self.boardLen   =   boardSize[0] * boardSize[1] * boardSize[2]
        self.board      =   [0 for i in range(self.boardLen)]
        self.last_move  =   0 

        self.scoringType = scoringType
        self.copy = self

#=================================== RESET ===============================================
    def reset(self):
        '''REINITIALIZE THE CURRENT PLAYER AND THE BOARD TO the initial status
        
        Returns:
            [tuple] -- return the board
        '''

        self.nplayer    =   1
        self.board      =   [0 for i in range(self.boardLen)]
        self.last_move  =   0 

        return self.board

#=================================== STEP ================================================
    def step(self, action):
        '''step
        it make a move, inherited from the openai gym environment
        
        Arguments:
            action {int} -- the move number to be done
        
        Returns:
            board {tuple} -- the current board, after the action was done
            score {tuple} -- the score/reward that was obtain after the move
            is_over{bool} -- check to see if the games is finished
        '''

        self.make_move(action)
        self.switch_player()
        score = self.scoring()

        return self.board, score, self.is_over(), {}

#==================================== POSSIBLE MOVES =====================================
    def possible_moves(self):
        '''All the possible moves that can be done on the board
        
        Returns:
            List -- the list with all possible moves
        '''

        lst = [i+1 for i,e in enumerate(self.board) if e==0]
        return lst
    
#==================================== MAKE MOVE ==========================================
    def make_move(self, move):
        '''Make move
        
        Arguments:
            move {int} -- the move that will be done 
        '''

        self.board[int(move)-1] = self.nplayer

#==================================== UNMAKE MOVE ========================================
    def unmake_move(self, move): 
        '''Make a box to 0. It speeds up the algorithms
        
        Arguments:
            move {int} -- the move that will be unmake
        '''

        self.board[int(move)-1] = 0

#==================================== LOSE ===============================================
    def lose(self):
        '''Check is oponent has lost
        
        Returns:
            bool -- -
        '''

        for move in self.lose_move:
            if self.board[move[0]-1] == self.board[move[1]-1] == self.board[move[2]-1] == self.nopponent :
                return True
        return False

#==================================== WIN ================================================
    def win(self):
        '''Check if the opponent has won
        
        Returns:
            bool -- -
        '''
        for move in self.lose_move:
            if self.board[move[0]-1] == self.board[move[1]-1] == self.board[move[2]-1] == self.nplayer :
                return True
        return False

#==================================== IS_OVER ============================================
    def is_over(self):
        '''Check to see if anybody has won or if there are no more moves to make.
        
        Returns:
            	bool -- if the game is over or not
        '''

        return (self.possible_moves() == []) or self.lose()
        
#==================================== SHOW ===============================================
    def show(self):
        '''
            Display the current board
        '''

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
        
#==================================== SCORING ============================================
    def scoring(self):
        '''The scoring type applied for the AI algorythm
        
        Raises:
            AttributeError -- when the scoring type is not correctly deffinied
        
        Returns:
            int -- score
        '''

        #offensive
        if self.scoringType == 0:
            if self.lose():
                return -100
            elif self.win():
                return 1000
           
            return 10

        #deffensive
        elif self.scoringType == 1:
            if self.lose():
                return -1000
            elif self.win():
                return 100
            return 10

        #normal
        elif self.scoringType == 2:
            if self.lose():
                return -105
            elif self.win():
                return 100
            return 10

        #not win
        elif self.scoringType == 3:
            if self.lose():
                return -1000
            return 0

        #normal reinf
        elif self.scoringType == 4:
            if self.lose():
                return -1
            elif self.win():
                return 1
            return -0.05

        else:
            raise AttributeError("Scoring not corectly configured")
            