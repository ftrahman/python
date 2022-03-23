
#problem 1
def add_spaces(s):
    '''if the length of string s is less than 2
    return the string, otherwise, add spaces between
    each letter in s'''
    if len(s) < 2:
        return s
    else:
        add_rest = add_spaces(s[1:])
        return s[0] + ' ' + add_rest


#problem 2
def num_diff(s1, s2):
    '''if both strings are the same, return 0
    differences between them, otherwise return
    the amount of differences between both strings
    '''
    if s1 == s2:
        return 0
    else:
        num_rest = num_diff(s1[1:], s2[1:])
        if s1[0] != s2[0]:
            return 1 + num_rest
        else:
            return 0 + num_rest


#problem 3
def index(elem,seq):
    '''returns -1 if sequence is empty, 0 if
    the first character in sequence is the same as
    the element, otherwise returns the index of the
    first position of element
    '''
    if seq == '' or seq == []:
        return -1
    elif elem == seq[0]:
        return 0
    else:
        index_rest = index(elem, seq[1:])
        if index_rest < 0:
            return index_rest
        else:
            return index_rest + 1


#problem 4
def one_dna_to_rna(c):
    """ returns the RNA transcription of
    a DNA sequence
    """
    assert(len(c) == 1)
    if c == 'C':
        return 'G'
    elif c == 'A':
        return 'U'
    elif c == 'G':
        return 'C'
    elif c == 'T':
        return 'A'
    else:
        return ''


#problem 5
def transcribe(s):
    '''returns the total number score corresponding
    to a word based on scrabble letter tiles
    '''
    if s == '':
        return ''
    else:
        rest = transcribe(s[1:])
        return one_dna_to_rna(s[0]) + rest



def test ():
    """ test function for the functions above """
    test1 = add_spaces('eccentric')
    print('the first test returns', test1)
    test2 = num_diff('alone', 'allen')
    print('the second test returns', test2)
    test3 = index('p', ['pineapple', 'chance', 'peaches', 'berry', 'porcupine'])
    print('the third test returns', test3)
    test4 = one_dna_to_rna('C')
    print('the fourth test returns', test4)
    test5 = one_dna_to_rna('T')
    print('the fifth test returns', test5)
    test6 = transcribe('CTAAGGTCT')
    print('the sixth test returns', test6)
       
