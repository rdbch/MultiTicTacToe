import  keras
import  numpy as np

from    keras import models

#=================================== RL agent ============================================
class RLAgent:
    '''This class aims to work be an interface for a keras model with the easyAI library.
    
    '''
    #=================================== INIT ============================================
    def __init__(self, modelPath):
        '''Constructor
        
        Arguments:
            modelPath {str} -- the path of the model(.h5 file)
        '''

        self.model = models.load_model(modelPath)

    #=================================== PREDICT =========================================
    def predict(self, state):
        '''Make a prediction with the current model
        
        Arguments:
            state {[type]} -- the type has to exact like that wich you have trained your 
            model
        
        Returns:
            [type] -- the prediction of the model
        '''

        return self.model.predict(state)

    #=================================== __CALL__ ========================================
    def __call__(self, game, normVal = 2):
        '''Used in easyAi library
        
        Arguments:
            game {TwoPlayerGame} -- the game 
        
        Keyword Arguments:
            normVal {int} -- the normalization value for the board(if necessary) (default: {2})
        
        Returns:
             int -- the best possible move
        '''

        predictBoard = np.array(game.board) / 2
        
        pred    =   self.predict([[predictBoard]])

        # get the best possible move
        while True:
            predPos = np.argmax(pred) + 1
            if predPos in game.possible_moves():
                break
            pred[0][predPos-1] = -1
        
        return predPos