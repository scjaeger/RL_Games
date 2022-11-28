from basic_tree.action import Action
from basic_tree.node import Node
from basic_tree.constants import UCB_COEFFICIENT
import numpy as np
import time



class Tree():
    def __init__(self, root: Node, children: list):
        self.root = root # Node object
        self.children = children # Node objects
        self.searches = 0
    
    def tree_search(self) -> Action:
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
            chosen_node = self.select_node(self.root)
            
            # simulate the value of a random walk starting from chosen node
            value = chosen_node.simulate_result()
            
            # backpropagate outcome to relevant nodes
            self.backpropagation(chosen_node, value)
            
            # break loop if time limit is reached
            if time.time() > timeout or n > 10000:
                break
        
        # choose highest scroding node after investigation
        chosen_node = self.choose_action()

        # set node of chosen action as root and prune tree
        self.prune_tree(chosen_node)

        return chosen_node.former_action    
    
    
    
    def prune_tree(self, node: Node) -> None:
        '''
        updates root and children of tree after taking an action
        
        node: Node refering to the action taken
        '''
        
        # list of children nodes that are still relevant
        kept_children = self.check_relevant_nodes([], node)
        
        # set node as root
        self.root = node
        
        # set children to children list after pruning
        self.children = kept_children
        
        
    def check_relevant_nodes(self, kept_children: list, node: Node) -> list:
        '''
        Given a tree this method makes a list of children nodes that are related to the input node
        
        :param kept children: List of node related to the input node
        :paran node: Node used as root node whos descendants are searched
        
        return: list of nodes
        '''
        
        # create list of nodes with input node as parent
        next_layer = [child for child in self.children if child.parent == node]
        
        for child in next_layer:
            # add child to list of children to keep
            kept_children.append(child)
            
            # start recursion if child node is not final
            if not child.is_leaf:
                self.check_relevant_nodes(kept_children, child)
                
        return kept_children
        
    def choose_action(self)-> Node:
        '''
        takes an action based on it's current mean value
        
        return: highest scoring node
        '''
        # create a list of next layer nodes
        next_layer = [child for child in self.children if child.parent == self.root]
        
        # get values of those nodes
        values = np.array([sub_node.value for sub_node in next_layer])
        
        # get their exploration values
        explorations = np.array([sub_node.exploration for sub_node in next_layer])
        
        # calculate mean by value and amount of exploration
        mean_values = values / explorations
        
        # grab choose node by highest mean value
        best_action_index = np.argmax(mean_values)
        chosen_node = next_layer[best_action_index]
        
        return chosen_node
     
    def expand_tree(self, node: Node):
        '''
        adds another layer to the tree by expanding a specific node
        
        :param node: Node chosenfor expansion
        '''
        
        # add children to node if no children available and node is not final
        if len(node.children) == 0 and node.is_leaf is False:
            self.children = self.children + node.get_children()

            
            
    def select_node(self, node: Node)-> Node:
        '''
        chooses a node for simulation based on ucb1 algorithm
        
        :param node: parent node, selections is made between its children
        
        return: node chosen for further investigation
        '''
        
        self.searches += 1
        # get child layer
        next_layer = [child for child in self.children if child.parent == node]

        # check for unexplored nodes
        exploration_tracker = [sub_node.exploration for sub_node in next_layer]

        if 0 in exploration_tracker:
            # randomly pick one of the unknown nodes
            unexplored = np.where(np.array(exploration_tracker) == 0)[0]
            action_index = np.random.choice(unexplored)
            chosen_node = next_layer[action_index]

        # check nodes for highest ucb value
        else:
            valuable_nodes = self.ucb(next_layer)
            action_index = np.random.choice(valuable_nodes)
            potential_node = next_layer[action_index]
            
            self.expand_tree(potential_node)
            
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
        values = np.array([sub_node.value for sub_node in layer])
        explorations = np.array([sub_node.exploration for sub_node in layer])
        mean_values = values / explorations
        mean_norm = self.normalize_vector(mean_values)
        
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
            print("Error in bandit.normalize_vector --> {}".format(err_msg))
        else:
            return norm_vector 
        
    def backpropagation(self, node: Node, value: int):
        node.value += value
        node.exploration += 1
        if node.parent:
            self.backpropagation(node.parent, value)