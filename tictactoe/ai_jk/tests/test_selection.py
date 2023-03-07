from ai_jk.mcts.Node import Node
from ai_jk.phases.selection import start_selection_phase, get_uct_scores


def test_start_selection_phase():
    node = Node(None, None, None)
    assert start_selection_phase(node) == node

def test_get_uct_scores():
    root = Node(None, None, None)
    node1 = Node(root, None, None)
    node2 = Node(root, None, None)
    node3 = Node(root, None, None)
    root.children.append(node1)
    root.children.append(node2)
    root.children.append(node3)

    root.visits = 10
    node1.visits = 4
    node2.visits = 3
    node3.visits = 3

    node1.value = 3
    node2.value = 1
    node3.value = 2

    assert get_uct_scores(root) == [[0.6793567823462866, 0], [0.5380434808130777, 1], [0.6380434808130777, 2]]