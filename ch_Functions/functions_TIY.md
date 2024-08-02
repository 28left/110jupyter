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
````{admonition} Domain
:class: tip

Let $f(x) = \dfrac{x - 1}{2x - 6}$ and $g(x) = \sqrt{2x + 1}$.  

Determine the domain for $f+g$, $f-g$, $fg$, and $f/g$.

```{dropdown} Show answer
Answer: Domain for $f+g$, $f-g$, $fg$: $[-1/2,3) \cup (3,\infty)$; Domain for $f/g$: $(-1/2,3) \cup (3,\infty)$
```
````


## Exercise 2
````{admonition} Composition of functions
:class: tip

Let $f(x) = 3\sqrt{x}$ and $g(x) = \dfrac{x}{2x-1}$.  

Determine the rule for the composite functions $f \circ g$ and $g \circ f$. 

```{dropdown} Show answer
Answer: $(f\circ g)(x) = 3\sqrt{x/(2x-1)}$; $(g\circ f)(x) = 3\sqrt{x}/(6\sqrt{x}-1)$
```
````


## Exercise 3
````{admonition} Break-even point
:class: tip

A manufacturer of Everlasting LED lightbulbs has fixed monthly costs of \$25,000 and a processing cost of \$3 for each lightbulb produced. Assuming each lightbulb sells for \$5, compute the break-even point.

```{dropdown} Show answer
Answer: 12,500 lightbulbs
```
````


## Exercise 4
````{admonition} Degree of a polynomial
:class: tip

Determine the degree of the polynomial $(x^4 + x)^2(x^3 + x + 1)^5$.

```{dropdown} Show answer
Answer: $23$
```
````


## Exercise 5
````{admonition} Rational function
:class: tip

Write $\dfrac{x}{x^2-4} - \dfrac{2x+1}{x+5}$ as a ratio of polynomials and determine its domain.

```{dropdown} Show answer
Answer: $(-2x^3 + 13x + 4)/(x^3 + 5x^2 - 4x - 20)$, Domain: $(-\infty,-5) \cup (-5,-2) \cup (-2,2) \cup (2,\infty)$
```
````


## Exercise 6
````{admonition} Equilibrium point
:class: tip

The demand and supply functions for *The Best of Math 110: A DVD Collection* are: 

\begin{align*}
p = d(x) &= -x^2 - 2x + 100\\
p = s(x) &= 2x^2 + 4x - 140
\end{align*}

where $x$ is the number of thousands of DVDs and $p$ is in dollars.  Determine the market equilibrium values.

```{dropdown} Show answer
Answer: Equilibrium quantity = 8000; Equilibrium price = \$20
```
````


## Exercise 7
````{admonition} Area of rectangular region enclosed by a fence
:class: tip

A rectangular field is to be enclosed by 200 feet of fence. One side of the field is a building, so fencing is not required on that side.

::::{grid} auto
:::{grid-item}
:margin: auto
```{image} ../images/pic_functions_tiy_exercise_7.png
:alt: Rectangular region enclosed by a fence on three sides
```
:::
::::
```{dropdown} Long Text Description
There is a thick black line representing the side of a building. Above this is a yellow rectangle representing the area enclosed by a fence. The height of this rectangle is marked as x.
```
If $x$ denotes the length of one side of the rectangle perpendicular to the building, determine the function in the variable $x$ giving the area (in square feet) of the fenced-in region and state the appropriate domain.


```{dropdown} Show answer
Answer: Area: $200x - 2x^2$, Domain: $[0,100]$
```
````

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
\begin{tikzpicture}[scale = 8]
\draw[fill = yellow,opacity=0.5] (0,0) rectangle (1,.5);
\draw[ultra thick] (-.2,0)--(1.2,0) node[midway,below] {Building};
\draw (0,0) -- (0,0.5) node[midway,left] {$x$} 
-- (1,0.5) %node[midway,above] {} 
-- (1,0) node[midway,right] {$x$};
\node at (.5,.25) {Fenced Area};
\end{tikzpicture}
\end{document}
```
-->

## Exercise 8
````{admonition} Profit function
:class: tip

A game box manufacturer determines that in order to sell $x$ units, the price per unit in dollars must be $p(x) = 250 - x$. The manufacture also determines that the total cost of producing $x$ units is given by $C(x) = 2500 + 10x$.  Determine the profit as a function of $x$ and state the appropriate domain.

```{dropdown} Show answer
Answer: Profit: $240x - x^2 - 2500$, Domain: $[0,250]$
```
````


## Exercise 9
````{admonition} Area of printed region
:class: tip

A printer needs to make a poster that has a total area of $200$ in$^2$, $1$ inch margins on the sides, a $2.5$ inch margin on the top, and a $1.5$ inch margin on the bottom.  If $x$ denotes the width (in inches) of the poster, find a function in the variable $x$ giving the area of the printed (i.e., shaded) region and state the appropriate domain.

::::{grid} auto
:::{grid-item}
:margin: auto
```{image} ../images/pic_functions_tiy_exercise_9.png
:alt: Poster with margins
```
:::
::::
```{dropdown} Long Text Description
There is a large white rectangle, representing the total area of a poster. There is a yellow rectangle inside the larger one, representing the area that may be printed on to give the required margins. The distance between the tops of the rectangles is marked as 2.5 inches. The distance between the corresponding sides of the two rectangles is given as 1 inch. The distance between the bottoms of both rectangles is given as 1.5 inches. The width of the white rectangle is given as x.
```

```{dropdown} Show answer
Answer: Area: $(x-2)(200/x-4)$, Domain: $[2,50]$
```
````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\def\bbWidth{6}
\def\bbHeight{4.5}
\def\bbSideMargin{1.0}
\def\bbTopMargin{1.1}
\def\bbBottomMargin{0.9}
\begin{tikzpicture}[scale=1.3]
\draw [thick,fill=white] (0,0) rectangle (\bbWidth,\bbHeight);
\draw [thick,fill=yellow,opacity=0.5] (\bbSideMargin,\bbBottomMargin) rectangle (\bbWidth - \bbSideMargin, \bbHeight - \bbTopMargin);
%\draw [<->] (0,\bbHeight + 0.25) -- +(\bbWidth,0) node [midway,fill=white] {$x$};
\draw [<-] (0,\bbHeight/2) -- +(-0.5,0); 
\draw [<-] (\bbSideMargin,\bbHeight/2) -- +(0.5,0);
\node at (\bbSideMargin/2,\bbHeight/2) {\small 1 in.};
\draw [<->] (\bbWidth/2,\bbHeight) -- +(0,-\bbTopMargin) node [midway,fill=white] {\small 2.5 in.};
\draw [<->] (\bbWidth/2,0) -- +(0,\bbBottomMargin) node [midway,fill=white] {\small 1.5 in.};

%label
\draw [|-|] (0,-0.4) -- (\bbWidth,-0.4) node [midway,fill=white] {$x$};
\end{tikzpicture}
\end{document}
```
-->

