from ai_jk.mcts.Node import Node

def test_change_player():
    node1 = Node(None, None, 1)
    node2 = Node(None, None, 2)
    
    assert node1.change_player() == 2
    assert node2.change_player() == 1


def test_get_UCT_score():
    root = Node(None, None, None)
    node = Node(root, None, None)
    
    # only exploitation value
    root.visits = 1
    node.visits = 1
    node.value = 1
    assert node.get_UCT_score() == 1
    node.value = 0.5
    assert node.get_UCT_score() == 0.5

    # only exploration value
    node.value = 0
    root.visits = 2
    assert round(node.get_UCT_score(), 2) == 0.42
    
    node.value = 0.5
    assert round(node.get_UCT_score(), 2) == 0.67