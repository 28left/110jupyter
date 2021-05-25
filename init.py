import cyllene
from cyllene import *
import sympy as sp
import random


# a, b, c, d, p, q, r, s, t, w, x, y, z = \
#     var('a b c d p q r s t w x y z', domain='real')
# # RealNumber = float; Integer = int


P_1 = pp.ExpressionProblem('1',
                 'What is the smallest sphenic number?',      
                 1,
                 '',
                 'numerical',
                 [expression(30)]
                 )

# Add problem to stack
ProbStack.add(P_1)


s_2 = sp.sympify('1/6', evaluate=True)

P_2 = pp.ExpressionProblem('2',
                 r'What is $\frac{2}{3}-\frac{1}{2}$?',
                 1,
                 '',
                 'numerical',
                 [s_2]
                 )

# Add problem to stack
ProbStack.add(P_2)




P_3 = pp.ExpressionProblem('3', r'$ 1.01+0.22 = $ ? ', 1,  '', 'numerical', [expression(1.23)])
ProbStack.add(P_3)


P_4 = pp.ExpressionProblem('4', r'Simplify:   $\qquad 5x - 3x$ ', 1,  '', 'expression', [expression('2x')])
ProbStack.add(P_4)


P_5 = pp.ExpressionProblem('5', r'Input the fraction $\qquad \dfrac{x+3}{x^2-1}$ ', 1,  '', 'expression', [expression('(x+3)/(x^2-1)')])
ProbStack.add(P_5)

 
def generate_problem(name, out=True):
    global problemStack

    params = [random.randint(2,6) for i in range(3)]
    sol = sp.sympify(sp.Rational(params[2]-params[1],params[0]), rational=True)

    myProblem = pp.ExpressionProblem(name,
                        r"Solve $ "+ str(params[0])+"x+"+str(params[1])+" = "+ str(params[2])+"$ for $x$.", 
                        1,
                        '',
                        'numerical',
                        [sol],
                        regen=True
                       )
    ProbStack.add(myProblem)

    if out:
        myProblem.state_problem()


generate_problem('6', out=False)
