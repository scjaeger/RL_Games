from game.node import Node
from game.state import State
from ai_sj.mcts import get_winning_child
import numpy as np


def test_get_winning_child_no_winner():
    state = State(player = 1)
    
    root = Node(None, state)
    
    for action in state.get_actions():
        child = Node(root, state.perform_action(action))
        root.children.append(child)
        
    assert get_winning_child(root) == None
    
    
    
def test_get_winning_child_winner():
    state = State(player = 1)
    
    state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 2, 1, 2, 0, 0, 0],
        [2, 1, 1, 2, 0, 0, 0],
    ])
    
    root = Node(None, state)
    
    for action in state.get_actions():
        
        child = Node(root, state.perform_action(action))
        root.children.append(child)
        
        if action == 2:
            winner = child
    
    assert type(get_winning_child(root)) == Node
    assert get_winning_child(root) == winner
    

def test_get_winning_child_no_input():
    state = State()
    root = Node(None, state)
    
    assert get_winning_child(root) == None