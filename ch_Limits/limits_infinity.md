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
# Limits at Infinity

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

## Definitions

```{admonition} Definition
:class: info

The _**limit of $f(x)$ as $x$ approaches (positive) infinity is equal to the finite number $L$**_, denoted by

$$\lim_{x\to \infty} f(x) = L $$ 

if $f(x)$ can be made as close to $L$ as we want by taking $x$ large enough.
```

```{admonition} Definition
:class: info

The _**limit of $f(x)$ as $x$ approaches negative infinity is equal to the finite number $M$**_, denoted by 

$$\lim_{x\to -\infty} f(x) = M $$ 

if $f(x)$ can be made as close to $M$ as we want by taking $x$ to be negative and sufficiently large in absolute value.
```


### Example 1

````{admonition} A limit at infinity
:class: tip

The following graph illustrates a function $f(x)$ that approaches a value of 400 as $x$ increases without bound.  In other words, 

$$\lim\limits_{x\to \infty} f(x) = 400.$$

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_limits_infinity_example_1.png
:alt: Graph of a function with a limit at infinity
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points 50, 100, 150, 200, 250, and 300 marked. There is a vertical y-axis with the points 100, 200, 300, and 400. There is a horizontal red dotted line at y = 400. The graph of a function is plotted on these axes. The function is increasing and approaches the horizontal dotted line from below, but never reaches it.  The closer the graph of the function gets to the horizontal dotted line, the slower the graph of the function increases.
```

````
<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2.5]
\tikzstyle{every node}=[font=\large]
 
% create a white background, with a black frame
%\draw [fill=white,white] (-0.75,-0.5) rectangle (6.75,3.75); 

% draw a grid
\draw[step=2.5mm, lightgray, thin] (0,0) grid (6.49,3.49); 

% draw axes
\draw [->,thick] (0,0) -- (6.5,0) node[below] {$x$}; 
\draw [->,thick] (0,0) -- (0,3.5) node[right] {$y$};

% tick marks
\foreach \x/\label in {1/50,2/100,3/150,4/200,5/250,6/300} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\label};
\foreach \y/\label in {0.75/100,1.5/200,2.25/300,3/400} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\label};

% plot curve
\draw [dashed, red,ultra thick](0,3) -- (6.5,3);
\draw [ultra thick] (0,0.4) .. controls (2,0.8) and (2,2.9) .. (6.5,2.95) node[below left] {\large $f(x)$};

\end{tikzpicture}
\end{document} 
```
-->







## Properties of Limits at Infinity

```{admonition} Properties
:class: info

All {ref}`lim:prop_lim` apply when $a$ is replaced with $\infty$ or $-\infty$.  Furthermore, the following additional properties are especially useful when evaluating limits at infinity.  For all $n>0$, we have

- $\lim\limits_{x \to \infty} \dfrac{1}{x^n}=0 $
- $\lim\limits_{x \to -\infty} \dfrac{1}{x^n}=0$, provided that $x^n$ is defined for $x<0$.
```

### Example 2
````{admonition} Limits at infinity of $1/x$
:class: tip

Notice how the graph of $y=1/x$ approaches the $x$-axis as $x$ approaches positive and negative infinity.  In other words,

$$\lim_{x\to -\infty} \frac{1}{x} = 0  ~~~~ \hbox{and} ~~~~~ \lim_{x\to \infty} \frac{1}{x} = 0.$$

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_limits_infinity_example_2.png
:alt: Graph of a $1/x$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -5, -3, -1, 1, 3, and 5 marked. There is a vertical y-axis with the points -1 and 1 marked. The graph of the function y = 1/x is plotted on these axes. This function comes in just below the x-axis from the left, decreases to negative infinity as x approaches zero from the left.  The function is not defined at x = 0.  As x increases past zero, the function comes down from positive infinity and decreases towards the x-axis as it continues to the right.
```

````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2]
\tikzstyle{every node}=[font=\large]
 
% create a white background, with a black frame
%\draw [fill=white,white] (-7.5,-2) rectangle (7.5,2.5); 

% draw a grid
\draw[step=5mm, lightgray, thin] (-6.99,-1.99) grid (6.99,1.99); 
%\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); 

% draw axes
\draw [->,thick] (-7,0) -- (7,0) node[below] {$x$}; 
\draw [->,thick] (0,-2) -- (0,2) node[right] {$y$};

% tick marks
\foreach \x in {-5,-3,-1,1,3,5} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\foreach \y in {-1,1} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\y};

% plot curve
\clip (-7,-2) rectangle (7,2);
\draw[ultra thick,domain=-7:-0.1,smooth,samples=100] plot (\x,{1/\x}); 
\draw[ultra thick,domain=0.1:7,smooth,samples=100] plot (\x,{1/\x});

\end{tikzpicture}
\end{document} 
```
-->



### Example 3
````{admonition} Limits at infinity of $1/\sqrt{x}$
:class: tip

Notice how the graph of $y=1/\sqrt{x}$ approaches the $x$-axis as $x$ approaches positive infinity.  In other words,

$$\lim_{x\to \infty} \frac{1}{\sqrt{x}} = 0.$$

Furthermore, there is no discussion of the limit as $x$ approaches negative infinity since $\sqrt{x}$ is not defined for negative values of $x$.


::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_limits_infinity_example_3.png
:alt: Graph of a $1/\sqrt{x}$
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -5, -3, -1, 1, 3, and 5 marked. There is a vertical y-axis with the points 1 and 2 marked. The graph of the function one over square root x is plotted on these axes. The graph does not appear above negative x values. The function is not defined at x = 0.  As x increases past zero, the function comes down from positive infinity and decreases towards the x-axis as it continues to the right.
```
````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2]
\tikzstyle{every node}=[font=\large]
 
% create a white background, with a black frame
%\draw [fill=white] (-7.5,-1.5) rectangle (7.5,3.5); 

% draw a grid
\draw[step=5mm, lightgray, thin] (-6.99,0) grid (6.99,2.99); 
%\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); 

% draw axes
\draw [->,thick] (-7,0) -- (7,0) node[below] {$x$}; 
\draw [->,thick] (0,-1) -- (0,3) node[right] {$y$};

% tick marks
\foreach \x in {-5,-3,-1,1,3,5} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\foreach \y in {1,2} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\y};

% plot curve
\clip (-7,-1) rectangle (7,3);
\draw[ultra thick,domain=0.1:7,smooth,samples=100] plot (\x,{1/pow(\x,0.5)});

\end{tikzpicture}
\end{document} 
```
-->

(lim:lim_infinity_rational)=
## Limits at Infinity of Rational Functions

```{admonition} How to Compute the Limit at Infinity of a Rational Function
:class: info

For rational functions, the limit as $x$ approaches positive or negative infinity can be determined by comparing the degree of the polynomial in the numerator to the degree of the polynomial in the denominator.

For infinite limits of Rational Functions, if the 
- highest power is in the denominator, then the limit will equal $0$
- highest power is in the numerator, then the limit will equal $\pm\infty$ (DNE)
- highest power is the same in both the numerator and denominator, then the limit will equal the ratio of the leading coefficients, i.e. the ratio of the coefficients in front of the highest powers in the numerator and the denominator.
```

### Example 4

````{admonition} Limits at infinity of rational functions
:class: tip

1. $\displaystyle\lim_{x\to\infty}\frac{x+3}{6x^2+3x+1}$
```{dropdown} Answer
Since the highest power of $x$ is in the denominator, the limit exists and is equal to $0$.
```

2. $\displaystyle\lim_{x\to-\infty}\frac{6x^{3}+3}{x^{2}+4x-7}$ 
```{dropdown} Answer
Since the highest power of $x$ is in the numerator, the limit does not exist.  

Furthermore, by comparing the leading terms in the numerator and the denominator, we can determine whether the limit goes to postive or negative infinity.  Since the leading term in the numerator, $6x^3$, is negative as $x$ goes to negative infinity and the leading term in the denominator, $x^2$, is postive as $x$ goes to negative infinity, the ratio of the two (negative/positive) is negative.  Therefore, we can conclude that the limit goes to negative infinity.   
```
3. $\displaystyle\lim_{x\to\infty}\frac{4x^5+3x-8}{9x^5-6x^3}$
```{dropdown} Answer
Since the highest power in the numerator and in the denominator are the same, the limit exists and is equal to the ratio of leading coefficients, which in this case is $4/9$.
```
````