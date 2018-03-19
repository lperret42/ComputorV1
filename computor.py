#!/usr/bin/python2.7
import sys

from polynomial import Polynomial

def main(entry):
    polynomial = Polynomial(entry)
    polynomial.parse_entry()
    polynomial.get_reduced_form()
    polynomial.get_degree()
    polynomial.solve()
    polynomial.print_reduced_form()
    polynomial.print_degree()
    polynomial.print_solution()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage:', sys.argv[0], 'polynomial_equation'
    else:
        entry = sys.argv[1]
        main(entry)
