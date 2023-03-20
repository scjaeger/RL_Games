from ai_jk.mcts.Node import Node
import math


def start_selection_phase(node):
    while(node.is_fully_expanded):
        scores = get_uct_scores(node)
        index = get_best_uct_node_index(scores)
        node = node.children[index]    

    return node


def get_uct_scores(node):
    scores = []
    for index, child in enumerate(node.children):
        if child.subtree_fully_expanded:
            score = -math.inf
        else:
            score = child.get_UCT_score()
        scores.append([score, index])

    return scores


def get_best_uct_node_index(scores):
    scores.sort(reverse=True)
    return scores[0][1]


if __name__ == "__main__":
    pass