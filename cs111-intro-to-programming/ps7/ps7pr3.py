def add_spaces(s):
    '''add spaces between each letter in s
    '''
    result = ''
    for c in s:
        result += c + ' '
    return result[:-1]

# returns the string without the last space 
        

def num_diff(s1, s2):
    '''finds the shorter string and determines the
    number of differences between the two strings
    '''
    result = 0
    len_shorter = min(len(s1), len(s2))
    len_longer = max(len(s1), len(s2))

    for i in range(len_shorter):
        if s1[i] != s2[i]:
            result += 1
        else:
            result += 0
    return result + (len_longer-len_shorter)

# len_longer-len_shorter included because if one word is longer
# than the other, they are that many letters different



def index(elem, seq):
    '''returns -1 if sequence is empty, 0 if
    the first character in sequence is the same as
    the element, otherwise returns the index of the
    first position of element
    '''
    result = 0
    for i in range(len(seq)):
        if elem == seq[i]:
            result = i
            return result
        else:
            result = -1
    return result


