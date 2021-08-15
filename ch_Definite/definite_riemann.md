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
# Riemann Sums and the Definite Integral

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

## Area Under a Curve and Riemann Sums

Consider trying to compute the area of a region (below left) between the graph of $y=f(x)$ and the $x$-axis on the interval $[a,b]$.

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[xscale=3,yscale=3.0]
  \draw[thick,->] (-0.6,0) -- (1.1,0) node[right] {$x$};
  \node at (-0.5, -0.1){$a$};
  \node at (1, -0.1) {$b$};
  \draw[fill=yellow!90] (-0.5,0) -- plot[smooth, samples=100, domain=-0.5:1 ] (\x,\x*\x/1.5 + 0.25) |- (-0.5,0);
  \draw[ultra thick,domain=-0.5:1,smooth,variable=\x,black] plot (\x,\x*\x/1.5 + 0.25) node[right]{$f(x)$};
\end{tikzpicture}
~~~
\begin{tikzpicture}[xscale=3,yscale=3.0]
  \node at (-0.5, -0.1){$a$};
  \node at (1, -0.1) {$b$};

  \draw[fill=yellow!90] (-0.5,0) rectangle ++(0.375,{(-0.3)^2 / 1.5 + 0.25});
  \draw [dashed] (-0.3,0) node[below] {$x_1$} -- (-0.3,{(-0.3)^2 / 1.5 + 0.25});

  \draw[fill=yellow!90] (-0.125,0) rectangle ++(0.375,{(0.0)^2 / 1.5 + 0.25});
  \draw [dashed] (0.0,0) node[below] {$x_2$} -- (0.0,{(0.0)^2 / 1.5 + 0.25});
        
  \draw[fill=yellow!90] (0.250,0) rectangle ++(0.375,{(0.5)^2 / 1.5 + 0.25});
  \draw [dashed] (0.5,0) node[below] {$x_3$} -- (0.5,{(0.5)^2 / 1.5 + 0.25});

  \draw[fill=yellow!90] (0.625,0) rectangle ++(0.375,{(0.8)^2 / 1.5 + 0.25});
  \draw [dashed] (0.8,0) node[below] {$x_4$} -- (0.8,{(0.8)^2 / 1.5 + 0.25});
        
  \draw[thick,->] (-0.6,0) -- (1.1,0) node[right] {$x$};
  \draw[ultra thick,domain=-0.5:1,smooth,variable=\x,black] plot (\x,\x*\x/1.5 + 0.25) node[right]{$f(x)$};

\end{tikzpicture}
\end{document} 
```

A *Riemann sum* uses rectangles (above right) to approximate the desired area in the following manner.  Start by selecting a value for $n$, which is the number of rectangles. Then break up the interval $[a,b]$ into $n$ subintervals, each having width $\Delta x = (b-a)/n$.  Each subinterval corresponds to the base of a rectangle where $\Delta x$ is the width of the rectangle. Next, pick one value, $x_i$, from each subinterval, and evaluate $f(x_i)$ to determine the height of the corresponding rectangle.

The total area of the $n$ rectangles is given by

$$[f(x_1) + f(x_2) + \cdots + f(x_n)] \Delta x$$

which is called a {\it Riemann Sum}. It approximates the area of the region between the graph of $y=f(x)$ and the $x$-axis on the interval $[a,b]$.

Here are several different ways to select the values $x_1,\ldots,x_n$.

- **Right Riemann Sum**: $x_1,\ldots, x_n$ are the right endpoints of the $n$ subintervals.
- **Left Riemann Sum**: $x_1,\ldots, x_n$ are the left endpoints of the $n$ subintervals.
- **Midpoint Rule**: $x_1,\ldots, x_n$ are the midpoints of the $n$ subintervals.

In general, a Riemann sum approximates the value of a definite integral (see below).

## The Limit Definition of a Definite Integral

```{admonition} Definition
:class: info

Suppose $f$ is a continuous function on $[a,b]$.  The **definite integral** of $f$ from $a$ to $b$, denoted by $\int_a^b f(x) ~dx$, is defined as

$$\int_a^b f(x) ~dx = \lim_{n\to \infty} [f(x_1) + f(x_2) + \cdots + f(x_n)] \Delta x$$

where the values of $x_1,x_2,\ldots, x_n$ are chosen from the $n$ subintervals of $[a,b]$ of equal width $\Delta x = \dfrac{b-a}{n}$.

The values $a$ and $b$ are referred to as **limits of integration**.
```

## Geometric Interpretation of the Definite Integral

If $f(x)\geq 0$ is continuous on $[a,b]$, then $\int_a^b f(x) ~dx$ is equal to the area of the region between the graph of $f$ and the $x$-axis on $[a,b]$.

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[scale=1.5]

  % shade region
  \draw[fill=yellow!90,domain=0.5:5.5,smooth,variable=\x] (0.5,0) -- plot ({\x},{1.2 + 0.25*sin(\x r)}) |- cycle;

  % draw axis
  \draw[thick,->] (-1,0) -- (7,0) node[right] {$x$};

  % draw curve
  \draw[ultra thick,domain=0:6,smooth,variable=\x,black] plot ({\x},{1.2 + 0.25*sin(\x r)}) node[right]{$y=f(x)$};

  \node at (0.5, -0.4) [above] {$a$};
  \node at (5.5, -0.4) [above] {$b$};      
        
  \node at (3, 0.6) {Area $ = \displaystyle \int_a^b f(x)dx$};
\end{tikzpicture}
\end{document} 
```

In general, $\int_a^b f(x) ~dx$ can be interpreted as the area of the regions that are below the graph of $f$ and above the $x$-axis minus the area of the regions that are below the $x$-axis and above the graph of $f$.

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[scale=1.5]

  % shade region
  \draw[fill=yellow!90,domain=0.5:5.5,smooth,variable=\x] (0.5,0) -- plot ({\x},{0.05 - 0.7*cos(1.8*0.9^(abs(\x-3))*(\x - 3.0) r)}) |- cycle;

  \draw[fill=green!90,domain=2.09:3.91,smooth,variable=\x] plot ({\x},{0.05 - 0.7*cos(1.8*0.9^(abs(\x-3))*(\x - 3.0) r)}) -- cycle;

  % draw axis
  \draw[thick,->] (-1,0) -- (7,0) node[right] {$x$};

  % draw curve
  \draw[ultra thick,domain=0:6,smooth,variable=\x,black] plot ({\x},{0.05 - 0.7*cos(1.8*0.9^(abs(\x-3))*(\x - 3.0) r)}) node[right]{$y=f(x)$};

  \node at (1.1, 0.3) {$R_1$};
  \node at (3, -0.3) {$R_2$};
  \node at (4.9, 0.3) {$R_3$};

  \node at (0.5, -0.4) [above] {$a$};
  \node at (5.5, -0.4) [above] {$b$};      
\end{tikzpicture}
\end{document} 
```

$$\int_a^b f(x) ~dx = \hbox{Area of $R_1$} - \hbox{Area of $R_2$} + \hbox{Area of $R_3$}$$

## Properties of the Definite Integral

```{admonition} Properties of the Definite Integral
:class: info

If $f$ and $g$ are continuous on $[a,b]$ and $c$ is a constant, then

- $\displaystyle \int_a^a f(x) ~dx = 0$
- $\displaystyle \int_a^b f(x) ~dx = -\int_b^af(x) ~dx$
- $\displaystyle \int_a^b cf(x) ~dx = c\int_a^b f(x) ~dx$
- $\displaystyle \int_a^b f(x) \pm g(x) ~dx = \int_a^b f(x) ~dx \pm \int_a^b g(x) ~dx$
- $\displaystyle \int_a^b f(x) ~dx = \int_a^c f(x) ~dx + \int_c^b f(x) ~dx$
```

## Example 1

Use a right Riemann sum, left Riemann sum, and midpoint rule to approximate the area under the graph of $y=x^2$ on $[1,3]$ using 4 subintervals.

```{admonition} Step 1: Find the length of each interval, $\Delta x$, and break up $[1,3]$ into 4 subintervals of length $\Delta x$.
:class: tip, dropdown

$$\Delta x = \frac{b - a}{n} = \frac{3 - 1}{4} = \frac{1}{2}.$$

The endpoints of the subintervals are labeled below the number line while the midpoints of each subinterval are labeled above the number line. Each midpoint is calculated by computing the average of the two endpoints of the corresponding subinterval.
```

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[baseline=-0.5ex,scale=4.5]
  \draw[thick,->] (0.75,0) -- (3.25,0);
  \foreach \x in {1, 2, 3}{
    \draw [ultra thick] (\x cm,1.0pt) -- (\x cm,-1.0pt) node[below]{\small$\x$};
  }
  \foreach \x in {3, 5}{
    \draw [ultra thick] (0.5*\x cm,1.0pt) -- (0.5*\x cm,-1.0pt) node[below]{\small$\x/2$};
  }
  \foreach \x in {5, 7,9,11}{
    \draw [thick] (0.25*\x cm,-0.5pt) -- (0.25*\x cm,0.5pt) node[above]{\small$\x/4$};
  }
\end{tikzpicture}
\end{document} 
```

```{admonition} Step 2: Use a right Riemann sum to approximate the area. 
:class: tip, dropdown

\begin{align*}
  \hbox{Area} &\approx \left[ f(3/2) + f(2) + f(5/2) + f(3)\right]\Delta x \\
  &= \left[\left(\frac{3}{2}\right)^2 + 2^2 + \left(\frac{5}{2}\right)^2 + 3^2 \right] \frac{1}{2}\\
  &= \left[\frac{9}{4} + \frac{16}{4} + \frac{25}{4} + \frac{36}{4}\right] \frac{1}{2}\\
  % &= \frac{1}{2}\cdot \frac{86}{4} \\
  &= 43/4
\end{align*}

Therefore, the area under the graph of $y=x^2$ on $[1,3]$ is approximately $43/4 = 10.75$.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[xscale=1.7,yscale=0.3]

  % create a white background, with a black frame
  \draw [fill=white] (0.6,-3) rectangle (3.4,10); 

  % draw Riemann Sum - Right Riemann sum 
  \foreach \x in { 1,1.5,2,2.5} {
    \draw [fill=yellow!90] (\x,0) rectangle +(0.5,{(\x+0.5)*(\x+0.5)});
  }

  % draw axes
  \draw [->,thick] (0.75,0) -- (3.25,0) node[below] {$x$}; 

  % tick marks
  \foreach \x in {2,3} 
    \draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
  \foreach \x in {3, 5}{
    \draw [ultra thick] (0.5*\x cm,2pt) -- (0.5*\x cm,-2pt) node[below]{$\frac{\x}{2}$};
    }

  % plot function
  \draw [ultra thick,smooth,variable=\x] plot [domain=1:3] (\x,\x*\x);

\end{tikzpicture}
\end{document} 
```

```{admonition} Step 3: Use a left Riemann sum to approximate the area.
:class: tip, dropdown

\begin{align*}
  \hbox{Area} &\approx \left[ f(1) + f(3/2) + f(2) + f(5/2)\right] \Delta x \\
  &= \left[1^2 + \left(\frac{3}{2}\right)^2 + 2^2 + \left(\frac{5}{2}\right)^2 \right] \frac{1}{2} \\
  &= \left[\frac{4}{4} + \frac{9}{4} + \frac{16}{4} + \frac{25}{4}\right]\frac{1}{2} \\
  %&= \frac{1}{2}\cdot \frac{54}{4} \\
  &= 27/4
\end{align*}

Therefore, the area under the graph of $y=x^2$ on $[1,3]$ is approximately $27/4 = 6.75$.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[xscale=1.7,yscale=0.3]

  % create a white background, with a black frame
  \draw [fill=white] (0.6,-3) rectangle (3.4,10); 

  % draw Riemann Sum - Left Riemann sum 
  \foreach \x in { 1,1.5,2,2.5} {
    \draw [fill=yellow!90] (\x,0) rectangle +(0.5,{(\x+0)*(\x+0)});
  }

  % draw axes
  \draw [->,thick] (0.75,0) -- (3.25,0) node[below] {$x$}; 

  % tick marks
  \foreach \x in {1,2} 
    \draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
  \foreach \x in {3, 5}{
    \draw [ultra thick] (0.5*\x cm,2pt) -- (0.5*\x cm,-2pt) node[below]{$\frac{\x}{2}$};
    }

  % plot function
  \draw [ultra thick,smooth,variable=\x] plot [domain=1:3] (\x,\x*\x);

\end{tikzpicture}
\end{document} 
```

```{admonition} Step 4: Use the midpoint rule to approximate the area.
:class: tip, dropdown

\begin{align*}
  \hbox{Area} &\approx \left[ f(5/4) + f(7/4) + f(9/4) + f(11/4)\right]\Delta x \\
  &= \left[\left(\frac{5}{4}\right)^2 + \left(\frac{7}{4}\right)^2 + \left(\frac{9}{4}\right)^2 + \left(\frac{11}{4}\right)^2 \right] \frac{1}{2} \\
  &= \left[\frac{25}{16} + \frac{49}{16} + \frac{81}{16} + \frac{121}{16}\right] \frac{1}{2} \\
  %&= \frac{1}{2}\cdot \frac{276}{16} \\
  &= 69/8
\end{align*}

Therefore, the area under the graph of $y=x^2$ on $[1,3]$ is approximately $69/8 = 8.625$.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

\begin{tikzpicture}[xscale=1.7,yscale=0.3]

  % create a white background, with a black frame
  \draw [fill=white] (0.6,-3) rectangle (3.4,10); 

  %% draw a grid
  %\draw[step=2mm, lightgray, thin] (-0.5,-0.7) grid (5.5,1.99); 
  %\draw[step=1cm, gray] (-0.5,-0.7) grid (5.5,1.99); 

  % draw Riemann Sum - Midpoint rule 
  \foreach \x in { 1,1.5,2,2.5} {
    \draw [fill=yellow!90] (\x,0) rectangle +(0.5,{(\x+0.25)*(\x+0.25)});
  }

  % draw axes
  \draw [->,thick] (0.75,0) -- (3.25,0) node[below] {$x$}; 

  % tick marks
  \foreach \x in {5, 7,9,11}{
    \draw [thick] (0.25*\x cm,-1pt) -- (0.25*\x cm,1pt) node[below]{$\frac{\x}{4}$};
    \draw [dashed] (0.25*\x cm,0) -- (0.25*\x cm,\x*\x/16);
    }

  % plot function
  \draw [ultra thick,smooth,variable=\x] plot [domain=1:3] (\x,\x*\x);

\end{tikzpicture}
\end{document} 
```