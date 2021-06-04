import pandas as pd

def function_to_table(func, values, name = ['x', 'f(x)']):

    return pd.DataFrame({name[0]: values, name[1]: [func(v) for v in values]})

def output_table(table):

    return table.style.hide_index()
