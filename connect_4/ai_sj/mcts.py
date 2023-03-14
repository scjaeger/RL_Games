from game.state import State
from game.node import Node
from ai_sj.selection import select_node
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
            
            print(f"possible nodes: {len(children)}")
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

    print(f"edges {root.edges}")
    
    start_time = time.time()
    
    loops = 0
    
    while True:
        loops += 1
        node = select_node(root)

        if node:
            winner = simulate(node.state)
            backpropagate(node, winner, root.state.player)
        
        if not get_valid_children(root) or time.time() - start_time > calc_time * safety_factor or loops > 20000:
            break
        
    top_node = get_fav_child(root)
    time_left = calc_time - (time.time() - start_time)
    stats = {
        "unexplored children": len(get_valid_children(root)),
        "time left": time_left,
        "loops": loops
    }
    # print(f"children: {len(root.children)}")
    # print(f"times_tested: {[child.times_tested for child in root.children]}")
    # print(f"times_won: {[child.times_won for child in root.children]}")
    # print(f"top node: children {len(top_node.children)}")
    
    return top_node, stats
    

        
if __name__ == "__main__":
    
    state = State(player = 1)
    root = Node(None, None)

    for i in range(100):
        root, stats = mcts(root, state)
        state = root.state
        if state.game_over:
            break
        
        action = random.choice(state.get_actions())
        state = state.perform_action(action)
        if state.game_over:
            break
        
    print(state.board)
        