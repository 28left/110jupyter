import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

import cyllene.f_aux as fa


# Reserve some (real-valued) symbols in Sympy
a, b, c, d, p, q, r, s, t, w, x, y, z = sp.symbols(
    'a b c d p q r s t w x y z', real=True)

MYLOCALS = {'a': a, 'b': b, 'c': c, 'd': d, 'p': p, 'q': q, 'r': r,
            's': s, 't': t, 'w': w, 'x': x, 'y': y, 'z': z}

def plot_from_list(x_vals, y_vals):
    """ Takes two lists of values and a scatter plot of the points """
    if len(x_vals) != len(y_vals):
        print("length not equal")
        return None

    # point_list_x = []
    # point_list_y = []
    # for i in range(len(x_vals)):
    #     point_list_x.append(x_vals[i])
    #     point_list_y.append(y_vals[i])
    point_list_x = np.asarray(x_vals)
    point_list_y = np.asarray(y_vals)
    return plt.scatter(point_list_x, point_list_y)



def d_control(func):

    # rename main variable to x
    func = func.subs(fa.get_variable(func), x)

    # control derivative
    yprime = func.diff(x)
    c_1 = sp.solve(yprime-10, x)
    c_2 = sp.solve(yprime+10, x)
    c_3 = sp.solve(sp.Eq(yprime*10, 1), x)
    c_4 = sp.solve(sp.Eq(yprime*10, -1), x)


    return fa.remove_complex(c_1 + c_2 + c_3 + c_4)

def nice_range (mylist, func):

    # rename main variable to x
    func = func.subs(fa.get_variable(func), x)

    yprime = sp.diff(func)
    a = yprime.subs(x, 0)
    b = yprime.subs(x, 10)

    c = func.subs(x,0)

    # if the control list is empty
    if not mylist:

        # if derivate is always small
        if -1 < 10*a < 1:
            zeros = sp.solve(func, x)

            # if it has no zeros
            if not zeros:
                min_x = -10
                max_x = 10
                min_y = c + 2
                max_y = c - 2
                range_x = [min_x, max_x]
                range_y = [min_y, max_y]

                return range_x, range_y

            l_x = fa.min_sp_list(zeros)
            r_x = fa.max_sp_list(zeros)

            min_x = l_x - (r_x-l_x)/4
            max_x = r_x + (r_x-l_x)/4

            min_y = - (max_x-min_x)/10
            max_y = (max_x-min_x)/10

            range_x = [min_x, max_x]
            range_y = [min_y, max_y]
            return range_x, range_y

        # if derivative is not always small, in this case f will be monotone, it must have zeros
        else:
            zeros = sp.solve(func, x)
            zeros = fa.remove_complex(zeros)

            l_x = fa.min_sp_list(zeros)
            r_x = fa.max_sp_list(zeros)

            min_x = l_x - (r_x-l_x)/10
            max_x = r_x + (r_x-l_x)/10

            # if derivative is medium
            if abs(a) < 20:
                min_y = - (r_x-l_x)*(abs(a)+abs(b))
                max_y = - min_y
            # if derivative is always huge
            else:
                min_y = - (r_x-l_x)*(abs(a)+abs(b))/2
                max_y = - min_y

            range_x = [min_x, max_x]
            range_y = [min_y, max_y]
            return range_x, range_y

    # if control list is not empty
    else:
        zeros = sp.solve(func, x)
        zeros = fa.remove_complex(zeros)
        mylist = zeros + mylist

        l_x = fa.min_sp_list(mylist)
        r_x = fa.max_sp_list(mylist)

        min_x = l_x - (r_x-l_x)/10
        max_x = r_x + (r_x-l_x)/10

        crits = sp.solve(yprime, x)
        crits = fa.remove_complex(crits)

        y_crits = [func.subs(x, t) for t in crits]
        y_list = [func.subs(x, t) for t in mylist]

        y_choice = y_crits + y_list
        y_choice = fa.remove_complex(y_choice)

        l_y = fa.min_sp_list(y_choice)
        r_y = fa.max_sp_list(y_choice)

        min_y = l_y - (r_y-l_y)/8
        max_y = r_y + (r_y-l_y)/8

        range_x = [min_x, max_x]
        range_y = [min_y, max_y]
        return range_x, range_y


def find_plot_range(func):

    # rename main variable to x
    func = func.subs(fa.get_variable(func), x)

    # case distinction based on type of function
    if func.is_constant():
        min_x = -5
        max_x = 5
        y_0 = func.subs(x,0)
        min_y = min(y_0, -1, 1)
        max_y = max(y_0, -1, 1)

        return [min_x, max_x], [min_y, max_y]

    elif fa.is_linear(func):
        y_0 = func.subs(x,0)
        l_x = min(sp.solve(func,x), 0, 1)
        r_x = max(sp.solve(func,x), 0, 1)
        min_x = l_x - (r_x-l_x)/8
        max_x = r_x + (r_x-l_x)/8

        l_y = min(y_0, -1, 1)
        r_y = max(y_0, -1, 1)

        min_y = l_y - (r_y-l_y)/10
        max_y = r_y + (r_y-l_y)/10
        return [min_x, max_x], [min_y, max_y]

    else:
        list_x = d_control(func)
        return nice_range(list_x, func)
