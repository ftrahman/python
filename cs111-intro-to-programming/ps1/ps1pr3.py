# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# name: Farheen Rahman
# email: ftrahman@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below


#function 1
def cube(x):
    """returns the cube of its input"""
    return x**3


#function 2
def compare(num1, num2):
    """returns 1 if num1 is greater, -1 if num2 is greater
    and 0 if inputs are equal
    """
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0


#function 3
def slope(x1,y1,x2,y2):
    """if x1 == x2, the function will output nan because slope is undefined,
    otherwise function returns slope
    """
    if x1 == x2:
        return float('nan')
    else:
        slope = (y2-y1) / (x2-x1)
        return slope


#function 4
def make_change(cents):
    """takes the input value and distributes it
    into quarters, dimes, nickels and pennies
    """
    quarters = cents // 25                 
    cents = cents % 25                    
    dimes = cents // 10                   
    cents = cents % 10
    nickels = cents // 5
    cents = cents % 5
    pennies = cents // 1
    return [quarters, dimes, nickels, pennies]



# test function with a sample test call for function 0
def test():
    """ performs test calls on the opposite function above """
    print('opposite(-8) returns', opposite(-8))
    """ performs test calls on the cube function above """
    print('cube(-8) returns', cube(-8))
    """ performs test calls on the compare function above """
    print('compare(5,6) returns', compare(5,6))
    print('compare(6,5) returns', compare(6,5))
    print('compare(6,6) returns', compare(6,6))
    """ performs test calls on the slope function above """
    print('slope(4,6,3,8) returns', slope(4,6,3,8))
    print('slope(4,8,4,9) returns', slope(4,8,4,9))
    """ performs test calls on the make function above """
    print('make_change(798) returns', make_change(798))

    # optional but encouraged: add test calls for your functions below
