#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Miguel Ocque
# email: mocque@bu.edu
#
# Did not work with a partner
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        # updates the tiles attribute given the string
        checker = 0
        
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                self.tiles[i][j] = digitstr[checker]
                checker += 1
                
        # updates the blank_r and blank_c attributes:
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] == '0':
                    self.blank_r = i
                    self.blank_c = j
                    break
        

    ### Add your other method definitions below. ###

    def __repr__(self):
        """ returns a string representation of a Board object. 
            Each tile should be represented by the appropriate 
            single-character string followed by a single space.
            The blank cell should be represented by an underscore 
            character ('_'). Make sure that you do not use a 
            hyphen ('-') by mistake. There should be a newline 
            character ('\n') after the characters for a given 
            row, so that each row will appear on a separate line 
            when you evaluate or print a Board object.
        """
        
        brdstr = ''
        
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] == '0':
                    brdstr += '_' 
                else:
                    brdstr += self.tiles[i][j]
                
                brdstr += ' '
            brdstr += '\n'
            
        return brdstr

    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the 
            direction in which the blank should move, and that 
            attempts to modify the contents of the called Board 
            object accordingly. Not all moves are possible on a
            given Board; for example, it isn’t possible to move 
            the blank down if it is already in the bottom row. 
            The method should return True or False to indicate 
            whether the requested move was possible.
        """
        # new coordinates that will be updated 
        new_r = 0
        new_c = 0
        
        # check for the up direction
        if direction == 'up' or direction == 'Up':
            if (self.blank_r - 1) < 0:
                return False
            else:
                # updating the coordinates
                new_r = self.blank_r - 1
                
                # swapping the two values at the specified coordinates.
                self.tiles[self.blank_r][self.blank_c] = self.tiles[new_r][self.blank_c]
                self.tiles[new_r][self.blank_c] = '0'
                
                # adjusting the attributes of the coordinates of the blank
                self.blank_r = new_r
                
                return True
        
        # check for the down direction
        elif direction == 'down' or direction == 'Down':
            if (self.blank_r + 1) == len(self.tiles[self.blank_r]):
                return False
            else:
                # updating the coordinates
                new_r = self.blank_r + 1
                
                # swapping the two values at the specified coordinates.
                self.tiles[self.blank_r][self.blank_c] = self.tiles[new_r][self.blank_c]
                self.tiles[new_r][self.blank_c] = '0'
                
                # adjusting the attributes of the coordinates of the blank
                self.blank_r = new_r
                
                return True
                
        # check for the right direction
        elif direction == 'right' or direction == 'Right':
            if (self.blank_c + 1) == len(self.tiles[self.blank_r]):
                return False
            else:
                # updating the new coordinates
                new_c = self.blank_c + 1
                
                # swapping the two values at the specified coordinates
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][new_c]
                self.tiles[self.blank_r][new_c] = '0'
                
                # adjusting the attributes of the coordinates
                self.blank_c = new_c
                
                return True
                
        # check for the left direction
        elif direction == 'left' or direction == 'Left':
            if (self.blank_c - 1) < 0:
                return False
            else:
                # updating the new coordinates
                new_c = self.blank_c - 1
                
                # swapping the two values at the specified coordinates
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][new_c]
                self.tiles[self.blank_r][new_c] = '0'
                
                # adjusting the attributes of the coordinates
                self.blank_c = new_c
                
                return True
                
        else:
            return False
                
        
    def digit_string(self):
        """ creates and returns a string of digits that corresponds 
            to the current contents of the called Board object’s tiles
            attribute.
        """
        
        copy = ''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                copy += self.tiles[i][j]
                
        return copy
    
    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep 
            copy of the called object (i.e., of the object represented by self)
            should use the Board constructor to create a new Board object 
            with the same configuration of tiles as self, and it should 
            return the newly created Board object.
        """
        
        # obtains the string representation of the board
        dgts_copy = self.digit_string()
        
        #contructs a new separate board object
        new_b = Board(dgts_copy)
        
        # returns the new board object
        return new_b
    
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board 
            object that are not where they should be in the goal state.
            You should not include the blank cell in this count, even 
            if it’s not where it should be in the goal state.
        """
        
        # count var that increments for each misplaced element
        count = 0
        
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] != '0':
                    if self.tiles[i][j] != GOAL_TILES[i][j]:
                        count += 1
                                      
        return count

    

    def  __eq__(self, other):
        """ can be called when the == operator is used to compare two 
            Board objects. The method should return True if the called
            object (self) and the argument (other) have the same 
        """
        
        if self.tiles == other.tiles:
            return True
        
        else:
            return False
    
    
    def row_misplaced(self):
        """ counts and returns the number of tiles that are placed
            in the wrong rows. blank cell is not included in the
            count
        """
        
        row_count = 0
        
        # loop checks if the given value is in the correct row in 
        # GOAL_TILES, and if not, increment the count
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] != '0':
                    if self.tiles[i][j] not in GOAL_TILES[i]:
                        row_count += 1
                            
        return row_count
    
    
    def col_misplaced(self):
        """ counts and returns the number of tiles that are placed
            in the wrong columns. blank cell is not included in the
            count
        """
        
        # the loop below creates an order of columns in a 2D list that
        # will allow the next loop to check if a number in the tiles
        # list is in the correct column
        correct_col = []

        for i in range(len(GOAL_TILES)):
            c = []
            for j in range(len(GOAL_TILES[0])):
                c += GOAL_TILES[j][i]
                
            correct_col.append(c)
         
        
        # loop below will go through and check if the specified value isn't in
        # the correct column
        col_count = 0

        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[c][r] != '0':
                    if self.tiles[c][r] not in correct_col[r]:
                        col_count += 1
                        
        return col_count
                        
                    
                    
        
            
                    







