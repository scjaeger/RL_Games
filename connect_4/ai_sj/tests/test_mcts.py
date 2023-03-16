from ai_sj.mcts import mcts
from ai_sj.simulation import simulate
from game.node import Node
from game.state import State
import numpy as np
import random


def test_mcts_type():
    state = State()
    root = Node(None, state)
    
    node, stats = mcts(root, state)

    assert isinstance(node, Node)
    assert isinstance(stats, dict)
    
def test_mcts_time_limit():
    state = State()
    root = Node(None, state)
    
    _, stats = mcts(root, state, 1)
    
    assert stats["time left"] > 0
    

def test_mcts_node_children():
    state = State(player = 1)
    
    node, _ = mcts(None, state)
    
    action = random.choice(node.state.get_actions())
    state = node.state.perform_action(action)
    
    node, _ = mcts(node, state)
    
    assert node.children


def test_mcts_obvious_win():
    
    init_state = State(player = 2)
    
    init_state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [1, 0, 1, 1, 2, 2, 0],
        ])
    
    win_state = init_state.perform_action(1)
    
    counter = 0
    
    runs = 10
    
    for _ in range(runs):
    
        state = State(player = 2)
        state.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [1, 0, 1, 1, 2, 2, 0],
            ])
        
        root = Node(None, state)
        
        node, _ = mcts(root, state)
        
        if win_state.is_equal(node.state):
            counter += 1

    assert counter == runs
    
    
def test_mcts_obvious_loose():
        
    init_state = State(player = 1)
    
    init_state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [1, 0, 1, 1, 2, 2, 0],
        ])
    
    win_state = init_state.perform_action(1)
    
    counter = 0
    
    runs = 5
    
    for _ in range(runs):
    
        state = State(player = 1)
        state.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [1, 0, 1, 1, 2, 2, 0],
            ])
        
        root = Node(None, state)
        
        node, stats = mcts(root, state)
        
        print(stats)
        
        if win_state.is_equal(node.state):
            counter += 1

    
    assert counter == runs
    
   
def test_mcts_multi_children():
    correct_move = 0
    runs = 100
    for _ in range(runs):
        state = State(player = 1)
        
        state.board = np.array([
            [0, 0, 1, 2, 2, 1, 1],
            [0, 0, 2, 1, 1, 2, 2],
            [2, 1, 2, 2, 2, 1, 1],
            [2, 1, 2, 1, 1, 2, 2],
            [1, 2, 1, 2, 2, 1, 1],
            [1, 1, 2, 2, 1, 2, 2],
        ])
        
        root = Node(None, state)
            
        node, stats = mcts(root, state)
    
        if node.state.board[1,0] == 2:
            correct_move += 1
    
    assert correct_move == runs
    assert stats["loops"] == 17      
    assert node.parent.times_tested == 17
    assert len(node.parent.children) == 2
    
    assert node.times_tested == 8
    assert 3.1 <= round(node.times_won, 1) <= 4.5
    assert node.explored
    
    for layer1_node in node.children:
        if layer1_node.state.board[1, 1] == 1:
            assert 0.6 <= round(layer1_node.times_won, 1) <= 0.9
            assert layer1_node.times_tested == 4
            assert len(layer1_node.children) == 2
            assert layer1_node.explored
        else:
            assert round(layer1_node.times_won, 1) == 0.9
            assert layer1_node.times_tested == 3
            assert len(layer1_node.children) == 1
            assert layer1_node.explored
        
        for layer2_node in layer1_node.children:
            if layer2_node.state.board[0, 0] == 2:
                assert layer2_node.times_won == 1
                assert layer2_node.times_tested == 1
                assert len(layer2_node.children) == 0
                assert layer2_node.explored
                assert layer2_node.state.winner == 2
            else:
                assert layer2_node.times_won == 0.6
                assert layer2_node.times_tested == 2
                assert len(layer2_node.children) == 1
                assert layer2_node.explored



    
    
if __name__ == "__main__":
    test_mcts_obvious_loose()
    