from game.state import State
from game.node import Node
from ai_sj.selection import select_node
from ai_sj.simulation import simulate
from ai_sj.backpropagation import backpropagate
from utils.utils import get_valid_children, get_children_tests, get_children_wins

import numpy as np
import random
import time





def get_fav_child(root: Node) -> Node:
    
    wins =  get_children_wins(root.children)
    tests = get_children_tests(root.children)
    
    mean = wins/ tests

    top_index = np.argmax(mean)
    
    return root.children[top_index]
    

def set_root(node: Node, state: State) -> Node:
    if node:
        for child in node.children:
            if np.array_equal(child.state.board, state.board):
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
    timeout = time.time() + calc_time * safety_factor
    
    loops = 0
    
    while True:
        loops += 1
        node = select_node(root)

        if node:
            winner = simulate(node)
            backpropagate(node, winner)
        
        if not get_valid_children(root) or time.time() > timeout or loops > 20000:
            break
        
    top_node = get_fav_child(root)
    time_left = time.time() - start_time
    stats = {
        "unexplored children": len(get_valid_children(root)),
        "time left": time_left,
        "loops": loops
    }
    # print(stats)
    
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
        