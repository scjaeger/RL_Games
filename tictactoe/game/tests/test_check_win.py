from game.state import State
import numpy as np

def test_check_win_zeros():
    state = State()
    
    assert state.check_win() == None
    
    
def test_check_win_full_lost():
    state = State()
    state.board = np.array([
        [1, 2, 1],
        [2, 1, 2],
        [2, 1, 2],
    ])
    
    assert state.check_win() == None
    
    
def test_check_win_col():
    state = State()
    state.board = np.array([
        [2, 2, 1],
        [2, 1, 2],
        [2, 1, 1],
    ])
    
    assert state.check_win() == 2
    
def test_check_win_row():
    state = State()
    state.board = np.array([
        [2, 2, 1],
        [1, 2, 2],
        [1, 1, 1],
    ])
    
    assert state.check_win() == 1
    
def test_check_win_diagonal_1():
    state = State()
    state.board = np.array([
        [1, 2, 1],
        [2, 1, 2],
        [1, 1, 2],
    ])
    
    assert state.check_win() == 1
    
    
def test_check_win_diagonal_2():
    state = State()
    state.board = np.array([
        [1, 2, 1],
        [2, 1, 2],
        [1, 2, 1],
    ])
    
    assert state.check_win() == 1