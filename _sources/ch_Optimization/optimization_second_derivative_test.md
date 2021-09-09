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
# The Second Derivative Test

## Using the Second Derivative to Classify Critical Points

```{admonition} The Second Derivative Test
:class: info

Suppose $c$ is a critical point of $f$ where $f'(c) = 0$ and $f''(x)$ is continuous near $x=c$.

1. If $f''(c) > 0$, then $f(x)$ has a **relative minimum** at $x=c$.
2. If $f''(c) < 0$, then $f(x)$ has a **relative maximum** at $x=c$.
3. If $f''(c) = 0$, then the test is **inconclusive**.
```

## Example 1

In [Example 1](optimization_critical_points_example_1), we found that the critical points of 

$$f(x)=2x^3-15x^2+36x+20$$ 

were $x=2$ and $x=3$. Classify each critical point using the Second Derivative Test. 

```{dropdown} **Step 1:** Compute $f''(x)$.

\begin{align*}
  f''(x) 
  &= \frac{d}{dx}(6x^2 - 30x+36) & \hbox{using $f'(x)$ from Example 4}\\
  &= 12x - 30
\end{align*}
```

```{dropdown} **Step 2:** Classify each critical point.

Since $f'(2) = 0$ and $f''(2) = -6 < 0$, $f(x)$ has a relative maximum at $x=2$.

Since $f'(3) = 0$ and  $f''(3) = 6 > 0$, $f(x)$ has a relative minimum at $x=3$.
```

## Example 2

In [Example 2](optimization_critical_points_example_2), we found that the only critical point of 

$$f(x)=\frac{1}{x^2-1}$$ 

was $x=0$. Classify the critical point using the Second Derivative Test. 

```{dropdown} **Step 1:** Compute $f''(x)$.

\begin{align*}
  f''(x) 
  &= \frac{d}{dx}\left(\frac{-2x}{(x^2-1)^2}\right) & \hbox{using $f'(x)$ from Example 5}\\
  &= \frac{-2(x^2-1)^2 - (-2x)\cdot 2(x^2-1)2x}{(x^2-1)^4}\\
  &= \frac{2(x^2-1)[-(x^2-1) + 4x^2]}{(x^2-1)^4}\\
  &= \frac{2(1 + 3x^2)}{(x^2-1)^3}
\end{align*}
```

```{dropdown} **Step 2:** Classify each critical point.

Since $f'(0) = 0$ and $f''(0) = -2 < 0$, $f(x)$ has a relative maximum at $x=0$.
```