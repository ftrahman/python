def jscore(s1, s2):
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

def numbersim(s1, s2, s3):
    if s3 in s2:
        y = sum(1 for x in s2 if x is s3)
        z = sum(1 for x in s1 if x is s3)
        if y > z:
            return 1
        elif z > y:
            return 0
        else:
            return y          
