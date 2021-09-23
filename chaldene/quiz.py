import ipyvuetify as v
import ipywidgets as w
from IPython.display import Markdown, HTML, display, clear_output

import random

class MultChoice():

    def __init__(self, statement, choices):

        # get number of choices
        self.num_choices = len(choices)     
        self.choices = choices
           
        # Shuffle answers
        self.indices = [i for i in range(self.num_choices)]
        random.shuffle(self.indices)
        self.correct = self.indices.index(0)  

        # Define CSS properties to make text larger
        display(HTML("<style>.large_font { font-size: 100% }</style>")) 
        display(HTML("<style>.xlarge_font { font-size: 120% }</style>")) 

        # store the statement in a widget
        self.statement = w.HTMLMath(value=statement)

        # enlarge text
        self.statement.add_class("xlarge_font")

        # Create labels for each answer choice
        answers = [w.Label(value=self.choices[self.indices[i]]) for i in range(self.num_choices)]

        # Enlarge text for labels
        for a in answers:
            a.add_class("large_font")

        # Create radio buttons with answers as labels (slots)
        self.choice_buttons = v.RadioGroup(
            v_model=None,
            children=[
                v.Radio(v_slots=[{
                    'name': 'label',
                    'children': [a] }]) for a in answers]
            )

        # Create a submit button
        self.check_button = v.Btn(color='primary', children=['Check Answer'])

        # If button is clicked, check the currently selected answer
        self.check_button.on_event("click",self.on_click_submit) 

        # Create a feedback area
        self.feedback = w.Output()

    def on_click_submit(self, widget, event, data):

        with self.feedback:
            clear_output()

            if self.choice_buttons.v_model == self.correct:
                display(v.Alert(text=True, type='success', children=['Correct!']))
                return True
            else: 
                display(v.Alert(text=True, type='error', children=['Incorrect!']))
                return False



    def show_problem(self):

        # show statement
        display(self.statement)

        # put answer radio buttons, submit button, and feedback area into a container and show
        con = v.Container(
            children=[self.choice_buttons, self.check_button]) 
        display(con)

        display(self.feedback)