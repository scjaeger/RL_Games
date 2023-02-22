from game.state import State
import numpy as np

def test_get_actions_empty():
    state = State()
    actions = state.get_actions()
    test_actions  = set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
    assert len(actions) == 9
    assert test_actions.intersection(set(actions)) == set(actions)
    
    
def test_get_actions_full():
    state = State()
    state.board = np.array([
        [1, 2, 1],
        [2, 2, 1],
        [2, 1, 2]
    ])
    
    actions = state.get_actions()
    
    assert len(actions) == 0
    

def test_get_actions_none_board():
    state = State()
    state.board = None
    
    assert state.get_actions() == False