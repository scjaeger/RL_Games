from game.node import Node
import random

def simulate(node: Node, show_steps: bool = False) -> int:
    
    try:
        state = node.state

        while not state.winner and not state.game_over:
            action = random.choice(state.get_actions())
            
            state = state.perform_action(action)
            
            if show_steps:
                print(state.board)
                
        if state.winner:
            return state.winner
        else:
            return 0
        
    except IndexError as error:
        print(f"IndexError in simulate --> {error}")
        return False
    except Exception as error:
        print(f"Error in simulate --> {error}")
        return False



if __name__ == "__main__":
    from game.state import State
    import numpy as np
    state = State(player = 1)
    
    state.winner = None
    state.game_over = True
    
    node = Node(None, state)
    
    print(simulate(node))