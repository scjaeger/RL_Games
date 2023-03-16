from game.node import Node
from utils.utils import get_valid_children

def update_exploration_status(node: Node)-> bool:
    try:
        if node.state.winner or node.state.game_over:
            return True
        else:
            children = get_valid_children(node)
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
            elif node.state.player == winner:
                node.times_won += 1
                
            node = node.parent
            
        node.times_tested += 1
        node.explored = update_exploration_status(node)
        
    except Exception as error:
        print(f"Error in backpropagation.backpropagate --> {error}")
        return False
    
    else:
        return None


if __name__ == "__main__":
    pass