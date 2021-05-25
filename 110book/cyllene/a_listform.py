#  Operators
#  List of standard mathematical operators
unary_operators = ['neg', 'sqrt', 'abs', 'exp', 'log', 'ln',
                   'sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'arcsin',
                   'arccos', 'arctan', 'arcsec', 'arccsc', 'arccot']
unary_operators_with_parameters = ['log']
binary_operators = ['+', '-', '*', '/', '^']


def list_to_string(list_form):
    if type(list_form) is not list:
        return list_form

    if len(list_form) == 2:
        return list_form[0] + '(' + list_to_string(list_form[1]) + ')'

    if len(list_form) == 3:
        if list_form[0] not in ['deriv', 'log']:
            return '(' + list_to_string(list_form[1]) + ')' \
                + list_form[0] + '(' + list_to_string(list_form[2]) + ')'
        if list_form[0] == 'log':
            return 'log(' + list_to_string(list_form[1]) + ',' \
                + list_to_string(list_form[2]) + ')'

        return 'deriv_' + list_form[1] + '(' \
            + list_to_string(list_form[2]) + ')'


def string_to_list(string):
    '''
    Transforms a input string properly formatted as a
    mathematical expression into tree in the form of a
    nested list. Each constituent list has either 2 or 3 elements.
    The first element is either a binary operator
    (for 3 element lists) or a function (for 2 element lists).
    The next elements of the list are the operands,
    which are either variables (in the form of strings), numbers,
    or other lists, representing composed functions.

    By the nature of function composition, this function is recursive.
    It uses order of operations to identify the
    top level function, breaks the function into the operand(s)
    of that function, and then calls itself on that (those)
    operand(s).

    IMPORTANT: this function assumes that the input has already been
    validated by check_format.

    Example 1:
        string_to_list('x+3') returns ['+','x',3]

    Example 2:
        string_to_list('x+3*sin(x^2)') returns
            ['+','x',['*',3,['sin',['^','x',2]]]]
    '''

    """
    if the function leads with a '-' character, the leading operator
    in the expression may be the negation operator.
    """
    if string[0] == '-':
        neg = True
    else:
        neg = False

    """
    step through the string recoding positions of all binary operators
    not inside parentheses.
    """
    nest_level = 0
    plus = []
    minus = []
    times = []
    divide = []
    power = []
    for i in range(len(string)):
        if string[i] == '(':
            nest_level += 1
        if string[i] == ')':
            nest_level -= 1
        if string[i] == '+' and nest_level == 0:
            plus += [i]
        if string[i] == '-' and nest_level == 0 and \
            (i == 0 or (i > 0 and string[i - 1] not in ['*', '/', '^'])):
            minus += [i]
        if string[i] == '*' and nest_level == 0:
            times += [i]
        if string[i] == '/' and nest_level == 0:
            divide += [i]
        if string[i] == '^' and nest_level == 0:
            power += [i]

    """
    use order of operations to determine which binary operator
    is the top-level operator, if any.
    """
    if len(plus) > 0:
        pos = plus[0]
    elif len(minus) > 0 and not neg:
        pos = minus[-1]
    elif len(minus) > 1 and neg:
        pos = minus[-1]
    elif len(times) > 0:
        pos = times[0]
    elif len(divide) > 0:
        pos = divide[0]
    elif len(power) > 0:
        pos = power[0]
    else:
        pos = -1
    if pos > -1:
        """
        if the top-level operator is a binary operator return
        a 3-element list whose first element
        is the binary operator, and the next two elements are
        the operands, in order. Note the
        recursive use of the function on the two operands.
        """
        return [string[pos],
                string_to_list(string[:pos]),
                string_to_list(string[pos + 1:])]

    """
    if the entire expression is contained in parentheses,
    evaluate this function only on what is inside the parentheses.
    """
    if string[0] == '(' and string[-1] == ')':
        return string_to_list(string[1:-1])

    """
    if the expression leads with '-', the negation operator is
    the top-level operator.
    """
    if neg:
        return ['neg', string_to_list(string[1:])]

    """
    if the expression leads with a unary operator,
    it is the top-level operator.
    """
    for func in unary_operators:
        if string.startswith(func):
            if func == 'log':
                comma_index = [i for i in range(len(string))
                               if (string[i] == ',' and get_parentheses_level(string, i) == 1)]
                if len(comma_index) > 0:
                    i = comma_index[0]
                    return ['log', get_context(string, i - 1), get_context(string, i + 1)]
            return [func, string_to_list(string[len(func):])]

    """
    the only other possibility is that input is an atomic expression
    -- either a variable or a number.
    """
    return string


def get_context(string, i):
    i0 = i
    while string[i0:i+1].count('(') - string[i0:i+1].count(')') <= 0 and i0 > 0:
        i0 -= 1

    i1 = 1
    while string[i:i1+1].count(')') - string[i:i1+1].count('(') <= 0 and i1 < len(string):
        i1 += 1

    return [string[i0:i1+1], i0, i1]


def get_parentheses_level(string, i):
    # does not count string[i], enven if it is a parenthesis.

    return string[:i].count('(') - string[:i].count(')')
