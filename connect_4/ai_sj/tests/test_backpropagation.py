from game.state import State
from game.node import Node
from ai_sj.backpropagation import backpropagate
import numpy as np

def test_backpropagate_single_layer():
    state = State(player = 1)
    
    state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
    ])
    
    root = Node(None, state)
    
    child = Node(root, state.perform_action(2))
    
    backpropagate(child, child.state.winner)
    
    print(f"times_tested: {child.times_tested}, {root.times_tested}")
    print(f"times_won {child.times_won}, {root.times_won}")
    
    assert child.times_won == 1
    assert child.times_tested == 1
    assert root.times_tested == 1
    assert root.times_won == 0
    
    
    
    
def test_backpropagate_multi_layer():
    state = State(player = 1)
    
    state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 2, 0],
        [0, 0, 1, 2, 0, 2, 0],
    ])
    
    root = Node(None, state)
    
    first_layer_child = Node(root, state.perform_action(0))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [1, 0, 1, 2, 0, 2, 0],
    
    second_layer_child = Node(first_layer_child, first_layer_child.state.perform_action(4))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [1, 0, 1, 2, 2, 2, 0],
        
    third_layer_child = Node(second_layer_child, second_layer_child.state.perform_action(2))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [1, 0, 1, 2, 2, 2, 0],
        # Winner should be player 1
        
    backpropagate(third_layer_child, third_layer_child.state.winner)
    
    assert third_layer_child.times_tested == 1
    assert second_layer_child.times_tested == 1
    assert first_layer_child.times_tested == 1
    assert root.times_tested == 1
    
    assert third_layer_child.times_won == 1
    assert second_layer_child.times_won == 0
    assert first_layer_child.times_won == 1
    assert root.times_won == 0
    
    
def test_backpropagate_multi_children():
    state = State(player = 1)
    
    state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 2, 0],
        [0, 0, 1, 2, 0, 2, 0],
    ])
    
    root = Node(None, state)
    
    first_layer_child_1 = Node(root, state.perform_action(0))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [1, 0, 1, 2, 0, 2, 0],
        
        # assume simulation outcome is 1
    backpropagate(first_layer_child_1, 1)
        # root: 1 test
        # first_layer 1: 1 test, 1 win
    
    
    first_layer_child_2 = Node(root, state.perform_action(1))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [0, 1, 1, 2, 0, 2, 0],
        
         # assume simulation outcome is 2
         
    backpropagate(first_layer_child_2, 2)
        # root: 2 test
        # first_layer 1: 1 test, 1 win
        # first_layer 2: 1 test, 0 win
        
        
    second_layer_child_1_2 = Node(first_layer_child_1, first_layer_child_1.state.perform_action(4))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [1, 0, 1, 2, 2, 2, 0],
        
        # assume simulation outcome is 2
        
    backpropagate(second_layer_child_1_2, 2)
        # root: 3 test
        # first_layer 1: 2 test, 1 win
        # first_layer 2: 1 test, 0 win
        # second_layer 1.2: 1 test, 2 win
        
    second_layer_child_2_2 = Node(first_layer_child_1, first_layer_child_1.state.perform_action(0))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [0, 1, 1, 2, 0, 2, 0],
        
        # assume simulation outcome is 1
        
    backpropagate(second_layer_child_2_2, 1)
        # root: 4 test
        # first_layer 1: 3 test, 2 win
        # first_layer 2: 1 test, 0 win
        # second_layer 1.2: 1 test, 1 win
        # second_layer 2.2: 1 test, 0 win
    

    assert root.times_tested == 4
    assert first_layer_child_1.times_tested == 3
    assert first_layer_child_2.times_tested == 1
    assert second_layer_child_1_2.times_tested == 1
    assert second_layer_child_2_2.times_tested == 1
    
    assert root.times_won == 0
    assert first_layer_child_1.times_won == 2
    assert first_layer_child_2.times_won == 0
    assert second_layer_child_1_2.times_won == 1
    assert second_layer_child_2_2.times_won == 0
    
    
    
def test_backpropagate_draw():
    state = State(player = 1)
    
    state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 2, 0],
        [0, 0, 1, 2, 0, 2, 0],
    ])
    
    root = Node(None, state)
    
    first_layer_child_1 = Node(root, state.perform_action(0))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [1, 0, 1, 2, 0, 2, 0],
        
        # assume simulation outcome is 0
    backpropagate(first_layer_child_1, 0)
        # root: 1 test
        # first_layer 1: 1 test, 0.3 win
    
    
    first_layer_child_2 = Node(root, state.perform_action(1))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [0, 1, 1, 2, 0, 2, 0],
        
         # assume simulation outcome is 2
         
    backpropagate(first_layer_child_2, 2)
        # root: 2 test
        # first_layer 1: 1 test, 0.3 win
        # first_layer 2: 1 test, 0 win
        
        
    second_layer_child_1_2 = Node(first_layer_child_1, first_layer_child_1.state.perform_action(4))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [1, 0, 1, 2, 2, 2, 0],
        
        # assume simulation outcome is 0
        
    backpropagate(second_layer_child_1_2, 0)
        # root: 3 test
        # first_layer 1: 2 test, 0.6 win
        # first_layer 2: 1 test, 0 win
        # second_layer 1.2: 1 test, 0.3 win
        
    second_layer_child_2_2 = Node(first_layer_child_1, first_layer_child_1.state.perform_action(0))
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 2, 0],
        # [0, 1, 1, 2, 0, 2, 0],
        
        # assume simulation outcome is 1
        
    backpropagate(second_layer_child_2_2, 1)
        # root: 4 test
        # first_layer 1: 3 test, 1.6 win
        # first_layer 2: 1 test, 0 win
        # second_layer 1.2: 1 test, 0.3 win
        # second_layer 2.2: 1 test, 0 win
    

    assert root.times_tested == 4
    assert first_layer_child_1.times_tested == 3
    assert first_layer_child_2.times_tested == 1
    assert second_layer_child_1_2.times_tested == 1
    assert second_layer_child_2_2.times_tested == 1
    
    assert root.times_won == 0
    assert first_layer_child_1.times_won == 1.6
    assert first_layer_child_2.times_won == 0
    assert second_layer_child_1_2.times_won == 0.3
    assert second_layer_child_2_2.times_won == 0
    
    
if __name__ == "__main__":
    test_backpropagate_draw()