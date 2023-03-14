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

    assert type(node) == Node
    assert type(stats) == dict
    
def test_mcts_time_limit():
    state = State()
    root = Node(None, state)
    
    _, stats = mcts(root, state, 1)
    
    assert stats["time left"] < 1
    

def test_mcts_node_children():
    state = State(player = 1)
    
    node, stats = mcts(None, state)
    
    print(node.state.board)
    print(stats)
    
    action = random.choice(node.state.get_actions())
    state = node.state.perform_action(action)
    
    node, stats = mcts(node, state)
    
    print(node.state.board)
    print(stats)
    

def test_mcts_stop_run():
    state = State(player = 1)
    state.board = np.array([
        [2, 1, 2, 2, 1, 0, 0],
        [1, 2, 1, 1, 2, 2, 0],
        [1, 2, 1, 1, 1, 2, 0],
        [1, 2, 2, 2, 1, 1, 0],
        [2, 1, 2, 1, 1, 1, 0],
        [1, 2, 1, 1, 2, 2, 0],
    ])
    
    root = Node(None, state)
    
    node, stats = mcts(root, state)
    
    # assert len(node.children) == 2
    print(stats)
    print(node.state.board)

def test_mcts_obvious_win():
    
    winning_board = np.array([
            [0, 0, 2, 2],
            [1, 1, 1, 1],
        ])
    
    counter = 0
    
    runs = 10
    
    for _ in range(runs):
    
        state = State(player = 2)
        state.board = np.array([
            [0, 0, 2, 2],
            [1, 0, 1, 1],
            ])
        
        root = Node(None, state)
        
        node, _ = mcts(root, state)
        
        if np.array_equal(winning_board, node.state.board):
            counter += 1
    
    

    assert counter == runs
    
    
def test_mcts_obvious_loose():
        
    state = State(player = 1)
    state.board = np.array([
        [0, 0, 2, 1],
        [0, 0, 2, 2],
        [0, 0, 2, 1],
        [1, 0, 1, 1],
    ])
    
    root = Node(None, state)
    
    node, _ = mcts(root, state)
    
    print(node.state.board)       
   
        


    
    
if __name__ == "__main__":
    test_mcts_obvious_loose()
    