import sympy as sp
import random

from cyllene import *
f = function('cubic')
f1 = function('quadratic')
f2 = function('quadratic')

r = random.randint(-2,2)
s = random.randint(-2,2)


def g(x):
    if x >= s:
        return f1(x)
    else:
        return f2(x)

F1 = Function(f1(x))
F2 = Function(f2(x))


P_1 = pp.ExpressionProblem(
    name = '1',
    statement = r'Below, you see a table in which we evaluate a function $f(x)$ for values of $x$ that are closer and closer to $%d$ (but **not equal to** $%d$). \
    What do the values $f(x)$ suggest $\lim_{x\to %d} f(x)$ would be?'%(r,r,r),
    num_inputs = 1,
    expression = '',
    answer_type = 'numerical',
    correct_answer = [f(r)],
    supplemental = function_to_sheet(f, ['x', 'f(x)'], [r+sign(i)*10**(-abs(i)) for i in [-1,-3,3,1]]),
    statement_after = r'(You can edit the table to compute further values of $f$)'
    )

# Add problem to stack
ProbStack.add(P_1)


P_2 = pp.ExpressionProblem(
    name = '2',
    statement = r'Use the function evaluation cell above to estimate the left-hand limit $\lim_{x \to {%d}^-} g(x)$'%s,
    num_inputs = 1,
    expression = '',
    answer_type = 'numerical',
    correct_answer = [f2(s)]
    )

# Add problem to stack
ProbStack.add(P_2)


P_3 = pp.ExpressionProblem(
    name = '3',
    statement = r'Use the function evaluation cell above to estimate the right-hand limit $\lim_{x \to {%d}^+} g(x)$'%s,
    num_inputs = 1,
    expression = '',
    answer_type = 'numerical',
    correct_answer = [f1(s)]
    )

# Add problem to stack
ProbStack.add(P_3)