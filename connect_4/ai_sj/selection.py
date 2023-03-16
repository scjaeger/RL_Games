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

def choose_uct(node: Node) -> Node:
    try:
        total_tests = node.times_tested
        
        children = get_valid_children(node)
        
        uct = calculate_uct(children, total_tests)

        value = np.amax(uct)

            
        index = random.choice(np.where(uct == value)[0])
        new_node = children[index]
        
        return new_node
    
    except Exception as error:
        print(f"Error in choose_uct --> {error}")
        return False
    
    
    
def select_node(node: Node) -> Node:
    try:
        depth = 1
        if node.edges:
            # print(f"depth: {depth}")
            return choose_random(node)
        
        else:
            while get_valid_children(node):
                depth += 1
                node = choose_uct(node)
                
            if node.edges:
                # print(f"depth: {depth}")
                return choose_random(node)
            else:
                return False
            
    except Exception as error:
        print(f"Error in select_node --> {error}")
        return False

        
        