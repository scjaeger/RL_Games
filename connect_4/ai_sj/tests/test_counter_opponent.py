from game.node import Node
from game.state import State
from ai_sj.mcts import counter_opponent
import numpy as np


def test_counter_opponent_no_winner():
    state = State()
    root = Node(None, state)
    
    for action in state.get_actions():
        child = Node(root, state.perform_action(action))
        
        for next_action in child.state.get_actions():
            grandchild = Node(root, child.state.perform_action(next_action))
            child.children.append(grandchild)
            
        root.children.append(child)
        
    assert type(counter_opponent(root)) == list
    assert len(counter_opponent(root)) == len(root.children)
    

def test_counter_opponent_winner():
    
    winning_board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [1, 2, 1, 1, 2, 2, 0],
    ])
    
    counter = 0
    runs = 10
    
    for _ in range(runs):
        state = State(player = 1)
        state.board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [1, 0, 1, 1, 2, 2, 0],
        ])

        root = Node(None, state)
        
        for action in state.get_actions():
            child = Node(root, state.perform_action(action))
            
            for next_action in child.state.get_actions():
                grandchild = Node(root, child.state.perform_action(next_action))
                child.children.append(grandchild)
                
            root.children.append(child)
            
        if np.array_equal(winning_board, counter_opponent(root)[0].state.board):
            counter += 1
