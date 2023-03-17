from game.state import State
from game.node import Node
from ai_sj.selection import select_node
from ai_sj.expansion import choose_random
from ai_sj.simulation import simulate
from ai_sj.backpropagation import backpropagate
from utils.utils import get_valid_children, get_children_tests, get_children_wins

import numpy as np
import random
import time



def get_winning_child(root: Node) -> Node:
    
    for child in root.children:
        if child.state.winner:
            return child
        
    return None



def counter_opponent(root: Node) -> "list[Node]":

    possible_children = []
    
    for child in root.children:
        if child.children:
            opponent_win = False
            for grandchild in child.children:
                if grandchild.state.winner:
                    opponent_win = True
                    break
            if not opponent_win:
                possible_children.append(child)
              
    return possible_children


def choose_by_mean(children: "list[Node]") -> Node:
    
    wins = get_children_wins(children)
    tests = get_children_tests(children)
    
    mean = wins / tests
    
    top_index = np.argmax(mean)
    
    return children[top_index]


def get_fav_child(root: Node) -> Node:
    
    try:
    
        winner = get_winning_child(root)
        
        if winner:
            return winner
        
        else:
            children = counter_opponent(root)
            
            if not children:
                children = root.children

            top_node = choose_by_mean(children)
            
            return top_node
        
    except Exception as error:
        print(f"Error in get_fav_child --> {error}")
        return random.choice(root.children)
    
    

def set_root(node: Node, state: State) -> Node:
    if node:
        for child in node.children:
            if state.is_equal(child.state):
                root = child
                root.parent = None
                return root
            
        if not "root" in locals():
            return Node(None, state)
        
    else:
        return Node(None, state)
        
 
def mcts(node: Node, state: State, calc_time: float = 1.0, safety_factor: float = 0.99) -> Node:

    root = set_root(node, state)
    
    start_time = time.time()
    
    loops = 0
    
    while True:
        loops += 1
        node = select_node(root)
        if node:
            node = choose_random(node)
            winner = simulate(node.state)
            backpropagate(node, winner)
        
        if not get_valid_children(root) or time.time() - start_time > calc_time * safety_factor or loops > 20000:
            break
        
    top_node = get_fav_child(root)
    # print(f"top node: {len(top_node.children)} children")
    time_left = calc_time - (time.time() - start_time)
    stats = {
        "unexplored children": len(get_valid_children(root)),
        "time left": time_left,
        "loops": loops
    }
    
    return top_node, stats

        
if __name__ == "__main__":
    state = State(player = 1)
    
    # state.board = np.array([
    #         [0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0],
    #         [1, 0, 1, 1, 2, 2, 2],
    #         ])
    
    state.board = np.array([
            [0, 0, 1, 2, 2, 1, 1],
            [0, 0, 2, 1, 1, 2, 2],
            [2, 1, 2, 2, 2, 1, 1],
            [2, 1, 2, 1, 1, 2, 2],
            [1, 2, 1, 2, 2, 1, 1],
            [1, 1, 2, 2, 1, 2, 2],
            ])
    
    root = Node(None, state)
    
    node, _ = mcts(root, state)
    
    print("\n", f"ROOT --> {len(node.parent.children)} children")
    for child in node.parent.children:
        print("\n")
        print(f"timeswon: {child.times_won}")
        print(f"times_tested: {child.times_tested}")
        print(f"{len(child.children)} children")
        print(child.state.board)

    
    
    print("\n", f"NODE --> {len(node.children)} children")
    for child in node.children:
        print("\n")
        print(f"timeswon: {child.times_won}")
        print(f"times_tested: {child.times_tested}")
        print(f"{len(child.children)} children")
        print(child.state.board)
