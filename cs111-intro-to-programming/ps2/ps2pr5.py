#
# ps2pr5.py - Problem Set 2, Problem 5
#
# list comprehensions
#

# Problem 5-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [x*2 for x in range(5)]
print(lc1)

# part b
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [w[1] for w in words]
print(lc2)

# part c
lc3 = [word[::-1]*3 for word in ['hello', 'bye', 'no']]
print(lc3)

# part d
lc4 = [x**2 for x in range(1, 10) if x%2 == 0]
print(lc4)

# part e
lc5 = [c == 'b' or c == 'u' for c in 'bu be you']
print(lc5)


# Problem 5-2: Put your definition of the powers_of() function below.
def powers_of(x,y):
    '''returns the base x to the powers given by
    a range of y in a list'''
    return [x**y for y in range(y)]


# Problem 5-3: Put your definition of the starts_with() function below.
def starts_with(prefix, wordlist):
    '''returns the words in wordlist that begin with
    or include the prefix'''
    return [x for x in wordlist if x[:len(prefix)] in prefix]


def test ():
    """ test function for the functions above """
    test1 = powers_of(3,5)
    print('the first test returns', test1)
    test2 = starts_with('be', ['before', 'believe', 'broken', 'breast', 'begin'])
    print('the second test returns', test2)
