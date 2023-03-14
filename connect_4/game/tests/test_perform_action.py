from game.state import State
import numpy as np

def test_perform_action_std():
    state = State(player = 1)
    action = 0
    state = state.perform_action(action)

    assert state.board[5, 0] == 2
    assert np.sum(state.board) == 2
    assert state.player == 2
    
def test_perform_action_wrong_field():
    state = State(player = 1)
    state.board = np.array([
        [2, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0],
        [1, 1, 2, 0, 0, 0, 0],
        [1, 2, 2, 0, 0, 0, 0],
    ])
    
    action = 0
    
    assert state.perform_action(action) is False
    
def test_perform_action_None():
    state = State(player = 1)
    action = None

    assert state.perform_action(action) is False