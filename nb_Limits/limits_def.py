import sympy as sp
import random

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

def show_limit_analysis(f,r):
    display(Markdown("We have set: "))
    display(Latex("$f(x)= "+sp.latex(f(x))+"$"))
    display(Latex("$r =  "+sp.latex(r)+"$"))

    display(Markdown("---"))
    
    display(Markdown("We generate a table of values of f around (but *not exactly at*) r"))

    display(show_table(f, [r-0.1, r-0.01, r-0.001, r+0.001, r+0.01, r+0.1]))

    display(Markdown("---"))

    display(Markdown("As the values of x get closer and closer to <br>")) 
    display(Markdown("`"+str(r)+"`"))
    display(Markdown("the values f(x) seem to get close to somewhere around")) 
    display(Markdown("`"+str((sp.N(f(r-0.001),4)+sp.N(f(r+0.001),4))/2)+"`"))










f1 = None
f2 = None    
g1 = None
g2 = None    

r = None
s = None



def g_right(x):
    if x > r:
        return f1(x)
    else:
        return f2(x)

def g(x):
    if x >= s:
        return g1(x)
    else:
        return g2(x)


def genP1(*args):
    f = function('cubic')
    r = random.randint(-2,2)
    return[
        r'Below, you see a table in which we evaluate a function $f(x)$ for values of $x$ that are closer and closer to $%d$ (but **not equal to** $%d$). \
    What do the values $f(x)$ suggest $\lim_{x\to %d} f(x)$ would be?'%(r,r,r),
        '',
        function_to_table(f, [r+sign(i)*10**(-abs(i)) for i in [-1,-2,-3,3,2,1]]),
        '',        
        [f(r)]
    ]

P_1 = pp.ParameterProblem(
    name = '1',
    num_inputs = 1,
    answer_type = 'numerical',
    generator = genP1,
    parameters = []
    )

# Add problem to stack
ProbStack.add(P_1)



def genP2(*args):

    global f1, f2, r 
    f1 = function('quadratic')
    f2 = function('quadratic')    
    r = random.randint(-2,2)
  
    return[
        r'Below, you see a spreadshet in which some values of a function $f(x)$ are computed. \
    What do the values $f(x)$ suggest the **right-hand limit** $\lim_{x\to %d^+} f(x)$ would be?'%r,
        '',
        function_to_sheet(g_right, ['x', 'f(x)'], [r+sign(i)*10**(-abs(i)) for i in [4,3,2,1]]),
        r'(You can edit the spreadsheet to compute further values of $f$)',        
        [f1(r)]
    ]

P_2 = pp.ParameterProblem(
    name = '2',
    num_inputs = 1,
    answer_type = 'numerical',
    generator = genP2,
    parameters = []
    )

# Add problem to stack
ProbStack.add(P_2)

# P_1 = pp.ExpressionProblem(
#     name = '1',
#     statement = r'Below, you see a table in which we evaluate a function $f(x)$ for values of $x$ that are closer and closer to $%d$ (but **not equal to** $%d$). \
#     What do the values $f(x)$ suggest $\lim_{x\to %d} f(x)$ would be?'%(r,r,r),
#     num_inputs = 1,
#     expression = '',
#     answer_type = 'numerical',
#     correct_answer = [f(r)],
#     supplemental = function_to_sheet(f, ['x', 'f(x)'], [r+sign(i)*10**(-abs(i)) for i in [-1,-3,3,1]]),
#     statement_after = r'(You can edit the table to compute further values of $f$)'
#     )

# # Add problem to stack
# ProbStack.add(P_1)




def genP3(*args):

    global g1, g2, s 
    g1 = function('quadratic')
    g2 = function('quadratic')    
    s = random.randint(-2,2)
    
    return[
        r'Use the function evaluation cell above to estimate the **left-hand limit** $\lim_{x \to {%d}^-} g(x)$'%s,
        '',
        None, 
        '',        
        [g2(s)]
    ]


P_3 = pp.ParameterProblem(
    name = '3',
    num_inputs = 1,
    answer_type = 'numerical',
    generator = genP3,
    parameters = []
    )


# Add problem to stack
ProbStack.add(P_3)
