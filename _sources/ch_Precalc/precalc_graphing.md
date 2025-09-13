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
# Graphing

## Equations for a Line

<!--
````{admonition} Slope-Intercept Form
:class: info


::::{grid} 2
:::{grid-item-card}
The equation of the line with slope $m$ and $y$-intercept equal to $b$ is given by

$$
\boxed{y = mx + b}
$$
:::

:::{grid-item-card}
```{image} ../images/pic_precalc_graphing_slope_intercept.png
alt: Graph of a line with y-intercept
:align: center
```
:::
::::

```{dropdown} Long Text Description
There is a horizontal x-axis with no points marked. There is a vertical y-axis with the point b marked. The graph of the linear function y=mx+b is plotted on these axes. It crosses the y-axis at the point y=b.
```
````
-->

````{admonition} Slope-Intercept Form
:class: info

The equation of the line with slope $m$ and $y$-intercept equal to $b$ is given by

$$y = mx + b $$

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_slope_intercept.png
:alt: Graph of a line with y-intercept
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with no points marked. There is a vertical y-axis with the point b marked. The graph of the linear function y=mx+b is plotted on these axes. It crosses the y-axis at the point y=b.
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
\begin{tikzpicture}[scale=2.5]
    \draw[white,fill=white] (-2,-1.5) rectangle (2.2,2.2);
    \draw[->] (-2,0) -- (2,0) node[below] {$x$};
    \draw[->] (0,-1.5) -- (0,2) node[right] {$y$};
    \draw[domain=-2:2,smooth,variable=\x,black,ultra thick] plot ({\x},{0.75*\x+0.5});
    \draw (0.2,0.5) -- (-0.2,0.5) node[left] {$b$};
\end{tikzpicture}
\end{document}
```
-->


````{admonition} Point-Slope Form
:class: info

The equation of the line with slope $m$ that goes through the point $(a,b)$ is given by

$$y = m(x-a) + b$$

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_point_slope.png
:alt: Graph of a line through the point (a,b)
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with no points marked. There is a vertical y-axis with no points marked. The line defined by y = m(x - a) + b is plotted on these axes. The point (a,b) on the line is marked.
```
````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2.5]
\draw[white,fill=white] (-1.5,-1.5) rectangle (2.7,2.2);
      \draw[->] (-1.5,0) -- (2.5,0) node[below] {$x$};
      \draw[->] (0,-1.5) -- (0,2) node[right] {$y$};
      \draw[domain=-1.5:2,smooth,variable=\x,black,ultra thick] plot ({\x},{0.75*\x+0.5});
      \fill (1,1.25) circle [radius = 2pt] node[below right] {$(a,b)$};
    \end{tikzpicture}
\end{document}
-->

```{admonition} Positive versus Negative Slope
:class: note

Recall that the slope of a line is positive if the line goes up from left-to-right and the slope is negative if the line goes down from left-to-right.
```


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
<a href="https://youtu.be/dFT-2xdJHrM" target="_blank">Equation of a Line</a> (Links to an external site) <br>
A review of the slope-intercept and point-slope form of the equation of a line.
:::
::::
````


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
<a href="https://youtu.be/IgZ-5oqDlkQ" target="_blank">The Graph of a Line</a> (Links to an external site) <br>
A review of graphing a line in slope-intercept and point-slope form.
:::
::::
````




### Example 1
`````{admonition} Sketch the graph of a line in slope-intercept form
:class: tip

Sketch the graph of the line defined by  $y = 2x + 3$.


```{dropdown} **Step 1:** &nbsp; Determine the slope and $y$-intercept.

Since $y=2x+3$ is in slope-intercept form, the line has slope $2$ and a $y$-intercept of $3$. 
```

````{dropdown} **Step 2:** &nbsp; Sketch the graph.

Draw the graph of the line that has a $y$-intercept of $3$ (i.e., goes through the point $(0,3)$) and a slope of $2$.

Note that the red dashed line is not part of the graph and is used only as a guide for drawing a line with slope 2.  In particular, in order for a line to have slope equal to $2$, if the $x$-coordinate of any point on the line is increased by 1 unit, then the $y$-coordinate must be increased by 2 units.


::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_1.png
:alt: Graph of line with slope 2 and y-intercept of 3
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -3 and 3 marked. There is a vertical y-axis with the points -3, 3, and 6 marked. There is a grid with one unit by one unit cells in the background. The graph of the linear function y = 2x + 3 is plotted. There is a red dashed staircase pattern which meets the linear function at the point (-3,-3) and moves to the right by one unit, and then up by two units in a repeating pattern which ends at the point (2,7).
```

````
`````

<!---
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.0]
\draw[black,fill=white] (-6.5,-4.5) rectangle (6.5,8.5);
%\draw[very thin,color=darkgray,step=3] (-8,-5) grid (8,8.9);
\draw[very thin,color=lightgray,step=1] (-5.9,-3.9) grid (5.9,7.9);
\draw[->] (-6,0) -- (6,0) node[below] {$x$};
\draw[->] (0,-4) -- (0,8) node[right] {$y$};
\node at (3.8, 6.5){$y = 2x+3$};

% draw slope
\draw[dashed,red,thick] (-3,-3) -| ++(1,2) -| ++(1,2) -| ++(1,2) -| ++(1,2) -| ++(1,2);
% draw line and point
\draw[domain=-3.5:2.5,smooth,variable=\x,black,ultra thick] plot ({\x},{2*\x+3});

% tick marks
\foreach \x in {-3,3} 
	\draw [thick] (\x cm,3pt) -- (\x cm,-3pt) node[below] {$\x$};
\foreach \y in {-3,3,6} 
	\draw [thick] (3pt,\y cm) -- (-3pt,\y cm) node[left] {$\y$};
\end{tikzpicture}
\end{document}
```
-->



### Example 2

`````{admonition} Sketch the graph of a line in point-slope form
:class: tip

Sketch the graph of the line defined by $y = -2(x - 4) + 3$.


```{dropdown} **Step 1:** &nbsp; Determine the slope and a point on the line.

Since $y = -2(x - 4) + 3$ is in point-slope form, the line has slope $-2$ and goes through the point $(4,3)$. 
```

````{dropdown} **Step 2:** &nbsp; Sketch the graph.

Draw the graph of the line that goes through the point $(4,3)$ and has a slope of $-2$.

In order for a line to have slope equal to $-2$, if the $x$-coordinate of any point on the line is increased by 1 unit, then the $y$-coordinate must be decreased by 2 units.


::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_2.png
:alt: Graph of line with slope -2 and goes through the point $(4,3)$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points 2 and 4 marked. There is a vertical y-axis with the points 3, 6, 9, and 12 marked. There is a grid with one unit by one unit cells in the background. The line defined by y-3 = -2(x-4) is plotted. There is a red dotted staircase pattern which meets the line at the point (-1,13) and moves to the right by one unit, and then down by two units in a repeating pattern which ends at the point (6,-1).
```
````
`````


<!---
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.0]
\draw[black,fill=white] (-2.5,-2.5) rectangle (8.5,14.5);
\draw[very thin,color=lightgray,step=1] (-1.9,-1.9) grid (7.9,13.9);
\draw[->] (-2,0) -- (8,0) node[below] {$x$};
\draw[->] (0,-2) -- (0,14) node[right] {$y$};
\node at (4.5, 10.5){$y = -2(x-4) + 3$};

% draw slope
%\draw[dashed,red,thick] (-1,13)|- ++(1,-2) |- ++(1,-2) |- ++(1,-2) |- ++(1,-2) |- ++(1,-2) |- ++(1,-2) |- ++(1,-2);
\draw[dashed,red,thick] (-1,13) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2) -| ++(1,-2);


% draw line and point
\draw[domain=-1.5:6.5,smooth,variable=\x,black,ultra thick] plot ({\x},{-2*\x + 11});
\draw [fill=black,thick] (4,3) circle [radius=0.15] node [below left] {$(4,3)$};

% tick marks
\foreach \x in {2,4} 
	\draw [thick] (\x cm,3pt) -- (\x cm,-3pt) node[below] {$\x$};
\foreach \y in {3,6,9,12} 
	\draw [thick] (-6pt,\y cm) -- (0pt,\y cm) node[right] {$\y$};
\end{tikzpicture}
\end{document}
```
-->



### Example 3


`````{admonition} Sketch the graph of a line in point-slope form
:class: tip

Sketch the graph of the line defined by $y = \dfrac{2}{5}(x + 2) + 1$.


```{dropdown} **Step 1:** &nbsp; Determine the slope and a point on the line.

Since $y = \dfrac{2}{5}(x + 2) + 1$ is in point-slope form, the line has slope $2/5$ and goes through the point $(-2,1)$. 
```

````{dropdown} **Step 2:** &nbsp; Sketch the graph.

Draw the graph of the line that goes through the point $(-2,1)$ and has a slope of $2/5$.

In order for a line to have slope equal to $2/5$, if the $x$-coordinate of any point on the line is increased by 5 units, then the $y$-coordinate must be increased by 2 units.


::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_3.png
:alt: Graph of line with slope -2 and goes through the point $(4,3)$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -6, -4, -2, 2, 4, 6, and 8 marked. There is a vertical y-axis with the points -2, 2, and 4 marked. There is a grid with one unit by one unit cells in the background. The line defined by y-1 = (2/5)(x+2) is plotted. There is a red dotted staircase pattern which meets the linear function at the point (-7,-1) and moves to the right by five units, and then up by two units in a repeating pattern which ends at the point (8,5).
```
````
`````

<!---
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.0]
\draw[black,fill=white] (-8.5,-3.5) rectangle (10.5,7.5);
\draw[very thin,color=lightgray,step=1] (-7.9,-2.9) grid (9.9,6.9);
\draw[->] (-8,0) -- (10,0) node[below] {$x$};
\draw[->] (0,-3) -- (0,7) node[right] {$y$};
\node at (4.5, 5.5){$y - 1 = \frac{2}{5}(x+2)$};

% draw slope
\draw[dashed,red,thick] (-7,-1) -| ++(5,2) -| ++(5,2) -| ++(5,2);

% draw line and point
\draw[domain=-8:10,smooth,variable=\x,black,ultra thick] plot ({\x},{0.4*\x+9/5});
\draw [fill=black,thick] (-2,1) circle [radius=0.15] node [above left] {$(-2,1)$};

% tick marks
\foreach \x in {-6,-4,-2,2,4,6,8} 
	\draw [thick] (\x cm,3pt) -- (\x cm,-3pt) node[below] {$\x$};
\foreach \y in {-2,2,4} 
	\draw [thick] (3pt,\y cm) -- (-3pt,\y cm) node[left] {$\y$};
\end{tikzpicture}
\end{document}
```
-->





## Graphing Quadratic Polynomials


```{admonition} Quadratic Polynomials
:class: info

The general form of a _**quadratic polynomial**_ (i.e., a polynomial of degree two) is

$$y = ax^2 + bx + c$$

where $a$, $b$, and $c$ are real numbers and $a\neq 0$.  The graph of a quadratic polynomial has the shape of a parabola.  If $a>0$, then the parabola opens upward (i.e., looks like the letter ``U'') and if $a<0$, then the parabola opens downward.
```



### Example 4

`````{admonition} Compare the graphs of two parabolas
:class: tip

Compare the graphs of $y = x^2$ and $y=-x^2$.


````{dropdown} Graph of $y=x^2$.

The graph of $y=x^2$ is a parabola that goes through the point $(0,0)$ and opens upward.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_4_1.png
:alt: Graph of $y=x^2$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -2 and 2 marked. There is a vertical y-axis with the points 2 and 4 marked. There is a grid of one unit by one unit cells in the background. The concave up quadratic function y = x squared is graphed on these axes, resembling a horseshoe shape. The function is decreasing as it comes from the left to x=0, meets the y-axis at (0,0), and increases as it goes off to the right.
```
````




````{dropdown} Graph of $y=-x^2$.

The graph of $y=x^2$ is a parabola that goes through the point $(0,0)$ and opens downward.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_4_2.png
:alt: Graph of $y=-x^2$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -2 and 2 marked. There is a vertical y-axis with the points -2 and -4 marked. There is a grid of one unit by one unit cells in the background. The concave down quadratic function y = -x squared is graphed on these axes, resembling a horseshoe shape. The function is increasing as it comes from the left to x=0, meets the y-axis at (0,0), and decreases as it goes off to the right.
```
````
`````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.5]

\draw[black,fill=white] (-3.75,-1.25) rectangle (3.75,5.25);
\draw[very thin,color=lightgray,step=0.5] (-3.4,-0.9) grid (3.4,4.9);
%\draw[very thin,color=gray,step=2] (-3.5,-1) grid (3.5,5);

\draw[->] (-3.5,0) -- (3.5,0) node[below] {$x$};
\draw[->] (0,-1) -- (0,5) node[right] {$y$};
\draw[domain=-2.23:2.23,smooth,variable=\x,black,ultra thick] plot ({\x},{\x*\x});%  node[right] {$y=x^2$};
       
\node[right] at (1.7, 3){$y = x^2$};

% tick marks
\foreach \x in {-2,2} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {2,4} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};
\end{tikzpicture}
\end{document}
```
-->

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.5]

\draw[black,fill=white] (-3.75,-5.25) rectangle (3.75,1.25);
\draw[very thin,color=lightgray,step=0.5] (-3.4,-4.9) grid (3.4,0.9);
%\draw[very thin,color=gray,step=2] (-3.5,-5) grid (3.5,1);

\draw[->] (-3.5,0) -- (3.5,0) node[below] {$x$};
\draw[->] (0,-5) -- (0,1) node[right] {$y$};
\draw[domain=-2.23:2.23,smooth,variable=\x,black,ultra thick] plot ({\x},{-\x*\x});%  node[right] {$y=x^2$};
       
\node[right] at (1.7, -3){$y = -x^2$};

% tick marks
\foreach \x in {-2,2} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {-2,-4} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};
\end{tikzpicture}
\end{document}
```
-->



### Example 5

`````{admonition} Compare the graphs of two parabolas
:class: tip

Compare the graphs of $y=x^2-4$ and $y=4-x^2$


````{dropdown} Graph of $y=x^2 - 4$.

Notice how the graph of $y=x^2-4$ looks like the graph of $y=x^2$ with each point shifted down $4$ units.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_5_1.png
:alt: Graph of $y=x^2-4$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -3, -1, 1 and 3 marked. There is a vertical y-axis with the points -2 and -4 marked. There is a grid of one unit by one unit cells in the background. The concave up quadratic function y = x squared - 4 is graphed on these axes. The function is decreasing as it comes from the left to x=0, meets the y-axis at (0,-4), and increases as it goes off to the right.
```
````


````{dropdown} Graph of $y= 4 - x^2$.

Notice how the graph of $y=4-x^2$ looks like the graph of $y=-x^2$ with each point shifted up $4$ units. 

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_5_2.png
:alt: Graph of $y=4 - x^2$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -3, -1, 1 and 3 marked. There is a vertical y-axis with the points 2 and 4 marked. There is a grid of one unit by one unit cells in the background. The concave down quadratic function y = -x squared + 4 is graphed on these axes. The function is increasing as it comes from the left to x=0, meets the y-axis at (0,4), and decreases as it goes off to the right.
```
````
`````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.5]
\draw[black,fill=white] (-3.75,-5.25) rectangle (3.75,1.25);
\draw[very thin,color=lightgray,step=0.5] (-3.4,-4.9) grid (3.4,0.9);
%\draw[very thin,color=gray,step=2] (-3.5,-5) grid (3.5,1);

\draw[->] (-3.5,0) -- (3.5,0) node[below] {$x$};
\draw[->] (0,-5) -- (0,1) node[right] {$y$};
\draw[domain=-2.23:2.23,smooth,variable=\x,black,ultra thick] plot ({\x},{\x*\x- 4});%  node[right] {$y=x^2$};
       
\node[right] at (0.9, -3.5){$y = x^2-4$};

% tick marks
\foreach \x in {-3,-1,1,3} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {-2} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};
\end{tikzpicture}
\end{document}
```
-->

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.5]
\draw[black,fill=white] (-3.75,-1.25) rectangle (3.75,5.25);
\draw[very thin,color=lightgray,step=0.5] (-3.4,-0.9) grid (3.4,4.9);
%\draw[very thin,color=gray,step=2] (-3.5,-1) grid (3.5,5);

\draw[->] (-3.5,0) -- (3.5,0) node[below] {$x$};
\draw[->] (0,-1) -- (0,5) node[right] {$y$};
\draw[domain=-2.23:2.23,smooth,variable=\x,black,ultra thick] plot ({\x},{4 - \x*\x});%  node[right] {$y=x^2$};
       
\node[right] at (0.9, 3.5){$y = 4-x^2$};

% tick marks
\foreach \x in {-3,-1,1,3} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {2} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};
\end{tikzpicture}
\end{document}
```
-->


```{admonition} Effect of Adding or Subtracting a Constant
:class: note

   For any function, $f(x)$, and constant, $C$, the graph of $y=f(x) + C$ is the result of shifting the graph of $y=f(x)$ up or down, depending on if the constant, $C$, is positive or negative, respectively.
```



(precalc:graphing:example6)=
### Example 6

`````{admonition} Sketch the graph of a parabola
:class: tip

Sketch the graph of $f(x) = x^2 - 4x -12$.


```{dropdown} **Step 1:** &nbsp; Determine the &nbsp; $y$-intercept by evaluating &nbsp; $f(0)$.

\begin{align*}
  f(0)
  &= 0^2 - 4(0) - 12 \\
  &= -12
\end{align*}

Therefore the graph of $y=f(x)$ goes through the point $(0,-12)$.
```

```{dropdown} **Step 2:** &nbsp; Determine the &nbsp; $x$-intercepts by setting &nbsp; $f(x)=0$ &nbsp; and solving for &nbsp; $x$.

Recall from [Factoring, Example 8](01_02_example8)  and [Solving Equations, Example 1](01_03_example1) that

$$x^2 - 4x - 12 = (x+2)(x-6)$$

Now set each factor equal to zero and solve for $x$.
\begin{align*}
x + 2 = 0 ~~~~&\Rightarrow~~~~ x = -2 \\
x - 6 = 0 ~~~~&\Rightarrow~~~~ x = 6 
\end{align*}

Therefore the graph of $y=f(x)$ goes through the points $(-2,0)$ and $(6,0)$.
```


````{dropdown} **Step 3:** &nbsp; Sketch the parabola based on the $x$ and $y$-intercepts.

Draw the graph of a parabola that opens upward (since the coefficient of $x^2$ in $f(x)$ is positive) and goes through the points found in **Steps 1** and **2**.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_6.png
:alt: Graph of $y= x^2 - 4x - 12$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -3, 3, 6 and 9 marked. There is a vertical y-axis with the points -12 marked. There is a grid of one unit by two unit cells in the background. The concave up quadratic function y = x squared - 4x - 12 is graphed on these axes. The function is decreasing as it comes from the left to x=2 and increases as it goes off to the right.  The function meets the y-axis at the point (0,-12) and meets the x-axis at the points (-3,0) and (6,0).
```
````
`````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[xscale=0.8,yscale=0.5]

\draw[black,fill=white] (-6.6,-19) rectangle (11.6,11);
\draw[very thin,color=lightgray,xstep=1,ystep=2] (-5.9,-17.9) grid (10.9,9.9);

\draw[->] (-6,0) -- (11,0) node[below] {$x$};
\draw[->] (0,-18) -- (0,10) node[right] {$y$};
\draw[domain=-3:7,smooth,variable=\x,black,ultra thick] plot ({\x},{\x*\x - 4*\x - 12});
       
\node[right] at (5, -9){$y = x^2-4x-12$};

%\draw [fill=black,thick] (-2,0) circle [radius=0.15];
%\draw [fill=black,thick] (6,0) circle [radius=0.15];
%\draw [fill=black,thick] (0,-12) circle [radius=0.15];
\draw [fill=black] (-2,0) ellipse [x radius = 0.15, y radius = 0.225];
\draw [fill=black] (6,0) ellipse [x radius = 0.15, y radius = 0.225];
\draw [fill=black] (0,-12) ellipse [x radius = 0.15, y radius = 0.225];

% tick marks
\foreach \x in {-3,3,9} 
	\draw [thick] (\x cm,6pt) -- (\x cm,-6pt) node[below] {$\x$};
\foreach \y in {-12} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};
	
\clip (-8,-20) rectangle (12,10);
\draw[domain=-4:8,smooth,variable=\x,black,ultra thick] plot ({\x},{\x*\x - 4*\x - 12});

\end{tikzpicture}
\end{document}
```
-->


## Graphing Power and Root Functions


```{admonition} Power Functions
:class: info 
Any function of the form

$$y = x^r$$

where $r$ is any real number is called a _**power function**_.  Thus $x^2$, $x^3$, $x^4$, etc. are examples of power functions.  Root functions, like the square root (i.e., $\sqrt{x}$ or $x^{1/2}$) and cube root (i.e., $\sqrt[3]{x}$ or $x^{1/3}$) are also examples of power functions.
```

### Example 7

`````{admonition} Sketch the graph of a power function
:class: tip

Sketch the graph of $y = x^3$.


````{dropdown} Graph of $y= x^3$.

Notice how the graph of $y=x^3$ always increases from left-to-right and looks like a horizontal line as it goes through the origin.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_7.png
:alt: Graph of $y=x^3$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -2, -1, 1 and 2 marked. There is a vertical y-axis with the points -3, -2, -1, 1, 2, and 3 marked. There is a grid of one unit by one unit cells in the background. The cubic function y = x cubed is graphed on these axes. The function is increasing and concave down as it comes from the left to x=0, meets the y-axis at (0,0), and is increasing and concave up as it goes off to the right.
```
````
`````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2]

\draw[black,fill=white] (-3.5,-4.3) rectangle (3.5,4.3);
\draw[very thin,color=lightgray,step=1] (-2.9,-3.9) grid (2.9,3.9);

      \draw[->] (-3,0) -- (3,0) node[below] {$x$};
      \draw[->] (0,-4) -- (0,4) node[right] {$y$};
      \draw[domain=-1.57:1.57,smooth,variable=\x,black,ultra thick,samples=100] plot ({\x},\x^3);
      \node at (2.4,3.2){$y = x^3$};
       
      % tick marks
\foreach \x in {-2,-1,1,2} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {-3,-2,-1,1,2,3} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {$\y$};

    \end{tikzpicture}
\end{document}
```
-->


### Example 8

`````{admonition} Sketch the graph of a root function
:class: tip

Sketch the graph of the square root function, $y = \sqrt{x}$.


````{dropdown} Graph of $y= \sqrt{x}$.

Notice how the graph of $y=\sqrt{x}$ looks like the upper half of a parabola that opens to the right.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_precalc_graphing_example_8.png
:alt: Graph of $y=\sqrt{x}$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points 1, 2, 3, 4, 5, 6, 7, 8, and 9 marked. There is a vertical y-axis with the points 1, 2, and 3 marked. There is a grid of one unit by one unit cells in the background. The increasing concave down function y = square root x is graphed on these axes. The graph begins at (0,0).
```
````
`````


<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2]

\draw[black,fill=white] (-0.8,-0.8) rectangle (10.3,4.3);
\draw[very thin,color=lightgray,step=1] (0,0) grid (9.9,3.9);

      \draw[->] (-0.5,0) -- (10,0) node[below] {$x$};
      \draw[->] (0,-0.5) -- (0,4) node[right] {$y$};
      \draw[domain=0:1,smooth,variable=\x,black,ultra thick,samples=100] plot ({\x},\x^0.5);
      \draw[domain=1:10,smooth,variable=\x,black,ultra thick,samples=36] plot ({\x},\x^0.5);
      \node at (7,3.2){$y = \sqrt{x}$};
       
      % tick marks
\foreach \x in {1,...,9} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {1,2,3} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {$\y$};

    \end{tikzpicture}
\end{document}
```
-->

