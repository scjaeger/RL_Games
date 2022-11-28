from basic_tree.state import State
from basic_tree.action import Action
from basic_tree.node import Node
from basic_tree.tree import Tree
from random import randint, choice

def main():
    
    #### initialize ####
    
    # define parts to use
    all_parts = [Action(randint(12, 50), randint(1, 35)) for _ in range(100)]
    
    
    # set beginning state
    state = State(all_parts)
    random_state = State(all_parts)
    print(f"available parts: {[(action.mass, action.value) for action in state.actions]}")
    
    # create root node
    root = Node(None, None, state)
    root.get_children()

    # create initial Tree
    tree = Tree(root, root.children)
    
    # set loop variables
    game = True
    rounds = 0
    
    # start game
    while game:
        # track round numbers
        rounds += 1

        # decide which action to take
        action = tree.tree_search()
        
        # create a new game state based on action
        state = state.do_action(action)
        
        # make random action for comparison
        if len(random_state.actions) > 0:
            random_action = choice(random_state.actions)
            random_state = random_state.do_action(random_action)
        
        # end game if no actions possible
        if len(state.actions) == 0:
            game = False

        # show current actions
        print(f"action {rounds}: mass: {action.mass}, value: {action.value}")
    

    
    # show outcome
    print(f"\nfinal score\nmass: {state.mass}\nvalue: {state.value}")
    print(f"\nrandom score\nmass: {random_state.mass}\nvalue: {random_state.value}")
   
    
        



if __name__ == "__main__":
    main()   