import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Reserve some (real-valued) symbols in Sympy
a, b, c, d, p, q, r, s, t, w, x, y, z = sp.symbols(
    'a b c d p q r s t w x y z', real=True)

MYLOCALS = {'a': a, 'b': b, 'c': c, 'd': d, 'p': p, 'q': q, 'r': r,
            's': s, 't': t, 'w': w, 'x': x, 'y': y, 'z': z}

def fit_poly(x_vals, y_vals, degree, plot=False):
    """ fit a polynomial based on points list """

    x_vals = np.asarray(x_vals)
    y_vals = np.asarray(y_vals)
    coeffs = np.polyfit(x_vals, y_vals, degree)
    func = 0
    for i in range(len(coeffs)):
        if coeffs[i] < 0.0000000001:
            coeffs[i] = 0
        func = func + sp.Pow(x, degree-i)*coeffs[i]

    if plot:
        x_min = x_vals.min()
        x_max = x_vals.max()
        x_axis = np.linspace(x_min - abs(x_max-x_min), x_max+abs(x_max-x_min), 100)
        y_axis = [func.subs(x, elem) for elem in x_axis]
        #print(y_axis)
        plt.plot(x_axis, y_axis)
        plt.scatter(x_vals, y_vals, color='r')
        plt.show()

    return func
