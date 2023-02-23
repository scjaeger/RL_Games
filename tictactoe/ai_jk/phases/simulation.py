import random

def start_simulation_phase(node):
    if is_leaf(node):
        return node, node.state
        
    state = do_simulation(node)

    return node, state


def is_leaf(node):
    if (node.state.is_final_state()):
        node.is_leaf = True
        node.subtree_fully_expanded = True
        return True
    else:
        return False


def do_simulation(node):
    state = node.state
    
    while(not state.is_final_state()):
        actions = state.get_actions()
        max_value = len(actions) - 1
        randint = random.randint(0, max_value)
        action = actions[randint]     
        state = state.get_next_state(state, action)

    return state


if __name__ == "__main__":
    pass