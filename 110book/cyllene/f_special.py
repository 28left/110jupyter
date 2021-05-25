import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def logistic_function(x,k,C,L):
    
    return L/(1+C*np.exp(-k*x))


def logistic_plot_L(L):

    plt.figure(2)
    x = np.linspace(-1, 20, num=1000)
    plt.plot(x, logistic_function(x,0.5, 10, L))
    plt.ylim(0, 10)
    plt.show()
