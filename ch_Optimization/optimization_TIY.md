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
# Try It Yourself

## Exercise 1
````{admonition} Relative extrema
:class: tip

Find the $x$-coordinates of the relative extrema of $g(x) = 3x^2 + 5x +5$

```{dropdown} Show answer
Answer: rel. min. at $x=-5/6$
```
````


## Exercise 2
````{admonition} Relative extrema
:class: tip

Find the $x$-coordinates of the relative extrema of $f(x) = x^3 - 27x + 9$.

```{dropdown} Show answer
Answer: rel. max. at $x=-3$, rel. min. at $x=3$
```
````


## Exercise 3
````{admonition} Relative extrema
:class: tip

Find the $x$-coordinates of the relative extrema of $h(x) = x^2 + \dfrac{16}{x}$.

```{dropdown} Show answer
Answer: rel. min. at $x=2$
```
````


## Exercise 4
````{admonition} Absolute extrema
:class: tip

Find the absolute extrema of $g(x) = 2x^3 + 18x^2 + 48x + 17$ on the interval $[0,1]$.

```{dropdown} Show answer
Answer: abs. min. value is $17$, abs. max. value is $85$
```
````


## Exercise 5
````{admonition} Absolute extrema
:class: tip

Find the absolute extrema of $g(x) = 42x^3 + 33x^2 - 36x + 12$ on the interval $[0,1]$.

```{dropdown} Show answer
Answer: abs. min. value is $141/27$, abs. max. value is $51$
```
````


## Exercise 6
````{admonition} Absolute extrema
:class: tip

Find the absolute extrema of $f(x) = x + \dfrac{49}{x} + 9$ on the interval $[1,98]$.

```{dropdown} Show answer
Answer: abs. min. value is $23$, abs. max. value is $215/2$
```
````


## Exercise 7
````{admonition} Absolute extrema
:class: tip

Find the absolute extrema of $f(x) = \dfrac{7x}{x^2+9}$ on the interval $[0,9]$.

```{dropdown} Show answer
Answer: abs. min. value is $0$, abs. max. value is $7/6$
```
````

## Exercise 8
````{admonition} Maximize profit
:class: tip

A game box manufacturer determines that in order to sell $x$ units, the price per unit in dollars must be $p(x) = 250 - x$. The manufacture also determines that the total cost of producing $x$ units is given by $C(x) = 2500 + 10x$. How many units must the company produce and sell in order to maximize profit?

```{dropdown} Show answer
Answer: $120$ units
```
````


## Exercise 9
`````{admonition} Maximize area
:class: tip

A printer needs to make a poster that will have a total area of $200$ in$^2$ and will have $1$ inch margins on the sides, a $2.5$ inch margin on the top, and a $1.5$ inch margin on the bottom. Find the  dimensions of the poster that maximize the area of the printed (i.e., shaded) area?

::::{grid} auto
:::{grid-item}
:margin: auto
```{image} ../images/pic_optimization_tiy_exercise_9.png
:alt: Poster with margins$
```
:::
::::
```{dropdown} Long Text Description
There are two rectangles, one inside of the other. The smaller rectangle is colored in yellow, and the space inside the larger rectangle but outside the smaller is not colored. The length between the top of the yellow rectangle and the top of the larger one is labelled as 2.5 inches. The length between the left side of the yellow rectangle and the left side of the larger rectangle is labelled 1 inch. The length between the bottom of the yellow rectangle and the bottom of the larger rectangle is labelled as 1.5 inches.
```
```{dropdown} Show answer
Answer: width is $10$ in., height is $20$ in.
```
`````

<!--
```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\usetikzlibrary{arrows}
\usetikzlibrary{arrows.meta}

\begin{document}
\def\bbWidth{6}
\def\bbHeight{4.5}
\def\bbSideMargin{1.0}
\def\bbTopMargin{1.1}
\def\bbBottomMargin{0.9}
\begin{tikzpicture}[scale=1.4]
\draw [thick,fill=white] (0,0) rectangle (\bbWidth,\bbHeight);
\draw [thick,fill=yellow] (\bbSideMargin,\bbBottomMargin) rectangle (\bbWidth - \bbSideMargin, \bbHeight - \bbTopMargin);
%\draw [<->] (0,\bbHeight + 0.25) -- +(\bbWidth,0) node [midway,fill=white] {$x$};
\draw [<-] (0,\bbHeight/2) -- +(-0.5,0); 
\draw [<-] (\bbSideMargin,\bbHeight/2) -- +(0.5,0);
\node at (\bbSideMargin/2,\bbHeight/2) {\large 1 in.};

\draw [<-] (\bbWidth - \bbSideMargin,\bbHeight/2) -- +(-0.5,0); 
\draw [<-] (\bbWidth,\bbHeight/2) -- +(0.5,0);
\node at (\bbWidth - \bbSideMargin/2,\bbHeight/2) {\small 1 in.};

\draw [<->] (\bbWidth/2,\bbHeight) -- +(0,-\bbTopMargin) node [midway,fill=white] {\large 2.5 in.};

\draw [<->] (\bbWidth/2,0) -- +(0,\bbBottomMargin) node [midway,fill=white] {\large 1.5 in.};
\end{tikzpicture}
\end{document}
```
-->


