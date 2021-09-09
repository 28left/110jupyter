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



```{admonition} Concave Up
:class: info

A function is **concave up** on an interval if its derivative is increasing on the interval.

*If $f''(x) > 0$ for all $x$ on the interval $(a,b)$, then $f$ is concave up on $(a,b)$.*
```

```{admonition} Concave Down
:class: info

A function is **concave down** on an interval if its derivative is decreasing on the interval.

*If $f''(x) < 0$ for all $x$ on the interval $(a,b)$, then $f$ is concave down on $(a,b)$.*
```



## Example 1

The following is the graph of a continuous function that is concave down on the interval $(1,4)$ and concave up on the interval $(4,7)$.

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


## Finding Intervals of Concavity using the Second Derivative

- Find all values of $x$ such that $f''(x) = 0$ or $f''(x)$ does not exist.
- Break up domain of $f$ into open intervals between values found in Step 1. 
- Evaluate $f''(x)$ at one value, $c$, from each interval, $(a,b)$, found in Step 2.
    - If $f''(c) > 0$, then $f$ is concave up on $(a,b)$.
    - If $f''(c) < 0$, then $f$ is concave down on $(a,b)$.


## Example 2

If the second derivative of $f(x)$ is 

$$\displaystyle f''(x) = \frac{x^2-4x}{x-6}$$ 

find the intervals  of concavity of $f$.


```{dropdown} **Step 1:** Find all values of $x$ such that $f''(x) = 0$.

\begin{align*}
f''(x) &= \frac{x(x-4)}{x-6}
\end{align*}

which equals zero when $x=0$ and $x=4$.
```


```{dropdown} **Step 2:** Find all values of $x$ such that $f''(x)$ does not exist.

$f''(x)$ does not exist when $x=6$.
```


````{dropdown} **Step 3:** Perform an interval sign analysis for $f''$.

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

Therefore, $f$ is concave up on the intervals $(0,4)$ and $(6,\infty)$ and concave down on the intervals $(-\infty,0)$ and $(4,6)$.
````