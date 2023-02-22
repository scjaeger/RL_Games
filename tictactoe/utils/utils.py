from game.node import Node
import numpy as np
import matplotlib.pyplot as plt
from game.state import State


def get_valid_children(node: Node) -> list:
    return [child for child in node.children if not child.explored]

def get_children_wins(children: "list[Node]") -> np.array:
    return np.array([child.times_won for child in children])

def get_children_tests(children: "list[Node]") -> np.array:
    return np.array([child.times_tested for child in children])

def plot_board(players: "list[str]", board: np.array, ax: plt.axes):
    r = np.where((board == 1) | (board == 0), 255, 0)
    g = np.where(board == 0, 255, 0)
    b = np.where((board == 2) | (board == 0), 255, 0)
    
    rgb = np.dstack((r, g, b))
    
    ax.axvline(0.5, color = "black")
    ax.axvline(1.5, color = "black")
    ax.axhline(0.5, color = "black")
    ax.axhline(1.5, color = "black")

    ax.set_title(f"{players[0]} in red, {players[1]} in blue")
    
    ax.imshow(rgb, vmin = 0, vmax = 255)
    
    return None

def plot_stats(game_stats: dict, ax: plt.axes):
    # unexplored nodes
    ax[1].set_title("unexplored nodes")
    nodes_1 = game_stats[1]["unexplored nodes"]
    ax[1].plot(nodes_1, label = game_stats[1]['name'], color = "red")
    nodes_2 = game_stats[2]["unexplored nodes"]
    ax[1].plot( nodes_2, label = game_stats[2]['name'], color = "blue")
    ax[1].legend()
    
    # time left 
    ax[2].set_title("time left")
    nodes_1 = game_stats[1]["time left"]
    ax[2].plot(nodes_1, label = game_stats[1]['name'], color = "red")
    nodes_2 = game_stats[2]["time left"]
    ax[2].plot( nodes_2, label = game_stats[2]['name'], color = "blue")
    ax[2].legend()
    
    # loops 
    ax[3].set_title("Exploration loops per turn")
    nodes_1 = game_stats[1]["loops"]
    ax[3].plot(nodes_1, label = game_stats[1]['name'], color = "red")
    nodes_2 = game_stats[2]["loops"]
    ax[3].plot( nodes_2, label = game_stats[2]['name'], color = "blue")
    ax[3].legend()

def plot_turn(state: State, game_stats: dict, round: int):
    
    fig, ax = plt.subplots(ncols = 4, figsize = (20, 5))
    
    fig.suptitle(f"{game_stats[state.change_player()]['name']}s Turn")
    
    plot_board([game_stats[1]['name'], game_stats[2]['name']], state.board, ax[0])
    
    plot_stats(game_stats, ax)
    
    plt.savefig(f"game_stats/round{round}")

    
    
if __name__ == "__main__":
    game_stats = {
    1: {
        "name": "Earl",
        "unexplored nodes": [9, 4, 1],
        "time left": [0.008, 0.007, 0.998],
        "loops": [5000, 4000, 23]
        },
    2: {
        "name": "Randy",
        "unexplored nodes": [8, 1, 0],
        "time left": [0.0001, 0.002, 0.999],
        "loops": [6000, 3432, 700]
        },
    }
       
    state = State()
    state.board = np.array([[1, 2, 0], [2, 0, 1], [0, 1, 0]])
    
    plot_turn(state, game_stats, 2)