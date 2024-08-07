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
# Asymptotes

## Definitions

```{admonition} Definition
:class: info

The line $x=a$ is a _**vertical asymptote**_ of the function $f$ if

$$\lim_{x \to a^+} f(x)= \pm \infty \qquad \text{or} \qquad
\lim_{x \to a^-} f(x)= \pm \infty$$
```

```{admonition} Vertical Asymptotes of a Rational Function
:class: note

The rational function 

$$f(x) = \dfrac{g(x)}{h(x)}$$ 

has a vertical asymptote at $x=a$ if $h(a) = 0$ and $g(a) \neq 0$. 

We can find the vertical asymptotes by factoring $g(x)$ and $h(x)$ and then cancelling common factors.  Any value of $x$ that makes the denominator equal to zero, after cancellation, corresponds to a vertical asymptote.
```


```{admonition} Definition
:class: info

The line $y=b$ is a _**horizontal asymptote**_ of the function $f$ if:

$$\lim_{x \to \infty} f(x)= b \qquad \text{or} \qquad \lim_{x \to -\infty} f(x)= b$$

Horizontal asymptotes describe the behavior of the graph of $f$ for large positive and large negative values of $x$.  The graph of $f$ should approach the horizontal asymptote for large values of $x$.  

A function can have at most two different horizontal asymptotes.
```


```{admonition} Horizontal Asymptotes of a Rational Function
:class: note

Horizontal asymptotes of rational functions are determined by computing the limit at infinity of the given rational function, which can be accomplished by comparing the degree of the numerator to the degree of the denominator.  See {ref}`lim:lim_infinity_rational` for a review of this process.
```


### Example 1

````{admonition} Graph of vertical and horizontal asymptotes
:class: tip

The following graph is an example of a function that has vertical asymptotes at $x=-1$ and $x=3$ and a horizontal asymptote at $y=1$.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_curvesketching_asymptotes.png
:alt: Graph of function with vertical and horizontal asymptotes$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -1 and 3 marked. There is a vertical y-axis. There is a grid in the background of 1/2 by 1/2 squares. There is a blue dashed horizontal line at y = 1. There is a red dashed vertical line at x = -1. There is a red dashed vertical line at x = 3. The graph of a function is plotted on these axes. From left to right, the function decreases from the blue dashed line and goes to negative infinity as it approaches the red dashed line at x = -1, comes down from positive infinity to the right of -1, goes down to negative infinity as it approaches the red dashed line at x = 3, and comes down from positive infinity at x = 3 towards the blue dashed line as it heads off to the right.
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
\usetikzlibrary{arrows}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}[baseline=70,ultra thick,smooth,domain=-4:4,variable=\x,scale=1.5]

% create a white background with a black frame
\draw [thin,fill=white] (-5,-2) rectangle (7,4);  

% draw grid
\draw[xstep=0.5cm, ystep=0.5cm, lightgray, thin] (-4.99,-1.99) grid (6.99,3.99); 

% draw axes
\draw [->,thick] (-5,0) -- (7,0);
\draw [->,thick] (0,-2) -- (0,4);


\clip (-5,-2) rectangle (7,4);

% x / (x^2-4) + 1
\draw plot [domain=-5:-1.1] (\x,{1 + (\x-1) / ((\x-1)*(\x-1) - 4)}); 
\draw plot [domain=-0.9:2.9] (\x,{1 + (\x-1) / ((\x-1)*(\x-1) - 4)}); 
\draw plot [domain=3.1:7] (\x,{1 + (\x-1) / ((\x-1)*(\x-1) - 4)}); 

% asymptotes
\draw[dashed,red,thick] (-1,-2) -- (-1,4);
\draw[dashed,red,thick] (3,-2) -- (3,4);
\draw[dashed,blue,thick] (-5,1) -- (7,1);

% tick marks
\foreach \x in {-1,3} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below, scale=1.8] {$\x$};

\end{tikzpicture}
\end{document}
```
-->


### Example 2

````{admonition} Find asymptotes
:class: tip

Find the horizontal and vertical asymptotes of $f(x)=\dfrac{7x^2+2x+1}{2x^2+3x-9}$.


```{dropdown} **Step 1:** &nbsp;  Horizontal Asymptotes.

Since the degree of the numerator and the denominator are the same, both limits at infinity are equal to the ratio of leading coefficients.

$$\lim_{x\to -\infty} f(x) = \frac{7}{2} = \lim_{x\to \infty} f(x)$$

Therefore, $y=7/2$ is the only horizontal asymptote of $f$.
```


```{dropdown} **Step 2:** &nbsp; Vertical Asymptotes.

Factor and simplify $f(x)$. 

\begin{align*}
f(x)
&= \frac{7x^2+2x+1}{2x^2+3x-9} \\ 
&= \frac{7x^2+2x+1}{(2x-3)(x+3)} && \text{AC grouping}
\end{align*}

Therefore $x =-3$ and $x=3/2$ are possible vertical asymptotes.  

Since the numerator cannot be factored, to make sure these values of $x$ correspond to vertical asymptotes, plug them into the numerator, $g(x) = 7x^2+2x+1$, and see if they also make the numerator equal to zero.  

Since $g(-3) \neq 0 $ and $g(3/2) \neq 0$, $x=-3$ and $x=3/2$ are both vertical asymptotes.
```
````



### Example 3

````{admonition} Find asymptotes
:class: tip

Find the horizontal and vertical asymptotes of $f(x)=\dfrac{x^4-x^2}{x^3 + x^2 - 2 x}$.


```{dropdown} **Step 1:** &nbsp;  Horizontal Asymptotes.

Since the degree of the numerator, $4$, is larger than the degree of the denominator, $3$, both limits at infinity do not exist.

$$\lim_{x\to -\infty} f(x) = -\infty \qquad \lim_{x\to \infty} f(x) = \infty$$

Therefore, $f$ does not have any horizontal asymptotes.
```


```{dropdown} **Step 2:** &nbsp; Vertical Asymptotes.

Factor and simplify $f(x)$.

\begin{align*}
f(x) 
&= \frac{x^2(x^2-1)}{x(x^2 + x - 2)} && \text{pull out common factors}\\
&= \frac{x^2(x-1)(x+1)}{x(x+2)(x-1)} && \text{factor numerator and denominator}\\
&=  \frac{x^{\cancel{2}}\cancel{(x-1)}(x+1)}{\cancel{x}(x+2)\cancel{(x-1)}} && \text{cancel common factors}\\
&= \frac{x(x+1)}{x+2} 
\end{align*}

Since only $x=-2$ makes the denominator equal to zero, after cancellation, $x=-2$ is the only vertical asymptote.
```
````



