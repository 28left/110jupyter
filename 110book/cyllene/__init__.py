__version__ = "0.2"

import cyllene.p_problem as pp
from cyllene.p_problem import ProbStack

import cyllene.m_input_tweaks
import cyllene.m_magics

from cyllene.m_user_cmd import function, expression, graph

# Reserve some (real-valued) symbols in Sympy
from sympy import symbols
a, b, c, d, p, q, r, s, t, w, x, y, z = \
    symbols('a b c d p q r s t w x y z', real=True)

# Reserve some more symbols
k, C, L = symbols('k C L', real=True)

# Reserve standard function symbols
# f, g, h = sp.symbols('f g h', cls=sp.core.function.Function)

MYLOCALS = {'a': a, 'b': b, 'c': c, 'd': d, 'p': p, 'q': q, 'r': r,
            's': s, 't': t, 'w': w, 'x': x, 'y': y, 'z': z}


# Basic library of specific functions
RANDOM_FUNCTION_LIST = [
    ['2x+1', 'linear'], ['3x-1', 'linear'], ['(1/2)*x+3', 'linear'],
    ['x+5', 'linear'], ['x-3', 'linear'], ['-x+4', 'linear'],
    ['(1/4)*x-1', 'linear'],
    ['6t', 'linear'], ['2-6t', 'linear'], ['(1/3)*x+2', 'linear'],
    ['(1/4)*x+3', 'linear'], ['(1/5)*x+4', 'linear'], ['(1/6)*x+5', 'linear'],
    ['(1/7)*x+6', 'linear'], ['(1/8)*x+7', 'linear'], ['(1/9)*x+8', 'linear'],
    ['(1/2)*(t**2)', 'quadratic'], ['3*(t**2)+7*t+1', 'quadratic'],
    ['6*(x**2)-8*x+3', 'quadratic'], ['3*(x**2)+5', 'quadratic'],
    ['(2*x+1)^2', 'quadratic'],
    ['(x+3)^2', 'quadratic'], ['(1/6)*(x**2)+1/2', 'quadratic'],
    ['(1/3)*x^2 +2x+1', 'quadratic'], ['(1/4)*(x**2)+2*x+1', 'quadratic'],
    ['(1/5)*(x**2)+4*x', 'quadratic'], ['(1/7)*x^2+3x-2', 'quadratic'],
    ['t**3 + 5*t -12 ', 'cubic'], ['x**3-3*(x**2)+5*x', 'cubic'],
    ['4*(x**3)-2', 'cubic'],
    ['2*(x**3)-3*(x**2)+1', 'cubic'], ['t**3+t', 'cubic'],
    ['t**3-8', 'cubic'], ['-2*x^3-3', 'cubic'], ['-4*x^3+1', 'cubic'],
    ['4*(x**3)+2*x+1', 'cubic'], ['-8*x^3+3*x^2+1', 'cubic'],
    ['y**3-4*y+2', 'cubic'], ['-2*y^3+3', 'cubic'],
    ['7*(x**3)+2*(x**2)', 'cubic'],
    ['x+5', 'increasing'], ['x**3+5', 'increasing'],
    ['2*(x**3)-8', 'increasing'],
    ['2*log(x)', 'increasing'], ['2*x^5-9', 'increasing'],
    ['3*x-3', 'increasing'],
    ['12*x^3-12', 'increasing'], ['7*x-2', 'increasing'],
    ['(1/4)*x-1/2', 'increasing'],
    ['(x-3)^3', 'increasing'], ['-x-2', 'decreasing'],
    ['-x^3+5', 'decreasing'],
    ['-2*log(x)+1', 'decreasing'], ['-2*x-4', 'decreasing'],
    ['-x^7+3', 'decreasing']
]

