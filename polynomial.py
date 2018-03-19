import re

from tools import remove_zero_at_the_end, float_is_int, print_error, sqrt,\
          print_float, print_complex, get_delimiters_str, get_float_str_to_print

class Polynomial(object):
    def __init__(self, entry, monome_delimiters=['+'],
                 mult_char = '*', expo_char = '^'):
        self.entry = entry
        self.monome_delimiters = monome_delimiters
        self.monome_delimiters_str = get_delimiters_str(monome_delimiters)
        self.mult_char = mult_char
        self.expo_char = expo_char

    def parse_entry(self):
        if not '=' in self.entry:
            print_error(0)
        l_member, r_member = self.entry.split('=')
        l_member = l_member.replace(' ', '')
        r_member = r_member.replace(' ', '')
        self.l_indeterminate, self.l_coefs = self.process_member(l_member)
        if r_member == '0':
            #particular case for process even if equation is in reduced form
            self.r_indeterminate, self.r_coefs = self.l_indeterminate, [0]
        else:
            self.r_indeterminate, self.r_coefs = self.process_member(r_member)
        if self.l_indeterminate != self.r_indeterminate:
            print_error(2)
        self.members_degree_max = max(len(self.l_coefs), len(self.r_coefs)) - 1

    def process_member(self, member):
        if member[0] == '-':
            member = '-' + member[1:].replace('-', '+-')
        else:
            member = member.replace('-', '+-')
        monomes = re.split(self.monome_delimiters_str, member)
        for monome in monomes:
            self.process_monome(monome, self.mult_char, self.expo_char)
        indeterminate, coefs = self.process_is_univariate_polynomial(monomes)
        coefs = map(float, coefs)
        coefs = remove_zero_at_the_end(coefs)
        return indeterminate, coefs

    def process_monome(self, monome, mult_char, expo_char):
        if not (len([c for c in monome if c == mult_char])) == 1:
            print_error(1)
        coef, indeterminate_with_degree = monome.split(mult_char)
        if not coef.replace('.', '').lstrip('-').isdigit(): #if coef isn't a nb
            print_error(1)
        if not expo_char in indeterminate_with_degree:
            print_error(1)
        indeterminate, degree = indeterminate_with_degree.split(expo_char)
        if not indeterminate.isupper():
            print_error(1)
        if not (degree.isdigit() and int(degree) >= 0):
            print_error(1)

    def process_is_univariate_polynomial(self, monomes):
        coefs = [m.split(self.mult_char)[0] for m in monomes]
        indeterminates = [m.split(self.mult_char)[1].split(self.expo_char)[0] \
                                                            for m in monomes]
        for indeterminate in indeterminates[1:]:  #test if all indeterminate are equals
            if indeterminate != indeterminates[0]:
                print_error(2)
        degrees = [m.split(self.mult_char)[1].split(self.expo_char)[1] for m in monomes]
        if not degrees == map(str, range(len(degrees))):  #test if degrees are ordinate
            print_error(2)
        return indeterminates[0], coefs

    def get_reduced_form(self):
        l_coefs = self.l_coefs + [0 for _ in \
                       range(self.members_degree_max - (len(self.l_coefs) - 1))]
        r_coefs = self.r_coefs + [0 for _ in \
                       range(self.members_degree_max - (len(self.r_coefs) - 1))]
        self.reduced_form = [l_coef - r_coef for l_coef, r_coef in \
                             zip(l_coefs, r_coefs)]
        self.reduced_form = remove_zero_at_the_end(self.reduced_form)

    def print_reduced_form(self):
        print "Reduced form:",
        for degree, coef in enumerate(self.reduced_form):
            sign = '-' if coef < 0 else '+'
            if (degree == 0 and sign == '-') or degree > 0:
                print sign,
            self.print_monome_abs(coef, degree)
        print "= 0"

    def print_monome_abs(self, coef, degree):
        if float_is_int(coef):
            coef = int(coef)
        coef = abs(coef)
        print "{} {} X{}{}".format(coef, self.mult_char,
                                   self.expo_char, degree),

    def get_degree(self):
        self.degree = len(self.reduced_form) - 1

    def print_degree(self):
        print 'Polynomial degree: {}'.format(self.degree)


    def solve(self):
        if self.degree == 1:
            self.solve_if_degree_one()
        elif self.degree == 2:
            self.solve_if_degree_two()

    def solve_if_degree_one(self):
        b, a = self.reduced_form
        self.x0 = -b / a

    def solve_if_degree_two(self):
        c, b, a = self.reduced_form
        delta = b * b - 4. * a * c
        if delta >= 0:
            if delta == b * b:
                # particular case to avoid rounding errors
                self.x0 = 0
                self.x1 = -b / a
            else:
                self.x0 = (-b + sqrt(delta)) / (2. * a)
                self.x1 = (-b - sqrt(delta)) / (2. * a)
        else:
            self.z0 = [-b / (2. * a), sqrt(-delta) / (2. * a)]
            self.z1 = [-b / (2. * a), -sqrt(-delta) / (2. * a)]
        self.delta = delta

    def print_solution(self):
        if self.degree == 0:
            self.print_if_degree_zero()
        elif self.degree == 1:
            self.print_if_degree_one()
        elif self.degree == 2:
            self.print_if_degree_two()
        else:
            print "The polynomial degree is stricly greater than 2, I can't solve."

    def print_if_degree_zero(self):
        if self.reduced_form[0] != 0:
            print "The equation has no solution."
        else:
            print "The solutions are all complex numbers."

    def print_if_degree_one(self):
        print "The solution is:\n{}".format(get_float_str_to_print(self.x0))

    def print_if_degree_two(self):
        if self.delta == 0:
            print "Discriminant is null, the only solution is:\n{}".format(self.x0)
        elif self.delta > 0:
            print "Discriminant is strictly positive, the two solutions are:\n{}\n{}".format(
                get_float_str_to_print(self.x0),
                get_float_str_to_print(self.x1),
                )
        else:
            print "Discriminant is strictly negative, the two complex solutions are:"
            print_complex(self.z0)
            print_complex(self.z1)
