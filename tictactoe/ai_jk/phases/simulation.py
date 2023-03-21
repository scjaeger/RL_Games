import random

def start_simulation_phase(node):
    if is_leaf(node):
        return node, node.state
    else:
        state = do_simulation(node)
        return node, state


def is_leaf(node):
    if (node.state.game_over):
        node.subtree_fully_expanded = True
        return True
    else:
        return False


def do_simulation(node):
    state = node.state
    
    while(not state.check_game_end()):
        actions = state.get_actions()
        max_value = len(actions) - 1
        randint = random.randint(0, max_value)
        action = actions[randint]     
        state = state.perform_action(action)

    return state


if __name__ == "__main__":
    pass