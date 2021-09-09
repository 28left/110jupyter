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
# Critical Points

```{admonition} Definition
:class: info

A **critical point** of the function $f$ is any number $c$ *in the domain of* $f$ such that 

$$f'(c)=0 \quad \text{or} \quad \text{$f'(c)$ does not exist.}$$
```

Critical points of $f$ correspond to *possible* locations of relative extrema.

(optimization_critical_points_example_1)=
## Example 1

Find all critical points of $f(x)=2x^3-15x^2+36x+20$.

```{dropdown} **Step 1:** Compute $f'(x)$. 

$$f'(x) = 6x^2-30x+36$$
```

```{dropdown} **Step 2:** Find $x$ such that $f'(x) = 0$.

\begin{align*} 
  6x^2-30x+36 &= 6(x^2-5x+6)\\
  &= 6(x-2)(x-3)\\
  &= 0
\end{align*}

when $x=2$ or when $x=3$.
```

```{dropdown} **Step 3:** Find $x$ such that $f'(x)$ does not exist.

Since $f'(x)$ is polynomial, it exists for all real numbers.
```

```{dropdown} **Step 4:** Verify that the values found in Steps 2 and 3 are in the domain of $f$.

The domain of $f(x)$ is all real numbers. Therefore, since both values are in the domain of $f$, $x=2$ and $x=3$ are critical points of $f$.
```

(optimization_critical_points_example_2)=
## Example 2

Find all critical points of $f(x)=\dfrac{1}{x^2-1}$.

```{dropdown} **Step 1:** Compute $f'(x)$.

\begin{align*} 
  f'(x) &= \frac{d}{dx}(x^2-1)^{-1}\\
  &= -(x^2-1)^{-2}\cdot 2x \\
  &= -\frac{2x}{(x^2-1)^2}
\end{align*}
```

```{dropdown} **Step 2:** Find $x$ such that $f'(x) = 0$.

$f'(x) = 0$ when $2x = 0$, which occurs when $x=0$.
```

```{dropdown} **Step 3:** Find $x$ such that $f'(x)$ does not exist.

$f'(x)$ does not exist when $(x^2-1)^2 = 0$, which occurs when $x=1$ and when $x=-1$.
```

```{dropdown} **Step 4:** Verify that the values found in Steps 2 and 3 are in the domain of $f$.

The domain of $f(x)$ is all real numbers except $x=1$ and $x=-1$. Therefore, $x=0$ is a critical point, but $x=1$ and $x=-1$ are not critical points since they are not in the domain of $f$. 
```