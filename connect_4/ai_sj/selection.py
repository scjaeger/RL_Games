from game.node import Node
from utils.utils import get_valid_children, get_children_tests, get_children_wins
import numpy as np
import random


def choose_random(node: Node) -> Node:
    
    action = random.choice(node.edges)
    node.edges.remove(action)
    
    state = node.state.perform_action(action)
    new_node = Node(node, state)
    node.children.append(new_node)
    return new_node


def calculate_uct(children: "list[Node]", total_tests: int,  c: float = np.sqrt(2)) -> np.array:
    try:
        child_wins = get_children_wins(children)
        child_tests = get_children_tests(children)
        uct = (child_wins/child_tests) + c * np.sqrt(np.emath.log(total_tests) / child_tests)
        
    except Exception as error:
        print(f"Error in calculate_uct --> {error}")
    
    else:
        return uct

def choose_uct(node: Node, player: int) -> Node:
    try:
        total_tests = node.times_tested
        
        children = get_valid_children(node)
        
        uct = calculate_uct(children, total_tests)
        
        if node.state.player == player:
            value = np.amin(uct)
        else:
            value = np.amax(uct)
            
        index = random.choice(np.where(uct == value)[0])
        new_node = children[index]
        
        return new_node
    
    except Exception as error:
        print(f"Error in choose_uct --> {error}")
        return False
    
    
    
def select_node(node: Node) -> Node:
    try:
        if node.edges:
            return choose_random(node)
        
        else:
            player = node.state.player
            while get_valid_children(node):
                node = choose_uct(node, player)
                
            if node.edges:
                return choose_random(node)
            else:
                # print("Node should be marked as explored or tree is fully explored")
                return False
            
    except Exception as error:
        print(f"Error in select_node --> {error}")
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    from game.state import State
    from ai_sj.backpropagation import backpropagate
    
    
    state = State(player = 1)
    
    state.board = np.array([
        [0, 1, 1],
        [2, 2, 1],
        [2, 0, 2],
    ])
    
    root = Node(None, state)
    
    for i in range(100):
        node = select_node(root)
        if node:
            backpropagate(node, node.state.winner)
        else:
            break
    
    print(len(root.children))