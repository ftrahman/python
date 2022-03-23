

from ps4pr1 import *


#Problem 1
def mul_bin(b1, b2):
    '''returns the product of two binary numbers
    '''
    x = bin_to_dec(b1)
    y = bin_to_dec(b2)
    z = x * y
    a = dec_to_bin(z)
    return a



#Problem 2
def add_bytes(b1,b2):
    '''returns the sum of two binary numbers
    '''
    x = bin_to_dec(b1)
    y = bin_to_dec(b2)
    z = x + y
    a = dec_to_bin(z)
    if len(a) > 8:
        return a[:8]
    elif len(a) < 8:
        b = 8 - len(a)
        c = '0' * b + a
        return c
    else:
        return a



#Test Function
def test():
    print('add_bytes("00011100", "00011110") is', add_bytes('00011100', '00011110'))
    print('mul_bin("1001", "101") is', mul_bin('1001', '101'))
