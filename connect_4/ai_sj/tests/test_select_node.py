from game.state import State
from game.node import Node
from ai_sj.selection import select_node
from ai_sj.expansion import choose_random
from ai_sj.backpropagation import backpropagate
from ai_sj.simulation import simulate
import numpy as np


def test_select_node_forced_random():
    state = State(player = 2)
    state.board = np.array([
        [1, 2, 1, 2, 1, 2, 0],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    root = Node(None, state)
    
    new_node = select_node(root)
    
    assert state.is_equal(new_node.state)
    assert new_node.parent == None
    assert new_node == root
    assert new_node.state.player == 2
    

def test_select_node_full_board():
    state = State(player = 1)
    state.board = np.array([
        [0, 2, 1, 2, 2, 1, 1],
        [2, 1, 2, 1, 1, 2, 2],
        [1, 1, 2, 2, 2, 1, 1],
        [2, 1, 2, 1, 1, 2, 2],
        [1, 2, 1, 2, 2, 1, 1],
        [1, 1, 2, 2, 1, 2, 2],
    ])
    
    state = state.perform_action(0)
    
    root = Node(None, state)
    
    assert select_node(root) is False
    
    
    

    
def test_select_node_multi_layer():
    state = State(player = 1)
    
    state.board = np.array([
        [0, 0, 1, 2, 2, 1, 1],
        [0, 0, 2, 1, 1, 2, 2],
        [2, 1, 2, 2, 2, 1, 1],
        [2, 1, 2, 1, 1, 2, 2],
        [1, 2, 1, 2, 2, 1, 1],
        [1, 1, 2, 2, 1, 2, 2],
    ])
    
    root = Node(None, state)
        
    for _ in range(17):
        node = select_node(root)
        if node:
            node = choose_random(node)
            winner = simulate(node.state)
            backpropagate(node, winner)
    
            
    assert len(root.children) == 2
    
    winner = 0
    for layer1_node in root.children:
        assert len(layer1_node.children) == 2
        for layer2_node in layer1_node.children:
            if 1 in [layer2_node.state.board[0, 0], layer2_node.state.board[0, 1]]:
                assert len(layer2_node.children) == 1
            elif 1 in [layer2_node.state.board[1, 0], layer2_node.state.board[1, 1]]:
                assert len(layer2_node.children) == 2
            
            for layer3_node in layer2_node.children:
                if layer3_node.state.board[0, 0] == 2 and layer3_node.state.board[1, 0] == 2:
                    winner += 1
                    assert layer3_node.explored
                    assert layer3_node.state.winner == 2
                else:
                    assert len(layer3_node.children) == 1
                    for layer4_node in layer3_node.children:
                        assert layer4_node.explored
                        assert layer4_node.state.winner == 0
                        
    assert winner == 1
    assert select_node(root) is False
    


if __name__ == "__main__":
    test_select_node_multi_layer()