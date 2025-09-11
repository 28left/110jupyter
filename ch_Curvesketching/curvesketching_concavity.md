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
# Intervals of Concavity

## Definitions

```{admonition} Definition
:class: info

A function is _**concave up**_ on an interval if its derivative is increasing on the interval.

The graph of a function that is concave up on an interval will resemble a portion of a parabola that opens up on that interval.
```




```{admonition} Definition
:class: info

A function is _**concave down**_ on an interval if its derivative is decreasing on the interval.

The graph of a function that is concave down on an interval will resemble a portion of a parabola that opens down on that interval.
```

```{admonition} What the Sign of $f''$ Tells Us About $f$.
:class: important

- If $f''(x) > 0$ for all $x$ on the interval $(a,b)$, then $f$ is concave up on $(a,b)$.
- If $f''(x) < 0$ for all $x$ on the interval $(a,b)$, then $f$ is concave down on $(a,b)$.

```



### Example 1

````{admonition} Finding intervals of concavity from the graph of a function
:class: tip

The following is the graph of a continuous function that is concave down on the interval $(1,4)$ and concave up on the interval $(4,7)$.  

Notice how the graph resembles a parabola that opens down on the interval $(1,4)$ and resembles a parabola that opens up on the interval $(4,7)$.


::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_curvesketching_concavity_example_1.png
:alt: Graph of generic function
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points 1, 2, 3, 4, 5, 6, and 7 marked. There is a vertical y-axis. The graph of a function is plotted on these axes. Reading from left to right, the function goes up at a slowing pace, reaches a rounded corner, decreases at an accelerating pace, decreases at a slowing pace, reaches another rounded corner, and goes upward at an accelerating pace.
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
\begin{tikzpicture}[xscale = 2,yscale=1.5]
\draw[white,fill=white] (0,0) rectangle (3,4);
 \draw[very thin,color=darkgray,step=1.0] (0,0) grid (8,4);
 \draw[very thin,color=lightgray,step=0.25] (0,0) grid (8,4);

\draw[->] (0,0) -- (8,0) node[below] {$x$};
\draw[->] (0,0) -- (0,4) node[right] {$y$};
     
% draw curve
\draw [ultra thick,smooth,variable=\x] plot [domain=1:7] (\x,{0.2*(pow(\x-4,3)) - 1.5*(\x-4) + 2});

% tick marks
\foreach \x in {1,...,7} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};

\end{tikzpicture}
\end{document}
```
-->



### Example 2

````{admonition} Finding intervals of concavity using the graph of the derivative
:class: tip

The following graph corresponds to $f'(x)$, the first derivative of $f(x)$.  

Using the graph of $f'(x)$, determine the intervals of concavity of $f(x)$.  You may assume that $f'(x)$ is continuous for all $x$ and that $f'(x)$ has relative extrema only at $x = -1$, $x = 1$, and $x = 4$.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_curvesketching_concavity_example_2.png
:alt: Graph of the derivative of a function
```
:::
::::
``` {dropdown} Long Text Description
There is a horizontal x-axis with the points -2, -1, 1, 2, 3, 4 and 5 marked. There is a vertical y-axis with no points marked. The graph of a continuous function is plotted here. The function is decreasing for x < -1, increasing for -1 < x < 1, decreasing for 1 < x < 4, and increasing for x > 4.
```



```{dropdown} **Step 1:** &nbsp;  Use the graph to determine the intervals of increase/decrease of $f'$.

Since we were given that the only relative extrema of $f'$ are at $x = -1$, $x = 1$, and $x = 4$, we can assume these are the only places where the increasing/decreasing behavior of $f'$ changes.  In other words, we only have to determine the behavior of $f'$ on each of the following intervals:

$$(-\infty,-1), ~(-1,1), ~(1,4) ~\hbox{ and }~  (4,\infty)$$

Using the given graph of the first derivative, we have that 

$f'$ is decreasing on $(-\infty,-1)$,

$f'$ is increasing on $(-1,1)$,

$f'$ is decreasing on $(1,4)$, and

$f'$ is increasing on $(4,\infty)$.

```


```{dropdown} **Step 2:** &nbsp;  Determine the intervals of concavity of $f$.

Recall that $f$ is concave up on intervals where $f'$ is increasing and concave down on intervals where $f'$ is decreasing.

Therefore, $f$ is concave up on $(-1,1) \cup (4,\infty)$ and concave down on $(-\infty,-1) \cup (1,4)$.
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
\begin{tikzpicture}[baseline=70,ultra thick,smooth,domain=-4:4,variable=\x,scale=1.5]

% create a white background with a black frame
\draw [white,thin,fill=white] (-3,-2) rectangle (4,4);  

% draw grid
\draw[xstep=0.5cm, ystep=0.5cm, lightgray, thin] (-2.99,-0.99) grid (5.99,2.99); 

% draw axes
\draw [->,thick] (-3,0) -- (6,0)  node[below] {$x$};
\draw [->,thick] (0,-1) -- (0,3)  node[right] {$y$};;


\clip (-3,-1) rectangle (6,3);

%
\draw plot [domain=-3:6] (\x,{((\x)*(\x)*(\x)*(\x)/4 - 4*(\x)*(\x)*(\x)/3 - (\x)*(\x)/2 + 4*(\x))/10 + 0.5}); 


\draw [black,ultra thick] (5,2.5) node [above,align=center] {$y=f'(x)$};


% tick marks
\foreach \x in {-2,-1,1,2,3,4,5} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below, scale=1.5] {$\x$};

\end{tikzpicture}
```
-->


## Finding Intervals of Concavity using the Second Derivative

```{admonition} How to Find Intervals of Concavity of a Function
:class: info

- Find all values of $x$ such that $f''(x) = 0$ or $f''(x)$ does not exist.
- Break up domain of $f$ into open intervals between values found in Step 1. 
- Evaluate $f''(x)$ at one value, $c$, from each interval, $(a,b)$, found in Step 2.
    - If $f''(c) > 0$, then $f$ is concave up on $(a,b)$.
    - If $f''(c) < 0$, then $f$ is concave down on $(a,b)$.
```


### Example 3

````{admonition} Finding intervals of concavity using the graph of the second derivative
:class: tip

The following graph corresponds to $f''(x)$, the second derivative of $f(x)$.  

Using the graph of $f''(x)$, determine the intervals of concavity of $f(x)$.  You may assume that $f''(x)$ is continuous for all $x$ and $f''(x) = 0$ only when $x = -2$ and $x = 1$.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_curvesketching_concavity_example_3.png
:alt: Graph of the second derivative of a function
```
:::
::::
``` {dropdown} Long Text Description
There is a horizontal x-axis with the points -4, -3, -2, -1, 1, and 2 marked. There is a vertical y-axis with no points marked. The graph of a continuous function is plotted here. The graph of the function touches the x-axis at x = -2 and at x = 1.  The graph is above the x-axis for x < - 2 and for -2 < x < 1.  The graph is below the x-axis for x > 1.
```




```{dropdown} **Step 1:** &nbsp; Find all values of &nbsp; $x$ &nbsp; such that &nbsp; $f''(x) = 0$.

We were given that $f''(x) = 0$ only when $x = -2$ and when $x = 1$.
```

```{dropdown} **Step 2:**  &nbsp;  Find all values of &nbsp; $x$ &nbsp; such that &nbsp; $f''(x)$ &nbsp; does not exist.

Notice that $f''(x)$ is defined for all real numbers since we were told that $f''(x)$ is continuous for all $x$.
```


```{dropdown} **Step 3:** &nbsp;  Break up the domain of &nbsp; $f$ &nbsp; into subintervals.

Break up the domain of &nbsp; $f$ &nbsp; into subintervals based on the values found in Steps 1 and 2.

Since we found $x=-2$ and $x=1$ to be the only values where $f''(x) = 0$ or where $f''(x)$ is not defined, we break up the domain of $f$ (which is $(-\infty,\infty)$) into the following subintervals:

$$(-\infty,-2), ~(-2,1), ~\hbox{ and }~  (1,\infty)$$
```


```{dropdown} **Step 4:** &nbsp;  Use the graph to determine the sign of $f''(x)$ on each interval.

$\mathbf{(-\infty,-2)}$: Since the graph of $f''(x)$ is above the $x$-axis on this interval, $f''(x) > 0$ for all $x$ on $(-\infty,-2)$.

$\mathbf{(-2,1)}$: Since the graph of $f''(x)$ is above the $x$-axis on this interval, $f''(x) > 0$ for all $x$ on $(-2,1)$.

$\mathbf{(1,\infty)}$: Since the graph of $f''(x)$ is below the $x$-axis on this interval, $f''(x) < 0$ for all $x$ on $(1,\infty)$.

```


```{dropdown} **Step 5:** &nbsp;  Use the sign of $f''$ to determine the intervals of concavity of $f$ .

Recall that $f(x)$ is concave up on intervals where $f''(x) > 0$ and concave down on intervals where $f''(x) < 0$.

Therefore, $f(x)$ is concave up on $(-\infty,-2) \cup (-2,1)$ and concave down on $(1,\infty)$.
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
\begin{tikzpicture}[baseline=70,ultra thick,smooth,domain=-4:4,variable=\x,scale=1.5]

% create a white background with a black frame
\draw [white,thin,fill=white] (-3,-2) rectangle (4,4);  

% draw grid
\draw[xstep=0.5cm, ystep=0.5cm, lightgray, thin] (-4.99,-2.99) grid (2.99,2.99); 

% draw axes
\draw [->,thick] (-5,0) -- (3,0)  node[below] {$x$};
\draw [->,thick] (0,-3) -- (0,3)  node[right] {$y$};;


\clip (-5,-3) rectangle (3,3);

%
\draw plot [domain=-5:3] (\x,{((\x+2)*(\x+2)*(1-\x))/10 }); 


\draw [black,ultra thick] (-3.3,2.5) node [above,align=center] {$y=f''(x)$};


% tick marks
\foreach \x in {-4,-3,-2,-1,1,2} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below, scale=1.5] {$\x$};

\end{tikzpicture}
```
-->


### Example 4

`````{admonition} Finding intervals of concavity
:class: tip

If the second derivative of $f(x)$ is 

$$\displaystyle f''(x) = \frac{x^2-4x}{x-6}$$ 

find the intervals  of concavity of $f$.


```{dropdown} **Step 1:** &nbsp; Find all values of &nbsp; $x$ &nbsp; such that &nbsp; $f''(x) = 0$.

\begin{align*}
f''(x) &= \frac{x(x-4)}{x-6}
\end{align*}

which equals zero when $x=0$ and $x=4$.
```


```{dropdown} **Step 2:** &nbsp; Find all values of &nbsp; $x$ &nbsp; such that &nbsp; $f''(x)$ &nbsp; does not exist.

$f''(x)$ does not exist when $x=6$.
```


````{dropdown} **Step 3:** &nbsp; Perform an interval sign analysis for &nbsp; $f''$.

Break up the domain of $f$ at each value found in Steps 1 and 2. Plug one number from each subinterval into $f''(x)$ to determine the sign of $f''(x)$ on each interval.

\begin{align*}
f''(-1) &= \frac{(-1)(-1-4)}{-1-6} < 0\\ 
f''(1) &= \frac{(1)(1-4)}{1-6} >0\\
f''(5) &= \frac{(5)(5-4)}{5-6} <0\\
f''(7) &= \frac{(7)(7-4)}{7-6} >0
\end{align*}

```{figure} ../images/pic_curvesketching_concavity.png
---
name: pic_curvesketching_concavity
width: 600px
---
Interval analysis of $f''(x) = \frac{x(x-4)}{x-6}$.
```
```{dropdown} Long Text Description
A number line with positive and negative signs assigned to intervals, which are negative to the left of zero, positive from zero to four, negative from four to six, and positive to the right of six.
```

Therefore, $f$ is concave up on the intervals $(0,4)$ and $(6,\infty)$ and concave down on the intervals $(-\infty,0)$ and $(4,6)$.
````
`````
