# 
# ps1pr4.py - Problem Set 1, Problem 4
#
# Functions with numeric inputs
#
# name: Farheen Rahman
# email: ftrahman@bu.edu


# function 1
def ends_match(s):
    """ returns True if the first letter and last letter are the same;
    False if they are not"""
    if s[0]==s[-1]:
        return True
    else:
        return False


# function 2
def front3(s):
    """returns the first three letters of a string
    repeated three times"""
    s = s[0:3] * 3
    return s


# function 3
def every_other(values):
    """returns every other value in a list"""
    values = values[::2]
    return values


# function 4
def begins_with(word, prefix):
    """returns True if the prefix is within the word"""
    x = len(prefix)
    if word[:x] == prefix:
        word = prefix
        return True
    else:
        return False    
    

# test function 
def test():
    print('ends_match("eerie") is', ends_match('eerie'))
    print('ends_match("ears") is', ends_match('ears'))
    print('front3("mascara") is', front3('mascara'))
    print('every_other(["eggs", "bacon", "grits", "sausage", "omelette", "pancakes", "waffles"]) is', every_other(['eggs', 'bacon', 'grits', 'sausage', 'omelette', 'pancakes', 'waffles']))
    print('begins_with("dandelion", "dand") is', begins_with('dandelion','dand'))
    print('begins_with("dandelion", "dane") is', begins_with('dandelion','dane'))
