from game.state import State
from game.node import Node
from ai_sj.simulation import simulate
import numpy as np

def test_simulate_one_left():
    state = State(player = 2)
    state.board = np.array([
        [1, 2, 1, 2, 1, 2, 0],
        [1, 2, 1, 2, 1, 2, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    node = Node(None, state)
    
    assert simulate(node) == 2
    
    
def test_simulate_full_draw():
    state = State(player = 1)
    
    state.winner = None
    state.game_over = True
    
    node = Node(None, state)
    
    assert simulate(node) == 0
    
def test_simulate_full_two_wins():
    state = State(player = 2)

    state.winner = 2
    state.game_over = True
    
    node = Node(None, state)
    
    assert simulate(node) == 2
    
def test_simulate_full_win_no_attributes():
    state = State(player = 1)
    state.board = np.array([
        [1, 2, 2],
        [2, 1, 1],
        [2, 2, 2],
    ])
    
    node = Node(None, state)
    
    assert simulate(node) == False
    