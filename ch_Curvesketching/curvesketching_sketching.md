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
- Graph some additional points to help identify the shape of $f$, if needed, and use all of this information to sketch the curve.
```


## Example 1

`````{admonition} Curve sketching
:class: tip

Sketch the graph of $y = \dfrac{2x + 3}{x + 4}$.



```{dropdown} **Step 1:** &nbsp;  Determine the domain.

In this case, $f(x)= \dfrac{2x + 3}{x + 4}$ is undefined when the denominator equals zero, which is when $x= -4$. Therefore, the domain of $f$ is $(-\infty, -4) \cup (-4, \infty)$.
```


```{dropdown} **Step 2:** &nbsp; Find the &nbsp; $x$ &nbsp; and &nbsp; $y$ &nbsp; intercepts, if any.

- $x$-intercept: Set $y=0$ and solve for $x$.

\begin{align*}
    \frac{2x + 3}{x + 4} &= 0 && \text{set $f(x) = 0$} \\
    \frac{2x + 3}{x + 4}(x + 4) &= 0(x + 4) && \text{multiply both sides by $(x + 4)$} \\
    2x + 3 &= 0  && \text{simplify both sides} \\
    x &= -\frac{3}{2}. &&  \text{solve for $x$}
\end{align*}


- $y$-intercept: Set $x=0$ and solve for $y$.

\begin{align*}
    y 
    &= f(0) && \text{plug in $x = 0$}\\
    &= \frac{2(0) + 3}{0 + 4} \\
    &= \frac{3}{4}
\end{align*}

Therefore, $f$ has an $x$-intercept at the point $(-3/2,0)$ and a $y$-intercept at the point $(0,3/4)$.
```


```{dropdown} **Step 3:** &nbsp; Find the vertical and horizontal asymptotes, if any.

- Vertical Asymptotes: Since the numerator and denominator are already factored, the vertical asymptotes correspond to the values of $x$ that make the denominator equal to zero.  This happens only when $x = -4$, so $x = -4$ is the only vertical asymptote.


- Horizontal Asymptotes: Since the degree of the numerator and the denominator are the same, both limits at infinity are equal to the ratio of leading coefficients.

  $$\lim_{x\to -\infty} \frac{2x + 3}{x + 4} = 2 = \lim_{x\to \infty} \frac{2x + 3}{x + 4}$$

  Therefore, $y=2$ is the only horizontal asymptote.
```


````{dropdown} **Step 4:** &nbsp; Determine the intervals of increase and decrease.

- Compute $f'(x)$.

  \begin{align*}
  f'(x) 
  &= \frac{2(x + 4) - (2x + 3)(1)}{(x + 4)^2} && \text{using the quotient rule}\\
  &= \frac{2x + 8 - 2x - 3}{(x + 4)^2} && \text{expand the numerator}\\
  &= \frac{5}{(x + 4)^2} && \text{combine like terms in numerator} 
  \end{align*}
  
  Notice that $f'(x)$ is never equal to zero and is defined for all values of $x$ in the domain of $f$  (i.e., $f$ doesn't have any critical points).

- Compute the sign of $f'(x)$ on the domain of $f$.

```{image} ../images/pic_curvesketching_sketching_1.png
:alt: Sign analysis of $f'(x)$
:width: 300px
:align: center
```
```{dropdown} Long Text Description
A number line with positive and negative signs assigned to intervals, with positive to the left of negative four, and with positive to the right of negative four.
```
Therefore, $f$ is increasing on $(-\infty, -4)$ and $(-4, \infty)$.
````


```{dropdown} **Step 5:** &nbsp; Find the relative extrema, if any.

Since $f$ does not have any critical points, $f$ does not have any relative extrema.
```


````{dropdown} **Step 6:** &nbsp; Determine the intervals of concavity.

- Compute $f''(x)$.

\begin{align*}
f''(x) 
&= \frac{d}{dx} 5(x+4)^{-2} && \text{rewrite $f'(x)$ } \\
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
```{dropdown} Long Text Description
A number line with positive and negative signs assigned to intervals, with positive to the left of negative four, and negative to the right of negative four.
```

Therefore, $f$ is concave up on $(-\infty, -4)$ and concave down on $(-4, \infty)$.  
````


```{dropdown} **Step 7:** &nbsp; Find the inflection points, if any.

The only change in sign of $f''(x)$ occurs at $x=-4$.  But since $x=-4$ is not in the domain of $f$, $f$ does not have any inflection points.
```


````{dropdown} **Step 8:** &nbsp; Use the information gathered to sketch the function.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_curvesketching_sketching_3.png
:alt: Graph of $f(x)$
```
:::
::::

```{dropdown} Long Text Description
There is a horizontal x-axis with the points -16, -12, -8, -4, 4, and 8 labeled. There is a vertical y-axis with the points -6, -2, 2, and 6 labeled. A curve is plotted. The curve has a horizontal asymptote represented by a blue dotted line at y=2, and a vertical asymptote represented by a red line at x= -4. The curve comes in increasing and concave up from its horizontal asymptote on the left, then heads towards infinity as x increases to -4. On the other side of x=-4, the curve comes increasing and concave down from negative infinity and increases towards its horizontal asymptote at y=2 as it heads off to the right.
```
````
`````