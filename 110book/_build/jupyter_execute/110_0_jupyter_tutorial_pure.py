#!/usr/bin/env python
# coding: utf-8

# # Working With Jupyter Notebooks

# Jupyter notebooks are interactive online notebooks that run directly in your web browser and can both display text and run code (such as Python).
# 
# In our course we will use Jupyter to provide some interactive content where you can learn new material and practice it at the same time, with instant feedback.

# ## The cell structure

# Every notebook is made up of **cells**. You can navigate between cells using the arrow keys or by clicking on them with the mouse pointer.

# Cells can either be **code cells** or **text cells** (using a formatting language called *Markdown*).

# All cells you have seen in this notebook so far have been text cells. They can display text with various formatting, such as *italics* or **bold**, as well as math formulas, for example $\dfrac{x^2-9}{x+3}$. 

# If you double-click a text cell, or select it with the keyboard or your mouse and press `ENTER`, you will see the raw format (markdown) version of the text. If you press 
# 
# >    `Shift + Enter`,
# 
# the text cell will be formatted and display nicely.

# ---
# 
# Cells can also be code cells and contain lines of code in a *programming language*, typically *Python*:

# In[1]:


for i in range(10):
    print("I love math!")


# If you select a code cell and press 
# 
# > `Shift + Enter`,
# 
# Jupyter will run the code in that cell. Any output that the computation produces will be shown **right beneath the code cell**. Try that with the code cell above. Select it and press `Shift + Enter`.

# We will use code cells mainly for *two purposes*:
# 1. **to perform mathematical computations**
# 2. **to enter and evaluate answers to problems**

# ## Initializing the notebook
# 
# The following code cell initializes the next part of the notebook. In particular, it loads the problems that you will be asked to solve. So please go ahead and run this cell using `Shift + Enter`.

# In[2]:


"""
Notebook Initialization
"""
from cyllene import *
get_ipython().run_line_magic('initialize', '')


# ---
# 
# <!-- The notebooks we will be using will have their code cells hidden by default. You can make them visible, if you want, by clicking on the `eye` button ![eye button](./eye_button.png "Hide code button") in the toolbar above. This button will toggle code cells from hidden to visible and back. -->
# 
# <!-- ### Go ahead and press the 'eye' button to make all code cells invisible.
# 
# (If you know some Python and you would like to experiment, you can of course make all code sections visible and play around with the code. You can't "break" anything. For example, in the code cell above, change the 10 to a 4 and hit `SHIFT+ENTER`.) -->

# ## Computing with Jupyter notebooks
# 
# You can use code cells like a powerful calculator. Give it a try.
# 
# Go ahead and execute (i.e `Shift+Enter`) the cell below.

# In[3]:


2021*(17-6)


# As you see, you enter calculations into code cells pretty much like you would enter it into a calculator, using `*` for multiplication.
# 
# We use `/` for divison and `^` for exponentiation.

# In[4]:


2^7/64


# You can also use `**` for exponentiation. (This is actually the standard notation in Python.)

# In[5]:


2**8


# As usual, exponentiation binds stronger than the other operations. If you want to change that, you have to use parentheses `(,)`.

# In[6]:


2^(7/64)


# ## Answering problems

# We also use cells to enter answers to problems.

# _Answer cells start with the line `%%answer`, followed by the problem name. You input your answer in the line below that and, as usual, press `Shift+Enter`._

# ### Problem 1
# 
# What is the smallest [*sphenic*](https://en.wikipedia.org/wiki/Sphenic_number) number?

# In[7]:


get_ipython().run_cell_magic('answer', 'Problem 1', '30')


# Try solving the next problem yourself.

# ### Problem 2
# 
# $ \dfrac{2}{3} - \dfrac{1}{2} = $ ?
# 
# (_Fractions are entered as `a/b`._)

# In[8]:


get_ipython().run_cell_magic('answer', 'Problem 2', '1/6')


# ### Problem 3
# 
# $ 1.01+0.22 = $ ? 
# 
# (*Decimal fractions are simply entered in the form `X.XXX`.*)

# In[9]:


get_ipython().run_cell_magic('answer', 'Problem 3', '')


# ---
# ## Entering algebraic expressions
# 
# We will also need to enter algebraic expressions containing variables, such as $x$, along with operations like multiplication and exponentiation. The basic format remains the pretty much the same. 
# 
# When entering answers, as usual in mathematical notation, you may omit the multiplication symbol `*`.

# ### Problem 4
# 
# Simplify:   $\qquad 5x - 3x$

# In[10]:


get_ipython().run_cell_magic('answer', 'Problem 4', '')


# ---
# 
# The general template to input fractional expressions like $\dfrac{x^2-9}{x+3}$ is `(...)/(...)`.

# ### Problem 5
# 
# Enter the fraction $\qquad \dfrac{x+3}{x^2-1}$.

# In[11]:


get_ipython().run_cell_magic('answer', 'Problem 5', '')


# ---
# ## Generating new problems with `Shift+Enter`
# 
# If you come across a problem heading starting with &#128260; symbol, this means you can generate new versions of this problem as often as you like. Simply select the problem cell and hit `Shift + Enter`. Give it a try below.

# ### &#128260; More Practice

# In[12]:


"""
Run this cell to generate a new problem
"""

generate_problem('6')


# In[13]:


get_ipython().run_cell_magic('answer', 'Problem 6', '-3/2')


# In[ ]:




