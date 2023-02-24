from game.state import State
from game.node import Node
from ai_sj.selection import choose_random
import numpy as np


def test_choose_random_one_left():
    state = State(player = 1)
    state.board = np.array([
        [1, 2, 1, 2, 1, 2, 0],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])

    node = Node(None, state)
    new_node = choose_random(node)
    
    reference_state = state.perform_action(6)
    
    assert np.array_equal(new_node.state.board, reference_state.board)
    assert new_node.state.player == reference_state.player
    assert new_node.parent == node
    
def test_choose_random_start_state():
    state = State(player = 1)
    node = Node(None, state)
                
    possible_boards = [state.perform_action(edge).board for edge in node.edges]
    new_node = choose_random(node)

    equal_boards = 0
    for board in possible_boards:
        if np.array_equal(board, new_node.state.board):
            equal_boards += 1
            
    assert equal_boards == 1
    assert new_node.parent == node
    
def test_choose_random_delete_edge():
    state = State(player = 1)
    node = Node(None, state)
    
    initial_actions = len(node.edges)
    
    choose_random(node)
    
    final_actions = len(node.edges)
    
    assert final_actions == initial_actions -1