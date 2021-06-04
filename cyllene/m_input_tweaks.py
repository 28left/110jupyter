import sys 

ipython = get_ipython()

# Allow using '^' for exponentiation
def replace_exponentiation_symbol(lines):
    new_lines = []
    for line in lines:
        new_line = ''
        occ_exp = [i for i, letter in enumerate(line) if letter == '^']
        position = 0
        for i in occ_exp:
            if line.count('\'',0,i) %2 == 0 and line.count('\"',0,i) %2 == 0:
                new_line += line[position:i+1].replace('^','**')
            else:
                new_line += line[position:i+1]
            position = i+1
        new_line += line[position:]
        new_lines.append(new_line)
    return new_lines



# Forbid entries where only the top line of an answer block is meaningfully filled
# This piece of code gets run on answer blocks and other magics alike, so have to check explicitly that this is truly an answer block
def check_cell_submitted(lines):
    if "answer" in lines[0] and len(lines) < 2:
        lines.append(" ")
    return lines


# Suppress long traceback messages and just output error 
def exception_handler(exception_type, exception, traceback):
    print("Your input led to an error. You can find more information about the error below.")
    print("%s: %s" % (exception_type.__name__, exception), file=sys.stderr)

    
# def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
#                    exception_only=False, running_compiled_code=False):
#     etype, value, tb = sys.exc_info()
#     value.__cause__ = None  # suppress chained exceptions
#     print("Your input led to an error. You can find more information about the error below.")
#     return ipython._showtraceback(etype, value, ipython.InteractiveTB.get_exception_only(etype, value))



# Register tweaks in ipython kernel
ipython.input_transformers_cleanup.extend((replace_exponentiation_symbol, check_cell_submitted))
# ipython._showtraceback = exception_handler
# ipython.showtraceback = hide_traceback






