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
# Absolute Extrema

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

```{admonition} Definition
:class: info

The absolute extrema of a function $f$:

- If $f(c) \geq f(x)$ for all $x$ in the domain of $f$, then $f(c)$ is called the **absolute maximum value** of $f$.
- If $f(c) \leq f(x)$ for all $x$ in the domain of $f$, then $f(c)$ is called the **absolute minimum value** of $f$.
```

## Absolute Extrema in a Closed Interval

If a function $f$ is continuous on a closed interval $[a,b]$, then $f$ has both an absolute maximum value and an absolute minimum value on $[a,b]$.

## Example 1

Observe that for a continuous function defined on a closed interval, absolute extrema can either appear at the endpoints of the interval or at the same place as a relative extrema.

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[scale = 1.8]

  \draw [white,fill=white] (-1,-1) rectangle (8.5,5);
  \draw [->] (-.5,0) -- (8,0) node [below] {$x$};
  \draw [->] (0,-.5) -- (0,4.5) node [right] {$y$};

  \draw [black,ultra thick] (1,3) node [above,align=center] {Not a Relative\\Extrema} 
  sin (2,1.5) node [below,align=center] {Relative\\Minimum} 
  cos (3,2.5) node [above,align=center] {Relative\\Maximum}
  sin (5,1.0)  node [below,align=center] {Abs. \& Rel.\\Minimum} 
  cos (7,4) node [above,align=center] {Absolute\\Maximum};

  % draw dashed lines
  \node [align=center, below] at (1,0) {$a$};
  \draw [dashed] (1,0) -- (1,3);
  %\node [align=center, below] at (2,0) {$x_{1}$};
  %\draw [dashed] (2,0) -- (2,1.5);
  %\node [align=center, below] at (3,0) {$x_{2}$};
  %\draw [dashed] (3,0) -- (3,2.5);
  %\node [align=center, below] at (5,0) {$x_{3}$};
  %\draw [dashed] (5,0) -- (5,1.0);
  \node [align=center, below] at (7,0) {$b$};
  \draw [dashed] (7,0) -- (7,4);

  % draw points
  \foreach \point in {(1,3), (2,1.5), (3,2.5), (5,1.0), (7,4)}
  \draw [black,fill=red] \point circle [radius=.06];

\end{tikzpicture}
\end{document} 
```

## How to Find the Absolute Extrema of a Function on a Closed Interval

```{admonition} Finding Absolute Extrema on a Closed Interval
:class: info

To find the absolute extrema of a function $f$ on a closed interval $[a,b]$

1. Find the critical points of $f$ that lie on $(a,b)$.
2. Compute the value of $f$ at each critical point found in Step 1 and compute $f(a)$ and $f(b)$.
3. The absolute maximum value and absolute minimum value of $f$ will correspond to the largest and smallest numbers, respectively, found in Step 2.
```

## Example 2

Find the absolute extrema of the function 

$$f(x)=x^3-2x^2-4x+4$$ 

on the interval $[0,3]$.

```{dropdown} **Step 1:** Decide whether $f$ is continuous on the interval.

Observe that $f$ is continuous on the closed interval $[0,3]$.
```

```{dropdown} **Step 2:** Find the critical points of $f$ on $(0,3)$, if any.

\begin{align*}
  f'(x) &= 3x^2-4x-4\\
  &=(3x+2)(x-2)
\end{align*}

Therefore, $f'(x)=0$ when $x=-2/3$ and $x=2$. But since $x=-2/3$ is not on the interval $(0,3)$, $x=2$ is the only critical point on $(0,3)$.
```

```{dropdown} **Step 3:** Evaluate $f(x)$ at critical points on $(0,3)$ and the endpoints of $[0,3]$.

\begin{align*}
  f(0) &= 4 \\
  f(2) &= -4 \\
  f(3) &= 1 
\end{align*}
```

```{dropdown} **Step 4:** Find absolute extrema by comparing values from Step 3.

It follows that $f(2)=-4$ is the absolute minimum value and $f(0)=4$ is the absolute maximum value.
```

## Example 3

Find the absolute extrema of the function 

$$f(x)=4x^5+5x^4$$ 

on the interval $[-2,1]$.

```{dropdown} **Step 1:** Decide whether $f$ is continuous on the interval.

Observe that $f$ is continuous on the closed interval $[-2,1]$.
```

```{dropdown} **Step 2:** Find the critical points of $f$ on $(-2,1)$, if any.

\begin{align*}
  f'(x) &= 20x^4+20x^3\\
  &=20x^3(x+1)
\end{align*}

Therefore, $f'(x) = 0$ when $x=0$ and $x=-1$, both of which are on $(-2,1)$.
```

```{dropdown} **Step 3:** Evaluate $f(x)$ at critical points on $(-2,1)$ and the endpoints of $[-2,1]$.

\begin{align*}
  f(-2) &= -48 \\
  f(-1) &= 1 \\
  f(0) &= 0 \\
  f(1) &= 9 
\end{align*}
```

```{dropdown} **Step 4:** Find absolute extrema by comparing values from Step 3.

It follows that $f(-2)=-48$ is the absolute minimum value and $f(1)=9$ is the absolute maximum value.
```

## Example 4

Find the absolute extrema of the function 

$$f(x)=\frac{1}{x-1}$$ 

on the interval $[2,4]$.

```{dropdown} **Step 1:** Decide whether $f$ is continuous on the interval.

Observe that $f$ has a discontinuity at $x=1$, however this is not on the interval $[2,4]$. Therefore $f$ is continuous on the closed interval $[2,4]$.  
```

```{dropdown} **Step 2:** Find the critical points of $f$ on $(2,4)$, if any.

\begin{align*}
  f'(x) 
  &= \frac{d}{dx} (x-1)^{-1} \\
  &= -(x-1)^{-2}\\
  &= -\frac{1}{(x-1)^2}
\end{align*}

which is never equal to zero, but does always exist on the interval $(2,4)$. Notice that $x=1$ is not a critical point of $f$ since $f(1)$ is not defined. In other words, $f$ does not have any critical points. 
```

```{dropdown} **Step 3:** Evaluate $f(x)$ at critical points on $(2,4)$ and the endpoints of $[2,4]$.

Since there are no critical points, we need only evaluate $f$ at $x=2$ and $x=4$.

\begin{align*}
  f(2) &= 1 \\
  f(4) &= 1/3
\end{align*}
```

```{dropdown} **Step 4:** Find absolute extrema by comparing values from Step 3.

It follows that $f(4)=1/3$ is the absolute minimum value and $f(2)=1$ is the absolute maximum value.
```