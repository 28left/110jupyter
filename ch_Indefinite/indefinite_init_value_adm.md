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
# Initial Value Problem

An initial value problem is a differential equation (i.e., an equation involving $f'$) combined with an initial condition (i.e., $f(a) = b$).

Use the following strategy to solve an initial value problem.

```{admonition} Strategy to Solve an Initial Value Problem
:class: info

- Find the general solution to the differential equation by using the techniques of integration. 
  \begin{align*}
    f(x) 
    &= \int f'(x)  ~dx \\
    &= F(x) + C
  \end{align*}
  where $F$ is an antiderivative of $f'$.

- Use the initial condition, $f(a) = b$, to solve for $C$.
```

## Example 11

Solve the following initial value problem:

\begin{align*}
  f'(x) &= 4x^3 -3x^2 +x+9\\
  f(1) &= 6
\end{align*}

```{dropdown} **Step 1:** Find the general solution to the differential equation.

\begin{align*}
  f(x) 
  &= \int f'(x) ~dx \\
  &= \int 4x^3 -3x^2 +x+9 ~dx\\
  &= x^4-x^3+\frac{x^2}{2}+9 x + C
\end{align*}
```

```{dropdown} **Step 2:** Use the initial condition to solve for $C$.

\begin{align*}
  6 
  &= f(1) \\
  &= 1 - 1 + \frac{1}{2} + 9 +C && \text{Plug $x=1$ into our result from Step 1}\\
  &= \frac{1}{2}+9 +C && \text{Simplify}
\end{align*}

Therefore

$$C = 6 - \frac{1}{2} - 9 = - \frac{7}{2}.$$
```

```{dropdown} **Step 3:** Combine the results from Steps 1 and 2 to get the solution to the initial value problem.

$$f(x) = x^4 - x^3 + \frac{x^2}{2} + 9x - \frac{7}{2}$$
```

## Example 12

The estimated marginal profit associated with producing/selling jasmine rice is $P'(x) = -0.08x + 24$ dollars per pound per month where $x$ is the production level in pounds per month. The fixed cost of producing/selling rice is \$1,500 a month. What is the maximum monthly profit?

```{dropdown} **Step 1:** Find the value of $x$ that maximizes profit.

$P'(x)$ equals zero when

$$-\frac{8}{100}x + 24 = 0$$

which is when 

$$x = \frac{24\cdot 100}{8} = 300$$

Notice that $P''(x) = -8/100$ is always negative. Therefore, $P(x)$ is always concave down and $x = 300$ corresponds to an absolute maximum profit.

Ultimately, we will evaluate $P(300)$ to find the maximum monthly profit, but we don't currently have a formula for $P(x)$. Therefore, our next goal is to find $P(x)$.
```

```{dropdown} **Step 2:** Identify the initial value problem.

\begin{align*}
  P'(x) &= -\frac{8}{100}x +24 && \text{Stated in the problem}\\
  P(0) &=- 1,500 && \text{Since fixed costs are \$1,500}
\end{align*}

Note that the initial profit is negative since fixed costs count against profit.
```

```{dropdown} **Step 3:** Solve the initial value problem:

\begin{align*}
  P(x) &= \int P'(x) ~dx \\
  &= \int -\frac{8}{100}x+24 ~ dx \\
  &= -\frac{8}{100}\cdot \frac{x^2}{2} + 24x +C \\ 
  &= -\frac{4}{100}x^2 +24x + C \\
\end{align*}

\begin{align*}
P(0) &= -1500 \\
&= -\frac{4}{100}(0)^2 + 24(0) +C \\
&= C
\end{align*}

Therefore, $P(x) = -\dfrac{4}{100}x^2 + 24x -1500$.
```

```{dropdown} **Step 4:** From Step 1, we know that profit is maximized when $x=300$.

\begin{align*}
  P(300) 
  &= -\frac{4}{100}(300)^2 + 24(300) - 1500 \\
  %&= -\frac{4}{100}(300)(300) + 24(300) - 1500 \\
  %&= -4(3)(300) + 24(300) - 1500 \\
  &= -3600 + 7200 - 1500 \\
  &= 2100
\end{align*}
```