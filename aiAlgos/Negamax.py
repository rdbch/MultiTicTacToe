import pickle
import random
inf = float('infinity')

#=================================== NEGAMAX RAND  =======================================
def negamax(game, depth, origDepth, scoring, alpha=+inf, beta=-inf, tt=None):
    if (depth == 0) or game.is_over():
        score = scoring(game)
        if score == 0:
            return score
        else:
            return  (score - 0.01*depth*abs(score)/score)
   
    possible_moves = game.possible_moves()
  
    state       =   game
    best_move   =   random.choice(possible_moves)

    if depth == origDepth:
        state.ai_move = best_move
        
    bestValue   = -inf
    unmake_move = hasattr(state, 'unmake_move')
    random.shuffle(possible_moves)

    for move in possible_moves:
        if not unmake_move:
            game = state.copy() # re-initialize move
        
        game.make_move(move)
        game.switch_player()
        
        move_alpha = - negamax(game, depth-1, origDepth, scoring,
                               -beta, -alpha, tt)
        
        if unmake_move:
            game.switch_player()
            game.unmake_move(move)
        
        if bestValue < move_alpha:
            bestValue = move_alpha
            best_move = move

        if  alpha < move_alpha :
            alpha = move_alpha
            if depth == origDepth:
                state.ai_move = move
            if (alpha >= beta):
                break

    return bestValue

        
class NegamaxRand:
    def __init__(self, depth, scoring=None, win_score=+inf, tt=None):
        self.scoring = scoring        
        self.depth = depth
        self.tt = tt
        self.win_score= win_score
    
    def __call__(self,game):
        scoring = self.scoring if self.scoring else (
                       lambda g: g.scoring() ) # horrible hack
                       
        self.alpha = negamax(game, self.depth, self.depth, scoring,
                     -self.win_score, +self.win_score, self.tt)
                     
        return game.ai_move
