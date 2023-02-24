from game.state import State
from game.node import Node
from ai_sj.selection import choose_uct


def test_choose_uct_pick_first():
    state = State(player = 1)
    root = Node(None, state)
    
    for action in root.edges:
        new_state = state.perform_action(action)
        child = Node(root, new_state)
        child.times_tested += 1
        root.times_tested += 1
        root.children.append(child)
    
    root.children[0].times_won += 1
    
    new_node = choose_uct(root, 1)

    assert new_node == root.children[0]
    
def test_choose_uct_pick_fewest_tests():
    state = State(player = 1)
    root = Node(None, state)
    
    for action in root.edges:
        new_state = state.perform_action(action)
        child = Node(root, new_state)
        child.times_tested += 2
        child.times_won += 1
        root.times_tested += 2
        root.children.append(child)
    
    root.children[2].times_tested -= 1
    
    new_node = choose_uct(root, 1)

    assert new_node == root.children[2]
    assert type(new_node) == Node
    
def test_choose_uct_no_children():
    state = State(player = 1)
    root = Node(None, state)

    assert choose_uct(root, 1) is False
