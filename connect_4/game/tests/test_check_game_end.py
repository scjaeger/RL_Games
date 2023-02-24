from game.state import State
import numpy as np

def test_check_game_end_start():
    state = State()
    
    assert state.check_game_end() is False
    
def test_check_game_end_full():
    state = State()
    state.board = np.array([
        [1, 2, 1],
        [2, 2, 1],
        [2, 1, 2]
    ])
    
    assert state.check_game_end() is True
    
def test_check_game_end_winner():
    state = State()
    state.winner = 2
    
    assert state.check_game_end() is True