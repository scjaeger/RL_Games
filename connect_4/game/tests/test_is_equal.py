from game.state import State
import numpy as np

def test_is_equal_same_state():
    
    state = State(player = 2)
    
    compare_state = State(player = 2)
    
    assert state.is_equal(compare_state) is True
    
    
    
def test_is_equal_wrong_board():
    
    state = State(player = 2)
    
    compare_state = State(player = 2)
    compare_state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
    ])
    
    assert state.is_equal(compare_state) is False
    
    
    
def test_is_equal_wrong_winner():
    
    state = State(player = 2)
    state.winner = 1
    compare_state = State(player = 2)
    
    assert state.is_equal(compare_state) is False
    
    
def test_is_equal_game_over():
    
    state = State(player = 2)
    state.game_over = True
    compare_state = State(player = 2)
    
    assert state.is_equal(compare_state) is False   
    
    
def test_is_equal_wrong_player():
    
    state = State(player = 1)

    compare_state = State(player = 2)
    
    assert state.is_equal(compare_state) is False
    
if __name__ == "__main__":
    test_is_equal_wrong_board()