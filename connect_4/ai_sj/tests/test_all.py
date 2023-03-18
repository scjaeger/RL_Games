# from game.node import Node
# from game.state import State
# from ai_sj.mcts import mcts
# import random


# def test_all_vs_random():

#     runs = 1
#     counter = 0

#     for _ in range(runs):

#         # initialize game
#         state = State(player = 1)
        
#         # initialize player
#         name_1 = "ai"
#         sj_root = Node(None, state)
        
#         # initialize player
#         name_2 = "Random" # enter losing player here ;)
        
#         # shuffle players to randomize start
#         players = [name_1, name_2]
#         random.shuffle(players)

#         game_stats = {
#             1: {
#                 "name": players[1],
#             },
#             2: {
#                 "name": players[0],
#             },
#         }
        
#         round = 0
        
#         # start game
#         while not state.game_over:
            
#             # loop through players
#             for player in players:
                
#                 # start player algorithm, updating the game state
#                 if player == name_1:
#                     # update game information
#                     round += 1
                    
#                     # make turn
#                     sj_root, _ = mcts(sj_root, state)
                    
#                     # update state
#                     state = sj_root.state

                
#                 # start player algorithm, updating the game state
#                 elif player == name_2:
#                     round += 1
                    
#                     action = random.choice(state.get_actions())     # < -- delete
                    
#                     state = state.perform_action(action)            # <-- Enter algorithm here
                
#                 if state.game_over:
#                     break
        
        
#         if game_stats[state.winner]['name'] == "ai":
#             counter += 1
            
#     assert counter == runs