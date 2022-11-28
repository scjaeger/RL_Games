from basic_tree.action import Action
from basic_tree.constants import MAX_MASS


class State():
    def __init__(self, actions, mass = 0, value = 0):
        self.max_mass = MAX_MASS
        self.mass = mass
        self.value = value
        self.actions = actions
        
    def do_action(self, action: Action):
        '''
        changes the state based on a given action
        
        return: new State object
        '''
        
        # add action's mass and value to state
        mass = self.mass + action.mass
        value = self.value + action.value

        # exclude actions already taken or exceeding the mass limit
        self.actions.remove(action)
        actions_left = self.possible_actions(action)
        
        return State(actions_left, mass, value)
    
    def possible_actions(self, last_action = None):
        '''
        returns a list of actions that can be made in the given state
        '''
        if last_action:
            possibilities = [action for action in self.actions if last_action.mass + action.mass + self.mass <= self.max_mass]
        return possibilities

    