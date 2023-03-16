from game.node import Node
from game.state import State
from ai_sj.mcts import counter_opponent
import numpy as np


def test_counter_opponent_no_winner():
    state = State()
    root = Node(None, state)
    
    for action in state.get_actions():
        child = Node(root, state.perform_action(action))
        root.children.append(child)
        
        for next_action in child.state.get_actions():
            grandchild = Node(root, child.state.perform_action(next_action))
            child.children.append(grandchild)
            
        
        
    assert type(counter_opponent(root)) == list
    assert len(counter_opponent(root)) == len(root.children)
    
def test_counter_opponent_single_choice():
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
        
    assert len(counter_opponent(root)) == 1
    
    

def test_counter_opponent_winner():
    
    state = State(player = 1)
    state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [1, 0, 1, 1, 2, 2, 0],
    ])
    
    win_state = state.perform_action(1)
    
    counter = 0
    runs = 100
    
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
            
        if win_state.is_equal(counter_opponent(root)[0].state):
            counter += 1

    assert counter == runs
