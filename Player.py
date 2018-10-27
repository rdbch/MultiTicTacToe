class Human_Player:
    def __init__(self, name = 'Human'):
        self.name = name

    def ask_move(self, game):
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

class AI_Player:
    def __init__(self, AI_algo, name = 'AI'):
        self.AI_algo = AI_algo
        self.name = name
        self.move = {}

    def ask_move(self, game):
        return self.AI_algo(game)
