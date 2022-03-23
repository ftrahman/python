#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps10pr3 import *


class AIPlayer(Player):
    """ a class for objects that represents a AI Connect Four player.
        Has four attributes: a checker and a count or the amount of moves made
        named num_moves (inhertied from Player class), a tiebreak option in the
        case of a tie and a lookahead option to predict future moves
    """

    def __init__(self, checker, tiebreak, lookahead):
        """ a constructor for object AIPlayer"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
         
        super().__init__(checker)
         
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representation of object AIPlayer
        """
        s = 'Player '
        s += self.checker
        s += ' ('
        s += self.tiebreak
        s += ', '
        s += str(self.lookahead)
        s += ')'
        

        return s

    def max_score_column(self, scores):
        ''' determines the column that produces the highest score. In the event
            of a tie, looks to the tiebreak to decide which column to choose
        '''
        max_score = max(scores)
        max_index = []
        
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_index += [i]

        if self.tiebreak == 'LEFT':
            max_index = max_index[0]
        if self.tiebreak == 'RIGHT':
            max_index = max_index[-1]
        if self.tiebreak == 'RANDOM':
            max_index = random.choice(max_index)

        return max_index

    def scores_for(self, board):
        ''' determines the scores for each column based upon the column's
            current occupied columns to produce a list of scores that outline
            each column point opportunity
        '''
        scores = [50] * board.width

        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponent_scores = opponent.scores_for(board)
                scores[col] = 100 - max(opponent_scores)
                board.remove_checker(col)
            

        return scores
          
                
    def next_move(self, board):
        """ Plays the next intended move for an AIPlayer on the
            Board object
        """
        
        scores = self.scores_for(board)
        max_score = self.max_score_column(scores)
        self.num_moves += 1
        
        return max_score
        
                    
                
                
                
            
        

        
        
