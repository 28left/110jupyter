# a_mathstring: auxiliary module to check and manipulate math strings 

#  Operators
#  List of standard mathematical operators
unary_operators=['neg','sqrt', 'abs','exp','log','ln','sin','cos','tan','sec','csc','cot','arcsin','arccos','arctan','arcsec','arccsc','arccot']
unary_operators_with_parameters=['log']
binary_operators=['+','-','*','/','^']


"""
Auxiliary functions
"""
def is_number(s):
    '''
    checks whether the string s is a number (integer or float)
    '''
    try:
        float(s)
        return True
    except (TypeError,ValueError):
        return False


def is_letter(s):
    '''
    checks whether the string is a single letter. Returns false if it contains more than one character,
    even if all those characters are letters.
    '''
    if len(s)==1 and s.isalpha():
        return True
    return False


def number_to_string(val):
    if val%1==0:
        return str(int(val))
    return str(val)


def check_adjacency(string):
    '''
    Checks whether it is okay for two given characters to be adjacent in an expression.
    s should be a two character string. Returns a one-element list with string description of the error
    incurred by these two characters, if any. If there are no errors, the list is empty

    Example 1:
        check_adjacency('7+') returns []

    Example 2:
        check_adjacency('()') returns ['empty parentheses: ()']

    Example 3:
        check_adjacency('(*') returns ['empty operand: (*']

    Example 4:
        check_adjacency('(-') returns [] because this okay, e.g., 'exp(-3*x)'

    Example 5:
        check_adjacency('-)') returns ['empty operand: -)']

    Example 6:
        check_adjacency('*+') returns ['double operator: *+']

    Example 7:
        check_adjacency('*-') returns [] because this is okay, e.g., 'log(x)*-y'
    '''
    if string[0]=='(' and string[1]==')':
        return ['emptry parentheses: ()']
    if string[0]=='(' and string[1] in ['+','*','/','^']:
        return ['empty operand: '+string]
    if string[0] in binary_operators and string[1]==')':
        return ['empty operand: '+string]
    if string[0] in binary_operators and string[1] in ['+','*','/','^']:
        return ['double operator: '+string]
    if string[0]=='(' and string[1]==',':
        return ['empty argument: '+string]
    if string[0]==',' and string[1]==')':
        return ['empty argument: '+string]
    if string[0]==',' and string[1]==',':
        return ['empty argument: '+string]


    return []


def get_context(string,i):
    i0=i
    while string[i0:i+1].count('(')-string[i0:i+1].count(')')<=0 and i0>0:
        i0-=1

    i1=1
    while string[i:i1+1].count(')')-string[i:i1+1].count('(')<=0 and i1<len(string):
        i1+=1

    return [string[i0:i1+1],i0,i1]

def get_parentheses_level(string,i):
    # does not count string[i], enven if it is a parenthesis.

    return string[:i].count('(')-string[:i].count(')')


def check_commas(string):
    issues=[]
    comma_indices=[i for i in range(len(string)) if string[i]==',']

    for i in comma_indices:
        context=get_context(string,i)
        if context[1]==0:
            issues+=['commas must separate function arguments']
            continue

        f=get_adjacent_characters(string,context[1]-1)[0]
        if f not in unary_operators:
            issues+=['commas must separate function arguments']
            continue

        if f not in unary_operators_with_parameters:
            issues+=[f+' does not accept multiple arguments.']
            continue

    log_indices=[i for i in range(len(string)-2) if string[i:i+3]=='log']
    for i in log_indices:
        context=get_context(string,i+3)
        comma_count=sum([1 for i in range(len(context[0])) if (context[0][i]==',' and get_context(context[0],i)[0]==context[0])])
        if comma_count>1:
            issues+=['log accepts a maximum of two arguments']

    return issues



def get_adjacent_characters(string,i,test=lambda x:is_letter(x)):
    '''
    returns a triple of the form [s,a,b] where s is the largest substring of string containing the index i
    where all the characters match a specific form. The default is that all the characters in s are letters.
    a and b are the indices in string of the first and last chcaracters in s respectively.

    Example 1:
        get_adjacent_characters('x+abc+123',3) returns ['abc',2,4]

    Example 2:
        get_adjacent_characters('x+abc+123',5) returns [] because '+' (at index 5) is not a letter.

    Example 3:
        get_adjacent_characters('x+abc+123',5,lambda x:x=='+') returns ['+',5,5]

    Example 4:
        get_adjacent_characters('x+abc+123',6,lambda x:is_number(x)) returns ['123',6,8]
    '''
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



"""
MathString class
---
Provides basic parsing functionality for strings that are to be interpreted as math expressions.
"""
class MathString:

    def __init__(self,*args):
        if len(args) == 0:
            self.s = ''
        elif type(args[0]) == str:
            self.s=args[0]
        else:
            self.s = str(args[0], errors='ignore')



    def remove_whitespace(self):

        """
        remove all blanks from input
        """
        self.s.replace(" ","")


    def needs_times(self,i):
        '''
        accepts a string and in index i. Returns true if string needs a '*' character inserted between positions
        i and i+1 in order to be properly interpreted as a function.

        Example 1:
            need_times('log(7x)',2) returns False because no '*' is needed between 'g' and '('.

        Example 2:
            need_times('log(7x)',4) returns True because '*' is needed between '7' and 'x'.

        Example 3:
            need_times('x(x+1)',0) returns True because '*' is needed between 'x' and '('.
        '''
        if i==len(self.s)-1:
            return False


        if is_letter(self.s[i]) and (is_number(self.s[i+1]) or self.s[i+1]=='.'):
            return True
        if is_letter(self.s[i+1]) and is_number(self.s[i]):
            return True

        if self.s[i] in ['x','y','z'] and self.s[i+1] in ['x','y','z']:
            return True

        if is_number(self.s[i]) and self.s[i+1]=='(':
            return True
        if is_letter(self.s[i]) and self.s[i+1]=='(' and get_adjacent_characters(self.s,i)[0] not in unary_operators:
            return True
        if self.s[i]==')' and is_letter(self.s[i+1]):
            return True
        if self.s[i]==')' and is_number(self.s[i+1]):
            return True
        if self.s[i]==')' and self.s[i+1]=='(':
            return True

        return False


    def add_times(self):
        '''
        Adds the '*' symbol wherever it is needed. Also removes white space.

        Example 1:
            add_times('7x') returns '7*x

        Example 2:
            add_times('x(x+1)') returns 'x*(x+1)'

        Example 3:
            add_times('log (7 x)') returns 'log(7*x)'
        '''
        i=0
        while i<len(self.s):
            if self.s[i] == ' ':
                ws=get_adjacent_characters(self.s,i,test=lambda x:x==' ')
                if ws[1]==0:
                    self.s=self.s[ws[2]+1:]
                elif ws[2]==len(self.s)-1:
                    self.s=self.s[:ws[1]]
                elif (is_letter(self.s[ws[1]-1]) or is_number(self.s[ws[1]-1]) or ws[1]-1=='.') and (is_letter(self.s[ws[1]+1]) or is_number(self.s[ws[1]+1]) or ws[1]+1=='.'):
                    self.s=self.s[:ws[1]]+'*'+self.s[ws[2]+1:]
                else:
                    self.s=self.s[:ws[1]]+self.s[ws[2]+1:]
                i-=1
            if self.needs_times(i):
                self.s=self.s[:i+1]+'*'+self.s[i+1:]
            i+=1

    def fix_exponents(self):
        self.s=self.s.replace('**','^')

    def fix_minuses(self):
        '''
        adjusts a string to account for the inconvenient fact that the '-' symbol can be interpreted as either
        a minus sign or a negative sign, and that arbitrarily many '-' characters can be placed in a row, and
        the expression is still technically sensible.

        Example 1:
            fix_minuses('x--y') returns 'x+y'

        Example 2:
            fix_minuses('x---y') returns 'x-y'

        Example 3:
            fix_minuses('x*--y') returns 'x*y'

        Example 4:
            fix_minuses('x*-y') returns 'x*-y'
        '''
        i=0
        while i<len(self.s):
            if self.s[i]=='-':
                [m,a,b]=get_adjacent_characters(self.s,i,test=lambda x:x=='-')
                if a==0:
                    if b%2==1:
                        self.s=self.s[b+1:]
                    else:
                        self.s='-'+self.s[b+1:]
                    i=0
                elif b<len(self.s)-1:
                    s1=self.s[:a]
                    s2=self.s[b+1:]
                    if self.s[a-1] in ['+','*','/','^']:
                        if (b-a)%2==1:
                            self.s=s1+s2
                        else:
                            self.s=s1+'-'+s2
                    else:
                        if (b-a)%2==1:
                            self.s=s1+'+'+s2
                        else:
                            self.s=s1+'-'+s2
                    i=a+1
                else:
                    if (b-a)%2==1:
                        self.s=self.s[:a]
                    else:
                        self.s=self.s[:a]+'-'
                    i=len(self.s)-1
            i+=1



    def check_format(self):
        '''
        checks if an input string is a valid mathematical expression. Returns a list of
        reasons the given expression is not valid. If it is valid, this list is empty.
        '''

        # first check if the input string is empty
        if self.s=='':
            self.issues = ['empty']
            self.compilable=False
            return

        # if the input string is non empty, check for other problems. We will fill
        # the list called issues with descriptions of the problems with the input string.
        self.issues=[]

        # we check if parentheses are balanced by stepping through each index of the string.
        # nest_level tracks the number of open parentheses at positions less than the current index minus
        # the number of close parentheses at positions less than the current index.
        # neg checks if the nest level is ever negative.
        nest_level=0
        neg=False

        # now step through each index in the list
        for i in range(len(self.s)):

            # count parentheses
            if self.s[i]=='(':
                nest_level+=1
            if self.s[i]==')':
                nest_level-=1
            if nest_level<0:
                neg=True

            # check if the character at index i and the one after it can appear together in a proper mathematical expression
            if i<len(self.s)-1:
                self.issues+=check_adjacency(self.s[i:i+2])

            # check if the character at index i is valid in a mathematical expression
            if (self.s[i] not in binary_operators) and (not is_letter(self.s[i])) and (not is_number(self.s[i])) and (self.s[i] not in ['.','(',')',',']):
                self.issues+=['invalid character: '+self.s[i]]

        # interpret the results of the parentheses counting variables
        if nest_level>0:
            self.issues+=['more open parentheses than close parentheses']
        if nest_level<0:
            self.issues+=['more close parentheses than open parentheses']
        if neg:
            self.issues+=['parentheses unbalanced']

        # check the begining and end of the input string
        if self.s[0] in ['+','*','/','^']:
            self.issues+=['cannot begin with an operator']

        if self.s[-1] in binary_operators:
            self.issues+=['cannot end with an operator']

        # check that special functions, e.g., sqrt, sin, exp, etc... are followed by open parentheses.
        i=0
        while i<len(self.s):
            if is_letter(self.s[i]):
                word=get_adjacent_characters(self.s,i)
                if word[0] in unary_operators and (word[2]==len(self.s)-1 or not self.s[word[2]+1]=='('):
                    self.issues+=['function '+word[0]+' must be followed by parentheses']
                i=word[2]
            i+=1

        self.issues+=check_commas(self.s)

        if len(self.issues) > 0:
            self.compilable = False
        else:
            self.compilable = True





def check_syntax(expr):

    # Basic function wrapper for MathString check syntax
    test_expr = MathString(expr)

    # do some pre-processing
    test_expr.add_times()
    test_expr.fix_exponents()
    test_expr.fix_minuses()

    # Check syntax
    test_expr.check_format()
    
    return test_expr.s, test_expr.compilable, test_expr.issues


