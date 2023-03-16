from game.node import Node
import random



def choose_random(node: Node) -> Node:
    
    action = random.choice(node.edges)
    node.edges.remove(action)
    
    state = node.state.perform_action(action)
    new_node = Node(node, state)
    node.children.append(new_node)
    return new_node