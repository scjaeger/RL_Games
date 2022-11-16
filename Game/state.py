from abc import ABCMeta, abstractmethod

class State(ABCMeta):
    def __init__(self):
        self.board
        self.player
        
    @abstractmethod
    def get_actions(self):
        pass   
    
    @abstractmethod
    def do_action(self, action):
        # initial board
        # return new state
        pass
    
    @abstractmethod
    def change_player(self):
        pass
    
    @abstractmethod
    def check_end_state(self):
        pass