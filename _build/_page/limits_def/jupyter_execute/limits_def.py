#!/usr/bin/env python
# coding: utf-8

# # Limit of a Function

# ## Definition
# 
# The function $f(x)$ has a limit of L as $x$ approaches $a$,
# 
# $$ \lim_{x\to a} f(x) = L$$
# 
# if the value of $f(x)$ can be made as close to the number $L$ as we please by taking x values *sufficiently close* to, but not equal to, $a$.

# In[1]:


from cyllene import *
f = function('x^2+1')


# ### Exercise
# 
# Below, you see a table in which we evaluate a function $f(x)$ for values of $x$ that are closer and closer to $2$ (but **not equal to $2$**). What do the values $f(x)$ suggest $\lim_{x\to 2} f(x)$ should be?

# In[2]:


tab = function_to_table(f, [2.1, 2.01, 2.0001])
output_table(tab)


# In[3]:


f(2.001)


# In[4]:


f(2.00000001)


# ````{admonition} Click the button to show solution.
# :class: dropdown
# The values $f(x)$ get closer to $5$ as $x$ gets closer to $2$.
# This suggests that 
# ```{math}
#     \lim_{x \to 2} f(x) = 5
# ```
# ````

# In[ ]:




