
import sympy as sp

import cyllene.f_aux as fa
import cyllene.f_functionclass as ff
import cyllene.f_compare as fc


def function(expr):
    """
    Defines a function based on a syntax check
    and a Function object, using lambda operator.
    Returns a pure function.
    """
    func = ff.Function(expr)

    if func.is_defined:
        return lambda x: func.eval_at(x)

    else:
        issues_report=''.join(['\t' + str(i+1) + '. ' + func.issues[i]+'\n' \
            for i in range(len(func.issues))])
        print('Problems encountered:\n' + issues_report)
        return None
        # raise ValueError('Problems encountered:\n'+issues_report)

# def function(expr):
#     [func, issues] = fd.define_function(expr)
#     if issues:
#         print("Invalid format")
#         return None
#     else:
#         return func

def random_function(arg='random'):
    """
    Pick a function at random. 
    One of the folliwing types can be specified:
    'const', 'linear', 'quadratic', 'cubic', 'squareroot',
    'cubicroot', 'rational', 'exp', 'tri', 'log', 'comp',
    'random'
    """
    if arg in ff.FUNCTION_LIST:
        func = ff.Function(arg)
    else:
        func = ff.Function('random')

    return lambda x: func.eval_at(x)
    

def expression(expr):
    """
    Defines a function based on a syntax check
    and a Function object.
    Returns a Sympy object.
    """
    func = ff.Function(expr)

    if func.is_defined:
        return func.sym_form

    else:
        issues_report=''.join(['\t' + str(i+1) + '. ' + func.issues[i]+'\n' \
            for i in range(len(func.issues))])
        print('Problems encountered:\n' + issues_report)
        return None


def compare(expr1, expr2):
    return fc.compare_functions(expr1, expr2)

    
def graph(expr):
    """ Try to find good plotting range and plot the graph """

    var = fa.get_variables(expr)

    try:
        [xran, yran] = fpl.find_plot_range(expr)
        sp.plot(expr, (var[0], xran[0], xran[1]), axis_center=(0,0),
            ylim=(yran[0],yran[1]))
    except:
        sp.plot(expr)
