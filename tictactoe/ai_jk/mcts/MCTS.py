import time
from ai_jk.mcts.Node import Node
from ai_jk.phases.selection import start_selection_phase
from ai_jk.phases.expansion import start_expansion_phase
from ai_jk.phases.simulation import start_simulation_phase
from ai_jk.phases.backpropagation import start_backpropagation_phase

from game.state import State

class MCTS():
    def __init__(self, player):
        self.player = player
        self.root = None

    def do_mcts(self, state):
        self.root = self.find_state_in_tree(state)
        #self.root = Node(None, state, state.player)
        
        t = time.process_time()
        elapsed_time = 0

        while (elapsed_time <= 1):
            node = start_selection_phase(self.root)
            node = start_expansion_phase(node)
            node, state = start_simulation_phase(node)
            start_backpropagation_phase(node, state)
            elapsed_time = time.process_time() - t

        node = self.get_best_child()
        self.root = node
        return node.state


    def find_state_in_tree(self, state):
        if self.root == None:
            return Node(None, state, state.player)
        else:
            for node in self.root.children:
                if node.state.is_equal(state):
                    node.parent = None
                    return node
                else:
                    return Node(None, state, state.player)
            

    def get_best_child(self):
        scores = []
        for index, node in enumerate(self.root.children):
            score = node.get_exploitation_score()
            scores.append([score, index])

        scores.sort(reverse=True)
        index = scores[0][1]
        best_child_node = self.root.children[index]
        
        return best_child_node


if __name__ == "__main__":
    import numpy as np
    state = State(player = 2)
    state.board = np.array([
        [2, 1, 0],
        [1, 2, 0],
        [0, 0, 0],
    ])

    mcts = MCTS(1)
    state = mcts.do_mcts(state)
    print("-----------------------")
    print(state.board)