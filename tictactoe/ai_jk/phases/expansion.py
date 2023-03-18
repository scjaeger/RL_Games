from ai_jk.mcts.Node import Node

def start_expansion_phase(node):
    first_node_initiation(node)
    if not check_node_expanded(node):
        action = choose_action(node)
        node = do_node_expansion(node, action)
    
    return node


def first_node_initiation(node):
    if (node.visits == 0):
        node.actions = node.state.get_actions()


def choose_action(node):
    action = node.actions.pop(0)
    return action


def do_node_expansion(node, action):
    new_state = node.state.perform_action(action)
    new_player = node.change_player()
    new_node = Node(node, new_state, new_player)
    node.children.append(new_node)
    return new_node

def check_node_expanded(node):
    if not node.actions:
        node.is_fully_expanded = True
        return True
    else:
        return False

if __name__ == "__main__":
    pass