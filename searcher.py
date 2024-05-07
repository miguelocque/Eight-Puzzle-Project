#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Miguel Ocque
# email: mocque@bu.edu
#
# Did not work with a partner
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, depth_limit):
        """ constructs a new Searcher Object; initializes the following:
            - an attribute states for the Searcher‘s list of untested states; 
            it should be initialized to an empty list
            - an attribute num_tested that will keep track of how many states
            the Searcher tests; it should be initialized to 0
            - an attribute depth_limit that specifies how deep in the 
            state-space search tree the Searcher will go; it should be 
            initialized to the value specified by the parameter depth_limit
            (a value of -1 indicates no depth lim)
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        

    def add_state(self, new_state):
        """ takes a single State object called new_state and adds 
            it to the Searcher‘s list of untested states. This 
            method should only require one line of code! It should
            not return a value.
        """
        self.states += [new_state]


    def should_add(self, state):
        """ takes a State object called state and returns True if the 
            called Searcher should add state to its list of untested 
            states, and False if the following:
            - the Searcher has a depth limit 
            (i.e., its depth limit is not -1) and state is beyond the 
            depth limit (i.e., the number of moves used to get to state 
                         is greater than the depth limit)
            - state creates a cycle in the search, because the same board 
            already appears in the sequence of moves that led to state
            (uses the creates_cycle() method given in the state class)
        """
        # as long as the state doesn't create a cycle, and the depth limit
        # is either -1 or greater than the current number of states tested, 
        # the state should be added and the method returns True.
        if state.creates_cycle() != True:
            if self.depth_limit == -1 or self.depth_limit < self.num_tested:
                return True
            
        return False

    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that processes 
            the elements of new_states one at a time as follows:
            - If a given state s should be added to the Searcher‘s list of 
            untested states (because s would not cause a cycle and is not 
            beyond the Searcher‘s depth limit), the method should use the
            Searcher‘s add_state() method to add s to the list of states
            - If a given state s should not be added to the Searcher object’s 
            list of states, the method should ignore the state
        """
        
        # uses a for loop to determine if each state should be added,
        # and adds it accordingly
        for st in new_states:
            if self.should_add(st):
                self.add_state(st)

    # code below this comment was given
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    # code above this comment was given
    
    
    def find_solution(self, init_state):
        """ performs a full state-space search that begins at the specified 
            initial state init_state and ends when the goal state is found 
            or when the Searcher runs out of untested states.
            - searcher should begin by adding init_state to its list of states
            - If the searcher finds a goal state, it should return it
            - If the searcher runs out of untested states before finding 
              a goal state, it should return the special keyword None
            - The method should increment the Searcher object’s num_tested
              attribute every time that it tests a state to see if it is 
              the goal
        """
        
        # adds the initial state passed into the method
        self.add_state(init_state)
        
        while len(self.states) != 0:
            s = self.next_state()
            if s.is_goal() == True:
                self.num_tested += 1
                return s
            else:
                self.num_tested += 1
                self.add_states(s.generate_successors())
                
        
        return None
                




    # code below this comment was given
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    # code above this comment was given

### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """ searcher objects that perform breadth-first search (BFS)
        instead of random search. BFS involves always choosing one
        the untested states that has the smallest depth
    """
    
    def next_state(self):
        """ overrides the next_state method that is inherited from 
            Searcher. Rather than choosing at random from the list 
            of untested states, this version of next_state should 
            follow FIFO (first-in first-out) ordering – choosing 
            the state that has been in the list the longest
        """
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    """  DFS involves always choosing one the untested states that
        has the largest depth (i.e., the largest number of moves 
                               from the initial state).
        DFS, the next state to be tested should be one of the ones 
        that has the largest depth in the state-space search tree.
    """
    
    def next_state(self):
        """ overrides the next_state method that is inherited from 
            Searcher. Rather than choosing at random from the list 
            of untested states, this version of next_state should 
            follow LIFO (last-in first-out) ordering – choosing 
            the state that was most recently added to the list.
        """
        s = self.states[-1]
        self.states.remove(s)
        return s


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    """ takes a State object called state, and that computes and 
        returns an estimate of how many additional moves are needed 
        to get from state to the goal state. Its estimate should 
        simply be the number of misplaced tiles in the Board object
        associated with state.
    """
    return state.board.num_misplaced()
    

def h2(state):
    """ takes in a State object, state, and uses an algorithm to 
        determine an optimal number that will give the informed 
        searches insight into efficiency.
    """
    return (state.board.row_misplaced()) + (state.board.col_misplaced())
    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def  __init__(self, heuristic):
        """ overrides the __init__ method in the searcher class, 
            since it contains a new attribute, but it will still utilize 
            the super() method to use the inherited constructor. 
        """
        
        super().__init__(-1)
        self.heuristic = heuristic
        
        
    # code below this comment was given
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    # code above this comment was given
        
    def add_state(self, state):
        """ overrides the add_state method that is inherited from 
            Searcher. The method should add a sublist that is a 
            [priority, state] pair, where priority is the priority
            of state that is determined by calling the priority method.
            Pairing each state with its priority will allow a 
            GreedySearcher to choose its next state based on the 
            priorities of the states.
        """
        
        # creates the pair in the list
        pair = [self.priority(state), state]
        # appends the new list to the already existing list of states. 
        self.states.append(pair)

    def next_state(self):
        """ overrides the next_state method that is inherited from 
            Searcher. This version of next_state should choose one 
            of the states with the highest priority.
        """
        s = max(self.states)
        self.states.remove(s)
        return s[-1]


    # code below this comment was given
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    # code above this comment was given

### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    """ an informed search algorithm that assigns a priority to each 
        state based on a heuristic function, and that selects the next 
        state based on those priorities. However, when A* assigns a 
        priority to a state, it also takes into account the cost that
        has already been expended to get to that state
    """
    
    # no need for a constructor, inherited from GreedySearcher
    
    def priority(self, state):
        """ overrides the priority method in GreedySearcher. 
            Computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
            and the number of moves it's taken to get to that state,
            taken from the attribute of state. 
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    






