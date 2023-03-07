import time
from ai_jk.mcts.Node import Node

class MCTS():
    def __init__(self, root, player):
        self.root = root
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
    root = Node(None, None, None)
    node1 = Node(root, 1, None)
    node2 = Node(root, 2, None)
    node3 = Node(root, 2, None)
    node4 = Node(root, 2, None)
    
    root.visits = 4
    node1.visits = node2.visits = node3.visits = node4.visits = 1
    node1.value = 2
    node2.value = node3.value = node4.value = 1

    root.children.append(node1)
    root.children.append(node2)
    root.children.append(node3)
    root.children.append(node4)

    mcts = MCTS(root, None)
    
    print(mcts.get_best_child())