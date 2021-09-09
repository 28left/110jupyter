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
# Continuity

## Defintion and Properties

```{admonition} Definition
:class: info

A function $f(x)$ is **continuous at a number $x = a$** if the following conditions are satisfied:
- $f(a)$ is defined
- $\displaystyle{\lim_{x \to \\a}} f(x)$ exists (rule for existence: 
$\displaystyle{\lim_{x \to \\a^-}} f(x) = \displaystyle{\lim_{x \to \\a^+}} f(x)$ )
- $\displaystyle{\lim_{x \to \\a}} f(x) = f(a)$

The function $f(x)$ is **continuous on the interval $(a, b)$** if it is continuous at each point in the interval.\\

If $f(x)$ is not continuous at $x=a$, then $f(x)$ is said to be **discontinuous** at $x=a$.
```

```{admonition} Properties of Continuous Functions
:class: info

If $f(x)$ and $g(x)$ are continuous at $x = a$ then:
- $[f(x)]^n$ where $n$ is a real number, is continuous at $x=a$ whenever it is defined at that number.
- $f(x) \pm g(x)$ is continuous at $x = a$
- $f(x) \times g(x)$ is continuous at $x = a$
- $\dfrac{f(x)}{g(x)}$ is continuous at $x = a$ provided $g(a)\neq 0$
```

```{admonition} Continuity of Polynomial and Rational Functions
:class: info
Polynomial and rational functions are continuous on their domains.

- A polynomial function $y = p(x)$ is continuous everywhere.
- A rational function $R(x) = \dfrac{p(x)}{q(x)}$ is continuous everywhere $q(x) \neq 0$.
```


## Examples

### Example: Continuity at a point

Is the function $f(x)$ continuous at $x=1$?

$$
f(x) =
\begin{cases}
-x^3+x^2-1 	& \hbox{if } x\leq 1 \\
3x^2-x-3	& \hbox{if } x > 1
\end{cases}
$$

```{dropdown} **Step 1:** Determine if $f(x)$ is defined at $x=1$.

When $x=1$, $f(x)$ is defined by $f(x) = -x^3+x^2-1$.  Therefore,

\begin{align*}
f(1) 
&= -(1)^3+(1)^2-1 & \hbox{Plug in $x=1$}\\
&= -1 
\end{align*}

Since $f(x)$ is defined at $x=1$, we now check to see if the limit exists.
```



```{dropdown} **Step 2:** Determine if the limit at $x=1$ exists.

For the left-hand limit, $x\to1^-$ means $x< 1$, and therefore $f(x) = -x^3+x^2-1$.

\begin{align*}
\lim_{x\to 1^-} f(x) 
&= \lim_{x\to 1^-} -x^3+x^2-1\\
&= -1^3+1^2-1 & \hbox{Plug in $x=1$}\\
&= -1 
\end{align*}

For the right-hand limit, $x\to1^+$ means $x> 1$, and therefore $f(x) = 3x^2-x-3$.
\begin{align*}
\lim_{x\to 1^+} f(x) 
&= \lim_{x\to 1^+} 3x^2-x-3 \\
&= 3(1)^2-1-3 & \hbox{Plug in $x=1$} \\
&= -1 
\end{align*}

Since both one-sided limits exist and are equal to $-1$, we conclude that

$$\lim_{x\to 1} f(x) = -1$$

Since the limit exists, we now check to see if the value of the function and the limit are equal to each other.
```


```{dropdown} **Step 3:** Compare $f(1)$ and $\lim\limits_{x \to 1} f(x)$.

Both the function at $x=1$ and the limit of the function as $x$ approaches $1$ are equal to $-1$.

$$f(1) = -1 = \lim_{x\to 1}f(x)$$
```


```{dropdown} **Step 4:** Conclusion

Since $f(1)$ is defined, $\lim\limits_{x \to 1} f(x)$ exists, and $\lim\limits_{x \to 1}f(x) = f(1)$,
we conclude that $f(x)$ is continuous at $x=1$.
```


### Example: Discontinuities

Find the discontinuities of $f(x)$ where

$$f(x) = \frac{2x^4-2x^3-12x^2}{x^4-9x^2}.$$

```{dropdown} **Step 1:** Factor the denominator.

\begin{align*}
x^4-9x^2
&= x^2(x^2-9) && \hbox{Pull out common factor of $x^2$}\\
&= x^2(x-3)(x+3) && \hbox{Since $A^2 - B^2 = (A-B)(A+B)$}
\end{align*}
```


```{dropdown} **Step 2:** Set each factor of the denominator equal to zero.

\begin{align*}
x^2 &= 0 ~~~~\hbox{ when $x=0$}\\
x-3 &= 0 ~~~~\hbox{ when $x = 3$}\\
x+3 &= 0 ~~~~\hbox{ when $x = -3$}
\end{align*}
Therefore, $f(x)$ has discontinuities at $x=0$, $x=3$, and $x=-3$.
```

```{warning}
Remember, rational functions have discontinuities whenever the *denominator* is equal to zero.  There is no need to factor and/or simplify the *numerator* when finding discontinuities of a rational function.
```



### Example: Choosing a parameter to make a function continuous

Find the value of $k$ that makes $f(x)$ continuous at $x=2$.

$$
f(x) = 
\begin{cases}
x+k & \hbox{ if $x < 2$}\\
x^2 + kx - 7 & \hbox{ if $x \geq 2$}
\end{cases}
$$


```{dropdown} **Step 1:** Evaluate $\displaystyle{\lim_{x \to 2}}  f(x)$ from left and right.

**Left**
\begin{align*}
\lim_{x \to 2^-} f(x) 
&= \lim_{x \to 2^-} x+k \\
&=2+k 
\end{align*}

**Right**
\begin{align*}
\lim_{x \to 2^+} f(x) 
&= \lim_{x \to 2^+} x^2 + kx -7 \\
&=2^2+k(2)-7 \\
&=2k-3 
\end{align*}
```

```{dropdown} **Step 2:** Set the left and right limits equal to each other.

$$2+k = 2k-3$$

Solve for $k$ by adding 3 to both sides and subtracting $k$ from both sides.  Thus $k=5$ makes the function $f(x)$ continuous at $x=2$.