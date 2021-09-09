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
# Intervals of Increase & Decrease

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

```{admonition} Definition
:class: info

A function $f$ is **increasing** on the interval $(a,b)$ if for any two numbers $c$ and $d$ in $(a,b)$, $f(c) < f(d)$ whenever $c<d$.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2.0]
\tikzstyle{every node}=[font=\large]
\draw[white,fill=white] (0,-0.2) rectangle (3,3.8);

% axis
\draw[<->] (0,3) |- (3,0);
     
% dash lines
\draw[dashed,red] (0,1.04) node[left] {\textcolor{black}{$f(c)$}} -| (1.2,0);
\draw[dashed,red] (0,1.94) node[left] {\textcolor{black}{$f(d)$}} -| (1.8,0);

% draw curve
\draw [ultra thick] (0.5,0.5) cos (1.5,1.5) sin (2.5,2.5);

% draw points
\draw [black,fill=red] (1.2,1.04) circle (2.0pt);
\draw [black,fill=red] (1.8,1.94) circle (2.0pt);

\node[rotate=90] at (-0.5,1.5) {$<$};
\node[above] at (0.5,-0.6) {$a$};
\node[above] at (1.2,-0.6) {$c$};
\node[above] at (1.5,-0.6) {$<$};
\node[above] at (1.8,-0.6) {$d$};
\node[above] at (2.5,-0.6) {$b$};

% tick marks
\draw [thick] (0.5 cm,2pt) -- (0.5 cm,-2pt);
\draw [thick] (1.2 cm,2pt) -- (1.2 cm,-2pt);
\draw [thick] (1.8 cm,2pt) -- (1.8 cm,-2pt);
\draw [thick] (2.5 cm,2pt) -- (2.5 cm,-2pt);
\end{tikzpicture}
\end{document}
```

```{admonition} Theorem
:class: warning

If $f'(x) > 0$ for all $x$ in the interval $(a,b)$, then $f$ is increasing on $(a,b)$.
```


```{admonition} Definition
:class: info

A function $f$ is decreasing on the interval $(a,b)$ if for any two numbers $c$ and $d$ in $(a,b)$, $f(c) > f(d)$ whenever $c<d$.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2.0]
\tikzstyle{every node}=[font=\large]
\draw[white,fill=white] (0,-0.2) rectangle (3,3.8);

% axis
\draw[<->] (0,3) |- (3,0);
     
% dash lines
\draw[dashed,red] (0,1.94) node[left] {\textcolor{black}{$f(c)$}} -| (1.2,0);
\draw[dashed,red] (0,1.04) node[left] {\textcolor{black}{$f(d)$}} -| (1.8,0);

% draw curve
\draw [ultra thick] (0.5,2.5) cos (1.5,1.5) sin (2.5,0.5);

% draw points
\draw [black,fill=red] (1.2,1.94) circle (2.0pt);
\draw [black,fill=red] (1.8,1.04) circle (2.0pt);

\node[rotate=90] at (-0.5,1.5) {$<$};
\node[above] at (0.5,-0.6) {$a$};
\node[above] at (1.2,-0.6) {$c$};
\node[above] at (1.5,-0.6) {$<$};
\node[above] at (1.8,-0.6) {$d$};
\node[above] at (2.5,-0.6) {$b$};

% tick marks
\draw [thick] (0.5 cm,2pt) -- (0.5 cm,-2pt);
\draw [thick] (1.2 cm,2pt) -- (1.2 cm,-2pt);
\draw [thick] (1.8 cm,2pt) -- (1.8 cm,-2pt);
\draw [thick] (2.5 cm,2pt) -- (2.5 cm,-2pt);
\end{tikzpicture}
\end{document}
```

```{admonition} Theorem
:class: warning

If $f'(x) < 0$ for all $x$ in the interval $(a,b)$, then $f$ is decreasing on $(a,b)$.
```



## Example 1

The following is the graph of a continuous function that is increasing on the intervals $(1,2)$ and $(4,6)$ and decreasing on the intervals $(2,4)$ and $(6,7)$.  

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2.0]
\tikzstyle{every node}=[font=\large]

\draw[white,fill=white] (0,0) rectangle (8,4);
 \draw[very thin,color=darkgray,step=1.0] (0,0) grid (8,4);
 \draw[very thin,color=lightgray,step=0.25] (0,0) grid (8,4);

\draw[->] (0,0) -- (8,0) node[below] {$x$};
\draw[->] (0,0) -- (0,4) node[right] {$y$};
     
% draw curve
\draw [ultra thick] 
(1,1.5) sin (2,2.5) cos (3,1.5) sin (4,0.5) cos (6,3.5) sin (7,1.5);


% tick marks
\foreach \x in {1,...,7} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\end{tikzpicture}
\end{document}
```


## Finding Intervals of Increase/Decrease using the Derivative

```{admonition} Follow these steps
:class: warning

1. Find all values of $x$ such that $f'(x) = 0$ or $f'(x)$ does not exist. <br><br>
2. Break up domain of $f$ into open intervals between values found in Step 1. <br><br>
3. Evaluate $f'(x)$ at one value, $c$, from each interval, $(a,b)$, found in Step 2. <br>
    - If $f'(c) > 0$, then $f$ is increasing on $(a,b)$.
    - If $f'(c) < 0$, then $f$ is decreasing on $(a,b)$.
```

(curvesketching:increasedecrease:example2)=
## Example 2

Determine the intervals where 

$$f(x) = x^3 + 3 x^2 - 9 x -8$$

is increasing and where it is decreasing.

```{dropdown} **Step 1:** Compute $f'(x)$.

$$f'(x) = 3 x^2 + 6 x - 9$$ 
```

```{dropdown} **Step 2:** Find all values of $x$ such that $f'(x) = 0$.

\begin{align*}
f'(x) 
&= 3 (x^2 + 2 x - 3) \\
&= 3 (x + 3)(x - 1)   
\end{align*}
which is equal to zero when $x=-3$ and $x=1$.  
```

```{dropdown} **Step 3:** Find all values of $x$ such that $f'(x)$ does not exist.

Notice that $f'(x)$ is defined for all real numbers.
```

```{dropdown} **Step 4:** Break up the domain of $f$ into subintervals based on the values found in Steps 2 and 3.

Since we found $x=-3$ and $x=1$ to be the only values where $f'(x)$ could change sign, we break up the domain of $f$ (which is $(-\infty,\infty)$) into the following subintervals:

$$(-\infty,-3), ~(-3,1), ~\hbox{ and }~  (1,\infty)$$
```

```{dropdown} **Step 5:** Plug one number from each subinterval into $f'(x)$  to determine the sign of $f'(x)$.

$\mathbf{(-\infty,-3)}$: Plug $x=-4$ into $f'(x)$.
Since $f'(-4) = 3(-1)(-5) > 0$, 
$f$ is increasing on $(-\infty,-3)$.


$\mathbf{(-3,1)}$: Plug $x=0$ into $f'(x)$.
Since $f'(0) = 3(3)(-1) < 0$, 
$f$ is decreasing on $(-3,1)$.

$\mathbf{(1,\infty)}$:  Plug $x=2$ into $f'(x)$.
Since $f'(2) = 3(5)(1) > 0$,  
$f$ is increasing on $(1,\infty)$.
```


## Graphical representation of sign analysis

We will typically represent the above sign analysis by drawing a number line, marking off the values in the domain of $f$ such that $f'(x) = 0$ or $f'(x)$ does not exist, and then putting a $+$ or $-$ above each interval according to the sign of $f'(c)$, where $c$ is the test value taken from the corresponding interval.  The number line associated with the calculations in {ref}`curvesketching:increasedecrease:example2` is shown below.

```{image} ../images/pic_curvesketching_intervalsignanalysis.png
:alt: graphical representation of sign analysis on the number line
:width: 600px
:align: center
```
