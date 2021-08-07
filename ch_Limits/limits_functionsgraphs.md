---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3.9 64-bit
  language: python
  name: python3
---
# Functions and Their Graphs

## The Basic Notions

```{admonition} Definition
:class: info
A _**function**_ is a rule that assigns to each element in a set $A$ **one and only one** element in a set $B$.

The set $A$ is called the _**domain**_ of the function.
```

It is customary to denote a function by a letter of the alphabet, such as $f$, $g$, $h$, etc.


```{admonition} Keep in mind
:class: warning

We only do Calculus **on functions**, and all analysis of the functions (i.e., models) is valid **on the domain**.
```

```{admonition} Definition
:class: info

The element in $B$ that $f$ associates with $x$ is written as 

$$f(x)$$ 

(read "$f$ of $x$") and is called the _**value**_ of $f$ at $x$.

The set of all possible values of $f(x)$ resulting from all the possible values of $x$ in its domain, is called the _**range**_ of $f(x)$.
```


```{figure} ./images/pic_limits_domainrange.png
---
name: illustration-domain-range
alt: Illustration of domain and range of a function
---
Illustration of the domain and the range of a function
```


```{admonition} Important
:class: warning

The output $f(x)$ associated with an input $x$ is **unique**:  Each input $x$ must correspond to **one and only one value** of $f$.
```

We have reserved special function designators for common business functions/models (e.g., $d(x)$, $s(x)$, $E(x)$)



## Function Evaluation


### Example 1
Let the function $g$ be defined by the rule

$$g(u) = (3u-2)^{3/2}$$

Compute $g(1)$ and $g(6)$.


````{panels}

\begin{align*}
g(1)
&= (3(1)-2)^{3/2} \\ 
&= (3-2)^{3/2} \\ 
&= (1)^{3/2} \\ 
&= 1 
\end{align*}

---

\begin{align*}
g(6)
&= (3(6)-2)^{3/2} \\ 
&= (18-2)^{3/2} \\ 
&= (16)^{3/2} \\ 
&= (16^{1/2})^{3} \\ 
&= (4)^{3} \\ 
&= 64
\end{align*}

````



### Example 2
Let the function $g$ be again defined by the rule

$$g(u) = (3u-2)^{3/2}$$

Compute $g(u+1)$.


````{panels}

\begin{align*}
g(u+1)
&=& (3(u+1)-2)^{3/2} \\
&=& (3u+3-2)^{3/2} \\
&=& (3u+1)^{3/2} 
\end{align*}

````

```{admonition} Important!
:class: danger

We cannot further simplify the last expression.  In particular

$$(3u+1)^{3/2} \neq (3u)^{3/2} + 1^{3/2}$$
```




## Determining Domain and Range of a Function

```{admonition} Definition
:class: info

Suppose we are given the function $y=f(x)$.  

- The variable $x$ is called the _**independent variable**_.
- The variable $y$, whose value depends on $x$, is called the _**dependent variable**_.
```


To determine the domain of a function, we need to find what restrictions, if any, are to be placed on the independent variable $x$.

In many practical problems, the domain of a function is dictated by the nature of the problem, and any restrictions on the pre-defined function(s) used in the expression.

```{admonition} Key restrictions
:class: danger

- We **cannot take the square root of a negative number**. 
- We **cannot divide by zero**.
```

### Example 3

```{panels}
Find the domain of the function

$$f(x) = \sqrt{x-1}$$
```

- Since the square root of a negative number is **undefined**, it is necessary that 
  \begin{equation*}
  0 \leq x-1
  \end{equation*}
  or equivalently 
  \begin{equation*}
  1 \leq x
  \end{equation*}

- Thus the domain of the function is 

  $$[1,\infty)$$


### Interval Notation

```{image} ./images/pic_precalc_intervaltypes.png
:alt: Table showing intervals corresponding to various inequalities
:class: bg-light mb-1
:align: center
```


### Example 4

```{panels}
Compare the domains of the following functions:
- $g(x) = 2 (x-1)^{5/2}$
- $h(x) = 2 (x-1)^{5/3}$
```

- Note that 
  \begin{equation*}
  2(x-1)^{5/2} = 2(\sqrt{x-1})^5
  \end{equation*}
  The domain of $g(x)$ is 
  \begin{equation*}
    [1,\infty).
  \end{equation*}

- Note that
  \begin{equation*}
  2(x-1)^{5/3} = 2(\sqrt[3]{x-1})^5
  \end{equation*}
  The domain of $h(x)$ is 
  \begin{equation*}
    (-\infty, \infty).
  \end{equation*}



### Example 5

```{panels}
Find the domain of the function

$$f(x) = \frac{1}{x^2-4}$$
```

Our only constraint here is that you **cannot divide by zero**.  So

$$
x^2 - 4 \neq 0
$$

which means that

\begin{align*}
x^2 - 4 & = (x+2)(x-2) \\
  &\neq 0
\end{align*}

Or more specifically $x\neq -2$ and $x\neq 2$. 
Thus the domain of $f$ is 

$$(-\infty,-2)\cup(-2,2)\cup (2,\infty).$$




### Example 6

```{panels}
Find the domain of the function

$$y = \sqrt{9-x^2}$$
```

The domain consists of values of $x$ such that
\begin{align*}
0 &\leq 9-x^2  \\ 
x^2 &\leq 9
\end{align*}
and hence

$$
-3 \leq x  \leq 3
$$

Therefore, the domain is $[-3,3]$.


```{figure} ./images/pic_limits_9-x2.png
---
height: 300px
name: graph_of_9-x^2
alt: The graph of $9-x^2$
---
The graph of $9-x^2$ 
```


### Example 7

```{panels}
Find the range of the function

$$y = \sqrt{9-x^2}$$

(Recall that the domain is $[-3,3]$)
```

For values of $x$ in the domain $[-3,3]$,
\begin{eqnarray*}
0 \leq &9-x^2& \leq 9 \\ 
\sqrt{0} \leq &\sqrt{9-x^2}& \leq \sqrt{9} \\ 
0 \leq &y& \leq 3 
\end{eqnarray*}
Therefore, the range is $[0,3]$.


```{figure} ./images/pic_limits_9-x2range.png
---
height: 300px
name: graph_of_9-x^2_in_domain
alt: The graph of $9-x^2$ restricted to $[-3,3]$
---
The graph of $9-x^2$ restricted to its domain $[-3,3]$. Values range between $0$ and $9$, hence values of $\sqrt{9-x^2}$ range between $0$ and $3$.
```


## The Vertical Line Test for Functions

```{admonition} Vertical Line Test
:class: warning

A curve in the $xy$-plane is the graph of a function if and only if each vertical line intersects the graph in at most one place.
```

This results from the **"one and only one"** restriction in the definition of a function:

> *a function is a rule that assigns to each element in a set $A$ one and only one element in a set $B$*

### Example 8

````{panels} 

```{image} ./images/pic_limits_vertlinetestok.png
:alt: graph of a curve passing the vertical line test
:class: bg-light mb-1
:align: center
```
+++
The curve passes the vertical line test. The vertical line intersects the graph in at most one place.

---

```{image} ./images/pic_limits_vertlinetestfail.png
:alt: graph of a curve failing the vertical line test
:class: bg-light mb-1
:align: center
```
+++
The curve fails the vertical line test. The vertical line intersects the graph in three places.

````


### Example 9

Which of the following curves is the graph of a function?


````{panels} 

```{image} ./images/pic_limits_x2.png
:alt: graph of $y=x^2$
:class: bg-light mb-1
:align: center
```
+++
$y = x^2$

---

```{image} ./images/pic_limits_1x.png
:alt: graph of $y=1/x$
:class: bg-light mb-1
:align: center
```
+++
$y = 1/x$

---

```{image} ./images/pic_limits_sqrtx.png
:alt: graph of $y=sqrt{x}$
:class: bg-light mb-1
:align: center
```
+++
$y = \sqrt{x}$


---

```{image} ./images/pic_limits_y2.png
:alt: graph of $x=y^2$
:class: bg-light mb-1
:align: center
```
+++
$x = y^2$


````



## Piecewise Functions

The function below is defined by the equation

$$
f(x)
= \begin{cases}
-x + 1 & \hbox{if $x<0$} \\
\sqrt{x} & \hbox{if $x\geq 0$}
\end{cases}
$$

The function is defined on the set of all real numbers, in other words, the domain is $(-\infty,\infty)$.

In the subdomain $(-\infty,0)$, the rule for $f$ is given by 

$$f(x) = -x + 1$$

In the subdomain $[0,\infty)$, the rule for $f$ is given by 

$$f(x) = \sqrt{x}$$





````{panels}

```{image} ./images/pic_limits_piecewise.png
:alt: graph of $f(x)$
:class: bg-light mb-1
:align: center
```
+++
The graph of $f(x)$

---

| $x$ | $-3$       | $-2$       | $-1$       | $0$        | $1$        | $2$                   | $3$            |
| -----: |------------: | ------------: | ------------: | ------------: | ------------: |-----------------------: | ----------------: |
| $y$ | $4$ | $3$ | $2$ | $0$ | $1$ | $\approx 1.41$ | $\approx 1.73$ |

+++
Some values of $f(x)$

````


## Equation of Lines

````{admonition} Slope-Intercept Form
:class: info

The equation of the line with slope $m$ and $y$-intercept equal to $b$ is

$$y = mx+ b$$

```{image} ./images/pic_limits_075x+05_slopeinter.png
:alt: graph of line $y = mx+b$
:class: bg-light mb-1
:align: center
```
````


````{admonition} Point-Slope Form
:class: info

The equation of the line with slope $m$ that goes through the point $(a,b)$ is

$$y = m(x-a) + b$$

```{image} ./images/pic_limits_075x+05_pointslope.png
:alt: graph of line $y = m(x-a)+b$
:class: bg-light mb-1
:align: center
```
````
