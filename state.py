#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Miguel Ocque
# email: mocque@bu.edu
#
# Did not work with a partner
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
    
    def __init__(self, board, predecessor, move):
        """ constructs a new State object by initializing an attribute board 
            that stores a reference to the Board object associated with this 
            state, as specified by the parameter board, an attribute predecessor
            that stores a reference to the State object that comes before this 
            state in the current sequence of moves, as specified by the parameter
            predecessor, an attribute move that stores a string representing 
            the move that was needed to transition from the predecessor state 
            to this state, as specified by the parameter move, and an attribute 
            num_moves that stores an integer representing the number of moves 
            that were needed to get from the initial state (the state at 
            the root of the tree) to this state. If predecessor is None–which
            means that this new state is the initial state–then num_moves 
            should be initialized to 0. Otherwise, it should be assigned a 
            value that is one more that the number of moves for the predecessor 
            state.
        """
        
        self.board = board
        self.predecessor = predecessor
        self.move = move

        if predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = self.predecessor.num_moves + 1
        
        
    # given code below this comment
    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
    # given code above this comment
    
    def is_goal(self):
        """  returns True if the called State object is a goal 
            state, and False otherwise.
        """
        
        if self.board.tiles == GOAL_TILES:
            return True
        else:
            return False
        
    def generate_successors(self):
        """ creates and returns a list of State objects for all
            successor states of the called State object.
        """
        # create the empty list to start with
        successors = []
        
        # loop through each move in the list MOVES, and test each move 
        # and if it works create a new state object derived from the move
        # and add it to the list
        for m in MOVES:
            # makes a copy of the current board
            b = self.board.copy()
            
            # checks if the current move is possible and does it
            if b.move_blank(m) == True:

                # creates a new state object
                nxt_st = State(b, self, m)
                
                # add the new state to the list
                successors += [nxt_st]
        
        return successors
        
        
        
    def print_moves_to(self):
        """ prints the sequence of moves that lead from the initial 
            state to the called State object
        """
        
        if self.predecessor == None:
            print('initial state:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            print('move the blank', self.move + ':')
            print(self.board)
        
        
        