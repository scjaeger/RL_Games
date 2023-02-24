from ai_sj.mcts import mcts
from game.node import Node
from game.state import State


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