from game.state import State
from game.node import Node
from ai_sj.mcts import get_fav_child


def test_get_fav_child():
    
    state = State()
    root = Node(None, state)
    
    child_1 = Node(root, state.perform_action((0,0)))
    child_1.times_tested += 3
    child_1.times_won += 2
    root.children.append(child_1)	
    
    child_2 = Node(root, state.perform_action((0,1)))
    child_2.times_tested += 2
    child_2.times_won += 0
    root.children.append(child_2)	
    
    child_3 = Node(root, state.perform_action((1,1)))
    child_3.times_tested += 1
    child_3.times_won += 1
    root.children.append(child_3)
    
    assert get_fav_child(root) == child_3