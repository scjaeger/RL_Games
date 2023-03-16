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
    
    assert new_node.state.is_equal(reference_state) is True
    assert new_node.parent == node
    
def test_choose_random_start_state():
    state = State(player = 1)
    node = Node(None, state)
                
    possible_states = [state.perform_action(edge) for edge in node.edges]
    new_node = choose_random(node)

    equal_boards = 0
    for state in possible_states:
        if state.is_equal(new_node.state):
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
    
if __name__ == "__main__":
    test_choose_random_one_left()