# problem and answer magics
from os import path
from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)

from IPython import get_ipython

from cyllene.p_problem import ProbStack

ip = get_ipython()

@register_line_magic
def initialize(line):

    if line=='':
        # if no argument is given, try to find .py file with 
        # same name as notebook
        init_file = 'init.py'
    else:
        init_file = line + '.py'

    try:    
        # run the init file to load problems etc.
        ip.magic('run '+init_file)
        print("Initialization successful!")

    except:
        # print(line)
        print("Error loading initialization file.")


@register_line_magic
def Problem(line):
    try:
        problem = ProbStack.stack[line]
        problem.state_problem()
        # add_answer_cell(problem)
    except:
        # print(line)
        print("Could not add problem to problem stack.")


@register_line_magic
def problem(line):
    try:
        problem = ProbStack.stack[line]
        problem.state_problem()
        # add_answer_cell(problem)
    except:
        # print(line)
        print("Could not add problem to problem stack.")

@register_cell_magic
def answer(line, cell):
    # Given this is an answer block, check the top line is written in a valid way
    try:
        problem = ProbStack.stack[line[8:]]
    except:
        print("Oops! Something in the top line won't let us find the right problem.")
        return None
    # PREWORK FOR CELL:
        # if for some reason cell is not defined, stop the process
    if(cell is None):
        print("Your answer seems to be empty. Please try again.")
        return None
        # eliminate any line from cell that is "essentially empty", i.e., only whitepace
    cell = "\n".join([ll.rstrip() for ll in cell.splitlines() if ll.strip()])
        # strip the empty space from the beginning of each line
    cell = "\n".join([ll.lstrip() for ll in cell.splitlines()])
        # check if cell is essentially empty
    if(cell == ""):
        print("Your answer is empty. Please try again!")
        return None
    
    # PARSING ANSWER DEPENDS ON NUM_INPUTS
    answer = []
    try:
        n = problem.num_inputs
    except:
        print("problem.num_inputs has not yet been defined. Please check problem's encoding")
        return None
    if(n < 1):
        print("This problem was coded with too few num_inputs.")
        return None
    elif(n == 1):
        # there are no "(i): " prefix strings in this case, so can just use the first meaningful line in code as our answer
        answer.append(cell.split('\n')[0])
    else: # num_inputs > 1
        # By default, let answer[i] = ""
        for i in range(n):
            answer.append("")

        # TWO CASES for parsing answer blocks for problems with multiple inputs

        #   Distinguish between the two cases by the truth value of prefix_found
        prefix_found = False
        prefix_string = ""
        prefix_index = 0
        while(prefix_index < n and not prefix_found):
            prefix_string = "(" + str(prefix_index + 1) + ")"
            for cell_line in cell.splitlines():
                if cell_line.startswith(prefix_string):
                    prefix_found = True
                    break
            prefix_index += 1

        if(prefix_found):
            # CASE 1: there are "(i): " prefices from (1),...,(n)            
            #         iterate through each line in code to update answer[i] if line begins with "(i):""
            #         ignore any lines with an (i) for i > n
            for cell_line in cell.splitlines():
                # could be improved
                for i in range(n):
                    if cell_line.startswith("(" + str(i + 1) + "):"):
                        answer[i] = cell_line[len("(" + str(i + 1) + "):"):].strip()
                        break
                    if cell_line.startswith("(" + str(i + 1) + ")"):
                        answer[i] = cell_line[len("(" + str(i + 1) + ")"):].strip()
                        break
        else:
            # CASE 2: submission assumed to be written in order without the prefices (1),...,(n)
            i = 0
            for cell_line in cell.splitlines():
                if(i >= n): 
                    break
                answer[i] = cell_line.strip()
                i += 1                

    problem.check_answer(answer)        