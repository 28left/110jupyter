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
# Inflection Points



```{admonition} Definition
:class: info

An **inflection point** is a point on the graph of a continuous function where the concavity changes.
```



## Example 1

An inflection point occurs at a point on a graph where the concavity changes from concave up to concave down or from concave down to concave up.


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
\begin{tikzpicture}[scale = 2.3]
     
% draw curve
\draw [ultra thick,smooth,variable=\x] plot [domain=-1.25:1.25] (\x,{2.3*(pow(\x,3) - \x)});
\draw [ultra thick,smooth,variable=\x,xshift=4cm] plot [domain=-1.25:1.25] (\x,{(pow(\x,3) + \x)/-2});
%\draw [ultra thick,smooth,variable=\x,yshift=-4cm] plot [domain=-1.25:1.25] (\x,{-2.3*(pow(\x,3) - \x)});
%\draw [ultra thick,smooth,variable=\x,xshift=4cm,yshift=-4cm] plot [domain=-1.25:1.25] (\x,{(pow(\x,3) + \x)/2});

% draw points
\draw [black,fill=red] (0,0) circle (1.5pt);
\draw [black,fill=red,xshift=4cm] (0,0) circle (1.5pt);
%\draw [black,fill=red,yshift=-4cm] (0,0) circle (2.0pt);
%\draw [black,fill=red,xshift=4cm,yshift=-4cm] (0,0) circle (2.0pt);

% label extrema
\draw [<-, >=stealth', shorten <=3pt] (0,0) -- (2,-1.5) node[below] {\bf Inflection Point}; 
\draw [<-, >=stealth', shorten <=3pt] (4,0) -- (2,-1.5) node[below] {}; 
%\draw [<-, >=stealth', shorten <=3pt] (0,-4) -- (2,-2.0) node[below] {}; 
%\draw [<-, >=stealth', shorten <=3pt] (4,-4) -- (2,-2.0) node[below] {}; 

\end{tikzpicture}
\end{document}
```


## Finding Inflection Points using the Second Derivative

- Find all values of $x$ such that $f''(x) = 0$ or $f''(x)$ does not exist.
- Break up domain of $f$ into open intervals between values found in Step 1.
- Evaluate $f''(x)$ at one value, $c$, from each interval found in Step 2.  

  If $f''(x)$ changes sign at $x=c$ and $x=c$ is in the domain of $f$, then the point $(c,f(c))$ is an inflection point of $f$. 


## Example 2

Find the inflection points of 

$$f(x) = x^3 + 10x - \dfrac{3}{x}.$$


```{dropdown} **Step 1:**  Compute $f''(x)$.

\begin{align*}
f'(x) 
&= \frac{d}{dx} (x^3 + 10x - 3x^{-1}) \\
&= 3x^2 + 10 + 3x^{-2} 
& \\
& \\
f''(x) 
&= 6x - 6x^{-3} \\
&= 6x - \frac{6}{x^3} \\
&= \frac{6x^4}{x^3} - \frac{6}{x^3} && \hbox{Get a common denominator}\\
&= \frac{6x^4 - 6}{x^3}  \\
&= \frac{6(x^4 - 1)}{x^3} \\
&= \frac{6(x - 1)(x+1)(x^2+1)}{x^3} && \hbox{Factor numerator}
\end{align*}

The last equality follows from treating $x^4-1$ as a difference of squares (i.e., $x^4 -1 = (x^2)^2 - 1^2 = (x^2-1)(x^2+1) = (x-1)(x+1)(x^2+1)$).
```


```{dropdown} **Step 2:** Find all values of $x$ such that $f''(x) = 0$.

$f''(x) = 0$ when $x=1$ and $x=-1$.
```


```{dropdown} **Step 3:** Find all values of $x$ such that $f''(x)$ does not exist.

$f''(x)$ does not exist when $x^3 = 0$ (i.e., when $x=0$).
```


````{dropdown} **Step 4:** Break up the domain of $f$.

Break up the domain of $f$ at each value found in Steps 2 and 3. Plug one number from each subinterval into $f''(x)$ to determine the sign of $f''(x)$ on that interval.

```{figure} ../images/pic_curvesketching_inflection_1.png
---
name: pic_curvesketching_inflection_1
width: 600px
---
Sign analysis of $f''(x) = \frac{6(x - 1)(x+1)(x^2+1)}{x^3}$.
```

Notice that $f''(x)$ changes sign at $x=-1$, $x=0$, and $x=1$, however, $x=0$ is not in the domain of $f$ and cannot correspond to an inflection point.  Therefore, $(-1, -8)$ and $(1,8)$ are the only inflection points of $f$.
````


## Points of Diminishing & Increasing Return

````{admonition} Point of Diminishing Returns
:class: info

A **point of diminishing returns** is an inflection point appearing where a function is increasing and the concavity changes from concave up to concave down.

```{image} ../images/pic_curvesketching_inflection_2.png
:alt: A point of diminishing returns
:align: center
:height: 300px
```
````


````{admonition} Point of Increasing Returns
:class: info

A **point of increasing returns** is an inflection point appearing where a function is increasing and the concavity changes from concave down to concave up.

```{image} ../images/pic_curvesketching_inflection_3.png
:alt: A point of increasing returns
:align: center
:height: 300px
```
````


## Example 3

Determine whether or not $f(x) = 3x^3-18x^2+81x+90$ has a point of diminishing or increasing return.


```{dropdown} **Step 1:**  Compute $f'(x)$.

\begin{align*}
f'(x)
&= 9x^2 - 36x + 81 \\
&= 9(x^2 - 4x + 9)
\end{align*}
```


```{dropdown} **Step 2:**  Compute $f''(x)$.

\begin{align*}
f''(x)
&= 18x - 36 \\
&= 18(x-2)
\end{align*}
```


````{dropdown} **Step 3:**  Find and analyze inflection points.

Find inflection points, if any, and determine if each one corresponds to a point of diminishing return, increasing return, or neither.

```{figure} ../images/pic_curvesketching_inflection_4.png
---
name: pic_curvesketching_inflection_4
width: 300px
---
Sign analysis of $f''(x) = 18(x-2)$.
``` 

Notice that $f''(x) = 0$ only when $x=2$.  Furthermore, $f'(2)$ is positive, which means that $f(x)$ is increasing near $x=2$.  And lastly, since $f''(x)$ changes sign from negative to positive at $x=2$, $f(x)$ has a point of increasing returns at $x=2$.
````




