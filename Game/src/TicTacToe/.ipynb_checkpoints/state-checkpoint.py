from Game.src.state_abc import StateABC

class State(StateABC):
    def __init__(self, board, player):
        super().__init__(board, player)
        
    def get_actions(self):
        actions = []
        for index, value in enumerate(self.board):
            if (value == ' '):
                actions.append(index)
        return actions
        
    def do_action(self, player, position):
        self.board[position] = player
    
    def change_player(self):
        if (self.player == 'X'):
            self.player == 'O'
        else:
            self.player == 'X'
    
    def check_end_state(self, player):
        if ((self.board[0] == self.board[1] == self.board[2] == player) or
            (self.board[3] == self.board[4] == self.board[5] == player) or
            (self.board[6] == self.board[7] == self.board[8] == player) or
            (self.board[0] == self.board[3] == self.board[6] == player) or
            (self.board[1] == self.board[4] == self.board[7] == player) or
            (self.board[2] == self.board[5] == self.board[8] == player) or
            (self.board[0] == self.board[4] == self.board[8] == player) or
            (self.board[2] == self.board[4] == self.board[6] == player)):
            return True, player
        else:
            return False
    
    def print_board(self):
        for index, value in enumerate(self.board):
            if ((index == 2) or (index == 5)):
                print(' {0} '.format(value))
                print('-----------')
            elif (index == 8):
                print(' {0} '.format(value), end='')
            else:
                print(' {0} |'.format(value), end='')
    
    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board
        
    def get_player(self):
        return self.player
    
    def set_player(self, player):
        self.player = player