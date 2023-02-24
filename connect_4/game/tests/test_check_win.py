from game.state import State
import numpy as np

def test_check_win_zeros():
    state = State()
    
    assert state.check_win(0, 0) == None
    
    
def test_check_win_full_lost():
    state = State()
    state.board = np.array([
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    assert state.check_win(0, 0) == None
    
    
def test_check_win_col():
    state = State(player = 2)
    state.board = np.array([
            [0, 0, 0, 0, 1, 2, 1],
            [1, 2, 1, 0, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 1, 1, 2, 1],
            [1, 2, 1, 1, 1, 2, 1],
        ])
    
    assert state.check_win(1, 3) == 1
    
def test_check_win_row():
    state = State(player = 2)
    state.board = np.array([
        [0, 2, 1, 2, 1, 2, 1],
        [0, 2, 1, 2, 1, 2, 1],
        [0, 1, 2, 1, 2, 1, 2],
        [1, 1, 1, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    assert state.check_win(3, 0) == 1
    
def test_check_win_diagonal_1():
    state = State(player = 1)
    state.board = np.array([
        [1, 2, 1, 0, 0, 0, 1],
        [1, 2, 1, 0, 2, 2, 1],
        [2, 1, 2, 2, 2, 1, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    assert state.check_win(2, 3) == 2
    
    
def test_check_win_diagonal_2():
    state = State(player =2)
    state.board = np.array([
        [1, 1, 0, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [2, 1, 2, 1, 1, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    assert state.check_win(1, 2) == 1