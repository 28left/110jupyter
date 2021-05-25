#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual, Layout
import ipywidgets as widgets
from traitlets import traitlets
from IPython.display import display, Math, Latex, Markdown, clear_output 
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from functools import partial
import random




#
# Auxiliary functions needed to parse function string inputs
#


# operator dictionary
unary_operators=['neg','sqrt','abs','exp','log','sin','cos','tan','sec','csc','cot','arcsin','arccos','arctan','arcsec','arccsc','arccot']
binary_operators=['+','-','*','/','^']

# Reserve some symbols in Sympy
x, y, z, h = sp.symbols('x y z h')

# Create dictionary with backslash terms
str_dict = {
    "Delta" : "\Delta",
    "frac"  : "\frac",
    "nl"    : "\n"
}

def is_number(s):
    # checks whether the string s is a number (integer or float)
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def is_letter(s):
    # checks whether the string s is a single letter. Returns false if s contains more than one character
    if len(s)==1 and s.isalpha():
        return True
    return False

def needs_times(string,i):
    # accepts a string and in index i. Returns true if string needs a '*' character inserted between positions i and i+1 in order to be properly interpreted as a function
    if i==len(string)-1:
        return False
    
    if is_letter(string[i]) and is_number(string[i+1]):
        return True
    if is_letter(string[i+1]) and is_number(string[i]):
        return True
    if is_number(string[i]) and string[i+1]=='(':
        return True
    if is_letter(string[i]) and string[i+1]=='(' and get_adjacent_characters(string,i)[0] not in unary_operators:
        return True
    if string[i]==')' and is_letter(string[i+1]):
        return True
    if string[i]==')' and is_number(string[i+1]):
        return True
    if string[i]==')' and string[i+1]=='(':
        return True
    
    return False

def get_adjacent_characters(string,i,test=lambda x:is_letter(x)):
    # returns a triple of the form [s,a,b] where s is the largest substring of string containing the index i where all the characters match a specific form. The default is that all the characters in s are letters. a and b are the indices in string of the first and last chcaracters in s respectively.
    s=string[i]

    if not test(s):
        return []
    
    j=i+1
    while j<len(string) and test(string[j]):
        s=s+string[j]
        j+=1
    
    k=i-1
    while k>-1 and test(string[k]):
        s=string[k]+s
        k-=1
    
    return [s,k+1,j-1]

def fix_minuses(string):
    # adjusts a string to account for the inconvenient fact that the '-' symbol can be interpreted as either a minus sign or a negative sign.
    i=0
    while i<len(string):
        if string[i]=='-':
            [m,a,b]=get_adjacent_characters(string,i,test=lambda x:x=='-')
            if a==0:
                if b%2==1:
                    string=string[b+1:]
                else:
                    string='-'+string[b+1:]
                i=0
            elif b<len(string)-1:
                s1=string[:a]
                s2=string[b+1:]
                if string[a-1] in ['+','*','/','^']:
                    if (b-a)%2==1:
                        string=s1+s2
                    else:
                        string=s1+'-'+s2
                else:
                    if (b-a)%2==1:
                        string=s1+'+'+s2
                    else:
                        string=s1+'-'+s2
                i=a+1
            else:
                if (b-a)%2==1:
                    string=string[:a]
                else:
                    string=string[:a]+'-'
                i=len(string)-1
        i+=1
    return string
                
                
def add_times(string):
    i=0
    while i<len(string):
        if string[i]==' ':
            ws=get_adjacent_characters(string,i,test=lambda x:x==' ')
            if ws[1]==0:
                string=string[ws[2]+1:]
            elif ws[2]==len(string)-1:
                string=string[:ws[1]]
            elif is_letter(string[ws[1]-1]) and is_letter(string[ws[2]+1]):
                string=string[:ws[1]]+'*'+string[ws[2]+1:]
            else:
                string=string[:ws[1]]+'*'+string[ws[2]+1:]
            i-=1
        if needs_times(string,i):
            string=string[:i+1]+'*'+string[i+1:]    
        i+=1
        
    return string


def check_adjacency(s):
    if s[0]=='(' and s[1]==')':
        return ['emptry parentheses: ()']
    if s[0]=='(' and s[1] in ['+','*','/','^']:
        return ['empty operand: '+s]
    if s[0] in binary_operators and s[1]==')':
        return ['empty operand: '+s]
    if s[0] in binary_operators and s[1] in ['+','*','/','^']:
        return ['double operator: '+s]
    
    return []


def get_variables(list_form):
    var=list(set(get_variables_dup(list_form)))
    var.sort()
    return var

def get_variables_dup(list_form):
    if  type(list_form) is not list:
        if is_number(list_form):
            return []
        else:
            return [list_form]
        
    if len(list_form)==2:
        return get_variables(list_form[1]) 
    else:
        return get_variables(list_form[1])+get_variables(list_form[2])


#
# end auxiliary parsing functions
#



# Check format of input string whether it corresponds to "correct" expression
def check_format(string):
    if string=='':
        return ['empty']
    issues=[]
    nest_level=0
    neg=False;
    for i in range(len(string)):
        if string[i]=='(':
            nest_level+=1
        if string[i]==')':
            nest_level-=1
        if nest_level<0:
            neg=True
        if i<len(string)-1:
            issues+=check_adjacency(string[i:i+2])
        if (string[i] not in binary_operators) and (not is_letter(string[i])) and (not is_number(string[i])) and (string[i] not in ['.','(',')']): 
            issues+=['invalid character: '+string[i]]
    if nest_level>0:
        issues+=['more open parentheses than close parentheses']
    if nest_level<0:
        issues+=['more close parentheses than open parentheses']
    if neg:
        issues+=['parentheses unbalanced']
            
    if string[0] in ['+','*','/','^']:
        issues+=['cannot begin with an operator']
    
    if string[-1] in binary_operators:
        issues+=['cannot end with an operator']
    
    i=0
    while i<len(string):
        if is_letter(string[i]):
            word=get_adjacent_characters(string,i)
            if word[0] in unary_operators and (word[2]==len(string)-1 or not string[word[2]+1]=='('):
                issues+=['function '+word[0]+' must be followed by parentheses']
            i=word[2]
        i+=1
    
    return issues



def to_list_form(string):
    if string[0]=='-':
        neg=True
    else:
        neg=False

    nest_level=0
    plus=[]
    minus=[]
    times=[]
    divide=[]
    power=[]
    for i in range(len(string)):
        if string[i]=='(':
            nest_level+=1
        if string[i]==')':
            nest_level-=1
        if string[i]=='+' and nest_level==0:
            plus+=[i]
        if string[i]=='-' and nest_level==0 and (i==0 or (i>0 and string[i-1] not in ['*','/','^'])):
            minus+=[i]
        if string[i]=='*' and nest_level==0:
            times+=[i]
        if string[i]=='/' and nest_level==0:
            divide+=[i]
        if string[i]=='^' and nest_level==0:
            power+=[i]
    
    if len(plus)>0:
        pos=plus[0]
    elif len(minus)>0 and not neg:
        pos=minus[0]
    elif len(minus)>1 and neg:
        pos=minus[1]
    elif len(times)>0:
        pos=times[0]
    elif len(divide)>0:
        pos=divide[0]
    elif len(power)>0:
        pos=power[0]
    else:
        pos=-1
    if pos>-1:
        return [string[pos],
                to_list_form(string[:pos]),
                to_list_form(string[pos+1:])]
    
    if string[0]=='(' and string[-1]==')':
        return to_list_form(string[1:-1])        
    
    if neg:
        return ['neg',to_list_form(string[1:])]
    for func in unary_operators:
        if string.startswith(func):
            return [func,to_list_form(string[len(func):])]
        
    return string





class BaseFunction:

    def __init__(self,*args):
        
        if len(args) > 0:
            self.set_function(args[0])
        else:
            self.set_function()
            

    def set_function(self,*args):
        
        if len(args) == 0:
            self.str_form = ''
            self.list_form = []
            self.tex_form = ''                
            self.sym_form = sp.sympify('-1')
            self.compilable = False
            self.func_is_defined = False

        # parse argument according to type (string or sympy expression)
        elif type(args[0]) == str:
            
            # perform some pre-processing  
            self.str_form=fix_minuses(add_times(args[0]))

            # check format of input string
            self.issues=check_format(self.str_form)

            # if format ok, try to convert to various forms
            if len(self.issues)==0:

                self.compileable=True

                try:
                    # get list_form
                    self.list_form=to_list_form(self.str_form)

                    # collect variables and get symbolic form

                    # get the variables from the list form and put them in a string
                    self.func_symbols = get_variables(self.list_form)

                    # now create sympy symbols for each variable symbol found
                    if len(self.func_symbols) > 0:
                        var_string=self.func_symbols[0]
                        i=1
                        while i < len(self.func_symbols):
                            var_string+=' '+self.func_symbols[i]
                            i+=1

                        self.func_vars = sp.symbols(var_string)

                    # create sympy expression from input string, converting usual exp sign to Python exp
                    self.sym_form = sp.sympify(self.str_form.replace('^','**'))

                    # use sympy converter to initialize tex form
                    self.tex_form = sp.latex(self.sym_form)

                    # Set "defined" flag
                    self.func_is_defined = True

                except:
                    self.compileable=False
                    self.list_form=[]
                    self.sym_form=sp.sympify('-1')
                    self.tex_form=''
                    self.issues=['This function could not be compiled for an unknown reason']
                    self.func_is_defined = False

            else:
                self.compileable=False
                self.list_form=[]
                self.sym_form=sp.sympify('-1')
                self.tex_form = ''
                self.func_is_defined = False


        # if agrument is sympy expression, we can initialize right away        
        elif isinstance(args[0], tuple(sp.core.all_classes)):
            self.sym_form = args[0]
            self.compileable=False
            self.str_form = str(self.sym_form)
            self.list_form=[]
            self.tex_form = sp.latex(self.sym_form)
            self.func_is_defined = True

            

        else:
            self.compileable=False
            self.list_form=[]
            self.sym_form=sp.sympify('-1')
            self.tex_form = ''
            self.func_is_defined = False



            
            

    # check whether function is equal to a given expression
    def check_function(self,expr):
        
        if self.func_is_defined == True:
            
            print(expr)
            test_function = BaseFunction(expr['new'])
            print(self.tex_form) 
            print(test_function.tex_form)
            if sp.simplify(self.sym_form-test_function.sym_form) == 0:
                print("Correct!")
                return True
            else:
                print("Not correct.")
                return False
                    
    

        
# Derive a function class with widget methods: 
class WidgetFunction(BaseFunction):

    def __init__(self, *args):
        if len(args) == 0:
            self.get_input_from_button_widget()
        else:
            self.set_function(args[0])
            
            
    def set_function_on_click(self,input_text,button):
        
        self.set_function(input_text.value)
        print("You entered: ")
        display(Math(self.tex_form))
        
        
    def get_input_from_button_widget(self):
        
        w_g = widgets.Text(
            value='',
            placeholder='Type something',
            description='g(x) = ',
            continuous_update=False,
            disabled=False
        )

        display(w_g)
        button = widgets.Button(description="Submit")
        display(button)
        button.on_click(partial(self.set_function_on_click,w_g))
    
    
    def subs_into_function(self,expr):
        
        return self.sym_form.subs(vars[0], expr)
    
    
        
    def check_function_against_input(self, name):

        # check whether function is equal to a given expression
        def evaluate_text_input(expr):

            input_function = BaseFunction(expr['new'])
            with output_field:
                clear_output()
                display(Markdown("You entered: ")) 
                display(Math(input_function.tex_form))

                if sp.simplify(self.sym_form - input_function.sym_form) == 0:
                    display(Markdown("Correct!"))
                    return True
                else:
                    display(Markdown("Not correct. Please try again or check solution."))
                    return False



        input_field = widgets.Text(
            value='',
            placeholder='Type answer and press enter',
            description= name + ' = ',
            continuous_update=False,
            disabled=False
        )

        input_field.observe(evaluate_text_input, names='value')            
        
        output_field = widgets.Output()
        display(widgets.VBox([input_field,output_field]))
            

            


#
# Linear Functions
#
class LinearFunction(WidgetFunction):

    def __init__(self, *args):
        # if two numerical args, initialize function
        if len(args) == 2 and (all(isinstance(item, (int,float))) for item in args):
            self.slope = args[0]
            self.intersect = args[1]
            self.set_function(self.slope*x+self.intersect)
 
        # otherwise assign values randomly                           
        else:
            self.set_function_random()
                

    # randomly choose linear function with parameters from -5 to 5
    def set_function_random(self):
 
        self.slope = random.randint(-5,6)
        self.intersect = random.randint(-5,6)
        self.set_function(self.slope*x+self.intersect)
        

    def pick_random_points(self):

        # fix two random points on line
        self.xpts = random.sample(range(-5, 6), 2)         
        self.pts = [0,0]
        for i in (0,1): 
            self.pts[i] = [self.xpts[i], self.sym_form.subs(x, self.xpts[i])]

            
    #
    # Problem types for linear functions
    #
    def find_slope_intersect_form(self):
        
        self.pick_random_points()
        
        problem_str = (
                    'Find the **slope-intercept equation** '
                    r'$y = m\cdot x + b$' + ' for the line' 
                    f' through the points {self.pts[0][0],self.pts[0][1]} and {self.pts[1][0],self.pts[1][1]}.'
                )
        
        sol_str = (
                'We first determine the slope of the line: \n\n'
                r'$$'
                r'\text{Slope } = ' + r'\frac{\Delta y}{\Delta x} = '
                r'\frac{' + f'{self.pts[1][1]} - {self.pts[0][1]}' +r'}{' + f'{self.pts[1][0]} - {self.pts[0][0]}' +r'} = ' + f'{self.slope}' 
                r'$$' + '\n\n' 
                f'Now we can determine the y-intersect. We use the point {self.pts[0][0],self.pts[0][1]}.' +'\n\n'
                'As it is a point on the line, it must satisfy the line equation \n\n'
                r'$ \begin{align}' 
                    r'y = m \cdot x +b'
                r'\end{align}$' + '\n\n'        
                f'We already know m = {self.slope}, and if we plug in {self.pts[0][0]} for x and {self.pts[0][1]} for y, we can solve this for b:' +'\n\n'
                r'$ \begin{align}'
                f' & {self.pts[0][1]} = {self.slope}' + r'\cdot' + f'{self.pts[0][0]} + b' + r'\quad \Rightarrow \quad b = '
                    f'{self.pts[0][1]} - {self.slope * self.pts[0][0]} = {self.intersect}'
                r'\end{align}$' + '\n\n' 
                'Thus, the slope-intercept equation is \n\n'
                r'$\begin{align}'
                f'y = {self.slope}x+{self.intersect}'
                r'\end{align}$'        
                )

        return problem_str, sol_str

    

    def find_parallel_line(self):
        
        self.pick_random_points()
        rand_intersect = random.randint(-10,11)
        
        problem_str = (
                    'Find the **slope-intercept equation** '
                    f' for the line through the point {self.pts[0][0],self.pts[0][1]} ' 
                    f' parallel to the line $y = {self.slope}' + r'\cdot x +' + f'{rand_intersect}$.'
                )
        
        sol_str = (
                f'Since our line is parallel to the line $y = {self.slope}' + r'\cdot x +' + f'{rand_intersect}$, '
                f'we know that our line has the same slope, i.e., $m = {self.slope}$.' +'\n' 
                f'Therefore, we only need to determine the y-intersect. We use the given point {self.pts[0][0],self.pts[0][1]}.' +'\n\n'
                'As it is a point on the line, it must satisfy the line equation \n\n'
                r'$ \begin{align}' 
                    r'y = m \cdot x +b'
                r'\end{align}$' + '\n\n'        
                f'We already know m = {self.slope}, and if we plug in {self.pts[0][0]} for x and {self.pts[0][1]} for y, we can solve this for b:' +'\n\n'
                r'$ \begin{align}'
                f' & {self.pts[0][1]} = {self.slope}' + r'\cdot' + f'{self.pts[0][0]} + b' + r'\quad \Rightarrow \quad b = '
                    f'{self.pts[0][1]} - {self.slope * self.pts[0][0]} = {self.intersect}'
                r'\end{align}$' + '\n\n' 
                'Thus, the slope-intercept equation is \n\n'
                r'$\begin{align}'
                f'y = {self.slope}x+{self.intersect}'
                r'\end{align}$'        
                )

        return problem_str, sol_str


# In[3]:


def create_problem_widget(func,problem_type_str):
    
    def problem_on_button_clicked(bt):

        func.set_function_random()
        problem, solution = problem_type()
  
        with statement_out:
            clear_output()
            display(Markdown(problem))
            func.check_function_against_input('y')
        
        with solution_out:
            clear_output()
            solution_check.value = False
            

    def solution_on_button_clicked(expr):
        
        problem, solution = problem_type()

        with solution_out:
            clear_output()

            if expr['new'] == True:
                # what happens when we press the button
                display(Markdown(solution))
                    
            
    new_problem_button = widgets.Button(description="Start a new problem", button_style='info')
    statement_out = widgets.Output(layout=Layout(width='50%',border='10px solid white'))
 

    solution_check = widgets.Checkbox(
        value=False,
        description='View solution',
        disabled=False
    )    
    solution_out = widgets.Output()


    new_problem_button.on_click(problem_on_button_clicked)
    solution_check.observe(solution_on_button_clicked, names='value')            


    #     solution_button.on_click(solution_on_button_clicked)

    problem_type = getattr(func, problem_type_str)
    problem, solution = problem_type()
    with statement_out:
            display(Markdown(problem))
            func.check_function_against_input('y')
        
    display(widgets.HBox([statement_out,widgets.VBox([solution_check,solution_out],layout=Layout(width='50%',border='10px solid white'))]))
    display(new_problem_button)




# ## Finding the equation of a line

# In this first problem, we find the the slope-intercept form of a line given two points on the line.

# In[4]:


f = LinearFunction()
create_problem_widget(f,'find_slope_intersect_form')


# ***

# ### Parallel lines
# 
# In the next problem, we find a line parallel to a given line. 
# 
# (Hint: If two lines are parallel, what does this mean for their respective slopes?)

# In[5]:


g = LinearFunction()
create_problem_widget(g,'find_parallel_line')


# In[ ]:




