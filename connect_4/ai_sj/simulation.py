from game.state import State
import random

def simulate(state: State, show_steps: bool = False) -> int:
    
    try:

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

