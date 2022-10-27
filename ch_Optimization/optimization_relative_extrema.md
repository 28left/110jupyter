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
# Relative Extrema

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

```{admonition} Definition
:class: info

The relative extrema of a function $f$:

- A function $f$ has a **relative maximum** at $x=c$ if there exists an open interval $(a,b)$ containing $c$ such that $f(c) \geq f(x)$ for all $x$ in $(a,b)$.
- A function $f$ has a **relative minimum** at $x=c$ if there exists an open interval $(a,b)$ containing $c$ such that $f(c) \leq f(x)$ for all $x$ in $(a,b)$.
```

## Example 1

The relative extrema are highlighted on the following graph. Observe how the relative extrema appear at points on the curve where the increasing/decreasing behavior of the function changes. 

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\usetikzlibrary{arrows}
\usetikzlibrary{arrows.meta}

\begin{document}

\begin{tikzpicture}[scale = 1.2]

  \draw[white,fill=white] (-1,-1) rectangle (12.5,7.5);
  \draw[->] (-0.5,0) -- (12,0) node[below] {$x$};
  \draw[->] (0,-0.5) -- (0,7) node[right] {$y$};
      
  % draw curve
  \draw [ultra thick] 
  (1,1) parabola bend (2.5,4) (4,2) 
  .. controls (5.5,5) and (7,2) .. (8.5,5) 
  parabola bend (10,3) (11.5,6);

  % draw points
  \draw [black,fill=red] (2.5,4) circle (2.5pt);
  \draw [black,fill=green] (4,2) circle (2.5pt);
  \draw [black,fill=red] (8.5,5) circle (2.5pt);
  \draw [black,fill=green] (10,3) circle (2.5pt);

  % label extrema
  \draw [<-, >=stealth', shorten <=3pt] (2.5,4) -- (3.25,6) node[right] {\bf \large Relative Maxima}; 
  \draw [<-, >=stealth', shorten <=3pt] (8.5,5) -- (7,6);
  \draw [<-, >=stealth', shorten <=3pt] (4,2) -- (5,1) node[right] {\bf \large Relative Minima}; 
  \draw [<-, >=stealth', shorten <=3pt] (10,3) -- (8.7,1);
\end{tikzpicture}
\end{document} 
```
```{dropdown} **Long Text Description**
There is a horizontal x axis. There is a vertical y axis. The graph of a function is plotted on these axes. Moving from left to right, the function goes up towards a rounded corner, which is marked in red and labeled a relative maximum, then goes downward towards a sharp corner, which is marked in green and labeled a relative minimum, then goes up again towards another sharp corner, which is marked in red and labeled a relative maximum, then goes down again towards a rounded corner, which is marked in green and labeled a relative minimum, and then goes upward.
```
In other words, relative extrema appear at points on the graph of the function where the derivative changes sign.

## How To Find Relative Extrema

The relative extrema of a function appear where $f'(x)$ changes from positive to negative or from negative to positive. Since $f'(x)$ changes sign when there is a relative extrema, it must be the case that either $f'(x)=0$ or $f'(x)$ does not exist at the relative extrema.

## Example 2

Compare the graphs of $f(x) = x^2 - 1$ and $f'(x) = 2x$.

:::::{grid}
::::{grid-item-card}
```{image} ../images/pic_optimization_relativeextrema_1.png
:alt: graph of $f(x) = x^2 - 1$
:height: 500px
:align: center
::::

::::{grid-item-card}
```{image} ../images/pic_optimization_relativeextrema_2.png
:alt: graph of $f'(x) = 2x$
:height: 500px
:align: center
```
::::
:::::

```{dropdown} **Long Text Description**
There are two sets of axes, in each a horizontal x axis and an unlabeled vertical axis.

On the left, the graph of the function x squared minus one is plotted. The function is concave up along its domain, is decreasing as it comes in from the left to a red dot at its rounded vertex at (0,-1), and increasing to the right of that.

On the right, the graph of it's derivative two x is plotted. It is linear increasing and passes through a red dot at the origin.
```
Observe that $f(x)$ has a relative minimum at $x=0$, $f'(0) = 0$, and $f'(x)$ changes sign (from negative to positive) at $x=0$.

## Example 3

Compare the graphs of $f(x) = x^3 + 1$ and $f'(x) = 3x^2$.

:::::{grid}
::::{grid-item-card}
```{image} ../images/pic_optimization_relativeextrema_3.png
:alt: graph of $f(x) = x^3 + 1$
:height: 500px
:align: center
::::

::::{grid-item-card}
```{image} ../images/pic_optimization_relativeextrema_4.png
:alt: graph of $f'(x) = 3x^2$
:height: 500px
:align: center
```
::::
:::::
```{dropdown} **Long Text Description**
There are two sets of axes, in each a horizontal x axis and an unlabeled vertical axis.

On the left, the graph of the function x cubed plus one is plotted. The function is increasing along its domain, is concave down as it comes in from the left to a red dot at a point of flatness at (0,1), and concave up to the right of that.

On the right, the graph of it's derivative three x squared is plotted. It is a concave up parabola which decreases on the left down to a red dot at its vertex (0,0), and then is increasing after that.
```
Observe that $f(x)$ does not have any relative extrema despite the fact that $f'(0) = 0$.  Notice that $f'(x)$ does not change sign at $x=0$. In other words, in order for a function to have a relative extrema, there must be a change in sign of its derivative.