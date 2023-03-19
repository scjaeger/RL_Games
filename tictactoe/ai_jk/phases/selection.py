from ai_jk.mcts.Node import Node


def start_selection_phase(node):
    while(node.is_fully_expanded):
        scores = get_uct_scores(node)
        index = get_best_uct_node_index(scores)
        node = node.children[index]    

    return node


def get_uct_scores(node):
    scores = []
    for index, node in enumerate(node.children):
        score = node.get_UCT_score()
        scores.append([score, index])

    return scores


def get_best_uct_node_index(scores):
    scores.sort(reverse=True)
    return scores[0][1]


if __name__ == "__main__":
    pass