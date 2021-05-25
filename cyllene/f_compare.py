import sympy as sp

import cyllene.f_aux as fa


def compare_functions(func_1, func_2, mode="full"):
    """
    check whether two sympy expressions are equivalent
    """
    
    # get variables
    var_1 = fa.get_variables(func_1)
    var_2 = fa.get_variables(func_2)

    # if the functions have different number of free symbols, stop right away
    if len(var_1) != len(var_2):
        return False

    # first check whether they are literally equal
    if func_1 == func_2:
        return True

    elif mode == "strict":
        return False

    # if mode is "terms", check whether they have the same terms

    # decompose both functions into terms
    f = func_1.as_terms()
    g = func_2.as_terms()

    # if number of terms different but we require equal terms, return False
    if len(f[0]) != len(g[0]):

        if mode == 'terms':
            return False

    else:
        # generate lists of terms
        f_terms = [sp.sympify(f[0][i][0]) for i in range(len(f[0]))]
        g_terms = [sp.sympify(g[0][i][0]) for i in range(len(f[0]))]

        # loop through terms and try to find match
        num = len(f[0])
        for i in range(len(f[0])):
            if num == 0:
                return True
            for j in range(num):
                if sp.simplify(f_terms[i] - g_terms[j]) == 0:
                    num = num - 1
                    del g_terms[j]
                    break
                else:
                    pass

        # all terms have matches
        if num == 0:
            return True

    # if we haven't returned True so far and mode is 'terms', return False
    if mode == "terms":
        return False

    # Now check whether Sympy can simplify difference to 0
    if sp.simplify((func_1 - func_2).expand(force=True)) == 0:
        return True

    # If mode is 'symbolic', this is all we can do
    if mode == 'symbolic':
        return False

    # Finally, perform a numerical test for equality.
    # Test 2000 equidistant points.
    if len(var_1) == 0:
        try:
            if float(func_1) == float(func_2):
                return True
        except:
            return False

    elif len(var_1) == 1:
        d1 = sp.calculus.util.continuous_domain(func_1, var_1[0], sp.S.Reals)
        d2 = sp.calculus.util.continuous_domain(func_2, var_2[0], sp.S.Reals)
        if d1 != d2:
            return False
        inf = d1.inf
        sup = d1.sup
        if inf == -sp.oo:
            inf = -100
        if sup == sp.oo:
            sup = 100
        sample = []
        h = (sup - inf) / 2000
        for i in range(2000):
            p = inf + (i * h)
            if d1.contains(p):
                sample.append(p)
                if func_1.subs(var_1[0], p) != func_2.subs(var_2[0], p):
                    return False
        if len(sample) > 500:
            return True

    """
    Not able to detect any difference between the functions.
    So we just assume they are identical.
    """
    return "undecided"
