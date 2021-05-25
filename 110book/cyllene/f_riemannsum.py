import sympy as sp
import cyllene.f_aux as fa

# Reserve some (real-valued) symbols in Sympy
a, b, c, d, p, q, r, s, t, w, x, y, z = sp.symbols(
    'a b c d p q r s t w x y z', real=True)

MYLOCALS = {'a': a, 'b': b, 'c': c, 'd': d, 'p': p, 'q': q, 'r': r,
            's': s, 't': t, 'w': w, 'x': x, 'y': y, 'z': z}

#Riemann sum, use left value
def LHS(func,min,max,n):

    func = fa.set_variable_x(func)
    h = (max - min)/(n+0.0)
    tmp = min
    sum = 0
    for i in range(n):  
        sum += func.subs(x,tmp)
        tmp += h

    return sum*h            
    
#Riemann sum, use right value
def RHS(func,min,max,n):

    func = fa.set_variable_x(func)
    h = (max - min)/(n+0.0)
    tmp = min
    sum = 0
    for i in range(n):  
        tmp += h
        sum += func.subs(x,tmp)
        
    return sum*h            