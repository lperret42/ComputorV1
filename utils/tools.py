def float_is_int(f):
    """
    return if the float f can be an int
    """
    if isinstance(f, int):
        return True
    elif not isinstance(f, float):
        return False
    f = str(f)
    return float(f[f.find('.'):]) == 0

def get_float_str_to_print(f):
    sign = '-' if f < 0 else ''
    if not isinstance(f, int) and float_is_int(f):
        f = str(f)
        f = int((f[:f.find('.')]))
    to_print = "{}{}".format(sign, abs(f))

    return to_print

def print_float(f):
    to_print = get_float_str_to_print(f)
    print to_print,

def print_complex(z):
    x, y = z
    y_to_print = get_float_str_to_print(abs(y))
    if not (x == 0 and y != 0):
        print_float(x)
        z_imaginary_sign = '+' if y >= 0 else '-'
        if y_to_print != '1':
            print "{} i * {}".format(z_imaginary_sign, y_to_print)
        else:
            print "{} i".format(z_imaginary_sign)
    else:
        z_imaginary_sign = '' if y >= 0 else '-'
        if y_to_print != '1':
            print "{}i * {}".format(z_imaginary_sign, y_to_print)
        else:
            print "{}i".format(z_imaginary_sign)

def print_error(num_error):
    print "The equation is not well formatted"
    exit()

def remove_zero_at_the_end(lst):
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
