from basic_tree.action import Action
from basic_tree.node import Node
from basic_tree.constants import UCB_COEFFICIENT
import numpy as np
import time




class Tree():
    def __init__(self):
        self.searches = 0
    
    def tree_search(self, node: Node) -> Action:
        '''
        Decides which action to make by using upper confidence tree
        
        return: best estimated action to take
        '''
        
        # set time limit of 1 second for calculations
        timeout = time.time() + 1
        # falback is a break after 10000 repititions
        n = 0
        
        
        while True:
            n += 1
            # choose a node to investigate
            chosen_node = self.select_node(node)
            
            # simulate the value of a random walk starting from chosen node
            value = chosen_node.simulate_result()
            
            # backpropagate outcome to relevant nodes
            self.backpropagation(chosen_node, value)
            
            # break loop if time limit is reached
            if time.time() > timeout or n > 100:
                break
        
        # choose highest scroding node after investigation
        chosen_node = self.choose_action(node)
        
        if len(chosen_node.children) == 0 and not chosen_node.is_leaf:
            chosen_node.get_children() 

        return chosen_node  

        
    def choose_action(self, node)-> Node:
        '''
        takes an action based on it's current mean value
        
        return: highest scoring node
        '''

        mean_values = []
        for child in node.children:
            if child.exploration != 0:
                mean_values.append(child.value / child.exploration)
            else:
                mean_values.append(0)

        # grab choose node by highest mean value
        best_action_index = np.argmax(mean_values)
        chosen_node = node.children[best_action_index]
        
        return chosen_node
            
            
    def select_node(self, node: Node)-> Node:
        '''
        chooses a node for simulation based on ucb1 algorithm
        
        :param node: parent node, selections is made between its children
        
        return: node chosen for further investigation
        '''
        
        self.searches += 1
        # check for unexplored nodes
        exploration_tracker = [sub_node.exploration for sub_node in node.children]

        if 0 in exploration_tracker:
            # randomly pick one of the unknown nodes
            unexplored = np.where(np.array(exploration_tracker) == 0)[0]
            action_index = np.random.choice(unexplored)
            chosen_node = node.children[action_index]

        # check nodes for highest ucb value
        else:
            valuable_nodes = self.ucb(node.children)
            action_index = np.random.choice(valuable_nodes)
            potential_node = node.children[action_index]
            
            if len(potential_node.children) == 0 and potential_node.is_leaf is False:
                potential_node.get_children()
            
            # return node if it is a leaf 
            if potential_node.is_leaf:
                chosen_node = potential_node
            
            # go to tree's next layer from that node if possible
            else:
                chosen_node = self.select_node(potential_node)

        return chosen_node
    
    
    def ucb(self, layer: list)->list:
        '''
        ranks node based on their value and the amount of times they have been investigated
        
        :param list: list of nodes to choose between
        
        return: list of (equally) high rated nodes
        '''
        # prepare data
        mean_values = []
        explorations = []
        for child in layer:
            if child.exploration == 0:
                print("0 in ucb")
            else:
                explorations.append(child.exploration)
            if child.exploration != 0:
                mean_values.append(child.value / child.exploration)
            else:
                mean_values.append(0)
        mean_norm = self.normalize_vector(np.array(mean_values))
        
        # ucb calculation
        ucb_exploration = UCB_COEFFICIENT * np.sqrt(np.log(self.searches)/explorations)
        choice_vector = mean_norm + ucb_exploration
        favorite = np.amax(choice_vector)
        possible_actions = np.where(choice_vector == favorite)[0]
        return possible_actions

    def normalize_vector(self, vector: np.array) -> np.array:
        '''
        Min-Max normalization of a given vector
        
        :param vector: np.array of numbers
        
        return: normalized vector
        '''
        try:
            # exclude vectors with only a single unique entry to avoid division by 0
            if len(np.unique(vector)) > 1:
                # norm = (x - x_min) / (x_max - x_min)
                norm_vector = (vector - np.amin(vector))/(np.amax(vector) - np.amin(vector))
            else:
                # vectors without unique values  will be divided by any given value
                norm_vector = vector / vector[0]
                
        except Exception as err_msg:
            print(f"Error in tree.normalize_vector --> {err_msg}\nvector = {vector}")
        else:
            return norm_vector 
        
    def backpropagation(self, node: Node, value: int):
        node.value += value
        node.exploration += 1
        if node.parent:
            self.backpropagation(node.parent, value)