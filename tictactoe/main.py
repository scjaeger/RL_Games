from game.state import State
from game.node import Node
from ai_sj.mcts import mcts
import matplotlib.pyplot as plt
import random
from utils.utils import plot_turn

if __name__ == "__main__":
  
    # initialize game
    state = State(player = 1)
    
    # initialize player
    name_1 = "Sebastian"
    sj_root = Node(None, state)
    
    # initialize player
    name_2 = "Random Randy" # enter losing player here ;)
    
    # shuffle players to randomize start
    players = [name_1, name_2]
    random.shuffle(players)
    print(f"{players[0]} starts marked as {state.player}")

    game_stats = {
        1: {
            "name": players[0],
            "unexplored nodes": [],
            "time left": [],
            "loops": []
        },
        2: {
            "name": players[1],
            "unexplored nodes": [],
            "time left": [],
            "loops": []
        },
    }
    
    round = 0
    
    # start game
    while not state.game_over:
        
        # loop through players
        for player in players:
            
            # start player algorithm, updating the game state
            if player == name_1:
                # update game information
                round += 1
                player_num = state.player
                
                # make turn
                sj_root, stats = mcts(sj_root, state)
                
                # feed statistics
                game_stats[player_num]["unexplored nodes"].append(stats["unexplored children"])
                game_stats[player_num]["time left"].append(stats["time left"])
                game_stats[player_num]["loops"].append(stats["loops"])
                
                # update state
                state = sj_root.state
                
                # plot current state
                plot_turn(state, game_stats, round)
            
            # start player algorithm, updating the game state
            elif player == name_2:
                round += 1
                
                action = random.choice(state.get_actions())     # < -- delete
                
                state = state.perform_action(action)            # <-- Enter algorithm here
                
                plot_turn(state, game_stats, round)
            
            
            
            if state.game_over:
                break
    
    
    print(f"\nGAME OVER\n\nPlayer {state.winner} won!\n")
    print(state.board)