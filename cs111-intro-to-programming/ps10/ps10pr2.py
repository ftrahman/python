#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class   
#

from ps10pr1 import Board



class Player:
    """ a class for objects that represents a Connect Four player.
        Has two attributes: a checker and a count or the amount of moves made
        named num_moves
    """

    def __init__(self, checker):
        """ a constructor for object Player """
            
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representation of object Player
        """
        s = 'Player '
        s += self.checker

        return s

    def opponent_checker(self):
        """ determines the opposing checker of the Player object
        """
        assert(self.checker == 'X' or self.checker == 'O')
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'
        
    def next_move(self, board):
        """ sees is the next intended move is a valid move on the
            Board object
        """
        while True:
            choice = int(input('Enter a column: '))
            if board.can_add_to(choice) == True:
                self.num_moves += 1
                return choice
            else:
                print('Try again!')
            
            
            
        
