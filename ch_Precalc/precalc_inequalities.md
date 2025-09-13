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
(solving_inequalities)=
# Solving Inequalities

## How to Solve an Inequality


```{admonition} Solving an Inequality
:class: info

In order to find all values of $x$ such that $f(x)>0$ or $f(x)<0$, use the following procedure.

- **Step 1:** Find all values of $x$ such that $f(x) = 0$ or $f(x)$ is not defined.
- **Step 2:** Use one of the following two methods to solve the inequality
	- **Method 1:** Use the values found to break up the number line into intervals and select one number from each interval to plug into $f(x)$ to determine if $f(x)$ is positive or negative on that interval.
	- **Method 2:** Use the values found to help draw the graph of $f(x)$.  Portions of the graph that are above the $x$-axis correspond to values of $x$ where $f(x)>0$ while portions of the graph that are below the $x$-axis correspond to values of $x$ where $f(x) < 0$.
```

(01_05_example1)=
### Example 1

``````{admonition} Determine the values of $x$ where $f(x)$ is positive.
:class: tip

Find all values of $x$ such that $x^2 + 2x - 3 > 0$.


```{dropdown} **Step 1:** &nbsp; Find all values of &nbsp; $x$ &nbsp; such that &nbsp; $x^2 + 2x - 3 = 0$.

Use the AC method to factor $x^2 + 2x - 3$.

$$ x^2 + 2x - 3 = (x+3)(x-1)  $$

since $3$ and $-1$ are two numbers that multiply to $-3$ and sum to $2$.  Now set each factor equal to zero and solve for $x$.

\begin{align*}
x + 3 = 0 ~~~~&\Rightarrow~~~~ x = -3 \\
x - 1 = 0 ~~~~&\Rightarrow~~~~ x = 1 
\end{align*}

Note that $x^2 + 2x - 3$ is defined for all values of $x$.
```

`````{dropdown} **Step 2:** &nbsp; Use one of the two methods to solve the inequality. 


````{dropdown} Method 1: Break up the number line

- Use the values of $x$ found in **Step 1** to break up the number line and plug in one value from each interval into $f(x) = (x+3)(x-1)$. <br><br>

- Since $f(-3) = 0$ and $f(1) = 0$, pick one value less $-3$, one value between $-3$ and $1$, and one value greater than $1$.  <br><br> For example, since $f(-4) = 5 > 0$, $f(x) >0 $ for all $x < -3$.  And since $f(2) = 5 > 0$, $f(x)>0$ for all $x > 1$.  However, $f(0) = -3 < 0$, and therefore $f(x) < 0$ for all $-3<x<1$. 


The calculations of Method 1 are summarized in the following diagram.

```{image} ../images/pic_precalc_inequalities_example_1_1.png
---
alt: Sign of $f(x)$
align: center
---
```

```{dropdown} Long Text Description
There is a number line with the numbers -4, -3, 0, 1, and 2 marked. The line is labeled "sign of f(x)". Some of the points are marked with signs. -4 is marked positive. Zero is marked negative. 2 is marked positive. The rest of the numbers are not marked with a sign.
```
Therefore, $x^2+2x-3 >0$ whenever $x<-3$ or $x>1$.

````


````{dropdown} Method 2: Draw a graph

Sketch the graph of $y=x^2+2x-3$ by drawing a parabola that opens upward and goes through the points $(-3,0)$ and $(1,0)$.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_inequalities_example_1_2.png
:alt: Graph of $y=x^2+2x-3$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -4, -2, and 2 marked. There is a vertical y-axis with no points marked. The graph of the concave up parabola y = x squared + 2x - 3. Its x-intercepts are marked with large black dots.
```

Finding values of $x$ such that $x^2+2x-3 > 0$ is equivalent to identifying the portions of the graph of $x^2+2x-3$ that are above the $x$-axis.  

Based on the graph shown above, $x^2+2x-3 >0$ whenever $x<-3$ or $x>1$.

````
`````
``````



```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```
<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1]
\draw[white,fill=white] (-9.5,-1) rectangle (4,1);
\draw[->](-6,0) -- (4,0) ;
\foreach \x in {-3, 1}
	\draw (\x, 6pt) -- (\x, -6pt) node[below, scale=1.5] {$\x$};
	
\node[above, scale=1.5] at (-4,0){$+$};
\node[above, scale=1.5] at (0,0){$-$};
\node[above, scale=1.5] at (2,0){$+$};

	\draw (-4, 3pt) -- (-4, -3pt) node[below, scale=1.5] {$-4$} ;
	\draw (0, 3pt) -- (0, -3pt) node[below, scale=1.5] {$0$} ;
	\draw (2, 3pt) -- (2, -3pt) node[below, scale=1.5] {$2$} ;

\node[left, scale=1.5] at (-6,0.5){sign of $f(x)$};
\end{tikzpicture} 
\end{document}
```
-->


<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin {document}
\begin{tikzpicture}[xscale=1,yscale=0.6]

\draw[white,fill=white] (-5.3,-5.3) rectangle (3.3,5.3);
%\draw[very thin,color=lightgray,step=1] (-4.9,-4.9) grid (2.9,4.9);

\draw[->] (-5,0) -- (3,0) node[below] {$x$};
\draw[->] (0,-5) -- (0,5) node[right] {$y$};
       
\draw [fill=black] (-3,0) ellipse [x radius = 0.15, y radius = 0.25];
\draw [fill=black] (1,0) ellipse [x radius = 0.15, y radius = 0.25];

% tick marks
\foreach \x in {-4,-2,2} 
	\draw [thick] (\x cm,6pt) -- (\x cm,-6pt) node[below] {$\x$};
\foreach \y in {} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};
	
\clip (-6,-5) rectangle (6,5);
\draw[domain=-4:2,smooth,variable=\x,black,ultra thick] plot ({\x},{\x*\x + 2*\x - 3}); 
%\node at (4.1, 4.5){$y = x^2 + 2x - 3$};
\end{tikzpicture}
\end{document}
```
-->




````{admonition} Video Resource
:class: important

::::{grid} 2
:::{grid-item}
:columns: 1
:padding: 1
```{image} ../images/UnderstandTheMath.png
:alt: UnderstandTheMath
```
:::
:::{grid-item}
:columns: 10
<a href="https://youtu.be/054oO_M1018" target="_blank">Solving Quadratic Inequalities</a> (Links to an external site) <br>
Several more examples of solving inequalities involving quadratic functions.
:::
::::
````




### Example 2

``````{admonition} Determine the values of $x$ where $f(x)$ is negative.
:class: tip

Find all values of $x$ such that $\dfrac{x^2(x^2+3)}{(4-x^2)^3} < 0$.



```{dropdown} **Step 1:** &nbsp; Find all &nbsp; $x$ &nbsp; such that &nbsp; $\frac{x^2(x^2+3)}{(4-x^2)^3} = 0$ &nbsp; or is not defined. 

$\frac{x^2(x^2+3)}{(4-x^2)^3} = 0$ whenever the numerator is equal to zero, which only happens when $x=0$ (since $x^2+3$ is never equal to zero).

$\frac{x^2(x^2+3)}{(4-x^2)^3}$ is not defined whenever the denominator is equal to zero, which only happens when $x=-2$ or $x=2$.
```




`````{dropdown} **Step 2:** &nbsp; Use one of the two methods to solve the inequality. 


````{dropdown} Method 1: Break up the number line

Break up the number line at $x=-2$, $x=0$, and $x=2$ and plug in one value from each interval to determine the sign of $f(x) = \frac{x^2(x^2+3)}{(4-x^2)^3}$ on that interval.


The calculations of Method 1 are summarized in the following diagram.

```{image} ../images/pic_precalc_inequalities_example_2_1.png
---
alt: Sign of $f(x)$
align: center
---
```

```{dropdown} Long Text Description
There is a number line with the numbers -3, -2, -1, 0, 1, 2, and 3 marked. The sign of f(x) is denoted at several points along the line, and is negative at the point -3, positive at the point -1, positive at the point 1, and negative at the point 3.
```
Therefore, $\frac{x^2(x^2+3)}{(4-x^2)^3} < 0$ when $x<-2$ or $x>2$.

````


````{dropdown} Method 2: Draw a graph

Notice that $x^2$ and $x^2+3$ are both positive for $x\neq 0$, therefore $\frac{x^2(x^2+3)}{(4-x^2)^3}<0$ whenever $4-x^2 < 0$.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_inequalities_example_2_2.png
:alt: Graph of $y=4-x^2$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -3, -1, 1, and 3 marked. There is a vertical y-axis with no points marked. The graph of the concave down quadratic function four minus x squared is plotted on these axes, with its x-intercepts at (-2,0) and (2,0) marked with large black dots.
```
The graph of $y = 4-x^2$ as shown above is below the $x$-axis (i.e., $4-x^2 < 0$) if $x<-2$ or $x>2$.  Therefore, $\frac{x^2(x^2+3)}{(4-x^2)^3} < 0$ when $x<-2$ or $x>2$.

````
`````
``````


<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin {document}
\begin{tikzpicture}[scale=1.5]
\draw[white,fill=white] (-6.5,-0.6) rectangle (4,0.6);
\draw[->](-4,0) -- (4,0) ;
\foreach \x in {-2,0,2}
	\draw (\x, 3pt) -- (\x, -3pt) node[below, scale=1.5] {$\x$} ;
	
\node[above, scale=1.5] at (-3,0){$-$};
\node[above, scale=1.5] at (-1,0){$+$};
\node[above, scale=1.5] at (1,0){$+$} ;
\node[above, scale=1.5] at (3,0){$-$} ;

	\draw (-3, 2pt) -- (-3, -2pt) node[below, scale=1.5] {$-3$} ;
	\draw (-1, 2pt) -- (-1, -2pt) node[below, scale=1.5] { $-1$} ;
	\draw (1, 2pt) -- (1, -2pt) node[below, scale=1.5] { $1$} ;
	\draw (3, 2pt) -- (3, -2pt) node[below, scale=1.5] {$3$} ;

\node[left, scale=1.5] at (-4,0.25){sign of $f(x)$};

\end{tikzpicture} 
\end{document}
```
-->


<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin {document}
\begin{tikzpicture}[xscale=1,yscale=0.6]

\draw[white,fill=white] (-4.3,-5.3) rectangle (4.3,5.3);
%\draw[very thin,color=lightgray,step=1] (-4.9,-4.9) grid (2.9,4.9);

\draw[->] (-4,0) -- (4,0) node[below] {$x$};
\draw[->] (0,-5) -- (0,5) node[right] {$y$};
       
\draw [fill=black] (-2,0) ellipse [x radius = 0.15, y radius = 0.25];
\draw [fill=black] (2,0) ellipse [x radius = 0.15, y radius = 0.25];

% tick marks
\foreach \x in {-3,-1,1,3} 
	\draw [thick] (\x cm,6pt) -- (\x cm,-6pt) node[below] {$\x$};
\foreach \y in {} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};
	
\clip (-6,-5) rectangle (6,5);
\draw[domain=-3:3,smooth,variable=\x,black,ultra thick] plot ({\x},{4 - \x*\x}); 
%\node at (4.1, 4.5){$y = x^2 + 2x - 3$};
\end{tikzpicture}
\end{document}
```
-->

