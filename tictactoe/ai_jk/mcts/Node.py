import math
from ai_jk.constants import EXPLORATION_VALUE

class Node:
    def __init__(self, parent, state, player):   
        self.parent = parent
        self.state = state
        self.player = player
        self.actions = []
        self.children = []
        self.initiated = False
        self.is_fully_expanded = False
        self.subtree_fully_expanded = False
        self.is_leaf = True
        self.value = 0
        self.visits = 0

    def get_UCT_score(self):
        return self.get_exploitation_score() + self.get_exploration_score()
        
    
    def get_exploitation_score(self):
        return self.value / self.visits
    
    
    def get_exploration_score(self):
        return EXPLORATION_VALUE * math.sqrt((math.log(self.parent.visits)/self.visits))

if __name__ == "__main__":
    pass