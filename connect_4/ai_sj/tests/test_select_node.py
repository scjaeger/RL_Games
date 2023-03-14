from game.state import State
from game.node import Node
from ai_sj.selection import select_node
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
    
    new_board = np.array([
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2],
        [2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1],
    ])
    
    assert np.array_equal(new_node.state.board, new_board)
    assert new_node.parent == root
    assert new_node.state.player == 1
    
    
def test_select_node_sum_edges_and_children():
    state = State()
    
    root = Node(None, state)
    
    initial_edges = len(root.edges)
    initial_children = len(root.children)
    
    for _ in range(3):
        new_node = select_node(root)
        
    final_edges = len(root.edges)
    final_children = len(root.children)
    
    assert final_edges == initial_edges - 3
    assert final_children == initial_children + 3
    

def test_select_node_full_board():
    state = State(player = 1)
    state.board = np.array([
        [1, 2, 1, 2, 2, 1, 1],
        [2, 1, 2, 1, 1, 2, 2],
        [1, 1, 2, 2, 2, 1, 1],
        [2, 1, 2, 1, 1, 2, 2],
        [1, 2, 1, 2, 2, 1, 1],
        [1, 1, 2, 2, 1, 2, 2],
    ])
    
    root = Node(None, state)
    
    assert select_node(root) is False
    
    
def test_select_node_no_edges():
    state = State(player = 1)
    root = Node(None, state)
    
    for _ in range(len(root.edges)):
        select_node(root)
        root.times_tested += 1
    
    for child in root.children:
        child.times_tested += 1
        
    root.children[3].times_won += 1

    new_node = select_node(root)
    
    assert new_node in root.children[3].children    
    

def test_select_node_fully_explored():
    state = State(player = 1)
    root = Node(None, state)
    
    for _ in range(len(root.edges)):
        select_node(root)
        root.times_tested += 1
    
    for child in root.children:
        child.times_tested += 1
        child.explored = True
    
    assert select_node(root) is False
    
    
def test_select_node_obvious_choice():
    state = State(player = 1)
    
    state.board = np.array([

        [0, 0, 2, 2],
        [1, 0, 1, 1],
    ])
    
    root = Node(None, state)
    
    for i in range(100):
        node = select_node(root)
        if node:
            winner = simulate(node.state)
            backpropagate(node, winner)
            
            # if node.state.board[1, 1] == 1:
            #     print(i)
            #     print(node.state.board)
            
            # depth = 0
            # while node.parent:
            #     depth += 1
            #     node = node.parent
            # print(f"depth {depth}")
            
        else:
            print(f"break at {i}")
            break

    for child in root.children:
        print(f"player: {child.state.player}")
        print(f"layer 1: {child.times_won/child.times_tested}")
        print(child.state.board)
        print("\n")
        
        for grandchild in child.children:
            print(f"player: {grandchild.state.player}")
            print(f"layer 2: {grandchild.times_won/grandchild.times_tested}")
            print(grandchild.state.board)
            print("\n")
        



def test_select_node_multi_layers():
    
    state = State(player = 1)
    
    root = Node(None, state)
    
    
        
    for _ in range(len(state.get_actions())):
        layer1_child = select_node(root)
        # layer1_child.times_won = np.random.randint(0, 2)
        layer1_child.times_tested = 1
        root.times_tested += 1
     
    root.children[0].times_won += 1
    
    print([child.times_tested for child in root.children])
    
    layer2_child = select_node(root)
    layer2_child.times_tested += 1
    layer2_child.times_won += 1
    root.children[0].times_won += 1
    
    print(layer2_child.state.board)
    print(select_node(root).state.board)


    # print(len(root.children))

if __name__ == "__main__":
    test_select_node_obvious_choice()
