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
# Composition of Functions

## Definitions

````{admonition} Definition
:class: info

Let $f$ and $g$ be functions.  The _**composition of $f$ and $g$**_ is the function $f\circ g$ (read "$f$ circle $g$" or "$f$ composed with $g$") defined by

$$(f\circ g)(x) = f(g(x))$$


The domain of $f\circ g$ is the set of all $x$ in the domain of $g$ such that $g(x)$ lies in the domain of $f$, as illustrated below.


```{figure} ../images/pic_functions_domaincomposition.png
---
name: illustration-composition-domains
alt: Domain and range of a composition of functions
---
Domain and range of a composition of functions
```
```{dropdown} Long Text Description
A diagram with three ovals arranged from left to right. The leftmost oval is marked domain of g, the oval in the center is marked domain of f, and the right most oval is marked range of f composed with g. There is an arrowed line representing the function g beginning in the leftmost oval at a point labeled x and ending in the center oval at a point labeled g(x). There is a second arrowed line representing the function f beginning in the center oval at the point labeled g(x) and ending in the rightmost oval at a point labeled f(g(x)). There is a third arrowed line representing the function f composed with g beginning in the leftmost oval at the point labeled x and ends in the rightmost oval at the point labeled f(g(x)).
```
````

```{admonition} Important
:class: warning

The order of composition is significant.  In other words, $f\circ g$ and $g\circ f$ are not necessarily the same functions.
```


### Example 1
````{admonition} The composition of functions
:class: tip

Let 

$$f(x) = \sqrt{7-x} \quad \text{ and } \quad g(x) = 3x + 2.$$  

Determine if $x=1$ and $x=2$ are in the domain of  $f\circ g$ and if so, evaluate the function at the given value of $x$.


```{dropdown} **Step 1:** &nbsp; Determine the domain of &nbsp; $f$ &nbsp; and &nbsp; $g$.

The domain of $f$ consists of all values of $x$ such that $7-x\geq 0$, or equivalently, $x\leq 7$.  The domain of $g$ consists of all real numbers.
```


```{dropdown} **Step 2:** &nbsp; Determine if &nbsp; $x=1$ &nbsp; is in the domain of &nbsp; $f \circ g$.

Note that $x=1$ is in the domain of $g$ and $g(1) = 5$, which is in the domain of $f$.  Therefore $x=1$ is in the domain of $f\circ g$ and 

\begin{align*}
(f \circ g)(1) 
&= f(g(1)) \\
&= f(5) \\
&= \sqrt{2}
\end{align*}
```


```{dropdown} **Step 3:** &nbsp; Determine if &nbsp; $x=2$ &nbsp; is in the domain of &nbsp; $f \circ g$.

Note that $x=2$ is in the domain of $g$, but $g(2) = 8$ is not in the domain of $f$.  Therefore $x=2$ is not in the domain of $f \circ g$.
```
````


### Example 2
````{admonition} The composition of functions
:class: tip

Let 

$$f(x) = \sqrt{7-x} \quad \text{ and } \quad g(x) = 3x + 2.$$  

Determine the rule for the composite functions $f \circ g$ and $g \circ f$. 


```{dropdown} **Step 1:** &nbsp; Determine the rule for the composite function &nbsp; $f \circ g$. 

\begin{align*}
(f \circ g)(x)
&= f(g(x)) \\
&= f(3x+2) \\
&= \sqrt{7-(3x+2)} \\
&= \sqrt{7-3x-2} \\
&= \sqrt{5-3x}
\end{align*}

The domain of $f\circ g$ consists of all values $x$ in the domain of $g$ such that $3x+2$ is in the domain of $f$.  As the above calculations show, this ultimately means that $x$ must satisfy the inequality $5-3x \geq 0$. Solving for $x$ in this inequality yields

$$x \leq 5/3$$

and therefore, the domain of $f\circ g$ is $(-\infty,5/3]$.
```

```{dropdown} **Step 2:** &nbsp; Determine the rule for the composite function &nbsp; $g \circ f$.  

\begin{align*}
(g \circ f)(x)
&= g(f(x)) \\
&= g(\sqrt{7-x}) \\
&= 3\sqrt{7-x} + 2
\end{align*}

The domain of $g\circ f$ consists of all values $x$ in the domain of $f$ such that $\sqrt{7-x}$ is in the domain of $g$.  As the above calculations show, this ultimately means that $x$ must satisfy the inequality $7-x\geq 0$. Solving for $x$ in this inequality yields

$$x \leq 7$$

and therefore, the domain of $g\circ f$ is $(-\infty,7]$.
```
````


### Example 3

````{admonition} Simplify a difference quotient
:class: tip

Let $f(x) = 3x^2 - 5x$.  Simplify 

$$\frac{f(a+h) - f(a)}{h}$$

until the factor of $h$ in the denominator has been cancelled out.


```{dropdown} **Step 1:** &nbsp; Evaluate $f(a)$.

To evaluate $f(a)$, replace every occurrence of $x$ in $f(x)$ with $a$.

$$f(a) = 3a^2 - 5a$$

```


```{dropdown} **Step 2:** &nbsp; Expand $f(a+h)$.

To evaluate $f(a+h)$, replace every occurrence of $x$ in $f(x)$ with $(a+h)$.

\begin{align*}
f(a+h) 
&= 3(a+h)^2 - 5(a+h) \\
&= 3(a^2 + 2ah + h^2) - 5(a+h) && \text{square the binomial} \\
&= 3a^2 + 6ah + 3h^2 - 5a - 5h && \text{distribute the $3$ and the $-5$} 
\end{align*}

```


```{dropdown} **Step 3:** &nbsp; Simplify $f(a+h) - f(a)$.

Using **Steps 1** and **2**:

\begin{align*}
f(a+h)  - f(a)
&= 3a^2 + 6ah + 3h^2 - 5a - 5h - (3a^2 - 5a)  && \text{Steps 1 and 2}\\
&= 3a^2 + 6ah + 3h^2 - 5a - 5h - 3a^2 + 5a && \text{distribute the minus sign} \\
&= 6ah + 3h^2 - 5h && \text{cancel out terms} 
\end{align*}

```


```{dropdown} **Step 4:** &nbsp; Simplify $\dfrac{f(a+h) - f(a)}{h}$.


Using **Step 3**:

\begin{align*}
\frac{f(a+h)  - f(a)}{h}
&= \frac{6ah + 3h^2 - 5h}{h} && \text{Step 3} \\
&= \frac{h(6a + 3h - 5)}{h} && \text{pull out a common factor of $h$ in the numerator} \\
&= 6a + 3h - 5 && \text{cancel out the factor of $h$}
\end{align*}
```

````