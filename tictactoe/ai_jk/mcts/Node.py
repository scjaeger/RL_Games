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
        self.is_leaf = False
        self.subtree_fully_expanded = False
        self.value = 0
        self.visits = 0
    

    def change_player(self):
        if (self.player):
            return False
        else:
            return True

    '''
    def is_fully_expanded(self) -> bool:
        if ((self.expanded == True) or
            ((len(self.actions) == 0) and
            (len(self.children) != 0))):
             return True
        else:
             return False
    '''

    def get_UCT_score(self):
        exploitation_score = self.value / self.parent.visits
        exploration_score = EXPLORATION_VALUE * math.sqrt((math.log(self.parent.visits)/self.visits))
        return exploitation_score + exploration_score
        
    
    def get_exploitation_score(self):
        return self.value / self.parent.visits

if __name__ == "__main__":
    root = Node(None, None, None)
    root.visits = 2
    node = Node(root, None, None)
    node.visits = 1

    test = node.get_UCT_score()
    print(round(test, 2))