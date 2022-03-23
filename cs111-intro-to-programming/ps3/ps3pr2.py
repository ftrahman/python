def abs_list_lc(values):
    return[abs(x) for x in values]

def abs_list_rec(values):
    if values == []:
        return values
    else:
        abs_rest = abs_list_rec(values[1:])
        return [abs(values[0])] + abs_rest

def num_factors(x):
    return len([y for y in range(1, x+1) if x % y == 0])


def max_factors(values):
     max_vals = max([[num_factors(x),x] for x in values])
     return max_vals[1]

