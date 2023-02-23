import time
from ai_jk.mcts.Node import Node

class MCTS():
    def __init__(self, root, player):
        self.root = Node(None, None, None)
        self.player = player

    def do_mcts(self, state):

        if (self.is_initial_root_state(state)):
            pass

        t = time.process_time()
        elapsed_time = 0

        while (elapsed_time <= 1):
            elapsed_time = time.process_time() - t


    def is_initial_root_state(self, state):
        pass

    def find_state_in_tree(self, state):
        pass

    def get_best_child(self):
        pass

