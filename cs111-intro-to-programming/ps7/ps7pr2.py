#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# Estimating the value of pi
#
# Computer Science 111
#

import random
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 2 BELOW. ###

def est_pi1(error):
    '''takes an error value and produces an estimate for the number of
    throw made to get less than the error value of the actual
    value of pi
    '''
    # have to set all of our accumulator variables to zero
    # so they are already assigned
    throws_made = 0 
    throws_hit = 0
    area_circle = 0
    while error < abs(math.pi - area_circle):
        if throw_dart() == False:
            throws_made += 1 # if throw_dart() does not hit the circle, only throws_made is increased by one
            area_circle = (throws_hit * 4) / throws_made #calculates an estimate of pi
            print(throws_hit, 'hit out of', throws_made, 'so that pi is', area_circle)
        else:
            throws_made += 1 # if throw_dart() does hit the circle, throws_made is increased by one
            throws_hit += 1 # as well as throws hit
            area_circle = (throws_hit * 4) / throws_made #calculates an estimate of pi
            print(throws_hit, 'hit out of', throws_made, 'so that pi is', area_circle)
            
    return throws_made


def est_pi2(n):
    '''takes an n value of darts thrown and produces a random estimate
    for the value of pi produced after those darts are thrown
    '''
    # have to set all of our accumulator variables to zero
    # so they are already assigned
    throws_made = 0
    throws_hit = 0
    area_circle = 0
    for x in range(n):
        if throw_dart() == False:
            throws_made += 1 # if throw_dart() does not hit the circle, only throws_made is increased by one
            area_circle = (throws_hit * 4) / throws_made #calculates an estimate of pi
            print(throws_hit, 'hit out of', throws_made, 'so that pi is', area_circle)
        else:
            throws_made += 1 # if throw_dart() does hit the circle, throws_made is increased by one
            throws_hit += 1 # as well as throws hit
            area_circle = (throws_hit * 4) / throws_made #calculates an estimate of pi
            print(throws_hit, 'hit out of', throws_made, 'so that pi is', area_circle)
            
    return area_circle
