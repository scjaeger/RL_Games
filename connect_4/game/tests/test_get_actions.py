from game.state import State
import numpy as np

def test_get_actions_empty():
    state = State()
    actions = state.get_actions()
    test_actions  = set([0,1,2,3,4,5,6])
    assert len(actions) == 7
    assert test_actions.intersection(set(actions)) == set(actions)
    
    
def test_get_actions_full():
    state = State()
    state.board = np.array([
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    actions = state.get_actions()
    
    assert len(actions) == 0
    

def test_get_actions_none_board():
    state = State()
    state.board = None
    
    assert state.get_actions() == False