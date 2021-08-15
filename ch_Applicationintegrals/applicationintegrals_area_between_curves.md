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
# Area Between Two Curves

## Computing the Area of a Region Bounded by Two Curves

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[scale=1.5]
      
  % shade region
  \draw[smooth,fill=yellow!90] plot[domain=0.5:3.5] ({\x},{2 + 0.5*sin(1.5*\x r)}) --
  plot[domain=3.5:0.5] ({\x},{1 - 0.5*sin(0.75*\x r)}) -- cycle;

  % draw axes
  \draw[thick,->] (-0.5,0) -- (4.5,0) node[above] {$x$};
  \draw[thick,->] (0,-0.5) -- (0,3) node[right] {$y$};

  % draw curve
  \draw[ultra thick,domain=0:4,smooth] plot ({\x},{2 + 0.5*sin(1.5*\x r)}) node[right] {$y=f(x)$};
  \draw[ultra thick,domain=0:4,smooth] plot ({\x},{1 - 0.5*sin(0.75*\x r)}) node[right] {$y=g(x)$};

  \draw (0.5,0.1) -- (0.5,-0.1);
  \draw (0.5,-0.4) node[above] {$a$};
  \draw (3.5,0.1) -- (3.5,-0.1);
  \draw (3.5,-0.4) node[above] {$b$};

  \node at (2,1.3) {$R$};
    
\end{tikzpicture}
\end{document} 

```

```{admonition} Computing the Area between Two Curves
:class: info

Suppose $f$ and $g$ are continuous functions with $f(x) \geq g(x)$ on $[a,b]$.

Then the area of the region, $R$, bounded above by $y=f(x)$ and below by $y=g(x)$ on $[a,b]$ is given by

$$\int_a^b f(x)-g(x) ~dx.$$
```


## When Finding the Area Between Two Curves

It's extremely important to draw the region in question to make sure the above formula is applied correctly. While it's not necessary to draw each curve using all of the techniques built up in the Curve Sketching packet, the curves should be drawn with enough detail to clearly identify the top and bottom functions and the corresponding boundaries.

The following guidelines should be applied to make sure the area of the region is computed correctly.

- Find all points of intersection of $f(x)$ and $g(x)$ on $[a,b]$.
- Use the points of intersection and the values of $f(x)$ and $g(x)$ at the endpoints to help sketch the region.
- Break up the given interval at the points of intersection.
- Determine which function is larger on each subinterval.
- Calculate the area of each subregion using the formula above.
- Combine the areas of the different subregions.

## Example 1

Find a sum of integrals that represents the area of the region bounded by $y=f(x)$ and $y=g(x)$ on $[1,7]$ as shown below.

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}

  % shade region
  \draw[smooth,fill=yellow!90] 
  plot[domain=1:7] ({\x},{-5/2 + (61*\x)/10 - (43*\x^2)/24 + \x^3/5 - \x^4/120}) --
  plot[domain=7:1] ({\x},{4 + (77*\x)/30 - (113*\x^2)/60 + \x^3/3 - \x^4/60}) -- cycle;

  % draw axes
  \draw[thick,->] (-1,0) -- (8.5,0) node[above] {$x$};
  \draw[thick,->] (0,-0.75) -- (0,5.5) node[right] {$y$};

  % draw curves
  \draw[ultra thick,domain=1:7,smooth,variable=\x,black] 
  plot ({\x},{-5/2 + (61*\x)/10 - (43*\x^2)/24 + \x^3/5 - \x^4/120}) node[right] {$y=g(x)$};
  \draw[ultra thick,domain=1:7,smooth,variable=\x,black] 
  plot ({\x},{4 + (77*\x)/30 - (113*\x^2)/60 + \x^3/3 - \x^4/60}) node[right] {$y=f(x)$};

  % tick marks
  \foreach \x in {1,2,6,7} 
    \draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
    
  \draw[dashed] (1,0) -- (1,2);
  \draw[dashed] (2,0) -- (2,4);
  \draw[dashed] (6,0) -- (6,2.1);
  \draw[dashed] (7,0) -- (7,1);

\end{tikzpicture}
\end{document} 
```

```{admonition} Step 1: Find the points of intersection.
:class: tip, dropdown

Notice that the functions intersect each other at $x=2$ and $x=6$. Therefore, we need to break up the original interval, $[1,7]$, into the following subintervals

$$[1,2], ~[2,6], ~\hbox{and} ~[6,7].$$
```

```{admonition} Step 2: Determine which function is larger on each subinterval and calculate the area of each subregion.
:class: tip, dropdown


- $[1,2]$: On this interval, $f(x) \geq g(x)$.  Therefore, the area of the region bounded by $f(x)$ and $g(x)$ on $[1,2]$ is 
    
    $$\int_1^2 f(x) - g(x) ~dx.$$

- $[2,6]$: On this interval, $g(x) \geq f(x)$.  Therefore, the area of the region bounded by $f(x)$ and $g(x)$ on $[2,6]$ is 

    $$\int_2^6 g(x) - f(x) ~dx.$$

- $[6,7]$: On this interval, $f(x) \geq g(x)$. Therefore, the area of the region bounded by $f(x)$ and $g(x)$ on $[6,7]$ is 

  $$\int_6^7 f(x) - g(x) ~dx.$$
```

```{admonition} Step 3: Combine the areas of the different subregions.
:class: tip, dropdown

The area of the region described above is given by

$$\int_1^2 f(x) - g(x)~dx + \int_2^6 g(x) - f(x) ~dx + \int_6^7 f(x)-g(x)~dx.$$
```

## Example 2

Find the area of the region bounded by $y = x^2-x$ and $y = 2$ on the interval $[0, 3]$.

```{admonition} Step 1: Find the points of intersection and use them to help sketch the region.
:class: tip, dropdown

The two curves intersect each other when $x^2-x = 2$, or equivalently when

$$x^2 - x - 2 = (x-2)(x+1)$$

equals zero, which happens when $x=2$ and $x=-1$. Notice that $x=-1$ is not relevant since it is not on the interval $[0,3]$.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[xscale=2.0,yscale=0.5]

  \draw[fill=white] (-0.75,-1.5) rectangle ++(5,9);

  % shade region
  \draw[fill=yellow!90] (0,2) -- plot[domain=0:3,smooth,variable=\x,black] ({\x},{\x* (\x -1)}) |- (0,2);

  % draw axes
  \draw[thick,->] (-0.5,0) -- (4,0) node[above] {$x$};
  \draw[thick,->] (0,-1) -- (0,7) node[right] {$y$};

  % draw curves
  \draw[ultra thick,domain=-0.25:3.1,smooth,variable=\x,black] plot ({\x},{\x* (\x -1)}) node[right] {$y=x^2-x$};
  \draw[ultra thick,domain=-0.25:3.1,smooth,variable=\x,black] plot ({\x},{2}) node[right] {$y=2$};
  %\draw[ultra thick,domain=-2.3:2.3,smooth,variable=\x,black] plot (\x,\x*\x*\x) node[right] {$y=x^3$};


  \draw (0.7, 1) node {$R_1$};
  \draw (2.6, 3.0) node {$R_2$};
        
  % tick marks
  \foreach \x in {1,2,3} 
    \draw [thick] (\x cm,4pt) -- (\x cm,-4pt) node[below] {$\x$};

\end{tikzpicture}
\end{document} 
```

```{admonition} Step 2: Calculate the area of each subregion.
:class: tip, dropdown

- Area of region $R_1$. Note that $2\geq x^2 - x$ on $[0,2]$. 

\begin{align*}
  \int_{0}^2 2 - (x^2 - x) ~dx
  &= \int_{0}^2 2 - x^2 + x ~dx\\
  &= \left( 2x - \frac{x^3}{3} + \frac{x^2}{2} \right) \Biggr|_{0}^2 \\
  &= \left( 4 - \frac{8}{3} + \frac{4}{2} \right) - \left( 0 - 0 + 0 \right) = 10/3
\end{align*}

- Area of region $R_2$. Note that $x^2 - x\geq 2$ on $[2,3]$. 

\begin{align*}
  \int_{2}^3 (x^2 - x) - 2 ~dx
  &= \int_{2}^3 x^2 - x - 2 ~dx\\
  &= \left( \frac{x^3}{3} - \frac{x^2}{2} - 2x \right) \Biggr|_{2}^3 \\
  &= \left( \frac{27}{3} - \frac{9}{2} - 6\right) - \left(\frac{8}{3} - \frac{4}{2} - 4\right) = 11/6
\end{align*}
```

```{admonition} Step 3: Combine the areas of the different subregions.
:class: tip, dropdown

The area of the region bounded by $y = x^2-x$ and $y = 2$ on $[0, 3]$ is $\frac{10}{3} + \frac{11}{6} = 31/6.$
```

```{admonition} Observation
:class: warning

Observe that the area of the region is not equal to $\int_0^3 2 - (x^2-x) ~dx  = 3/2$. This underscores the importance of drawing the region **before** setting up the integral.
```

## Example 3

Find the area of the bounded region enclosed by $y=\dfrac{2}{\sqrt{x}}$, $y= \dfrac{2}{x^3}$, and $x=2$.

```{admonition} Step 1: Find the points of intersection and use them to help sketch the region.
:class: tip, dropdown

\begin{align*}
  \frac{2}{\sqrt{x}} &= \frac{2}{x^3} && \text{Set the equations equal to each other}\\
  2x^3 &= 2\sqrt{x} && \text{Cross multiply}\\
  x^3&=\sqrt{x} && \text{Divide both sides by 2}\\
  x^\frac{5}{2} &= 1 && \text{Divide both sides by }\sqrt{x}\\
  x&=1 && \hbox{Raise both sides to the power of $2/5$}
\end{align*}

Therefore, the curves intersect only when $x=1$.  And since only one vertical line, $x=2$, was given that bounds the region, we must use the point of intersection at $x=1$ as the other vertical line that bounds the region.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[xscale=2.5]

  \draw[fill=white] (-0.75,-1) rectangle ++(4.5,6);

  % shade region
  \draw[fill=yellow!90] plot[smooth, samples=100, domain=1:2] ({\x},{2 / \x^0.5}) -- plot[smooth, samples=100, domain=2:1] ({\x},{2 / \x^3});

  %draw axes
  \draw[thick,->] (-0.5,0) -- (3.5,0) node[above] {$x$};
  \draw[thick,->] (0,-0.5) -- (0,4.2) node[right] {$y$};

  % draw curves
  \clip (0,-0.5) rectangle ++(3.4,4.5);
  \draw[ultra thick,domain=0.2:2.5,smooth,variable=\x,black] plot ({\x},{2 / \x^0.5}) node[above right] {$y=2/\sqrt{x}$};
  \draw[ultra thick,domain=0.8:2.5,smooth,variable=\x,black] plot ({\x},{2 / \x^3}) node[above right] {$y=2/x^3$};

  % tick marks
  \foreach \x in {1,2} 
    \draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};

\end{tikzpicture}
\end{document} 
```

```{admonition} Step 2: Calculate the area of the region.
:class: tip, dropdown

Note that $\dfrac{2}{\sqrt{x}} \geq \dfrac{2}{x^3}$ on $[1,2]$ and therefore the area of the region is given by $\int_1^2 \frac{2}{\sqrt{x}} - \frac{2}{x^3} ~dx$.

\begin{align*}
  \int_1^2 \frac{2}{\sqrt{x}} - \frac{2}{x^3} ~dx
  &= \int_1^2 2x^{-1/2} - 2x^{-3} ~dx \\
  &= \left(2\frac{x^{1/2}}{1/2} - 2 \frac{x^{-2}}{-2} \right) \Biggr|_1^2 && \hbox{Power rule}\\
  &= \left(4\sqrt{x} + \frac{1}{x^2} \right) \Biggr|_1^2 && \hbox{Simplify}\\
  &= \left(4 \sqrt{2} + \frac{1}{4}\right) - (4 + 1) \\
  &= 4 \sqrt{2} - \frac{19}{4}
\end{align*}

Therefore, the area of the region bounded by $y=12\sqrt{x}$, $y=2/x^3$, and $x=2$ is $4 \sqrt{2} - 19/4$.
```

## Example 4

Find the area of the bounded region enclosed by $y=x$ and $y=x^2$.

```{admonition} Step 1: Find the points of intersection and use them to help sketch the region.
:class: tip, dropdown

\begin{align*}
  x&=x^2 && \text{Set the two functions equal to each other}\\
  0&=x^2-x && \text{Move everything to one side}\\
  0&=x(x-1) && \text{Factor}
\end{align*}

Therefore, the curves intersect when $x=0$ and when $x=1$.

Notice that the points of intersection are used as the left and right boundaries of our region.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}
  \draw[fill=white] (-1.5,-1.5) rectangle ++(6,6);

  % shade region
  \draw[fill=yellow!90] plot[smooth, samples=100, domain=0:2.5 ] (\x,0.4*\x*\x) -- (0,0) -- cycle;

  % draw axes
  \draw[thick,->] (-1,0) -- (4,0) node[above] {$x$};
  \draw[thick,->] (0,-1) -- (0,4) node[right] {$y$};

  % draw curves
  \draw[ultra thick,domain=-1:3,smooth,variable=\x,black] plot ({\x},{0.4*\x*\x}) node[right] {$x^2$};
  \draw[ultra thick, domain=-1:3,smooth,variable=\x,black] plot ({\x},{\x}) node[right] {$x$};
        
  \draw[dashed] (2.5,2.5) -- (2.5,0) node[below] {1};
\end{tikzpicture}
\end{document} 
```

```{admonition} Step 2: Calculate the area of the region.
:class: tip, dropdown

Note that $x \geq x^2$ on $[0,1]$ and therefore the area of the region is given by $\int_0^1 x-x^2 ~dx$.

\begin{align*}
  \int^1_0 x-x^2 ~dx
  &= \left(\frac{x^2}{2} - \frac{x^3}{3}\right)\Biggr|^1_0 && \text{Compute the antiderivative}\\
  &= \left(\frac{1^2}{2} - \frac{1^3}{3}\right)-\left(\frac{0^2}{2} + \frac{0^3}{3}\right) && \text{Plug in the limits of integration}\\
  &= \frac{1}{2} - \frac{1}{3} \\
  &= 1/6
\end{align*}

Therefore, the area of the region bounded by $y=x$ and $y=x^2$ is $1/6$.
```

## Example 5

Find the area of the bounded region enclosed by $y = x^3$ and $y = 4x$.

```{admonition} Step 1: Find the points of intersection and use them to help sketch the region.
:class: tip, dropdown

\begin{align*}
  x^3 &= 4x && \text{Set the functions equal to each other}\\
  x^3 - 4x &= 0 && \text{Subtract $4x$ from both sides}\\
  x(x^2-4) &= 0 && \text{Factor out an }x\\
  x(x-2)(x+2) &= 0 && \text{Factor } x^2 - 4
\end{align*}

Therefore, the curves intersect when $x=-2$, when $x=0$, and when $x=2$.  
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[yscale=0.25]
  \draw[fill=white] (-4,-15) rectangle ++(8,30);

  % draw axes
  \draw[thick,->] (-3,0) -- (3,0) node[above] {$x$};
  \draw[thick,->] (0,-13) -- (0,13) node[right] {$y$};

  % shade region
  \draw[fill=yellow!90] plot[smooth, samples=100, domain=-2:2] (\x,\x*\x*\x) -- cycle;

  % draw curves
  \draw[ultra thick,domain=-2.3:2.3,smooth,variable=\x,black] plot (\x,\x*\x*\x) node[right] {$y=x^3$};
  \draw[ultra thick,domain=-2.5:2.5,smooth,variable=\x,black] plot (\x,4.1*\x) node[right] {$y=4x$};
      
  \draw[dashed] (2,8) -- (2,0) node[below] {2};
  \draw[dashed] (-2,-8) -- (-2,0) node[below] {-2};

  \draw (-1, -2.5) node {$R_1$};
  \draw (1, 2.5) node {$R_2$};
\end{tikzpicture}
\end{document} 
```

```{admonition} Step 2: Calculate the area of each subregion.
:class: tip, dropdown


- Area of region $R_1$. Note that $x^3\geq 4x$ on $[-2,0]$. 

\begin{align*}
  \int^0_{-2} x^3-4x ~dx
  &= \left(\frac{x^4}{4} - 2x^2\right)\Biggr|^0_{-2} \\
  &= \left(\frac{0^4}{4} - 2(0)^2\right)-\left(\frac{(-2)^4}{4}- 2(-2)^2\right) \\
  &= 0 - (4-8) = 4 
\end{align*}

- Area of region $R_2$. Note that $4x\geq x^3$ on $[0,2]$. 

\begin{align*}
  \int^2_{0} 4x-x^3 ~dx
  &= \left(2x^2 -\frac{x^4}{4} \right)\Biggr|^2_{0} \\
  &= \left(2(2)^2 - \frac{2^4}{4}\right)-\left(2(0)^2 - \frac{0^4}{4}\right) \\
  &= (8-4) - 0 = 4 
\end{align*}
```

```{admonition} Step 3: Combine the areas of the different subregions.
:class: tip, dropdown

The area of the region bounded by the curves $y = x^3$ and $y = 4x$ on the interval $[-1, 3]$ is 

$$4 + 4 = 8.$$
```