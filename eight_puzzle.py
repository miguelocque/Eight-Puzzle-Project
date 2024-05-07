#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Miguel Ocque
# email: mocque@bu.edu
#
# Did not work with a partner
#

from searcher import *
from timer import *

# code below this comment was given
def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher
# code above this comment was given

# code below this comment was given
def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
# code above this comment was given


def process_file(filename, algorithm, param):
    """ open the file with the specified filename for reading, and 
        it should use a loop to process the file one line at a time.
        For each line it should:
            - obtain the digit string on that line 
            - take the steps needed to solve the eight puzzle for 
              that digit string using the algorithm and parameter 
              specified by the second and third inputs to the function
            - report the number of moves in the solution, and the number
              of states tested during the search for a solution
        In addition, the function should perform the cumulative computations
        needed to report: number of puzzles solved, the average number of 
        moves in the solutions, and the average number of states tested
    """
    
    f = open(filename, 'r')
    
    num_puz_solved = 0
    avg_moves = 0
    avg_states = 0
    count = 0
    
    for line in f:
        # getting the line and chopping off the new-line char
        line = line[:-1]
        # creating a new board with the string repr of the line
        new_board = Board(str(line))
        # creating a new initial state from the board
        new_state = State(new_board, None, 'init')
        # creating a new searcher with the algorithm and param passed in
        searcher = create_searcher(algorithm, param)
        if searcher == None:
            return
        
        # setting the solution to None
        soln = None
        try:
            # finds the solution for the current line
            soln = searcher.find_solution(new_state)
        except KeyboardInterrupt:
            # if the search is taking too long, user can interrupt and
            # we have a error message printed
            # the continue statement skips the rest of the loop and goes
            # to the next line. 
            print(str(line) + ': search terminated, no solution')
            continue
        
        # if we stil have no solution, we print that we don't, and increment
        # the count of lines we've gone through
        if soln == None:
            count += 1
            print(str(line) + ':', 'no solution')
            
        # otherwise, we update all the variables accordingly and we
        # print the stats for each line for the solution found.
        else:
            num_puz_solved += 1
            avg_states += searcher.num_tested
            avg_moves += soln.num_moves
            count += 1
            print(str(line) + ':', soln.num_moves, 'moves,',  searcher.num_tested, 'states tested')
        
    # closes the file 
    f.close()
    
    # if we didn't solve any puzzles, we don't need to print averages
    if num_puz_solved == 0:
        print()
        print('solved', num_puz_solved, 'puzzles')
        
    # else we print them
    else:
        print()
        print('solved', num_puz_solved, 'puzzles')
        print('averages:', (avg_moves / count), 'moves,', (avg_states / count), 'states tested')

    




