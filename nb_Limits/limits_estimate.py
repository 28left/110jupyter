import sympy as sp
import random

import sys, os
sys.path.append(os.path.abspath('..'))
from cyllene import *
from IPython.display import Markdown, Latex


def show_values(f,r):
    display(Markdown("Current values: "))
    display(Latex("$f(x)= "+sp.latex(f(x))+"$"))
    display(Latex("r =  "+sp.latex(r)))


def show_limit_estimate(f,r):

    display(Markdown("As the values of x get closer and closer to <br>")) 
    display(Markdown("`"+str(r)+"`"))
    display(Markdown("the values f(x) seem to get close to somewhere around")) 
    display(Markdown("`"+str((sp.N(f(r-0.001),4)+sp.N(f(r+0.001),4))/2)+"`"))

def limit(f,r):

    return sp.limit(f(x),x,r)

def lim_left(f,r):

    return sp.limit(f(x),x,r, dir='-')

def lim_right(f,r, dir='-'):

    return sp.limit(f(x),x,r)


def show_limit_analysis(f,r):
    display(Markdown("We have set: "))
    display(Latex("$f(x)= "+sp.latex(f(x))+"$"))
    display(Latex("$r =  "+sp.latex(r)+"$"))

    display(Markdown("<br>"))
    display(Markdown("**Problem**: *Estimate*  "))
    display(Latex("$\large \lim_{x \\to r} f(x)$"))
    display(Markdown("---"))
    
    display(Markdown("We generate a table of values of f around (but *not exactly at*) r"))

    display(show_table(f, [r-0.1, r-0.01, r-0.001, r+0.001, r+0.01, r+0.1]))

    display(Markdown("<br>"))

    display(Markdown("What do the values suggest a reasonable estimate for the limit would be?"))
    # display(Markdown("As the values of x get closer and closer to <br>")) 
    # display(Markdown("`"+str(r)+"`"))
    # display(Markdown("the values f(x) seem to get close to somewhere around")) 
    # display(Markdown("`"+str((sp.N(f(r-0.001),4)+sp.N(f(r+0.001),4))/2)+"`"))



def generate_example():

    s = random.randint(-30,30)/10
    b = (random.randint(-10,10)+5)**2/10
    g1 = function('quadratic')
    g2 = function(g1(x)+b)
    g = function(sp.Piecewise((g1(x), x<s),  (g2(x),x>s), (g1(s)+2*b, True)))

    display(Latex("$\\text{New $g(x), s$ generated}$"))
    display(Latex("$s = " + str(s) + "$"))
    # display(Markdown('<br>'))
    display(Markdown("**Problem**: *Estimate the one-sided limits*  "))
    display(Latex("$ \lim_{x \\to s^-} g(x) \\text{ and } \lim_{x \\to s^+} g(x)$"))

    return g, s





display(Markdown("Initialization successful"))
