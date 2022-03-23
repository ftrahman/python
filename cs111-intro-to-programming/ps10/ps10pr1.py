


class Board:
    """ a class for objects that represent a Connect Four board.
        it has three attributes: a height, a width and slots
    """

    def __init__(self, height, width):
        """ a constructor for Board objects"""
        self.width = width
        self.height = height
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """returns a string representation of the Board object
            called self
        """
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'

        s += '-' * self.width * 2 + '-'
        s += '\n'
        count = -1

        for i in range(self.width):
            count += 1
            s += ' '+ str(count)
            if count > 8:
                count = -1
            
        return s


    def add_checker(self, checker, col):
        """ adds either checker 'O' or 'X' to input column
            of Board object called self
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        count = self.height - 1
        for row in range(count, -1, -1):
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                break
            

    def reset(self):
        """ clears the object Board called self of all checker
            inputs
        """
        self.__init__(self.height, self.width)
        self.__repr__()
        

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker,col)

        # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    
    def can_add_to(self, col):
        """ returns True if a column named col in object Board
            called self has space to add more checkers, and False
            if the column is full
        """
        if -1 < col < self.width:
            for row in range(self.height - 1, -1, -1):
                if self.slots[row][col] == ' ':
                    return True

        return False


    def is_full(self):
        """ returns True if the Board object called self is
            completely full with checkers, False if not
        """
        area = self.height * self.width
        count = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                    count += 1
                    if count == area:
                        return True
               
        return False


    def remove_checker(self, col):
        """ removes a checker from the column col in
            Board object called self
        """
        for row in range(self.height):
            if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
                self.slots[row][col] = ' '
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                    return True

    # if we make it here, there were no horizontal wins
        return False


    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for an up diagonal win for the specified checker.
        """
        for row in range(self.height - 1, 0, -1):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True

        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True

        return False
        
    def is_win_for(self, checker):
        """ Checks for a win for a specified checker
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        else:
            return False

        
               















    
