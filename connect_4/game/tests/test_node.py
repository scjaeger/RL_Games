from game.node import Node
from game.state import State
import numpy as np


def test_node_edges():
    
    state = State(player = 2)
    state.board = np.array([
        [0, 2, 1, 2, 2, 1, 2],
        [1, 1, 2, 1, 2, 1, 2],
        [2, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 1, 2, 2],
        [1, 1, 2, 2, 2, 1, 2],
        [1, 2, 2, 1, 2, 1, 1],
    ])
    
    node = Node(None, state)
    
    assert len(node.edges) == 1
    assert 0 in node.edges
    
    
def test_node_explored_full():
    
    state = State(player = 1)
    state.board = np.array([
        [0, 2, 1, 2, 2, 1, 2],
        [1, 1, 2, 1, 2, 1, 2],
        [2, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 1, 2, 2],
        [1, 1, 2, 2, 2, 1, 2],
        [1, 2, 2, 1, 2, 1, 1],
    ])
    
    state = state.perform_action(0)
    
    node = Node(None, state)
    
    assert node.explored


def test_node_explored_win():
    
    state = State(player = 1)
    state.board = np.array([
        [0, 0, 0, 2, 0, 1, 2],
        [0, 0, 0, 1, 0, 1, 2],
        [2, 2, 0, 2, 0, 2, 1],
        [2, 1, 2, 1, 0, 2, 2],
        [1, 1, 2, 2, 2, 1, 2],
        [1, 2, 2, 1, 2, 1, 1],
    ])
    
    state = state.perform_action(2)
    
    node = Node(None, state)
    
    assert node.explored
