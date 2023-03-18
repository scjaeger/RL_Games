from ai_sj.selection import calculate_uct
from game.state import State
from game.node import Node
import numpy as np

def test_calculate_uct_zeros():
    state = State()
    root = Node(None, state)
    
    for action in root.edges:
        new_state = state.perform_action(action)
        child = Node(root, new_state)
        child.times_tested += 1
        root.times_tested += 1
        root.children.append(child)
        
    uct = calculate_uct(root.children, root.times_tested)

    assert len(np.unique(uct)) == 1
    

def test_calculate_uct_single_winner():
    state = State()
    root = Node(None, state)
    
    for action in root.edges:
        new_state = state.perform_action(action)
        child = Node(root, new_state)
        child.times_tested += 1
        root.times_tested += 1
        root.children.append(child)
    
    root.children[0].times_won += 1
    uct = calculate_uct(root.children, root.times_tested)

    assert len(np.unique(uct)) == 2
    assert np.argmax(uct) == 0
    