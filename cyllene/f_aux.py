import sympy as sp
import cyllene.a_mathstring as ms

# Reserve some (real-valued) symbols in Sympy
a, b, c, d, p, q, r, s, t, w, x, y, z = sp.symbols(
    'a b c d p q r s t w x y z', real=True)

MYLOCALS = {'a': a, 'b': b, 'c': c, 'd': d, 'p': p, 'q': q, 'r': r,
            's': s, 't': t, 'w': w, 'x': x, 'y': y, 'z': z}


def get_variables_from_list_form(list_form):
    '''
    Accepts a list form of a function (as given by string_to_list)
    and returns a list of all variables
    without duplicates.
    '''
    var = list(set(get_variables_with_duplicates(list_form)))
    return var


def get_variables_with_duplicates(list_form):
    '''
    Accepts a list form of a function (as given by string_to_list)
    and returns a list of all variables.
    It does this by recursively checking each constituent list
    for variables. The result may include duplicates.
    '''
    if type(list_form) is not list:
        if ms.is_number(list_form):
            return []
        else:
            return [list_form]

    if len(list_form) == 2:
        return get_variables_from_list_form(list_form[1])
    else:
        return get_variables_from_list_form(list_form[1])\
            + get_variables_from_list_form(list_form[2])


def get_variables(expr):
    """
    If the parameter is a sympy expression, pull the variables
    using free_symbols.
    If list form, call separate subroutine.
    """
    if isinstance(expr, sp.Basic):
        return list(expr.free_symbols)

    else:
        return get_variables_from_list_form(expr)


def set_variable_x(expr):
    """
    Given an expression, return one with
    the first (only) variable to be x.
    """
    if get_variables(expr):
        return expr.subs(get_variables(expr)[0], x)
    else:
        return expr


def get_domain(expr):
    """
    Get the (real) domain of an expression.
    Returns Sympy set
    """
    var = get_variables(expr)

    try:
        if var:
            return sp.calculus.util.continuous_domain(expr, var[0], sp.S.Reals)
        else:
            return sp.calculus.util.continuous_domain(expr, x, sp.S.Reals)

    # ran into a bug in sp.calculus.util.continuous_domain, return R for now
    except TypeError:
        return sp.S.Reals



def remove_complex(mylist):
    """ returns a list that is free of complex valued entries """

    new_list = []
    for r in mylist:
        # treat very small complex parts as real
        # (due to numerics)
        if round(sp.N(r), 10).is_real:
            new_list.append(sp.re(r))

    return new_list

"""
input list of numbers in sympy form, output the max and min value of it.
"""
def max_sp_list(mylist):
    if not list:
        return 0
    else:
        mylist =  [r.evalf() for r in mylist]
        return  round(max(mylist), 3)


def min_sp_list(mylist):
    if not mylist:
        return 0
    else:
        mylist =  [r.evalf() for r in mylist]
        return  round(min(mylist), 3)


"""
Given a sympy expression and a list of numbers, output the min y-value
"""
def min_sp_list_y(mylist, func):

    # rename main variable to x
    func = func.subs(get_variable(func), x)

    if not mylist:
        return 0
    else:
        mylist_y = [round(func.subs(x,r),3) for r in mylist]
        return  round(min(mylist_y), 3)


def is_linear(func):

    return bool(sp.diff(func).is_constant())
