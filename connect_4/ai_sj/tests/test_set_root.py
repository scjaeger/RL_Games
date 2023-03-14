from game.state import State
from game.node import Node
from ai_sj.mcts import set_root
import numpy as np

def test_set_root_new():
    
    node = None
    state = State()
    
    new_root = set_root(node, state)
    
    assert np.array_equal(new_root.state.board, state.board)
    
def test_set_root_given_state():
    
    state = State()
    
    root = Node(None, state)
    
    for action in [0, 1, 2, 3]:
        child = Node(root, state.perform_action(action))
        root.children.append(child)
        
    new_state = state.perform_action(0)
    
    new_root = set_root(root, new_state)
    
    assert np.array_equal(new_root.state.board, new_state.board)