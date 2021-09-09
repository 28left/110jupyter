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
# Solving Equations

## How to Solve an Equation

To find all values of $x$ that satisfy an equation (e.g., $f(x) = g(x)$), complete the following steps: 

```{admonition} Steps for solving an equation
:class: info
1. Rewrite equation as $f(x) - g(x) = 0$, if needed.
2. Simplify and factor the left-hand side.
3. Set each factor equal to zero and solve for $x$.
```

Find all values of $x$ such that $x^2 - 4x - 12 = 0$.


(01_03_example1)=
### Example 1

```{admonition} Solving a quadratic equation
:class: tip

Find all values of $x$ such that $x^2 - 4x - 12 = 0$.
```

```{dropdown} **Step 1:** Factor $x^2 - 4x - 12$.

*Recall from [Factoring, Example 8](01_02_example8) that* 

$$x^2 - 4x - 12 = (x+2)(x-6)$$
```

```{dropdown} **Step 2:** Set each factor equal to zero and solve for $x$.

\begin{align*}
x + 2 &= 0  ~~~~\Rightarrow~~~~  x = -2\\
x - 6 &= 0  ~~~~\Rightarrow~~~~  x = 6
\end{align*}

Therefore, $x=6$ and $x=-2$ satisfy $x^2 - 4x - 12 = 0$.
```

```{dropdown} Check Your Work.
:title: bg-warning font-weight-bold

\begin{align*}
(-2)^2 - 4(-2) - 12 &= 4 + 8 - 12 = 0 \\
6^2 - 4(6) - 12 &= 36 - 24 - 12 = 0
\end{align*}
```


### Example 2

```{admonition} Solving a rational equation
:class: tip

Find all values of $p$ such that $\dfrac{3p}{180-6p} = 1$.
```

```{dropdown} **Step 1:** Multiply both sides of $\frac{3p}{180-6p} = 1$ by the denominator, $180-6p$.

$$3p = 180 - 6p$$
```

```{dropdown} **Step 2:** Subtract $180 - 6p$ from both sides.

\begin{align*}
3p - (180-6p) &= 0 \\
3p - 180 +6p &= 0 && \hbox{Distribute the minus sign}\\
9p - 180 &= 0 && \hbox{Combine like terms}
\end{align*}
```

```{dropdown} **Step 3:** Solve for $p$.

\begin{align*}
    9p &= 180 && \text{Add $180$ to both sides} \\
    p &= 20 && \text{Divide both sides by 9}
\end{align*}

Therefore, $p=20$ is the only value that satisfies $\frac{3p}{180-6p} = 1$.
```

```{dropdown} Check Your Work.
:title: bg-warning font-weight-bold

$$\dfrac{3(20)}{180-6(20)} = \frac{60}{180-120} = \frac{60}{60} = 1$$
```

### Example 3

```{admonition} Points of intersection
:class: tip

Find all points of intersection of $f(x) = 6x^2 - 4x$ and $g(x) = 2 - 5x$.
```

```{dropdown} **Step 1:** Set $f(x) = g(x)$.
Points of intersection can be found by setting the two curves equal to each other and solving for $x$.

$$6x^2 - 4x =  2 - 5x$$
```

```{dropdown} **Step 2:** Subtract $2-5x$ from both sides of the equation in Step 1.

\begin{align*}
6x^2 - 4x - (2 - 5x) &=  0 && \hbox{Note the parentheses around $2-5x$}\\
6x^2 - 4x - 2 + 5x &=  0 && \hbox{Distribute the minus sign}\\
6x^2 + x - 2 &=  0 && \hbox{Combine like terms}
\end{align*}
```

```{dropdown} **Step 3:** Use the AC grouping method to factor $6x^2 + x - 2$.

Find two integers that multiply to $6(-2) = -12$ and sum to $1$.

| Product equals $-12$ | Sum equals $1$? |
| -------------------- | --------------- |
| $-1 \times 12$       | NO  |
| $-2 \times 6$        | NO  |
| $-3 \times 4$        | **YES** |

Therefore,
\begin{align*}
6x^2 + x - 2
&= 6x^2 - 3x + 4x - 2 \\
&= 3x(2x-1) + 2(2x-1) \\
&= (3x+2)(2x-1) 
\end{align*}
```


```{dropdown} **Step 4:** Set each factor equal to zero and solve for $x$.

\begin{align*}
3x + 2 &= 0  ~~~~\Rightarrow~~~~  3x = -2 ~~~~\Rightarrow~~~~ x = -2/3\\
2x - 1 &= 0  ~~~~\Rightarrow~~~~  2x = 1 \hspace{25pt}\Rightarrow~~~~ x = 1/2
\end{align*}

Therefore, the only points of intersection of $f(x) = 6x^2 - 4x$ and $g(x) = 2 - 5x$ occur when $x=-2/3$ and $x=1/2$.
```

```{dropdown} Check Your Work.
:title: bg-warning font-weight-bold

| $x$  | $f(x) = 6x^2 - 4x$ | $g(x) = 2 - 5x$ |
| ---  | ----               | ----            |
| $-2/3$ | $6(-2/3)^2 - 4(-2/3) = 16/3 $ | $2 - 5(-2/3) = 16/3$ |
| $1/2$  | $6(1/2)^2 - 4(1/2) = -1/2$    | $2 - 5(1/2) = -1/2$  |
```
