import sympy as sp
import random

# aux parsing libraries
import cyllene.a_mathstring as ms
import cyllene.a_listform as lf

# import other modules
import cyllene.f_aux as fa
import cyllene.f_define as fd


# Reserve some (real-valued) symbols in Sympy
a, b, c, d, p, q, r, s, t, w, x, y, z = sp.symbols(
    'a b c d p q r s t w x y z', real=True)

MYLOCALS = {'a': a, 'b': b, 'c': c, 'd': d, 'p': p, 'q': q, 'r': r,
            's': s, 't': t, 'w': w, 'x': x, 'y': y, 'z': z}


class Function:

    """
    Basic class to represent a single-variable, real-valued
    function. Every function has four basic attributes:
    - sympy expression
    - tree form
    - table
    - graph
    """

    def __init__(self, expr):

        [new_expr, self.issues] = fd.define_expression(expr)
        
        if new_expr != None:
            # input ok
            self.is_defined = True
        else:
            # Initialize zero function and set flag
            self.is_defined = False
            expr = sp.sympify(0)

        # Initialize all basic function attributes
        self.sym_form = new_expr
        self.str_form = str(new_expr).replace('**', '^')
        self.list_form = lf.string_to_list(self.str_form)
        self.tex_form = sp.latex(self.sym_form)
        # self.graph_form = plt.figure()
        self.table_form = {}

        # initialize further attributes of a function
        self.variables = fa.get_variables(self.sym_form)

        # get the domain
        """
        get_domain method from sympy does not seem stable currently
        (as of Nov 15, 2020) -- disabled for now
        """
        # self.domain = fa.get_domain(self.sym_form)

        # lambda form is a callable function, so you can evaluate the function 
        # as 'f(3)', for example
        if self.variables:
            self.lambda_form = sp.lambdify(self.variables[0], self.sym_form) 
        else:
            self.lambda_form = sp.lambdify(x, self.sym_form) 

    # def lambda_form(self):
    #     return sp.lambdify(self.variables[0], self.sym_form)

    def eval_at(self, val):

        # Evaluate the function at the first variable
        if self.variables:
            return self.sym_form.subs(self.variables[0], val)
        else:
            return self.sym_form.subs(x, val)


#This is new, do we need to merge this with the previous eval function?
    def eval_np(self,npx):
        return sp.lambdify(self.variables[0], self.sym_form)(npx)
    
    
 ####################################BehaviourMethod##################################


#Helper functions for the behavior method.   
    def Increasing(self):
        if self.variables == []:
            return sp.EmptySet
        else:
            x = self.variables[0]
            p = sp.diff(self.sym_form,x)
            return sp.solveset(p>0, x, sp.Reals)

    def Decreasing(self):
        if self.variables==[]:
            return sp.EmptySet
        else:
            x = self.variables[0]
            p = sp.diff(self.sym_form,x)
            return sp.solveset(p<0, x, sp.Reals)

   
    def Concave_Up(self):
        if self.variables==[]:
            return sp.EmptySet
        else:
            x = self.variables[0]
            p = sp.diff(self.sym_form,x)
            q = sp.diff(p,x)
            CU = sp.solveset(q>0, x, sp.Reals)
            return CU

    def Concave_Down(self):
        if self.variables==[]:
            return sp.EmptySet
        else:
            x = self.variables[0]
            p = sp.diff(self.sym_form,x)
            q = sp.diff(p,x)
            CD = sp.solveset(q<0, x, sp.Reals)
            return CD

    def inflection_points(self):
        if self.variables==[]:
            return sp.EmptySet
        else:
            x = self.variables[0] 
            p = sp.diff(self.sym_form,x)
            q = sp.diff(p,x)
            if q==0:
                return sp.EmptySet
            else:
                A = sp.solveset(q,x, sp.Reals)
                return A


    def zeros(self):
        if self.variables:
            x =self.variables[0]
            S = sp.solveset(self.sym_form, x, sp.Reals)
            return S 
        else:
            return sp.EmptySet

    def extrema(self):
        if self.variables==[]:
            return sp.EmptySet
        else:       
            x = self.variables[0]
            df = self.derv()
            S = df.zeros()
            return S 

 


    def singularities(self):
        return sp.Complement(sp.Reals, self.domain)


    def Inflection_Interval(self):
        I=self.inflection_points()
        if len(I)>1:
            a=min(I)
            b=max(I)
            return sp.Interval(a,b)
        else:

            return sp.Interval(-10,10)
        
        
    def Largest_Interval(self):
        zeros = self.zeros()
        extrema = self.extrema()
        inflection_points = self.inflection_points()
        zero = 0


        left_zero, right_zero = self.boundries(zeros)
        left_extrem, right_extrem  = self.boundries(extrema)
        left_infliction,right_infliction = self.boundries(inflection_points)

        left_boundry = min(left_zero,left_extrem,left_infliction,zero) -1 
        right_boundry= min(right_zero,right_extrem,right_infliction,zero) + 1

    
        I = sp.Interval(left_boundry, right_boundry)
        return I

    
    def range(self,I):
        left_point, right_point = float(I.args[0]), float(I.args[1])

        extrme_floats = [left_point,right_point]
        for p in self.extrema():
            extrme_floats.append(float(p))

        max = self.eval_np(extrme_floats[0])
        min = self.eval_np(extrme_floats[0])

        for p in extrme_floats:
            fp = self.eval_np(p)

            if(fp > max):
                max = fp
            elif(fp < min):
                min = fp

        I = sp.Interval(min,max)
        return I


    def intersect_intervals(self,Intervals):
        I = Intervals[0]
        for J in Intervals:
            I = I.intersect(J)
        return I

    def union_intervals(self,Intervals):
        I = Intervals[0]
        for J in Intervals:
            I = I.union(J)
        return J

    def boundries(self,S):
        if(S == sp.EmptySet):
            return 0, 0
        else:
            return float(S.args[0]), float(S.args[-1])



    def behaviour(self, *pars):
        #The Behavior Dictionary
        behaviour_dict ={"increasing":self.Increasing() ,
        "decreasing":self.Decreasing() , 
        "concaveup":self.Concave_Up() , 
        "concavedown":self.Concave_Down(),
        "largestinterval":self.Largest_Interval()} 

        #Build a list of Intervals from the parameters
        Intervals = [] 
        for par in pars:
            try: 
                Intervals.append(behaviour_dict[par.lower().replace(" ", "")])
            except KeyError:
                print("Check the parameter {}".format(par))
                return

        #Intersect the Intervals 
        return self.intersect_intervals(Intervals) 


# ###################################END of the Behaviour ######################################## 

   #Derivative: This function returns the derevative, of function class
    def derv(self):
        return Function(sp.diff(self.sym_form))

    def average(self,x1,x2):
        return (self.eval_at(x2) - self.eval_at(x1))/(x2-x1)

    #the following functions returns a linear function, corresponding to the secant or tangent
    def secant_line(self,x1,x2):
        x = self.variables[0]
        m = self.average(x1,x2)
        fx1 = self.eval_at(x1)

        return Function("{}(x-{}) +{} ".format(m,x1,fx1))

    def tangent_line(self,x1):
        x = self.variables[0]
        m = self.derv().eval_at(x1)
        fx1 = self.eval_at(x1)

        return Function("{}(x-{}) +{} ".format(m,x1,fx1))

    #Transformation of Functions : Need to decide, return a new function or modify the current one? 

    def shift_x(self,a):
        x = self.variables[0]
        expr = self.sym_form.subs(x, x-a)
        return Function(expr)

    def shift_y(self, a):
        expr = self.sym_form
        return Function(expr + a)


    def scale_x(self,a):
        x = self.variables[0]
        expr = self.sym_form.subs(x, x/a)
        return Function(expr)


    def scale_y(self,a):
        expr = a * self.sym_form
        return Function(expr)
    
    def __eq__(self, other):
        pass
