def float_is_int(f):                                        #return if float is int
    f = f * (-1 if f < 0 else 1)
    return int(f) == f

def print_error(num_error):
    print "The equation is not well formatted"
    exit()

def get_delimiters_str(delimiters):
    delimiters_str = '['
    for delimiter in delimiters:
        delimiters_str += delimiter
    delimiters_str += ']'
    return delimiters_str

def remove_zero_at_the_end(lst):
    while True:
        if lst[-1] == 0:
            del lst[-1]
        else:
            break
    return lst
