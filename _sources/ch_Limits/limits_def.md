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
The limit of $f(x)$ as $x$ approaches $a$ is equal to the finite number $L$, denoted by

$$ \lim_{x\to a} f(x) = L$$

if the value of $f(x)$ can be made as close to $L$ as we want by taking x values *sufficiently close* to, but not equal to, $a$.
```

+++

Keep in mind that the value of a limit does not depend on the value of the function at $x=a$.  In fact, it is possible that $\lim\limits_{x\to a}f(x) = L$ even though
- $f(a)$ does not exist, or
- $f(a)$ exists, but is not equal to $L$.


````{admonition} Exercise
:class: warning

Below, you see a table in which we evaluate a function $f(x)$ for values of $x$ that are closer and closer to $1$ (but **not equal to** $1$). What do the values $f(x)$ suggest $\lim\limits_{x\to 1} f(x)$ would be?

:::{card}
:width: 50%

| $x$ | $f(x)$ |
|-----|-------:|
| 1.100000 | 4.63000000 |
| 1.010000 | 4.06030000 |
| 1.001000 | 4.00600300 |
| 1.000100 | 4.00060003 |
:::
````

```{admonition} Show solution
:class: tip, dropdown
The values $f(x)$ get closer to $4$ as $x$ gets closer to $1$.
This suggests that $\lim\limits_{x \to 1} f(x) = 4$.
```

+++

## One-Sided Limits

+++

```{admonition} Definition
:class: info

The limit of $f(x)$ as $x$ approaches $a$ *from the right* is equal to the finite number $L$, denoted by

$$\lim_{x\to a^+} f(x) = L $$ 

if the values of $f(x)$ can be made as close to $L$ as we want by taking $x$ *sufficiently close* to (but not equal to) $a$ and to the right of $a$ (i.e., $x>a$).

Similarly, the limit of $f(x)$ as $x$ approaches $a$ *from the left* is equal to the finite number $M$, denoted by

$$\lim_{x\to a^-} f(x) = M$$ 

if the values of $f(x)$ can be made as close to $M$ as we want by taking $x$ *sufficiently close* to (but not equal to) $a$ and to the left of $a$ (i.e., $x<a$).
```


+++

````{admonition} Exercise
:class: warning

Below, you see a table in which we evaluate a function $f(x)$ for values of $x$ that are closer and closer to $1$ (but **not equal to** $1$). The first four values are for inputs $x < 1$, the next four are for inputs $x> 1$. 

:::{card}
:width: 50%
| $x$ | $f(x)$ |
|-----|-------:|
| 0.900000 | 1.810000 |
| 0.990000 | 1.980100 |
| 0.999000 | 1.998001 |
| 0.999900 | 1.999800 |
| 1.000100 | 1.000600 |
| 1.001000 | 1.006003 |
| 1.010000 | 1.060300 |
| 1.100000 | 1.630000 |
:::

What do the values $f(x)$ suggest $\lim\limits_{x\to 1^+} f(x)$ and $\lim\limits_{x\to 1^-} f(x)$  would be?
````


```{admonition} Show solution
:class: tip, dropdown
If approaching from the left ($x< 1$), the values $f(x)$ get closer to $2$ as $x$ gets closer to $1$. This suggests that $\lim\limits_{x \to 1^-} f(x) = 2$.

If approaching from the right ($x> 1$), the values $f(x)$ get closer to $1$ as $x$ gets closer to $1$. This suggests that $\lim\limits_{x \to 1^+} f(x) = 1$.
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
