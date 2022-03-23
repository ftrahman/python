#problem one
def mult(n,m):
    '''reptitively adds n variable m amount of times
    if both integers are positive, makes the function
    negative if both integers are negative
    '''
    if m == 1:
        return n
    elif n == 1:
        return m
    elif n < 0:
        return -mult(-n, m)
    elif m < 0:
        return -mult(n, -m)
    else:
        mult_rest = mult(n, m-1)
        return n + mult_rest


#problem two
def dot(l1,l2):
    '''returns the dot product of two lists
    '''
    if l1 == [] or l2 == [] or len(l1) != len(l2):
        return 0.0
    else:
        rest = dot(l1[1:],l2[1:])
        return l1[0] * l2[0] + rest
    

#problem three
def letter_score(letter):
    '''returns the number score corresponding
    to a scrabble letter tile
    '''
    assert(len(letter) == 1)
    if letter in 'aeinorstul':
        return 1
    elif letter in 'dg':
        return 2
    elif letter in 'bcmp':
        return 3
    elif letter in 'fhvwy':
        return 4
    elif letter in 'k':
        return 5
    elif letter in 'jx':
        return 8
    elif letter in 'qz':
        return 10
    else:
        return 0


#problem four
def scrabble_score(word):
    '''returns the total number score corresponding
    to a word based on scrabble letter tiles
    '''
    if word == '':
        return 0
    else:
        rest = scrabble_score(word[1:])
        return rest + letter_score(word[0])


#problem five
def test ():
    """ test function for the functions above """
    test1 = mult(6, 8)
    print('the first test returns', test1)
    test2 = mult(6, -8)
    print('the second test returns', test2)
    test3 = dot([4,2,7],[3,6,2])
    print('the third test returns', test3)
    test4 = dot([4,2,7],[3,6])
    print('the fourth test returns', test4)
    test5 = letter_score('t')
    print('the fifth test returns', test5)
    test6 = letter_score('z')
    print('the sixth test returns', test6)
    test7 = scrabble_score('monkies')
    print('the seventh test returns', test7)
    
    
        
    
