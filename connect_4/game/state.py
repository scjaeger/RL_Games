import numpy as np

class State():
    def __init__(self, board: np.array = np.zeros((6,7), dtype=int), player: int = np.random.randint(1, 3)):
        self.board = board
        self.player = player
        self.winner = None
        self.game_over = False
        
        
    def get_actions(self) -> list:
        '''
        creates a list of column indices that are available for turns
        
        return:
            list of column indices
        '''
        try:
            # get all columns where the top row is 0 / empty
            actions = np.where(self.board[0,:] == 0)
            
            return list(actions[0])
        
        except Exception as error:
            print(f"Error in State.get_actions --> {error}")
            return False

    
    
    def perform_action(self, action: int):
        try:
            # set height 
            height = self.board.shape[0]
            
            # loop backwards from height to 0
            for row in range(height -1, -1, -1):
                
                # add player number to position if it is empty (0) and break loop
                if self.board[row, action] == 0:
                    player = self.change_player()
                    
                    new_board = self.board.copy()
                    new_board[row, action] = player
                    
                    state = State(new_board, player)
                    
                    state.winner = state.check_win(row, action)
                    state.game_over = state.check_game_end()
                    
                    return state
            
            print(f"Column {action} is already filled. Not a legal turn")
            return False
            
        except Exception as err:
            print(f"Error in perform_action --> {err}")
            return False
        

    def is_equal(self, state) -> bool:
        
        if type(state) == State:
        
            board_check = np.array_equal(self.board, state.board)
            player_check = self.player == state.player
            win_check = self.winner == state.winner
            end_check = self.game_over == state.game_over
            if board_check and player_check and win_check and end_check:
                return True
            else:
                return False
            
        else:
            print("Type Error in State.is_equal")
            return None


    
    
    def check_win(self, row: int, column: int) -> int:
        board = self.board
        
        lines = {
            "horizontal": board[row, :],
            "vertical": board[:, column],
            "diagonal_1": np.diagonal(board, offset= column - row),
            "diagonal_2": np.diagonal(np.flipud(board), offset = column - (board.shape[0] - row - 1)),
            }
        
        # loop through possible lines and check for positions marked with current player's number
        for key in lines.keys():
            # set counter and loop through line
            counter = 0
            for position in lines[key]:
                
                # increase counter if player's number is found
                if position == self.player:
                    counter += 1
                    
                    # return true and end loop if counter reaches 4
                    if counter >= 4:
                        # print(f"{key} winning line at row {row}, column {column}")
                        return self.player
                    
                # reset counter if another value than the player's number is found 
                else:
                    counter = 0
        
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
    
    
if __name__ == "__main__":
    state = State(player = 1)
    
    state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 1, 0, 0, 0, 0, 0,],
        [0, 1, 0, 0, 0, 0, 0,],
        [0, 1, 0, 0, 0, 0, 0,],
    ])
    state = state.perform_action(1)
    print(state.board)
    print(state.winner)