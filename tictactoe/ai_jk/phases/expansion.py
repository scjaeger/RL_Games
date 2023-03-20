from ai_jk.mcts.Node import Node

def start_expansion_phase(node):
    first_node_initiation(node)
    if is_expandable(node):
        node.is_leaf = False
        action = choose_action(node)
        check_node_expanded(node)
        node = do_node_expansion(node, action)

    return node


def first_node_initiation(node):
    if (node.initiated == False):
        node.actions = node.state.get_actions()
        node.initiated = True


def is_expandable(node):
    # bug: state with game_over = True should not return any actions
    if (node.is_fully_expanded or node.state.game_over):
        return False
    else:
        return True

def choose_action(node):
    action = node.actions.pop(0)
    return action


def do_node_expansion(node, action):
    new_state = node.state.perform_action(action)
    new_player = node.state.change_player()
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