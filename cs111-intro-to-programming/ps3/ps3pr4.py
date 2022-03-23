
#Problem 1
def sort_bits(bits):
    '''returns the bits in a list in
    increasing order'''
    if bits == []:
        return bits
    else:
        bits_rest = sort_bits(bits[1:])
        if bits[0] == 0:
            return [bits[0]] + bits_rest
        else:
            return bits_rest + [bits[0]]

#Problem 2      
def jscore(s1, s2):
    '''returns the number of letters shared
    between two strings, with repeating letters
    if the repetition occurs in both strings'''
    if s1 == s2:
        return len(s1)
    elif s1 == '' or s2 == '':
        return 0
    else:
        j_rest = jscore(s1[1:],s2)
        if s1[0] in s2:
            x = s1[0]
            return numbersim(s1, s2, x) + j_rest
        else:
            return j_rest

#Helper Function
def numbersim(s1, s2, s3):
    '''returns 1 if s2 has more of the letter in string
    s3 than s1, returns 0 if s1 has more of the letter in
    string s3 than s2, and if there are an equal number of
    letters shared returns that number'''
    y = sum(1 for x in s2 if x is s3)
    z = sum(1 for x in s1 if x is s3)
    if y > z:
        return 1
    elif z > y:
        return 0
    else:
        return y
    
#Problem 3
def lcs(s1,s2):
    '''takes two strings s1 and s2 and returns
    the longest common subsequence, appear in the same
    order but not consecutively'''
    if s1 == '' or s2 == '':
        return ''
    else:
        lcs_rest = lcs(s1[1:],s2[1:])
        if s1[0] == s2[0]:
            return s1[0] + lcs_rest
        else:
            result1 = lcs(s1[1:], s2)
            result2 = lcs(s1, s2[1:])
            if len(result1) > len(result2):
                return result1
            else:
                return result2
