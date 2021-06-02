import ipysheet

def function_to_sheet(func, name, values):
    
    sh = ipysheet.sheet(rows=len(name), columns=len(values), row_headers=name, column_headers=False)
    x = ipysheet.row(0, values, numeric_format='0.00000')
    y = ipysheet.row(1, [func(v) for v in values], numeric_format='0.00000')
    # x = ipysheet.row(0, values)
    # y = ipysheet.row(1, [func(v) for v in values])
    
    @ipysheet.calculation(inputs=[x], output=y, initial_calculation=True)
    def calculate(a):
        return [func(i) for i in a] 
    
    return sh

