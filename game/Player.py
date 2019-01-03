class Human_Player:
    #=================================== INIT ============================================
    def __init__(self, name = 'Human'):
        self.name = name

    #=================================== ASK_MOVE ========================================
    def ask_move(self, game):
        '''Ask for a keyboard move.
        
        Arguments:
            game {TwoPlayerGame} -- the current game that you are playing
        
        Returns:
            move -- the move
        '''

        possible_moves      =   game.possible_moves()
        possible_moves_str  =   list(map(str, game.possible_moves()))
        move                =   "NO_MOVE_DECIDED_YET"
        
        while True:
            move = input("\nPlayer %s what do you play ? "%(game.nplayer))
            if move == 'show moves':
                
                print ("Possible moves:\n"+ "\n".join(
                       ["#%d: %s"%(i+1,m) for i,m in enumerate(possible_moves)])
                       +"\nType a move or type 'move #move_number' to play.")

            elif move in ['exit', 'quit', 'q']:
                exit()

            elif move.startswith("move #"):
                move = possible_moves[int(move[6:])-1]
                return move

            elif str(move) in possible_moves_str:
                move = possible_moves[possible_moves_str.index(str(move))]
                return move

#=================================== AI PLAYER ===========================================
class AI_Player:
    '''AI PLayer class
    
    Returns:
        move -- the best possible move from the AI algorithm
    '''
    #=================================== INIT ============================================
    def __init__(self, AI_algo, name = 'AI'):
        '''Constructor
        
        Arguments:
            AI_algo {AI_Algo} -- an algorithm from the easyAI library
        
        Keyword Arguments:
            name {str} -- The AI name (default: {'AI'})
        '''

        self.AI_algo = AI_algo
        self.name = name
        self.move = {}

    #=================================== ASK_MOVE ========================================
    def ask_move(self, game):
        '''Ask for a move from the ai algo, given the current game
        
        Arguments:
            game {TwoPLayerGame} -- the current game
        
        Returns:
            move -- the best move
        '''

        return self.AI_algo(game)
