
#Problem 1
def bitwise_and(b1, b2):
    '''takes two strings of binary numbers and
    returns the corresponding 'ANDed' numbers'''
    if len(b1) != len(b2):
        a = abs(len(b1) - len(b2))
        if len(b1) < len(b2):
            b = a * '0' + b1
            return bitwise_and(b,b2)
        else:
            c = a * '0' + b2
            return bitwise_and(b1,c)
    elif b1 == '' and b2 == '':
        return ''
    else:
        bit_rest = bitwise_and(b1[:-1],b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            return bit_rest + '1'
        else:
            return bit_rest + '0'


#Problem Two      
def add_bitwise(b1, b2):
    '''takes two strings of bits and returns the
    sum of the resultant string'''
    if b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        add_rest = add_bitwise(b1[:-1],b2[:-1])
        if b1[-1] == '0' and b2[-1] == '0':
            return add_rest + '0'
        elif b1[-1] == '1' and b2[-1] == '0':
            return add_rest + '1'
        elif b1[-1] == '0' and b2[-1] == '1':
            return add_rest + '1'
        else:
            print("this is carrying one "  + add_rest)
            print("b1 =" + b1 + "b2 =" + b2)
            return add_bitwise(add_rest,'1') + '0'
            



#Test Function
def test():
    print('bitwise_and("11010", "10011") is', bitwise_and('11010', '10011'))
    print('bitwise_and("1001111", "11011") is', bitwise_and('1001111', '11011'))
    print('add_bitwise("11100", "11110") is', add_bitwise('11100', '11110'))
    print('add_bitwise("10101", "10101")', add_bitwise('10101', '10101'))
    
