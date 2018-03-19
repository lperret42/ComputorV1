def float_is_int(f):
    """
    return if the float f can be an int
    """
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
    print lst
    if len(lst) < 2:
        return lst
    while True:
        if lst[-1] == 0:
            del lst[-1]
        else:
            break

    return lst

def sqrt(x, epsilon=10e-12):
    """
    implementation of the sqrt function, both suites u and v converge to sqrt(x)
    """
    if x < 0:
        return None
    if x == 0:
        return 0
    u = 1
    v = x
    error_u = abs(u * u - x)
    error_v = abs(v * v - x)
    old_error_u = error_u
    old_error_v = error_v
    while error_u > epsilon and error_v > epsilon:
        tmp = u
        u = 2. / (1. / u + 1. / v)
        v = (tmp + v) / 2.
        error_u = abs(u * u - x)
        error_v = abs(v * v - x)
        if old_error_u == error_u and old_error_v == old_error_v:
            break
        old_error_u = error_u
        old_error_v = error_v

    return u if error_u <= error_v else v
