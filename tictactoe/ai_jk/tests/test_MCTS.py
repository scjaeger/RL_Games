from ai_jk.mcts.MCTS import MCTS
from ai_jk.mcts.Node import Node

def test_get_best_child():
    root = Node(None, None, None)
    node1 = Node(root, 1, None)
    node2 = Node(root, 2, None)
    node3 = Node(root, 2, None)
    node4 = Node(root, 2, None)
    
    root.visits = 4
    node1.visits = node2.visits = node3.visits = node4.visits = 1
    node1.value = 2
    node2.value = node3.value = node4.value = 1

    root.children.append(node1)
    root.children.append(node2)
    root.children.append(node3)
    root.children.append(node4)

    mcts = MCTS()
    mcts.root = root
    
    assert mcts.get_best_child().state == 1

    