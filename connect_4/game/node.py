from game.state import State

class Node():
    def __init__(self, parent, state: State):
        self.state = state
        
        self.parent = parent
        self.edges = self.state.get_actions()
        self.children  = []
        
        self.times_tested = 0
        self.times_won = 0
        self.explored = False if self.edges else True