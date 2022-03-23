

#Problem 1
def dec_to_bin(n):
    '''converts decimal numbers to binary
    '''
    if n == 1:
        return '1'
    elif n == 0:
        return '0'
    else:
        dec_rest = dec_to_bin(n//2)
        if n % 2 == 0:
            return dec_rest + '0'
        else:
            return dec_rest + '1'

#Problem 2
def bin_to_dec(b):
    '''converts binary numbers to decimal
    '''
    if b == '1':
        return 1
    elif b == '0':
        return 0
    else:
        bin_rest = bin_to_dec(b[:-1])
        if bin_to_dec(b[-1]) == 0:
            return 2 * bin_rest
        else:
            return 2 * bin_rest + 1


#Test Function
def test():
    print('dec_to_bin(5) is', dec_to_bin(5))
    print('dec_to_bin(10) is', dec_to_bin(10))
    print('bin_to_dec("1110") is', bin_to_dec('1110'))
    print('bin_to_dec("00011010") is', bin_to_dec('00011010'))
    
