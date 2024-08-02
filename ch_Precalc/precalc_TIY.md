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
````{admonition} Simplify
:class: tip

Rewrite $\dfrac{3}{x-1} - \dfrac{5}{2x+1}$ as a single ratio. 

```{dropdown} Show answer
Answer:  $\dfrac{x+8}{(x-1)(2x+1)}$
```
````

## Exercise 2
````{admonition} Expand
:class: tip

Expand $(8x+11)(2x-5)$ using the FOIL method. 

```{dropdown} Show answer
Answer: $16x^2 - 18x - 55$
```
````

## Exercise 3
````{admonition} Expand
:class: tip

Expand $5x^6(3x-4)^2$. 

```{dropdown} Show answer
Answer: $45x^8 - 120x^7 + 80x^6$
```
````

## Exercise 4
````{admonition} Expand
:class: tip

Expand $(1+3x)(1-3x)(2+x)$. 

```{dropdown} Show answer
Answer: $2 + x - 18x^2 - 9x^3$
```
````

## Exercise 5
````{admonition} Expand
:class: tip

Factor $4x^5 - 25x^3$. 

```{dropdown} Show answer
Answer:  $x^3(2x-5)(2x+5)$ (use difference of squares)
```
````

## Exercise 6
````{admonition} Simplify
:class: tip

Simplify 

$$\dfrac{2x^4 - 2x^3 -12x^2}{9x^2 - x^4}$$ 

by factoring both the numerator and the denominator.  Assume that $x\neq 0$ and $x\neq 3$. 

```{dropdown} Show answer
Answer: $-2(x+2)/(x+3)$
```
````


## Exercise 7
````{admonition} Factor and Simplify
:class: tip

Factor and simplify $10x(x+2)^5 - 5x^2(x+2)^3$. 

```{dropdown} Show answer
Answer: $5x(x+2)^3(2x^2+7x + 8)$
```
````

## Exercise 8
`````{admonition} Sketch a line
:class: tip

Sketch the graph of the line defined by $y = \dfrac{1}{4}(x-5) - 2$. Use the fact that the line is described in point-slope form.  

::::{grid} auto
:::{grid-item}
:margin: auto
```{image} ../images/pic_precalc_tiy_exercise_8.png
:alt: Grid
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -4, 4, 8, 12, and 16 marked. There is a vertical y-axis with the points -4, -2, and 2 marked. There is a grey grid of one unit by one unit cells in the background.
```
````{dropdown} Show answer
Answer: Line through the point $(5,-2)$ with a slope of $1/4$.  The line has an $x$-intercept at $x=13$ and a $y$-intercept at $y=-3.25$

::::{grid} auto
:::{grid-item}
:margin: auto
```{image} ../images/pic_precalc_tiy_exercise_8_answer.png
:alt: Graph of $y= \dfrac{1}{4}(x-5) - 2$
```
:::
::::
```{dropdown} Long Text Description
Graph of the line y = (x-5)/4 - 2.  The line crosses the y-axis at the point (0,-3.25) and crosses the x-axis at the point (13,0).
```
````
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
\begin{document}

\begin{tikzpicture}[scale=0.8]

\draw[black,fill=white] (-5.5,-6.5) rectangle (20.5,3.5);
\draw[very thin,color=lightgray,step=1] (-4.9,-5.9) grid (19.9,2.9);

      \draw[->] (-5,0) -- (20,0) node[below] {$x$};
      \draw[->] (0,-6) -- (0,3) node[right] {$y$};
%\draw[domain=-5:20,smooth,variable=\x,black,ultra thick,samples=100] plot ({\x},\x/4 - 13/4);
       
      % tick marks
\foreach \x in {-4,4,8,12,16} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {-4,-2,2} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {$\y$};

    \end{tikzpicture}
\end{document}
```
-->


## Exercise 9
````{admonition} Solve an inequality
:class: tip

Find all values of $x$ such that $x^2 - 16 > 0$.  Write your answer using interval notation. 

```{dropdown} Show answer
Answer: $(-\infty,-4) \cup (4,\infty)$
```
````


## Exercise 10
`````{admonition} Sketch a line
:class: tip

Sketch the graph of $f(x) = 12x^2 - x - 6$ by finding the $x$ and $y$-intercepts (see Graphing, {ref}`precalc:graphing:example6`).  

::::{grid} auto
:::{grid-item}
:margin: auto
```{image} ../images/pic_precalc_tiy_exercise_10.png
:alt: Graph of $y=\sqrt{x}$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -1 and 1 marked. There is a vertical y-axis with the points -8, -6, -4, -2, 2, 4, and 6 marked. There is a grey grid of one quarter unit by one unit cells in the background.
```

````{dropdown} Show answer
Answer: Parabola that opens upward and goes through the points $(0,-6)$, $(3/4,0)$, and $(-2/3,0)$.

::::{grid} auto
:::{grid-item}
:margin: auto
```{image} ../images/pic_precalc_tiy_exercise_10_answer.png
:alt: Graph of $y=\sqrt{x}$
```
:::
::::
```{dropdown} Long Text Description
The graph of the function y = 12 x squared - x - 6.  The graph is a parabola that opens up, crosses the x-axis at the points (-2/3,0) and (3/4,0), and crosses the y-axis at the point (0,-6).  
```
````
`````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[xscale=3,yscale=0.6]

\draw[black,fill=white] (-1.5,-8.6) rectangle (1.5,8.6);
\draw[very thin,color=lightgray,ystep=1,xstep=0.25] (-1.3,-7.9) grid (1.3,7.9);

      \draw[->] (-1.3,0) -- (1.3,0) node[below] {$x$};
      \draw[->] (0,-8) -- (0,8) node[right] {$y$};
%\draw[domain=-1:1,smooth,variable=\x,black,ultra thick,samples=100] plot ({\x},12*\x*\x-\x-6);
       
      % tick marks
\foreach \x in {-1,1} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {-8,-6,-4,-2,2,4,6} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {$\y$};

    \end{tikzpicture}
\end{document}
```
-->




## Exercise 11
````{admonition} Domain
:class: tip

Determine the domain of each of the following functions.  Write your answer using interval notation. 

1. $g(x) = \dfrac{x}{12x^2 - x - 6}$ <br><br>
2. $h(x) = \dfrac{x}{\sqrt{12x^2 - x - 6}}$ 

```{dropdown} Show answer
Answer: 1.) $(-\infty,-2/3) \cup (-2/3,3/4) \cup (3/4,\infty)$,  
2.) $(-\infty,-2/3) \cup (3/4,\infty)$
```
````
