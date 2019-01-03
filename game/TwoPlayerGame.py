from copy import deepcopy

class TwoPlayersGame:

    def play(self, nmoves=1000, verbose=True):
        history = []

        if verbose:
            self.show()

        for self.nmove in range(1, nmoves + 1):

            if self.is_over():
                if(len(self.possible_moves()) == 0):
                    print("Draw! :(")
                    break
                
                if verbose:
                    print("Player %d won!" % (self.nopponent))
                break

            move = self.player.ask_move(self)
            history.append((deepcopy(self), move))
            self.make_move(move)

            if verbose:
                print("\nMove #%d: player %d plays %s :" % (
                      self.nmove, self.nplayer, str(move)))
                self.show()

            self.switch_player()

        history.append(deepcopy(self))

        return history

    @property
    def nopponent(self):
        return 2 if (self.nplayer == 1) else 1

    @property
    def player(self):
        return self.players[self.nplayer - 1]

    @property
    def opponent(self):
        return self.players[self.nopponent - 1]

    def switch_player(self):
        self.nplayer = self.nopponent

    def copy(self):
        return deepcopy(self)

    def get_move(self):
        return self.player.ask_move(self)

    def play_move(self, move):
        result = self.make_move(move)
        self.switch_player()
        return result
