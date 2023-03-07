import time
from ai_jk.mcts.Node import Node
from ai_jk.phases.selection import start_selection_phase
from ai_jk.phases.expansion import start_expansion_phase
from ai_jk.phases.simulation import start_simulation_phase
from ai_jk.phases.backpropagation import start_backpropagation_phase

from game.state import State

class MCTS():
    def __init__(self):
        self.root = None

    def do_mcts(self, state):
        root = Node(None, state, None)

        t = time.process_time()
        elapsed_time = 0

        while (elapsed_time <= 1):
            node = start_selection_phase(root)
            node = start_expansion_phase(node)
            node, state = start_simulation_phase(node)
            start_backpropagation_phase(node, state)

            elapsed_time = time.process_time() - t

        node = self.get_best_child()

        return node.state


    def is_initial_root_state(self, state):
        pass

    def find_state_in_tree(self, state):
        pass
        #state.compare needed

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
    state = State(player = 1)
    state.board = np.array([
        [1, 0, 0],
        [2, 0, 0],
        [0, 0, 0],
    ])

    mcts = MCTS()
    state = mcts.do_mcts(state)
    print(state)