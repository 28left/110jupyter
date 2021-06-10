#!/usr/bin/env python
# coding: utf-8

# # Examples: Computing Limits Algebraically
# 
# ## Example: Constant Function
# 
# If $f(x) = 2$, find $\lim\limits_{x\to 1^{-}}f(x)$.
# 
# ```{admonition} Solution
# :class: tip, dropdown
# 
# $f$ is a constant function, hence a polynomial. Therefore, by Property 7 of {ref}`lim:prop_lim`, $\lim\limits_{x\to 1} f(x) = f(1) = 2$. Since the limit exists, the one-sided limits exist, too and coincide with the limit. Thus, $\lim\limits_{x\to 1^{-}}f(x) = 2$.
# ```
# 
# ## Example: Rational Function
# 
# Evaluate 
# 
# $$\lim\limits_{x\to -1} \dfrac{x^3 +4x^2-x-3}{2x^2+1}.$$
# 
# ```{admonition} Solution
# :class: tip, dropdown
# 
# The function 
# 
# $$ g(x) = \dfrac{x^3 +4x^2-x-3}{2x^2+1}$$
# 
# is a rational function, and since $2(-1)^2 + 1 = 3 \neq 0$, it follows that $-1$ is in the domain of $g$. 
# Again by Property 7 of {ref}`lim:prop_lim`, $\lim\limits_{x\to -1} g(x)$ exists and equals 
# 
# $$g(-1) = \frac{(-1)^3 + 4(-1)^2 - (-1) -3}{2(-1)^2+1} = \frac{1}{3}.$$
# ```
# 
# 
# ## Example: Piecewise Polynomial Function
# 
# Evaluate $\displaystyle\lim_{x\to 6} h(x)$, where
# 
# \begin{equation*}
# h(x)=
# \begin{cases} 
# x^2-4x-12 & \hbox{if } x<6 \\
# 8 & \hbox{if } x=6 \\
# x^2-5x-6 & \hbox{if } x>6 \\  
# \end{cases}
# \end{equation*}
# 
# ```{admonition} Step 1: Find the limit from the left.
# :class: tip, dropdown
# 
# In this case, since we are approaching 6 from the left, we can assume that $x<6$, and therefore $h(x) = x^2-4x-12$.
# \begin{align*}
# \lim_{x\to 6^{-}} h(x) 
# &= \lim_{x\to 6^-} x^2-4x-12\\ \\
# &= 6^2-4(6)-12 && \text{Plug in $x=6$ (Property 7)}\\ \\
# &= 36-24-12 && \text{Simplify}\\ \\
# &= 0
# \end{align*}
# ```
# 
# ```{admonition} Step 2: Find the limit from the right. 
# :class: tip, dropdown
# 
# In this case, since we are approaching 6 from the right, we can assume that $x>6$, and therefore $h(x) = x^2-5x-6$.
# \begin{align*}
# \lim_{x\to 6^{+}} h(x) 
# &= \lim_{x\to 6^+} x^2-5x-6\\ \\
# &= 6^2-5(6)-6  && \text{Plug in $x=6$ (Property 7)}\\ \\
# &= 36-30-6 && \text{Simplify}\\ \\
# &= 0
# \end{align*}
# ```
# 
# ```{admonition} Step 3: Check to see if the two limits are equal.
# :class: tip, dropdown
# 
# Since $\displaystyle \lim_{x\to 6^-} h(x) = \lim_{x\to 6^+} h(x) = 0$, we conclude that the limit exists and
# 
# $$\lim_{x\to 6} h(x) = 0.$$
# ```
# 
# ```{warning} 
# Keep in mind that just because $\displaystyle\lim_{x\to 6} h(x) \neq h(6) = 8$, this does not mean that the limit does not exist.
# ```
