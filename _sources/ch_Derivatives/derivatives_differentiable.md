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
# Differentiability

## Definition

```{admonition} Definition
:class: info

The function $f(x)$ is _**differentiable at $x = a$**_ if the following limit exists.

$$\lim_{h\to 0} \frac{f(a+h) - f(a)}{h}$$

Intuitively, $f(x)$ is differentiable at $x=a$ if we can zoom in on the graph of $y=f(x)$ at the point $(a,f(a))$ until the graph looks like a single uninterrupted straight line.
```


```{admonition} Differentiability versus Continuity
:class: warning

If a function is differentiable at $x=a$, then it is continuous at $x=a$. This also means that if a function is **not** continuous at $x=a$, then it is automatically **not** differentiable at $x=a$.

However, if a function is continuous at $x=a$, then it **is not necessarily** differentiable at $x=a$.
```


### Example 1

````{admonition} Continuous and differentiable
:class: tip 

The function defined by the following graph is continuous and differentiable at every point on the graph.  

Intuitively, the graph can be drawn without picking up a pencil from the paper (i.e., it's continuous) and we can zoom in close enough to any point on the graph so that the graph looks like a straight line (i.e., it's differentiable).

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_derivatives_differentiable_example_1.png
:alt: Graph of a function that is continuous and differentiable
```
:::
::::
```{dropdown} Long Text Description
The graph of a continuous function that increases before x = -1, decreases between x=-1 and x=1, and then increases after x=1.  The graph does not have any sharp corners or vertical tangent lines.
```
````

<!--
\begin{tikzpicture}[scale=2]

\draw[black,fill=white] (-2.55,-1.1) rectangle (2.8,4.2);
\draw[very thin,color=lightgray,step=1] (-2.35,-0.9) grid (2.6,3.9);

\draw[->] (-2.35,0) -- (2.6,0) node[below] {$x$};
\draw[->] (0,-1) -- (0,4) node[right] {$y$};

\draw[domain=-2.35:2.55,smooth,variable=\x,blue,ultra thick,samples=100] plot ({\x},\x^3/3 - \x + 1);
       
% tick marks
\foreach \x in {-2,-1,1,2} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {1,2,3} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {$\y$};

\end{tikzpicture}
-->

(der:diff_example_2)=
### Example 2

````{admonition} Continuous but not differentiable at a point
:class: tip 

The functions defined by the following two graphs are continuous at every point on the graph.  However, both functions are not differentiable at $x=1$.  

For the graph on the left, the function is not differentiable at $x=1$ since there is a sharp corner on the graph at $x=1$ (i.e., $f'(1)$ does not exist).  The function is differentiable everywhere else.

For the graph on the right, the function is not differentiable at $x=1$ since it has a vertical tangent line at $x=1$ and vertical lines do not have a slope associated with them (i.e., $f'(1)$ does not exist).  The function is differentiable everywhere else.


::::{grid} 2
:::{grid-item-card}
:columns: 5
:margin: 0 0 4 4
```{image} ../images/pic_derivatives_differentiable_example_2.png
:alt: Graph of a function that is continuous and but not differentiable at a point
:align: center
```
:::

:::{grid-item-card}
:columns: 5
```{image} ../images/pic_derivatives_differentiable_example_2_2.png
:alt: Graph of a function that is continuous and but not differentiable at a point
:align: center
```
:::
::::


```{dropdown} Long Text Description
There are two graphs displayed.  The first graph corresponds to a function that increases linearly with a slope of postive 1 to the point (1,3) where it reaches a corner and then decreases linearly with a slope of -1. 

The second graph corresponds to a function that increases from left to right.  The curve becomes increaseingly steep as x approaches 1 from the left and ultimately becomes vertical at x = 1.  The curve continues to increase for x greater than 1 but flattens out as x increases.
```
````

<!--
\begin{tikzpicture}[scale=1.5]

\draw[black,fill=white] (-2.6,-1.6) rectangle (4.7,3.7);
\draw[very thin,color=lightgray,step=1] (-2.5,-1.5) grid (4.5,3.5);
%\draw[very thin,color=gray,step=2] (-3.5,-5) grid (3.5,1);

\draw[->] (-2.5,0) -- (4.5,0) node[below] {$x$};
\draw[->] (0,-1.5) -- (0,3.5) node[right] {$y$};
       
%s\node[right] at (0.9, -0.5){$y = x^2-4$};

% tick marks
\foreach \x in {-2,-1,1,2,3,4} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {-1,1,2,3} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};

%\draw[domain=-2.1:4.1,smooth,variable=\x,blue,ultra thick] plot ({\x},{3 - abs(\x-1)});

\draw[blue,ultra thick] (-2.5,-0.5) -- (1,3) -- (4.5,-0.5);

\end{tikzpicture}


\begin{tikzpicture}[scale=1.5]

\draw[black,fill=white] (-2.6,-1.6) rectangle (4.7,3.7);
\draw[very thin,color=lightgray,step=1] (-2.5,-1.5) grid (4.5,3.5);
%\draw[very thin,color=gray,step=2] (-3.5,-5) grid (3.5,1);

\draw[->] (-2.5,0) -- (4.5,0) node[below] {$x$};
\draw[->] (0,-1.5) -- (0,3.5) node[right] {$y$};
       
%s\node[right] at (0.9, -0.5){$y = x^2-4$};

% tick marks
\foreach \x in {-2,-1,1,2,3,4} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {-1,1,2,3} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};

\draw[domain=-1.5:1.5,smooth,variable=\x,blue,ultra thick,samples=200] plot ({\x*\x*\x+ 1},{\x + 1});

\end{tikzpicture}
-->


### Example 3

````{admonition} Not continuous and not differentiable at a point
:class: tip 

The functions defined by the following graphs are not continuous and not differentiable at $x=-1$.

For the graph on the left, the function is not defined at $x=-1$ and therefore is not continuous and not differentiable at $x=-1$.  The function is continuous and differentiable everywhere else.

For the graph on the right, the function has a jump discontinuity at $x=-1$ (i.e., $\lim\limits_{x\to-1} f(x)$ does not exist) and therefore is not continuous and not differentiable at $x=-1$.  The function is continuous and differentiable everywhere else.

::::{grid} 2
:::{grid-item-card}
:columns: 5
:margin: 0 0 4 4
```{image} ../images/pic_derivatives_differentiable_example_3.png
:alt: Graph of a function that is not continuous and not differentiable
:align: center
```
:::

:::{grid-item-card}
:columns: 5
```{image} ../images/pic_derivatives_differentiable_example_3_2.png
:alt: Graph of a function that is not continuous and not differentiable
:align: center
```
:::
::::
```{dropdown} Long Text Description

There are two graphs displayed.  The first graph corresponds to a function that increases for x less than -1, is not defined at x = -1 (indicated by an open circle at the point (-1,1.6)), decreases between x-1 and x=1, and then increases after x = 1.  The graph does not have any sharp corners or vertical tangent lines, but has a discontinuity at x = -1.

The second graph corresponds to a function that increases for x less than -1 until it reaches an open circle at the point (-1,1.6).  The value of the function then jumps to 2.6, as indicated by a closed circle at the point (-1,2.6).  The curve continues to increase from that point, until x = 1, at which point the function decreases. 
```
````

<!--
\begin{tikzpicture}[scale=2]

\draw[black,fill=white] (-2.55,-1.1) rectangle (2.8,4.2);
\draw[very thin,color=lightgray,step=1] (-2.35,-0.9) grid (2.6,3.9);

\draw[->] (-2.35,0) -- (2.6,0) node[below] {$x$};
\draw[->] (0,-1) -- (0,4) node[right] {$y$};

\draw[domain=-2.35:2.55,smooth,variable=\x,blue,ultra thick,samples=100] plot ({\x},\x^3/3 - \x + 1);
       
% tick marks
\foreach \x in {-2,-1,1,2} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {1,2,3} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {$\y$};

\draw [blue,fill=white] (-1,5/3) circle (2pt);

\end{tikzpicture}


\begin{tikzpicture}[scale=2]

\draw[black,fill=white] (-2.55,-1.1) rectangle (2.8,4.2);
\draw[very thin,color=lightgray,step=1] (-2.35,-0.9) grid (2.6,3.9);

\draw[->] (-2.35,0) -- (2.6,0) node[below] {$x$};
\draw[->] (0,-1) -- (0,4) node[right] {$y$};

\draw[domain=-2.35:-1,smooth,variable=\x,blue,ultra thick,samples=100] plot ({\x},\x^3/3 - \x + 1);

\draw[domain=-1:2.55,smooth,variable=\x,blue,ultra thick,samples=100] plot ({\x},-\x^3/6 + \x/2 + 3);
       
% tick marks
\foreach \x in {-2,-1,1,2} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {1,2,3} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {$\y$};

\draw [blue,fill=white] (-1,5/3) circle (2pt);
\draw [blue,fill=blue] (-1,8/3) circle (2pt);

\end{tikzpicture}

-->

