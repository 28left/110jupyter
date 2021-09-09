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
# Curve Sketching


```{admonition} Drawing the graph of $y=f(x)$
:class: info

- Determine the domain.
- Find the $x$ and $y$ intercepts, if any.
- Find the vertical and horizontal asymptotes, if any.
- Determine the intervals of increase and decrease.
- Find the relative extrema, if any.
- Determine the intervals of concavity.
- Find the inflection points, if any.
- Graph some additional points to help identify the shape of $f$, if needed, and use this information to sketch the curve.
```


## Example 1

Sketch the graph of 

$$y = \dfrac{2x + 3}{x + 4}.$$



```{dropdown} **Step 1:**  Determine the domain.

In this case, $f(x)$ is undefined when the denominator equals zero, which is when $x= -4$. Therefore, the domain of $f$ is $(-\infty, -4) \cup (-4, \infty)$.
```


```{dropdown} **Step 2:** Find the $x$ and $y$ intercepts, if any.

- $x$-intercept: Set $y=0$ and solve for $x$.

\begin{align*}
    \frac{2x + 3}{x + 4} &= 0 && \text{Set $f(x) = 0$} \\
    \frac{2x + 3}{x + 4}(x + 4) &= 0(x + 4) && \text{Multiply both sides by $(x + 4)$} \\
    2x + 3 &= 0  && \text{Simplify both sides} \\
    x &= -\frac{3}{2}. &&  \text{Solve for $x$}
\end{align*}


- $y$-intercept: Set $x=0$ and solve for $y$.

\begin{align*}
    y 
    &= f(0) && \text{Plug in $x = 0$}\\
    &= \frac{2(0) + 3}{0 + 4} \\
    &= \frac{3}{4}
\end{align*}

Therefore, $f$ has an $x$-intercept at the point $(-3/2,0)$ and a $y$-intercept at the point $(0,3/4)$.
```


```{dropdown} **Step 3:** Find the vertical and horizontal asymptotes, if any.

- Vertical Asymptotes: Since the numerator and denominator are already factored, the vertical asymptotes correspond to the values of $x$ that make the denominator equal to zero.  This happens only when $x = -4$, so $x = -4$ is the only vertical asymptote.


- Horizontal Asymptotes: Since the degree of the numerator and the denominator are the same, both limits at infinity are equal to the ratio of leading coefficients.

  $$\lim_{x\to -\infty} \frac{2x + 3}{x + 4} = 2 = \lim_{x\to \infty} \frac{2x + 3}{x + 4}$$

  Therefore, $y=2$ is the only horizontal asymptote.
```


````{dropdown} **Step 4:** Determine the intervals of increase and decrease.

- Compute $f'(x)$.

  \begin{align*}
  f'(x) 
  &= \frac{2(x + 4) - (2x + 3)(1)}{(x + 4)^2} && \text{Using the   quotient rule}\\
  &= \frac{2x + 8 - 2x - 3}{(x + 4)^2} && \text{Simplify}\\
  &= \frac{5}{(x + 4)^2} && \text{Simplify} 
  \end{align*}
  
  Notice that $f'(x)$ is never equal to zero and is defined for all values of $x$ in the domain of $f$  (i.e., $f$ doesn't have any critical points).

- Compute the sign of $f'(x)$ on the domain of $f$.

```{image} ../images/pic_curvesketching_sketching_1.png
:alt: Sign analysis of $f'(x)$
:width: 300px
:align: center
```

  Therefore, $f$ is increasing on $(-\infty, -4)$ and $(-4, \infty)$.
````

```{dropdown} **Step 5:** Find the relative extrema, if any.

Since $f$ does not have any critical points, $f$ does not have any relative extrema.
```


````{dropdown} **Step 6:** Determine the intervals of concavity.

- Compute $f''(x)$.

\begin{align*}
f''(x) 
&= \frac{d}{dx} 5(x+4)^{-2} && \text{Rewrite $f'(x)$ } \\
&= -10(x+4)^{-3} \\
&= -\frac{10}{(x+4)^3}
\end{align*}

  Notice that $f''(x)$ is never equal to zero and is defined for all values of $x$ in the domain of $f$.\\

- Compute the sign of $f''(x)$ on the domain of $f$.

```{image} ../images/pic_curvesketching_sketching_2.png
:alt: Sign analysis of $f''(x)$
:width: 300px
:align: center
```

  Therefore, $f$ is concave up on $(-\infty, -4)$ and concave down on $(-4, \infty)$.  
````

```{dropdown} **Step 7:** Find the inflection points, if any.

The only change in sign of $f''(x)$ occurs at $x=-4$.  But since $x=-4$ is not in the domain of $f$, $f$ does not have any inflection points.
```


```{dropdown} **Step 8:** Use the information gathered to sketch the function.

```{image} ../images/pic_curvesketching_sketching_3.png
:alt: Graph of $f(x)$
:align: center
```

