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

```{admonition} Definition
:class: info

The function $f(x)$ has the limit $L$ as $x$ increases without bound (as $x$ approaches infinity), 

$$\lim_{x\to \infty} f(x) = L $$ 

if $f(x)$ can be made as close to $L$ by taking $x$ large enough.

Similarly, the function $f(x)$ has the limit $M$ as $x$ decreases without bound (as $x$ approaches negative infinity), 

$$\lim_{x\to -\infty} f(x) = M $$ 

if $f(x)$ can be made as close to $M$ by taking $x$  to be negative and sufficiently large in absolute value.
```

## Example 1

The following graph illustrates a function $f(x)$ that approaches a value of 400 as $x$ increases without bound.  In other words, 

$$\lim\limits_{x\to \infty} f(x) = 400.$$

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







## Properties of Limits at Infinity

All previous properties for limits apply when $a$ is replaced with $\infty$ or $-\infty$.  Furthermore, the following additional properties are especially useful when evaluating limits at infinity.  For all $n>0$, we have

- $\lim\limits_{x \to \infty} \dfrac{1}{x^n}=0 $
- $\lim\limits_{x \to -\infty} \dfrac{1}{x^n}=0$, provided that $x^n$ is defined for $x<0$.


## Example 2

Notice how the graph of $y=1/x$ approaches the $x$-axis as $x$ approaches positive and negative infinity.  In other words,

$$\lim_{x\to -\infty} \frac{1}{x} = 0  ~~~~ \hbox{and} ~~~~~ \lim_{x\to \infty} \frac{1}{x} = 0.$$

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



## Example 3

Notice how the graph of $y=1/\sqrt{x}$ approaches the $x$-axis as $x$ approaches positive infinity.  In other words,

$$\lim_{x\to \infty} \frac{1}{\sqrt{x}} = 0.$$

Furthermore, there is no discussion of the limit as $x$ approaches negative infinity since $\sqrt{x}$ is not defined for negative values of $x$. 

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


## Limits at Infinity of Rational Functions

For Rational Functions, a limit at infinity, whether it be $\displaystyle\lim_{x\to\infty}$ or $\displaystyle\lim_{x\to -\infty}$, can be determined by comparing the degree of the polynomial in the numerator to the degree of the polynomial in the denominator.

For infinite limits of Rational Functions, if the 
- highest power is in the denominator, then the limit will equal $0$
- highest power in the numerator, then the limit will equal $\pm\infty$ (DNE)
- highest power is the same in both the numerator and denominator, then the limit will equal the ratio of the leading coefficients, i.e. the ratio of the coefficients in front of the highest powers in the numerator and the denominator.

## Example 4

Applying the guidelines:
1. $\displaystyle\lim_{x\to\infty}\frac{x+3}{6x^2+3x+1}$ = 0 (highest power is in denominator)   <br>  &nbsp;

2. $\displaystyle\lim_{x\to-\infty}\frac{6x^{3}+3}{x^{2}+4x-7}$ = $-\infty$ or DNE (highest power is in numerator)  <br>  &nbsp;

3. $\displaystyle\lim_{x\to\infty}\frac{4x^5+3x-8}{9x^5-6x^3}$ = $4/9$ (highest powers are the same)  