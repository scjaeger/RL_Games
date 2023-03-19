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
        self.root = Node(None, state, 2)
        print("Root: ", self.root)
        print("-----------------------------------------------")
        counter = 0
        while (counter < 10):
            print("Counter: ", counter)
            print("Root fully expanded: ", self.root.is_fully_expanded)
            node = start_selection_phase(self.root)
            print("Selection: ", counter, node)
            print("Node actions: ", node.actions)
            print("Node chidlren: ", node.children)
            node = start_expansion_phase(node)
            print("Expansion: ", counter, node)
            print(node.state.board)
            node, state = start_simulation_phase(node)
            start_backpropagation_phase(node, state)
            counter += 1
            print("-----------------------------------------------")

        '''
        t = time.process_time()
        elapsed_time = 0

        while (elapsed_time <= 1):
            node = start_selection_phase(self.root)
            node = start_expansion_phase(node)
            node, state = start_simulation_phase(node)
            start_backpropagation_phase(node, state)

            elapsed_time = time.process_time() - t

        node = self.get_best_child()
        '''
        print(self.root.children)
        return node.state
        

    def is_initial_root_state(self, state):
        pass

    def find_state_in_tree(self, state):
        pass
        #state.compare needed

    def get_best_child(self):
        scores = []
        for index, node in enumerate(self.root.children):
            print(node.value, node.visits)
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
        [1, 2, 2],
        [2, 1, 0],
        [1, 0, 0],
    ])

    mcts = MCTS()
    state = mcts.do_mcts(state)
    print(state.board)