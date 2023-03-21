
def start_backpropagation_phase(node, state):
    winner = state.winner
    do_backpropagation(node, winner)
    

def do_backpropagation(node, winner):
    while(node.parent != None):
        if (winner == None):
            node.value += 0.5
        elif (winner == node.player):
            node.value += 1
    
        node.visits += 1
        subtree_is_fully_expanded(node)
        node = node.parent

    if node.parent == None:
        node.visits +=1

def subtree_is_fully_expanded(node):
    if not node.is_leaf:
        is_fully_expanded = True
        for child in node.children:
            if (child.subtree_fully_expanded == False):
                is_fully_expanded = False
        
        node.subtree_fully_expanded = is_fully_expanded


if __name__ == "__main__":
    pass