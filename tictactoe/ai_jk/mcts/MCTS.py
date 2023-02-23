import time
from ai_jk.mcts.Node import Node

class MCTS():
    def __init__(self, root, player):
        self.root = Node(None, None, None)
        self.player = player

    def do_mcts(self, state):

        if (is_initial_root_state(state))
        t = time.process_time()
        elapsed_time = 0

        while (elapsed_time <= 1):
            elapsed_time = time.process_time() - t


    def is_initial_root_state(self, state):
        if 