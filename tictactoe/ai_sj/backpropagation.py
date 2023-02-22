from game.node import Node

def update_exploration_status(node: Node)-> bool:
    try:
        children = [child for child in node.children if not child.explored]
        if node.edges or children:
            return False
        else:
            return True
    
    except Exception as error:
        print(f"Error in backpropagation.update_exploration_status --> {error}")
        
        
def backpropagate(node: Node, winner: int) -> None:
    
    try:
        while node.parent:
            node.times_tested += 1
            
            if not node.explored:
                node.explored = update_exploration_status(node)
            
            if winner == 0:
                node.times_won += 0.3
            elif node.state.change_player() == winner:
                node.times_won += 1
                
            node = node.parent
            
        node.times_tested += 1
        
    except Exception as error:
        print(f"Error in backpropagation.backpropagate --> {error}")
        return False
    
    else:
        return None


if __name__ == "__main__":
    from game.state import State
    import numpy as np 
    
    state = State(player=1)
    state.board = np.array([
        [1, 0, 1],
        [2, 0, 2],
        [0, 0, 0],
    ])
    
    state = state.perform_action((0, 1))
    
    print(state.game_over)
    print(state.winner)