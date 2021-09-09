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
3. If $f''(c) = 0$, then the test is **inconclusive** and the First Derivative Test should be used instead.
```

## Example 1

Find the relative extrema of 

$$f(x) = 12 x^5 - 45 x^4 - 200 x^3 +12.$$

```{dropdown} **Step 1:** Find the critical points of $f$.

\begin{align*}
f'(x) &= 60 x^4 - 180 x^3 - 600 x^2 \\
&= 60x^2(x^2-3x-10) && \text{Pull out common factor of $60x^2$}\\
&= 60x^2(x-5)(x+2) && \text{Factor}\\
\end{align*}

which equals zero when $x=-2$, $x=0$, and $x=5$.  Also note that $f'(x)$ exists for all $x$ in the domain of $f$.  Since the domain of $f$ is $(-\infty,\infty)$, all of these values of $x$ are critical points.
```

```{dropdown} **Step 2:** Compute $f''(x)$.

\begin{align*}
f''(x) 
&= \frac{d}{dx}(60 x^4 - 180 x^3 - 600 x^2)\\
&= 240 x^3 - 540 x^2 - 1200 x \\
&=  60 x (4 x^2 - 9 x - 20) \\
\end{align*}
```

````{dropdown} **Step 3:** Evaluate $f''(x)$ at each critical point.

Evaluate $f''(x)$ at each critical point where $f'(x)=0$ and use the Second Derivative Test to classify each critical point, if possible.

- $x=-2$: Since $f'(-2) = 0$ and $f''(-2) = 60(-2)(16+18-20) < 0$, $f$ has a relative maximum at $x=-2$.


- $x=0$: Since $f'(0) = 0$ and $f''(0) = 60(0)(-20) = 0$, the Second Derivative test is inconclusive.  Instead, using the First Derivative test, we see that there is no change in sign of $f'(x)$ at $x=0$, and therefore, $f$ does not have a relative extreme at $x=0$.

```{figure} ../images/pic_curvesketching_secondderivativetest.png
---
name: pic_curvesketching_secondderivativetest
width: 400px
---
Interval analysis of $f''(x) = 60 x (4 x^2 - 9 x - 20)$.
```

- $x=5$: Since $f'(5) = 0$ and $f''(5) = 60(5)(100-45-20) > 0$, $f$ has a relative minimum at $x=5$.
````
