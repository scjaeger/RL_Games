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
    
    for i in range(6):
        ax.axvline(i + 0.5, color = "black")
    for i in range(5):
        ax.axhline(i + 0.5, color = "black")

    ax.set_title(f"{players[0]} in red, {players[1]} in blue")
    
    ax.imshow(rgb, vmin = 0, vmax = 255)
    
    return None

def make_bar_plot(game_stats: dict, stat_name: str, ax: plt.axes):
    
    ax.set_title(stat_name)
    for i, color, shift in zip([1, 2], ["red", "blue"], [- 0.2, 0.2]):
        if i == 2:
            color = "red"
        else:
            color = "blue"
            
        stat = game_stats[i][stat_name]
        X_axis = np.arange(len(stat))
        ax.bar(X_axis + shift, stat, 0.4, label = game_stats[i]["name"], color = color, alpha = 0.5)
        
    ax.legend()



def plot_turn(state: State, game_stats: dict, round: int):
    
    fig, ax = plt.subplots(ncols = 4, figsize = (20, 5))
    
    fig.suptitle(f"{game_stats[state.change_player()]['name']}s Turn")
    
    plot_board([game_stats[1]['name'], game_stats[2]['name']], state.board, ax[0])
    
    make_bar_plot(game_stats, "unexplored nodes", ax[1])
    make_bar_plot(game_stats, "time left", ax[2])
    make_bar_plot(game_stats, "loops", ax[3])

    
    plt.savefig(f"game_stats/round{round}")
    plt.close(fig)
    
    
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