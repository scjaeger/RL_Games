from game.state import State

def test_change_player_1():
    state = State(player = 1)
    
    assert state.change_player() == 2
    
def test_change_player_not_in_range():
    state = State(player = 4)
    
    assert state.change_player() is False
    
def test_change_player_not_int():
    state = State(player = "one")
    
    assert state.change_player() is False