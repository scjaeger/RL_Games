from game.state import State
from game.node import Node
from ai_sj.simulation import simulate
import numpy as np

def test_simulate_one_left():
    state = State(player = 1)
    state.board = np.array([
        [1, 2, 1, 2, 1, 2, 0],
        [1, 2, 1, 2, 1, 2, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    node = Node(None, state)
    
    assert simulate(node.state) == 2
    
    
def test_simulate_full_draw():
    state = State(player = 1)
    
    state.winner = None
    state.game_over = True
    
    node = Node(None, state)
    
    assert simulate(node.state) == 0
    
def test_simulate_full_two_wins():
    state = State(player = 2)

    state.winner = 2
    state.game_over = True
    
    node = Node(None, state)
    
    assert simulate(node.state) == 2
    
def test_simulate_full_win_no_attributes():
    state = State(player = 1)
    state.board = np.array([
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    node = Node(None, state)
    
    assert simulate(node.state) == False
    
    
def test_simulate_forced_win():
    state = State(player = 2)
    state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [1, 0, 1, 1, 2, 0, 2],
    ])
    
    root = Node(None, state)
    
    node = Node(root, state.perform_action(1))
    
    winner = simulate(node.state)
    
    assert winner == 1
    
    
def test_simulate_obvious_win():
    state = State(player = 2)
    state.board = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [1, 0, 1, 1, 2, 0, 2],
    ])
    
    node = Node(None, state)
    
    one_wins = 0
    two_wins = 0
    draw = 0
    for _ in range(100):
        winner = simulate(node.state)
        if winner == 1:
            one_wins += 1
        elif winner == 2:
            two_wins += 1
        elif winner == 0:
            draw += 0
    
    assert one_wins > two_wins and one_wins > draw