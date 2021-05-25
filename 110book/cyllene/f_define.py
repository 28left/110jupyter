import sympy as sp
import random

from fractions import Fraction

# MathString parsing library
import cyllene.a_mathstring as ms

# random function generator
import cyllene.f_random


# Reserve some (real-valued) symbols in Sympy
a, b, c, d, p, q, r, s, t, w, x, y, z = sp.symbols(
    'a b c d p q r s t w x y z', real=True)


MYLOCALS = {'a': a, 'b': b, 'c': c, 'd': d, 'p': p, 'q': q, 'r': r,
            's': s, 't': t, 'w': w, 'x': x, 'y': y, 'z': z}

FUNCTION_LIST = ['const', 'linear', 'quadratic', 'cubic', 'squareroot',
                 'cubicroot', 'rational', 'exp', 'tri', 'log', 'comp',
                 'random']


def define_expression(expr,
                      eval_mode=False,
                      return_issues=True):
    """
    sympify an input and return a sympy expression
    together with a list of issues (optional, possibly empty)

    parameters:
        eval_mode (Boolean): should sympify try to evaluate expression
        return_issues (Boolean): should list of issues during syntax check
            be returned

    Valid arguments
    - a string
    - a constant
    - a sympy expression

    The string can be a math string or one of the following expression types:
    'const', 'linear', 'quadratic', 'cubic', 'squareroot',
    'cubicroot', 'rational', 'exp', 'tri', 'log', 'comp', 'monomial'

    One can also pass 'random' to pick an expression randomly.        
    """

    
    if expr in FUNCTION_LIST:

        # First check whether string argument is a keyword
        if expr == 'random':
            expr = random.choice([
                'const', 'linear', 'quadratic',
                'cubic', 'squareroot',
                'cubicroot', 'rational',
                'comp', 'exp', 'tri', 'log'])

        if expr == 'comp':
            comp = [random.choice([
                    'const', 'linear', 'quadratic',
                    'cubic', 'squareroot',
                    'cubicroot', 'rational', 'exp', 'tri', 'log'])
                    for i in range(2)]
            new_expr = sp.sympify(
                f_random.set_function_random('comp', comp[0], comp[1]))

        else:
            new_expr = sp.sympify(f_random.set_function_random(expr))
        
        expr_ok = True 
        issues = []

    elif isinstance(expr, sp.Basic):
        # if expr is Sympy type, skip syntax check
        expr_ok = True
        new_expr = expr
        issues = []

    elif isinstance(expr, (int, float)):
        # if expr is numerical, directly sympify 
        expr_ok = True
        new_expr = sp.sympify(expr, evaluate=eval_mode)
        issues = []

    elif isinstance(expr, str):
        
#         try:
#             # if input can be turned into number, do this to avoid
#             # weird sympy bug
#             if '1/' in expr:
#                 # force sympy to ev
#                 check = [Fraction(expr), True, []]
#             elif '.' in expr:
#                 # has decimal point, try float conversion
#                 check = [float(expr), True, []]
#             else:
#                 # check integer
#                 check = [int(expr), True, []]
                
#         except ValueError:
#             # check syntax of expr;
#             # returns triple:
#             #   ['sanitized' string, compilable flag (boolean), issues list]
    
        check = ms.check_syntax(expr)
        
        if check[1]:
                  
            try:
                new_expr = sp.sympify(
                    check[0], locals=MYLOCALS, evaluate=eval_mode)
                if new_expr.is_real:
                    # if input is number, evaluate
                    new_expr = sp.sympify(
                        check[0], locals=MYLOCALS, evaluate=True)
                expr_ok = True
                issues = []

            except:
                expr_ok = False
                issues = ["invalid syntax"]

        else:
            # check_syntax discovered issues
            expr_ok = False
            issues = check[2]

    else:
        # argument expr is not of the right type
        expr_ok = False
        issues = ['unknown format']

    if expr_ok:
        return new_expr, []
    else:
        return None, issues



def define_function(expr, mode='numerical'):
    """
    sympify an expression and return a function evaluating this expression,
    together with a list of issues (optional, possibly empty)

    This uses SymPy's lambdify function.

    parameters:
        eval_mode (Boolean): should sympify try to evaluate expression
        return_issues (Boolean): should list of issues during syntax check
            be returned
    """
    
    [func, issues] = define_expression(expr, eval_mode=True)

    if func:
        if mode=='numerical':
            if len(func.free_symbols) > 0:
                # if there free symbols in func, use the first as the function var
                return sp.lambdify([func.free_symbols.pop()], func)
            #     return lambda u: func.evalf(subs={x, u}, n=5)
            else:
                # otherwise any symbol will do
                return sp.lambdify([x], func)
                # return lambda u: func.evalf(subs={x, u}, n=5)        

        else:
            if len(func.free_symbols) > 0:
                # if there free symbols in func, use the first as the function var
                # return sp.lambdify(func.free_symbols.pop(), func)
                return lambda u: func.subs(func.free_symbols.pop(), u)
            else:
                # otherwise any symbol will do
                # return sp.lambdify(x, func)
                return lambda u: func.subs(x, u)

    else:
        return None

