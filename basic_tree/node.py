from basic_tree.state import State
from basic_tree.action import Action
from random import choice

class Node():
    def __init__(self, parent, former_action: Action, state: State):
        self.parent = parent
        self.former_action = former_action
        self.children = []
        self.state = state
        self.exploration = 0
        self.value = 0
        self.is_leaf = False
    
    # extra function to avoid recursion that creates full tree
    def get_children(self) -> list:
        '''
        adds child layer to a given node
        
        return: list of children
        '''
        # prepare variables
        children = []
        actions = self.state.actions.copy()
        state = self.state
        
        # loop through possible actions
        for action in actions:
            # calcutlate action state of each action
            child_state = state.do_action(action)
            # add action to actions list as "do_action" method removes it
            state.actions.append(action)
            # append node based on action and state to children list
            children.append(Node(self, action, child_state))
        
        # classify node as leaf if no children found
        if len(children) == 0:
                self.is_leaf = True
                
        # add children to node and return list
        self.children = children
        return children
            
            
    def simulate_result(self) -> float:
        '''
        takes random path starting from self
        
        return: value of leaf state
        '''
        # create simulation state and loop variable
        simulation_state = self.state
        action_counter = len(simulation_state.actions)

        while action_counter > 0:
            # pick random action
            random_action = choice(simulation_state.actions)
            # update simulation state based on random action
            simulation_state = simulation_state.do_action(random_action)
            # check if state is final
            action_counter = len(simulation_state.actions)
          
        return simulation_state.value
        

