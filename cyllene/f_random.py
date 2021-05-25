import random
import sympy as sp

# Reserve some (real-valued) symbols in Sympy
a, b, c, d, p, q, r, s, t, w, x, y, z = sp.symbols(
    'a b c d p q r s t w x y z', real=True)

# Basic library of specific functions
RANDOM_FUNC_LIST = [
    ['2x+1', 'linear'], ['3x-1', 'linear'], ['(1/2)*x+3', 'linear'],
    ['x+5', 'linear'], ['x-3', 'linear'], ['-x+4',
                                           'linear'], ['(1/4)*x-1', 'linear'],
    ['6t', 'linear'], ['2-6t', 'linear'], ['(1/3)*x+2', 'linear'],
    ['(1/4)*x+3', 'linear'], ['(1/5)*x+4', 'linear'], ['(1/6)*x+5', 'linear'],
    ['(1/7)*x+6', 'linear'], ['(1/8)*x+7', 'linear'], ['(1/9)*x+8', 'linear'],
    ['(1/2)*(t**2)', 'quadratic'], ['3*(t**2)+7*t+1', 'quadratic'],
    ['6*(x**2)-8*x+3', 'quadratic'], ['3*(x**2)+5',
                                      'quadratic'], ['(2*x+1)^2', 'quadratic'],
    ['(x+3)^2', 'quadratic'], ['(1/6)*(x**2)+1/2', 'quadratic'],
    ['(1/3)*x^2 +2x+1', 'quadratic'], ['(1/4)*(x**2)+2*x+1', 'quadratic'],
    ['(1/5)*(x**2)+4*x', 'quadratic'], ['(1/7)*x^2+3x-2', 'quadratic'],
    ['t**3 + 5*t -12 ',
        'cubic'], ['x**3-3*(x**2)+5*x', 'cubic'], ['4*(x**3)-2', 'cubic'],
    ['2*(x**3)-3*(x**2)+1', 'cubic'], ['t**3+t', 'cubic'],
    ['t**3-8', 'cubic'], ['-2*x^3-3', 'cubic'], ['-4*x^3+1', 'cubic'],
    ['4*(x**3)+2*x+1', 'cubic'], ['-8*x^3+3*x^2+1', 'cubic'],
    ['y**3-4*y+2', 'cubic'], ['-2*y^3+3',
                              'cubic'], ['7*(x**3)+2*(x**2)', 'cubic'],
    ['x+5', 'increasing'], ['x**3+5',
                            'increasing'], ['2*(x**3)-8', 'increasing'],
    ['2*log(x)', 'increasing'], ['2*x^5-9',
                                 'increasing'], ['3*x-3', 'increasing'],
    ['12*x^3-12', 'increasing'], ['7*x-2',
                                  'increasing'], ['(1/4)*x-1/2', 'increasing'],
    ['(x-3)^3', 'increasing'], ['-x-2', 'decreasing'],
    ['-x^3+5', 'decreasing'], ['-2*log(x)+1', 'decreasing'],
    ['-2*x-4', 'decreasing'], ['-x^7+3', 'decreasing']
]


def set_linear(coeff_low=-5, coeff_high=5):
    a = random.randint(coeff_low, coeff_high)
    return x + a


def set_quadratic(coeff_low=-5, coeff_high=5):
    return random.randint(coeff_low, coeff_high)*(x**2) + random.randint(coeff_low, coeff_high)*x+random.randint(coeff_low, coeff_high)


def set_cubic(low=-5, high=5):
    a = random.randint(low, high)
    b = random.randint(low, high)
    c = random.randint(low, high)
    d = random.randint(low, high)
    return a*(x ** 3)+b*(x ** 2)+c ** x + d

# set_pow() can generate any power function, e.g. 'const', 'linear', 'quadratic', 'cubic'


def set_pow(exponent=1, coeff_low=-5, coeff_high=5):
    result = 0*x
    for c in range(exponent+1):
        result += random.randint(coeff_low, coeff_high)*(x**c)
    return result

# set_mon(deg) can generate monomial with degree 'deg'


def set_mon(deg=2):
    a = random.randint(-4, 6)
    if a == 0:
        return x**deg
    else:
        return a*(x**deg)


def set_sqrt(coeff_low=1, coeff_high=8):
    return sp.sqrt(random.randint(coeff_low, coeff_high)*x + random.randint(coeff_low, coeff_high))


def set_cbrt(coeff_low=1, coeff_high=8):
    return sp.cbrt(random.randint(coeff_low, coeff_high)*x + random.randint(coeff_low, coeff_high))


def set_rational():
    a = random.randint(-3, 3)
    b = random.randint(-3, 3)
    c = random.randint(1, 2)
    d = random.randint(-2, 2)
    return (a*x+b) / (c*(x**2)+d)


def set_exp(coeff_low=-5, coeff_high=5):
    a = random.randint(coeff_low, coeff_high)
    b = random.randint(coeff_low, coeff_high)
    if a != 0:
        return a*sp.exp(x)+b
    else:
        return sp.exp(x) + b


def set_log(coeff_low=-5, coeff_high=5):
    a = random.randint(coeff_low, coeff_high)
    b = random.randint(coeff_low, coeff_high)
    if a != 0:
        return a*sp.log(x) + b
    else:
        return sp.log(x) + b


def set_sin(coeff_low=-5, coeff_high=5):
    a = random.randint(coeff_low, coeff_high)
    b = random.randint(coeff_low, coeff_high)
    if a != 0:
        return a*sp.sin(x) + b
    else:
        return sp.sin(x) + b


def set_cos(coeff_low=-5, coeff_high=5):
    a = random.randint(coeff_low, coeff_high)
    b = random.randint(coeff_low, coeff_high)
    if a != 0:
        return a*sp.cos(x) + b
    else:
        return sp.cos(x) + b


def set_type(*args):
    if args[0] == 'pow':
        return set_pow(args[1])
    elif args[0] == 'linear':
        return set_linear()
    elif args[0] == 'quadratic':
        return set_quadratic()
    elif args[0] == 'cubic':
        return set_cubic()
    elif args[0] == 'squareroot':
        return set_sqrt()
    elif args[0] == 'cubicroot':
        return set_cbrt()
    elif args[0] == 'rational':
        return set_rational()
    elif args[0] == 'exp':
        return set_exp()
    elif args[0] == 'log':
        return set_log()
    elif args[0] == 'sin':
        return set_sin()
    elif args[0] == 'cos':
        return set_cos()
    elif args[0] == 'tri':
        sign = random.choice([0, 1])
        if sign == 1:
            return set_sin()
        else:
            return set_cos()


def set_function_random(*args):

    FUNCTION_LIST = ['const', 'linear', 'quadratic', 'cubic', 'squareroot',
                     'cubicroot', 'rational', 'exp', 'tri', 'log',
                     'comp', 'monomial']

    if (len(args) == 0) or (args[0] not in FUNCTION_LIST):
        function_type = random.choice(FUNCTION_LIST)
    else:
        function_type = args[0]

    if function_type == 'const':
        expr = set_pow(0, -5, 5)

    elif function_type == 'linear':
        expr = set_pow(1, -5, 5)

    elif function_type == 'quadratic':
        expr = set_pow(2, -6, 6)

    elif function_type == 'cubic':
        expr = set_pow(3, -6, 6)

    elif function_type == 'squareroot':
        expr = set_sqrt()

    elif function_type == 'cubicroot':
        expr = set_cbrt()

    elif function_type == 'rational':
        expr = set_rational()

    elif function_type == 'exp':
        expr = set_exp()

    elif function_type == 'tri':

        sign = random.choice([0, 1])
        if sign == 1:
            expr = set_sin()

        else:
            expr = set_cos()

    elif function_type == 'monomial':
        expr = set_mon(args[1])

        """
        when we want to generate a monomial,
        we call set_function_random('monomial',power)
        where 'power' should be a  !!! integer number !!!,
        indicating the degree, e.g.
        f = set_function_random('monomial',2) can generate
        a quadratical monomial.
        """

    elif function_type == 'log':
        expr = set_log()

    elif function_type == 'comp':
        """
        in this case, if we want to create some composite function,
        in the *args, we need to provide
        ('comp','out_layer func','In_layer func')
        for example:  f = ...('comp','quadratic','log')
        could generate function like (log(x))^2 + 3
        """
        if len(args) < 3:
            args = ['comp', '', '']
            args[1] = random.choice(['const', 'linear', 'quadratic', 'cubic', 'squareroot',
                     'cubicroot', 'rational', 'exp', 'tri', 'log'])
            args[2] = random.choice(['const', 'linear', 'quadratic', 'cubic', 'squareroot',
                     'cubicroot', 'rational', 'exp', 'tri', 'log'])

        tmp = set_type(args[1])
        expr_in = set_type(args[2])

        expr = tmp.subs(x, expr_in)

    return expr
