import cyllene
from cyllene import *

from sympy import diff

f= function('4^x')

P_1 = pp.TrueFalse('1',"The function $f(x) = 4^x$ is one-to-one.", True, input_widget=True, output_widget=True)
ProbStack.add(P_1)

P_2 = pp.MultipleChoice('2', "The domain of $f(x) = 4^x$ is", ["$(-\infty,\infty)$", "$(0,\infty)$", "$(-1,1)$", "$(-\infty,0]$", "$[4,\infty)$"], input_widget=True, output_widget=True)
ProbStack.add(P_2)

P_3 = pp.MultipleChoice('3', "The range of $f(x) = 4^x$ is", ["$(0,\infty)$", "$(-\infty,\infty)$", "$[-1,1]$", "$(-\infty,0]$", "$[4,\infty)$"], input_widget=True, output_widget=True)
ProbStack.add(P_3)

P_4 = pp.ExpressionProblem('4', 'The $y$-intercept of $f(x) = 4^x$ is at', 1, '$y =$ ', 'numerical', f(0), eval_mode='full', input_widget=True, output_widget=True)
ProbStack.add(P_4)

P_5 = pp.ExpressionProblem('5', 'Fill in the blank:', 1, 'The graph of $f$ contains the point $(1,$\_\_\_$)$.', 'numerical', f(1))
ProbStack.add(P_5)
