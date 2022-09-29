---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3.9.4 64-bit
  language: python
  name: python3
---

# Limit of a Function

+++

## Definition of a Limit

```{admonition} Definition
:class: info
The function $f(x)$ has a limit of L as $x$ approaches $a$,

$$ \lim_{x\to a} f(x) = L$$

if the value of $f(x)$ can be made as close to the number $L$ as we please by taking x values *sufficiently close* to, but not equal to, $a$.
```

+++

Keep in mind that the value of a limit does not depend on the value of the function at $x=a$.  In fact, it is possible that $\lim\limits_{x\to a}f(x) = L$ even though
- $f(a)$ does not exist, or
- $f(a)$ exists, but is not equal to $L$.

```{code-cell} ipython3
:tags: [remove-cell, thebe-init]

import sys, os
sys.path.append(os.path.abspath('..'))

from cyllene import *
f = function('3x^2+1')

from myst_nb import glue
limit = f(1)
glue("limit_val", limit, display=False)
```

```{code-cell} ipython3
:tags: [remove-input]

tab = function_to_table(f, [1.1, 1.01, 1.001, 1.0001])
table = output_table(tab)
glue("limit_table", table, display=False)
```

````{admonition} Exercise
:class: warning

Below, you see a table in which we evaluate a function $f(x)$ for values of $x$ that are closer and closer to $1$ (but **not equal to** $1$). What do the values $f(x)$ suggest $\lim_{x\to 1} f(x)$ would be?
```{glue:} limit_table
```
````

```{admonition} Click the button to show solution.
:class: tip, dropdown
The values $f(x)$ get closer to {glue:}`limit_val` as $x$ gets closer to $1$.
This suggests that $\lim_{x \to 1} f(x) =$  {glue:}`limit_val`.
```

+++

## One-Sided Limits

+++

```{admonition} Definition
:class: info

The function $f(x)$ has the **right-hand limit** $L$ as $x$ approaches $a$ from the right, 

$$\lim_{x\to a^+} f(x) = L $$ 

if the values of $f(x)$ can be made as close to $L$ as we please by taking $x$  sufficiently close to (but not equal to) $a$ and to the right of $a$ (i.e., $x>a$).

Similarly, the function $f(x)$ has the **left-hand limit** $M$ as $x$ approaches $a$ from the left, 

$$\lim_{x\to a^-} f(x) = M$$ 

if the values of $f(x)$ can be made as close to $M$ as we please by taking $x$ sufficiently close to (but not equal to) $a$ and to the left of $a$ (i.e., $x<a$).
```

+++

```{code-cell} ipython3
:tags: [remove-input]

def one_sided(x):
    if x >= 1:
        return 3*x**2-2
    else:
        return x**2+1
    
tab2 = function_to_table(one_sided, [0.9, 0.99, 0.999, 0.9999, 1.0001, 1.001, 1.01, 1.1])
table2 = output_table(tab2)
glue("limit_table2", table2, display=False)
```

+++

````{admonition} Exercise
:class: warning

Below, you see a table in which we evaluate a function $f(x)$ for values of $x$ that are closer and closer to $1$ (but **not equal to** $1$). The first four values are for inputs $x < 1$, the next four are for inputs $x> 1$. 

```{glue:} limit_table2
```

What do the values $f(x)$ suggest $\lim_{x\to 1^+} f(x)$ and $\lim_{x\to 1^-} f(x)$  would be?
````


```{admonition} Click the button to show solution.
:class: tip, dropdown
If approaching from the left ($x< 1$), the values $f(x)$ get closer to $2$ as $x$ gets closer to $1$. This suggests that $\lim_{x \to 1^-} f(x) = 2$.

If approaching from the right ($x> 1$), the values $f(x)$ get closer to $1$ as $x$ gets closer to $1$. This suggests that $\lim_{x \to 1^+} f(x) = 1$.
```


## Limit vs. One-Sided Limits

```{admonition} Fact
:class: info

If both one-sided limits exist and are equal to the same value, $L$, then we can say that the limit exists, and is also equal to $L$.  In other words, 

$$\lim_{x\to a} f(x) = L$$

means the same thing as

$$\lim_{x\to a^-} f(x) = L ~~~~ \hbox{and} ~~~~ \lim_{x\to a^+} f(x)= L.$$
```

+++

<!-- ## Try It Yourself!

```{link-button} https://binder.jupytr.cloud.psu.edu/v2/gh/28left/110jupyter/master?filepath=ch_Limits/limits_def_TIY.ipynb
    :type: url
    :text: Click to launch activity
    :classes: btn-outline-warning btn-block
``` -->
