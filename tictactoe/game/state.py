import numpy as np

class State():
    def __init__(self, board: np.array = np.zeros((3,3), dtype=int), player: int = np.random.randint(1, 3)):
        self.board = board
        self.player = player
        self.winner = self.check_win()
        self.game_over = self.check_game_end()
        
        
    def get_actions(self) -> list:
        '''
        creates a list of column indices that are available for turns
        
        return:
            list of column indices
        '''
        try:
            # get all columns where the top row is 0 / empty
            rows, cols = np.where(self.board == 0)
            
            actions = list(zip(rows, cols))
        
        except Exception as error:
            print(f"Error in State.get_actions --> {error}")
            return False
            
        else:
            return actions
    
    
    def perform_action(self, action: tuple):
        try: 
            row, col = action
            if self.board[row, col] == 0:     
                new_board = self.board.copy()
                new_board[row, col] = self.player
                
                player = self.change_player()
                
                return State(new_board, player) 
            
            else:
                print(f"Forbidden input in State.perform_action: {action} not an empty field")
                return False 
                
        except ValueError as error:
            print(f"ValueError in State.perform_action --> {error}")
            return False
        except Exception as error:
            print(f"Error in State.perform_action --> {error}")
            return False
        


    
    
    def check_win(self) -> int:
        for player in [1, 2]:
            # check rows
            for row in self.board:
                if np.count_nonzero(row == player) == 3:
                    return player
            
            # check columns
            for col in self.board.T:
                if np.count_nonzero(col == player) == 3:
                    return player
                
            # check diagonals
            if np.count_nonzero(np.diagonal(self.board) == player) == 3:
                return player
            elif np.count_nonzero(np.diagonal(np.flipud(self.board)) == player) == 3:
                return player

        return None

    def check_game_end(self):
        if self.winner:
            return True
        elif 0 not in self.board:
            return True
        else:
            return False
        
    
    def change_player(self) -> int:
        '''
        Sets the value of the player to 2 if 1 is given and vice versa
        
        return:
            number of new player
        '''
        if self.player in [1, 2]:
            if self.player == 1:
                player = 2
            else:
                player = 1
        
            return player
        
        else:
            print(f"Error in State.change_player --> self.player = {self.player}, should be in [1, 2]")
            return False
    
    
