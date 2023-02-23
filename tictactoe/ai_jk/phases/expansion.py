from ai_jk.mcts.Node import Node

def start_expansion_phase(node):
    action = node.actions.pop(0)
    new_state = node.state.get_next_state(node.state, action)
    new_player = node.change_player()
    new_node = Node(node.parent, new_state, new_player)
    node.children.append(new_node)
    check_node_expanded(node)

    return new_node

def check_node_expanded(node):
    if not node.actions:
        node.is_fully_expanded = True

if __name__ == "__main__":
    pass