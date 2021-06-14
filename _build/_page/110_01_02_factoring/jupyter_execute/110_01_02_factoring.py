#!/usr/bin/env python
# coding: utf-8

# # Factoring Techniques
# 
# ## Pull out Common Factors
# 
# ```{admonition} Common factors
# :class: info
# 
# The act of pulling out common factors from a sum can be thought of as applying the distributive property of multiplication in reverse.
# 
# $$AB + AC = A(B+C)$$
# 
# e.g., $21 + 14 = 7\cdot 3 + 7\cdot 2 = 7(3+2)$
# ```
# 
# ### Example 1
# Factor $10x^5 + 15x^4$ by pulling out common factors.
# 
# 
# ```{admonition} Step 1: Determine the factors common to both terms.
# :class: tip, dropdown
# 
# - Constant factors: $10$ and $15$ are both multiples of $5$.
# - Powers of $x$: the smallest power of $x$ is $4$.
# 
# Therefore, the factor common to both terms is $5x^4$.
# ```
# 
# ```{admonition} Step 2: Pull out the common factor of $5x^4$.
# :class: tip, dropdown
# 
# \begin{align*}
# 10x^5 + 15x^4 
# &= 5x^4\cdot 2x  + 5x^4\cdot3  && \hbox{Write each term as a multiple of $5x^4$} \\
# &= 5x^4(2x + 3) && \hbox{Pull out common factor}
# \end{align*}
# ```
# 
# 
# ### Example 2
# Factor 
# 
# $$4x^3(2x^3+1)^5 + 30x^6(2x^3+1)^4$$ 
# 
# by first pulling out common factors.
# 
# ```{admonition} Step 1: Determine the factors common to both terms.
# :class: tip, dropdown
# 
# - Constant factors: $4$ and $30$ are both multiples of $2$.
# - Powers of $x$: the smallest power of $x$ is $3$.
# - Powers of $2x^3+1$: the smallest power of $2x^3+1$ is $4$.
# 
# Therefore, the factor common to both terms is $2x^3(2x^3+1)^4$.
# ```
# 
# ```{admonition} Step 2: Pull out the common factor of $2x^3(2x^3+1)^4$.
# :class: tip, dropdown
# 
# \begin{align*}
# & 4x^3(2x^3+1)^5 + 30x^6(2x^3+1)^4 \\
# &= 2x^3(2x^3+1)^4\cdot 2(2x^3+1) + 2x^3(2x^3+1)^4 \cdot 15x^3 \\%&& \hbox{Write each term as a multiple of $2x^3(2x^3+1)^4$}\\
# &= 2x^3(2x^3+1)^4[2(2x^3+1) + 15x^3] && \hbox{Pull out common factor}\\
# &= 2x^3(2x^3+1)^4(4x^3+2 + 15x^3) && \hbox{Simplify expression inside $[ ~ ]$}\\
# &= 2x^3(2x^3+1)^4(19x^3+2)
# \end{align*}
# ```
# 
# 
# ### Example 3
# Factor 
# 
# $$4x^3(2x^3+1)^{1/2} + 3x^6(2x^3+1)^{-1/2}$$ 
# 
# by first pulling out common factors.
# 
# ```{admonition} Step 1: Determine the factors common to both terms.
# :class: tip, dropdown
# 
# - Constant factors: $4$ and $3$ do not have any factors in common.
# - Powers of $x$: the smallest power of $x$ is $3$.
# - Powers of $2x^3+1$: the smallest power of $2x^3+1$ is $-1/2$.
# 
# Therefore, the factor common to both terms is $x^3(2x^3+1)^{-1/2}$.
# ```
# 
# ```{admonition} Step 2: Pull out the common factor of $x^3(2x^3+1)^{-1/2}$.
# :class: tip, dropdown
# 
# \begin{align*}
# & 4x^3(2x^3+1)^{1/2} + 3x^6(2x^3+1)^{-1/2} \\ \\ 
# &= x^3(2x^3+1)^{-1/2}\cdot 4(2x^3+1) + x^3(2x^3+1)^{-1/2} \cdot 3x^3 \\ \\
# &= x^3(2x^3+1)^{-1/2}[4(2x^3+1) + 3x^3] && \hbox{Pull out common factor}\\ \\
# &= x^3(2x^3+1)^{-1/2}(8x^3+4 + 3x^3) && \hbox{Simplify expression inside $[ ~ ]$}\\ \\
# &= x^3(2x^3+1)^{-1/2}(11x^3+4) && \hbox{Combine like terms}\\ \\
# &= \frac{x^3(11x^3+4)}{\sqrt{2x^3+1}}
# \end{align*}
# ```
