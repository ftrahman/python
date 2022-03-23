#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# Playing the game    
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board


def process_move(player, board):
    '''plays the next intended move given by the Player object on the Board object
    '''
    turn = player.__repr__()
    turn += "'s turn"
    print(turn)
    print()

    choice = player.next_move(board)
    
    board.add_checker(player.checker, choice)
    print()
    print(board.__repr__())
    print()
    opponent = player.opponent_checker()
    if board.is_win_for(player.checker) == True:
        print(player.__repr__(), "wins in", player.num_moves, "moves. \nCongratulations!")
        return True
    if board.is_full() == True:
        if board.is_win_for(player.checker) == False:
            if board.is_win_for(player.opponent_checker()) == False:  
                print("It's a tie!")
                return True



    else:
        return False


class RandomPlayer(Player):
    """ a class for objects that represents an unintelligent Connect Four player.
        Has two attributes: a checker and a count or the amount of moves made
        named num_moves (inhertied from Player class)
    """

    def next_move(self, board):
        """ Plays the next intended move for an unintelligent Player on the
            Board object
        """
        choices = []
        for x in range(board.width):
            if board.can_add_to(x) == True:
                choices += [x]

        play = random.choice(choices)
        self.num_moves += 1

        return play

        

        
        

        

    
            
                
            
        
    

    
