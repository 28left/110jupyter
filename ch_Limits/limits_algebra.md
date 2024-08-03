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

# Computing Limits Algebraically

## Example 1
````{admonition} The limit of a constant function
:class: tip

If $f(x) = 2$, evaluate $\lim\limits_{x\to 1^{-}}f(x)$.


```{dropdown} **Step 1:** &nbsp; Recall the limit property of a constant function.

For any real number $c$, $\lim\limits_{x\to a}c = c$.

See {ref}`lim:prop_lim` for a list of all limit properties.
```

```{dropdown} **Step 2:** &nbsp; Apply the limit property of a constant function.

Since $f(x) = 2$ is a constant function, $\lim\limits_{x\to 1}f(x) = 2$, which implies that the one-side limit also exists and

$$\lim\limits_{x\to 1^{-}}f(x) = 2.$$
```
````

## Example 2

````{admonition} The limit of a rational function
:class: tip

Evaluate $\lim\limits_{x\to -1} \dfrac{x^3 +4x^2-x-3}{2x^2+1}$.


```{dropdown} **Step 1:** &nbsp; Recall the limit property of a rational function.

If $f(x)$ is a rational function and $a$ is in the domain of $f(x)$, then $\lim\limits_{x\to a}f(x) = f(a)$.

See {ref}`lim:prop_lim` for a list of all limit properties.
```

```{dropdown} **Step 2:** &nbsp; Determine if $x=-1$ is in the domain of the function.

The function 

$$ g(x) = \dfrac{x^3 +4x^2-x-3}{2x^2+1}$$

is a rational function and since $2(-1)^2 + 1 \neq 0$ (i.e., the denominator is not equal to zero when $x=-1$), it follows that $-1$ is in the domain of $g$.  

Therefore, the limit exists and

$$\lim\limits_{x\to -1} g(x) = g(-1) = \frac{(-1)^3 + 4(-1)^2 - (-1) -3}{2(-1)^2+1} = \frac{1}{3}.$$
```
````


## Example 3
````{admonition} The limit of a rational function
:class: tip

Evaluate $\lim\limits_{x\to 2} \dfrac{x^2 +4x-1}{x-2}$.


```{dropdown} **Step 1:** &nbsp; Determine if $x=2$ is in the domain of the function.

The function 

$$ h(x) = \dfrac{x^2 +4x-1}{x-2}$$

is a rational function and since $2-2 = 0$ (i.e., the denominator equals zero when $x=2$), it follows that $2$ is not in the domain of $h$.  Unfortunately, this means that the limit property we used in the previous example does not apply.
```

```{dropdown} **Step 2:** &nbsp; Determine if the limit exists.

When we evaluate the numerator of $h(x)$ at $x=2$, we get

$$2^2 +4(2) - 1 = 11.$$

Since the denominator goes to zero but the numerator does not, we can immediately conclude that $\lim\limits_{x\to 2} \dfrac{x^2 +4x-1}{x-2}$ does not exist.
 

Moreover, if we let $x$ approach $2$ from the left (i.e., $x<2$), the values of $(x^2 +4x-1)/(x-2)$ will be negative and we can conclude that 

$$\lim\limits_{x\to 2^-} \dfrac{x^2 +4x-1}{x-2} = -\infty $$

And if we let $x$ approach $2$ from the right (i.e., $x>2$), the values of $(x^2 +4x-1)/(x-2)$ will be positive and we can conclude that 

$$\lim\limits_{x\to 2^+} \dfrac{x^2 +4x-1}{x-2} = \infty$$

Even though we can say that the one-sided limits are equal to positive or negative infinity, this still means that the one-sided limits do not exist, and therefore the original limit does not exist either.
```
````

+++

```{admonition} Evaluating the Limit of a Rational Function
:class: note

When evaluating the limit of a rational function, $\lim\limits_{x\to a} \dfrac{f(x)}{g(x)}$, start by plugging in $x=a$ into both $f(x)$ and $g(x)$.

- If $g(a) \neq 0$, then the limit exists and is equal to $f(a)/g(a)$.

- If $g(a)=0$ and $f(a)\neq 0$, then the limit does not exist.  By carefully analyzing the sign of the numerator and of the denominator, we can determine if the one-sided limits go to positive or negative infinity.

- If $g(a) = 0$ and $f(a)=0$, it's still possible the limit exists.  We will consider this situation in the next section.
```

## Example 4
````{admonition} The limit of a piecewise function
:class: tip

Evaluate $\displaystyle\lim_{x\to 6} h(x)$, where

\begin{equation*}
h(x)=
\begin{cases} 
x^2-4x-12 & \hbox{if } x<6 \\
8 & \hbox{if } x=6 \\
x^2-5x-6 & \hbox{if } x>6 \\  
\end{cases}
\end{equation*}


```{dropdown} **Step 1:** &nbsp; Recall the limit property of a polynomial

If $f(x)$ is a polynomial function, then $\lim\limits_{x\to a}f(x) = f(a)$.

See {ref}`lim:prop_lim` for a list of all limit properties.
```

```{dropdown} **Step 2:** &nbsp; Compute the limit from the left.

Since we are approaching 6 from the left, we can assume that $x<6$, which means $h(x) = x^2-4x-12$ and we can apply the limit property of a polynomial.
\begin{align*}
\lim_{x\to 6^{-}} h(x) 
&= \lim_{x\to 6^-} x^2-4x-12\\ \\
&= 6^2-4(6)-12 && \text{plug in $x=6$}\\ \\
&= 36-24-12 && \text{simplify}\\ \\
&= 0
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Compute the limit from the right. 

Since we are approaching 6 from the right, we can assume that $x>6$, which means $h(x) = x^2-5x-6$, and we can apply the limit property of a polynomial.
\begin{align*}
\lim_{x\to 6^{+}} h(x) 
&= \lim_{x\to 6^+} x^2-5x-6\\ \\
&= 6^2-5(6)-6  && \text{plug in $x=6$}\\ \\
&= 36-30-6 && \text{simplify}\\ \\
&= 0
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Check to see if the two one-sided limits are equal.

Since $\displaystyle \lim_{x\to 6^-} h(x) = 0$ and $\displaystyle \lim_{x\to 6^+} h(x) = 0$ (i.e., the two one-sided limits both exist and are equal), we conclude that the limit exists and

$$\lim_{x\to 6} h(x) = 0.$$
```

```{warning} 

Notice that we did not use the fact that $h(6) = 8$ while computing $\displaystyle\lim_{x\to 6} h(x)$.  Futhermore, the fact that $\displaystyle\lim_{x\to 6} h(x) \neq h(6)$  does not mean that the limit does not exist.
```
````


## Example 5
````{admonition} The limit of a piecewise function
:class: tip

Evaluate $\displaystyle\lim_{x\to 4} g(x)$, where

\begin{equation*}
g(x)=
\begin{cases} 
\dfrac{x+5}{3} & \hbox{if } x\leq 4 \\
6 - x^2& \hbox{if } x>4 
\end{cases}
\end{equation*}



```{dropdown} **Step 1:** &nbsp; Compute the limit from the left.

Since we are approaching 4 from the left, we can assume that $x<4$, which means $g(x) =\frac{x+5}{3}$ and we can apply the limit property of a polynomial.
\begin{align*}
\lim_{x\to 4^{-}} g(x) 
&= \lim_{x\to 4^-} \frac{x+5}{3} \\ \\
&= \frac{4+5}{3} && \text{plug in $x=4$}\\ \\
&= 9/3 && \text{simplify}\\ \\
&= 3
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Compute the limit from the right. 

Since we are approaching 4 from the right, we can assume that $x>4$, which means $g(x) = 6 - x^2$, and we can apply the limit property of a polynomial.
\begin{align*}
\lim_{x\to 4^{+}} g(x) 
&= \lim_{x\to 6^+} 6 - x^2\\ \\
&= 6 - 4^2  && \text{plug in $x=4$}\\ \\
&= 6 - 16 && \text{simplify}\\ \\
&= -10
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Check to see if the two one-sided limits are equal.

Since $\displaystyle \lim_{x\to 4^-} g(x) = 3$ and $\displaystyle \lim_{x\to 4^+} g(x) = -10$ (i.e., the two one-sided limits both exist but are not equal), we conclude that 
$\lim\limits_{x\to 4} g(x)$ does not exist.
```
````

