# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions with numeric inputs
#
# name: Farheen Rahman
# email: ftrahman@bu.edu


# function 1
def reverse(s):
    """returns the reverse of the string input
    """
    s = s[::-1]
    return s


# function 2
def outer_vals(values):
    """returns the first and last values in a list
    """
    values = values[:1] + values[-1:]
    return values


# function 3
def flipside(s):
    """finds if there are an even or odd number of characters
    and flips the order of letter in a string
    """
    x = len(s)//2
    y = len(s[(x+1):]) + 1
    if x == y:
        s = s[x:] + s[:x]
        return s
    else:
        s = s[(y-1):] + s[:x]
        return s
        

# function 4
def adjust(s, length):
    """determines the length of the string compared to value length
    and produces number of spaces or removes letters depending
    on relationsip"""
    if len(s) > length:
        x = length - len(s)
        s = s[:x]
        return s
    elif len(s) < length:
        x = length - len(s) 
        y = ' ' * x
        s = y + s
        return s
    else:
        return s


#test function
def test():
    print('reverse("silly") is', reverse('silly'))
    print('outer_vals(["eggs", "bacon", "grits", "sausage", "omelette", "pancakes", "waffles"]) is', outer_vals(["eggs", "bacon", "grits", "sausage", "omelette", "pancakes", "waffles"]))
    print('flipside("barnyard") is', flipside('barnyard'))
    print('flipside("cupcake") is', flipside('cupcake'))
    print('adjust("monkey", 6) is', adjust('monkey', 6))
    print('adjust("monkey", 8) is', adjust('monkey', 8))
    print('adjust("monkey", 4) is', adjust('monkey', 4))
       
