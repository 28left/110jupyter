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

(curvesketching_critical_points_example_1)=
## Example 1

Find the critical points of 

$$f(x) = \sqrt[3]{x^2-1}.$$

```{dropdown} **Step 1:** Compute $f'(x)$. 

\begin{align*}
f'(x)
&= \frac{d}{dx} (x^2-1)^{1/3} \\
&= \frac{1}{3}(x^2 - 1)^{-2/3} (2x) \\
&= \frac{2x}{3(x^2 - 1)^{2/3}}  
\end{align*}
```

```{dropdown} **Step 2:** Find all $x$ such that $f'(x) = 0$.

$f'(x)=0$ when $2x=0$, which occurs when $x=0$.
```

```{dropdown} **Step 3:** Find all $x$ such that $f'(x)$ does not exist.

$f'(x)$ does not exist when $x^2-1 = 0$, which occurs when $x=1$ and when $x=-1$.
```

```{dropdown} **Step 4:** Verify that the values found in Steps 2 and 3 are in the domain of $f$.

The domain of $f$ is all real numbers.  Therefore, $x=-1$, $x=0$, and $x=1$ are all critical points of $f$.
```



(curvesketching_critical_points_example_2)=
## Example 2

Find the critical points of 

$$f(x) = x^3 +3x^2 - 24x + 1.$$

```{dropdown} **Step 1:** Compute $f'(x)$.

\begin{align*}
f'(x)
&= 3x^2 + 6x - 24 
\end{align*}
```

```{dropdown} **Step 2:** Find all $x$ such that $f'(x) = 0$.

\begin{align*}
f'(x)
&= 3(x^2 + 2x - 8) \\
&= 3(x+4)(x-2)
\end{align*}

which equals zero when $x=-4$ and $x=2$.
```

```{dropdown} **Step 3:** Find all $x$ such that $f'(x)$ does not exist.

Since $f'(x)$ is a polynomial, it exists for all real numbers.
```

```{dropdown} **Step 4:** Verify that the values found in Steps 2 and 3 are in the domain of $f$.

The domain of $f$ is all real numbers.  Therefore, $x=-4$ and $x=2$ are both critical points of $f$.
```