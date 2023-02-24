from game.state import State
from game.node import Node
from ai_sj.selection import select_node
from ai_sj.backpropagation import backpropagate
import numpy as np


def test_select_node_forced_random():
    state = State(player = 1)
    state.board = np.array([
        [1, 2, 1],
        [2, 2, 0],
        [2, 1, 1]
    ])
    
    root = Node(None, state)
    
    new_node = select_node(root)
    
    new_board = np.array([
        [1, 2, 1],
        [2, 2, 1],
        [2, 1, 1]
    ])
    
    assert np.array_equal(new_node.state.board, new_board)
    assert new_node.parent == root
    assert new_node.state.player == 2
    
    
def test_select_node_sum_edges_and_children():
    state = State()
    
    root = Node(None, state)
    
    initial_edges = len(root.edges)
    initial_children = len(root.children)
    
    for _ in range(3):
        new_node = select_node(root)
        
    final_edges = len(root.edges)
    final_children = len(root.children)
    
    assert final_edges == initial_edges - 3
    assert final_children == initial_children + 3
    

def test_select_node_full_board():
    state = State(player = 1)
    state.board = np.array([
        [1, 2, 1],
        [2, 1, 2],
        [2, 1, 1]
    ])
    
    root = Node(None, state)
    
    assert select_node(root) is False
    
    
def test_select_node_no_edges():
    state = State(player = 1)
    root = Node(None, state)
    
    for _ in range(len(root.edges)):
        select_node(root)
        root.times_tested += 1
    
    for child in root.children:
        child.times_tested += 1
        
    root.children[3].times_won += 1

    new_node = select_node(root)
    
    assert new_node in root.children[3].children    
    

def test_select_node_fully_explored():
    state = State(player = 1)
    root = Node(None, state)
    
    for _ in range(len(root.edges)):
        select_node(root)
        root.times_tested += 1
    
    for child in root.children:
        child.times_tested += 1
        child.explored = True
    
    assert select_node(root) is False
    
    
def test_select_node_obvious_choice():
    state = State(player = 1)
    
    state.board = np.array([
        [0, 1, 1],
        [2, 2, 1],
        [2, 0, 2],
    ])
    
    root = Node(None, state)
    
    for i in range(100):
        node = select_node(root)
        if node:
            backpropagate(node, node.state.winner)
        else:
            break
        
    print([child.times_won / child.times_tested for child in root.children if child != 0])

if __name__ == "__main__":
    test_select_node_obvious_choice()
