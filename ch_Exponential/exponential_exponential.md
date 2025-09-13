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
# Exponential Functions

## Definition and Properties of Exponential Functions

```{admonition} Definition of an Exponential Function
:class: info

For any constant $b>0$ and $b\neq 1$, the function 

$$f(x) = b^x$$ 

is called the _**exponential function with base $b$**_.

```

```{admonition} Properties of Exponential Functions
:class: info

For a function $y = b^x$, the following properties hold:

- Its domain is $(-\infty,\infty)$ and range is $(0,\infty)$.
- Its graph passes through the point $(0,1)$ (i.e., $b^0 = 1$).
- It is continuous on $(-\infty,\infty)$.
- If $b>1$
  - $b^x$ is increasing on $(-\infty,\infty)$
  - $\lim\limits_{x\to -\infty} b^x = 0$  and $\lim\limits_{x\to \infty} b^x = \infty$ <br><br>
- If $0 < b <1$
  - $b^x$ is decreasing on $(-\infty,\infty)$
  - $\lim\limits_{x\to -\infty} b^x = \infty$  and $\lim\limits_{x\to \infty} b^x = 0$
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
<a href="https://youtu.be/q2j7M7l41LE" target="_blank">Introduction to Exponential Functions</a> (Links to an external site) <br>
A review of the definition, properties, graph, and real world applications of exponential functions.
:::
::::
````

### Example 1
````{admonition} Graphs of exponential growth functions
:class: tip

The graphs of the exponential functions $5^x$, $2^x$, and $(3/2)^x$ are all shown below.  Since the base associated with each function is greater than one, each exponential function is increasing and goes to infinity as $x$ goes to infinity.  For this reason, exponential functions with a base greater than one are referred to as **exponential growth functions**.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_exponential_functions_exponential_growth.png
:alt: Graphs of various exponential growth functions
:width: 500px

```
:::
::::
```{dropdown} Long Text Description

The graphs of 5 to the power of x, 2 to the power of x, and 3/2 to the power of x are all shown on the same coordinate axes.  The values -3, -1, 1, and 3 are marked on the x-axis and the values 1, 2, 3, and 4 are marked on the y-axis.

From left-to-right, the graph of y = 5 to the power of x starts very close to and above the x-axis.  The graph slowly increases to the point (0,1) and continues to increase for positive values of x.  The steepness of the curve also increases from left-to-right.

From left-to-right, the graph of y = 2 to the power of x starts very close to and above the graph of y = 5 to the power of x.  The graph slowly increases to the point (0,1), at which point it crosses the graph of y = 5 to the power of x.  It continues to increase for positive values of x, staying below the graph of y = 5 to the power of x.  The steepness of the curve also increases from left-to-right, but it is not as steep as the graph of y = 5 to the power of x.

From left-to-right, the graph of y = 3/2 to the power of x starts very close to and above the graph of y = 2 to the power of x.  The graph slowly increases to the point (0,1), at which point it crosses the graphs of y = 5 to the power of x and y = 2 to the power of x.  It continues to increase for positive values of x, staying below the graph of y = 2 to the power of x.  The steepness of the curve also increases from left-to-right, but it is not as steep as the graph of y = 2 to the power of x.
```
````

<!--
\begin{tikzpicture}[scale=1.4]
\tikzstyle{every node}=[font=\large]
 
% create a white background, with a black frame
%\draw [fill=white] (-7.5,-1.5) rectangle (7.5,3.5); 

% draw a grid
\draw[step=5mm, lightgray, thin] (-4.99,0) grid (4.99,4.99); 
%\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); 

% draw axes
\draw [->,thick] (-5,0) -- (5,0) node[below] {$x$}; 
\draw [->,thick] (0,-0.5) -- (0,5) node[right] {$y$};

% tick marks
\foreach \x in {-3,-1,1,3} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\foreach \y in {1,2,3,4} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\y};

% plot curve
\clip (-5,-1) rectangle (5,5);
\draw[ultra thick,domain=-5:3.96,smooth,samples=100,red] plot (\x,{pow(1.5,\x)}) node [below right,fill=white] {$\left(\frac{3}{2}\right)^x$};
\draw[ultra thick,domain=-5:2.316,smooth,samples=100,blue] plot (\x,{pow(2,\x)}) node [below right,fill=white] {$2^x$};
\draw[ultra thick,domain=-5:1,smooth,samples=100] plot (\x,{pow(5,\x)}) node [below right,fill=white] {$5^x$};

\end{tikzpicture}

-->


### Example 2
````{admonition} Graphs of exponential decay functions
:class: tip

The graphs of the exponential functions $(2/3)^x$, $(1/2)^x$, and $(1/5)^x$ are all shown below.  Since the base associated with each function is between zero and one, each exponential function is decreasing and goes to zero as $x$ goes to infinity.  For this reason, exponential functions with a base between zero and one are referred to as **exponential decay functions**


::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_exponential_functions_exponential_decay.png
:alt: Graphs of various exponential decay functions
:width: 500px
```
:::
::::
```{dropdown} Long Text Description
The graphs of 2/3 to the power of x, 1/2 to the power of x, and 1/5 to the power of x are all shown on the same coordinate axes.  The values -3, -1, 1, and 3 are marked on the x-axis and the values 1, 2, 3, and 4 are marked on the y-axis.

From left-to-right, the graph of y = 2/3 to the power of x starts very far above the x-axis.  The graph quickly decreases to the point (0,1) and continues to decrease for positive values of x, getting closer and closer to the x-axis, but always staying above it.  The steepness of the curve decreases from left-to-right.

From left-to-right, the graph of y = 1/2 to the power of x starts very far above the graph of y = 2/3 to the power of x.  The graph quickly decreases to the point (0,1), at which point it crosses the graph of y = 2/3 to the power of x.  It continues to decrease for positive values of x, staying below the graph of y = 2/3 to the power of x while getting closer and closer to the x-axis from above.  The steepness of the curve also decreases from left-to-right.

From left-to-right, the graph of y = 1/5 to the power of x starts very far above the graph of y = 1/2 to the power of x.  The graph quickly decreases to the point (0,1), at which point it crosses the graphs of y = 1/2 to the power of x and y = 2/3 to the power of x.  It continues to decrease for positive values of x, staying below the graph of y = 1/2 to the power of x while getting closer and closer to the x-axis from above.  The steepness of the curve also decreases from left-to-right.
```
````

<!--
\begin{tikzpicture}[scale=1.4]
\tikzstyle{every node}=[font=\large]
 
% create a white background, with a black frame
%\draw [fill=white] (-7.5,-1.5) rectangle (7.5,3.5); 

% draw a grid
\draw[step=5mm, lightgray, thin] (-4.99,0) grid (4.99,4.99); 
%\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); 

% draw axes
\draw [->,thick] (-5,0) -- (5,0) node[below] {$x$}; 
\draw [->,thick] (0,-0.5) -- (0,5) node[right] {$y$};

% tick marks
\foreach \x in {-3,-1,1,3} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\foreach \y in {1,2,3,4} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\y};

% plot curve
\clip (-5,-1) rectangle (5,5);
\draw[ultra thick,domain=-5:3.96,smooth,samples=100,red] plot (-\x,{pow(1.5,\x)}) node [below left,fill=white] {$\left(\frac{2}{3}\right)^x$};
\draw[ultra thick,domain=-5:2.316,smooth,samples=100,blue] plot (-\x,{pow(2,\x)}) node [below left,fill=white] {$\left(\frac{1}{2}\right)^x$};
\draw[ultra thick,domain=-5:1,smooth,samples=100] plot (-\x,{pow(5,\x)})node [below left,fill=white] {$\left(\frac{1}{5}\right)^x$};

\end{tikzpicture}
-->


### Example 3
````{admonition} Limits of exponential functions
:class: tip

Evaluate the following limits by first evaluating the limit of the exponent and then applying the corresponding limit property of exponential functions to evaluate the given limit.

1. $\lim\limits_{x \to -\infty} 2^{-x^7}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $-x^7$, goes to positive infinity as $x$ goes to negative infinity.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to positive infinity and the base is bigger than one, we'll apply the property that 

$$\lim_{x\to \infty} b^x = \infty$$

for $b>1$.  Therefore, $\lim\limits_{x \to -\infty} 2^{-x^7} = \infty$.
```
---

2. $\lim\limits_{x \to \infty} 4^{-x^2}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $-x^2$, goes to negative infinity as $x$ goes to positive infinity.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to negative infinity and the base is bigger than one, we'll apply the property that 

$$\lim_{x\to -\infty} b^x = 0$$

for $b>1$.  Therefore, $\lim\limits_{x \to \infty} 4^{-x^2} = 0$.
```
---


3. $\lim\limits_{x \to 0^+} (1/3)^{5/x}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $5/x$, goes to positive infinity as $x$ goes to zero from the right.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to positive infinity and the base is between zero and one, we'll apply the property that 

$$\lim_{x\to \infty} b^x = 0$$

for $0<b<1$.  Therefore, $\lim\limits_{x \to 0^+} (1/3)^{5/x} = 0$.
```
---

4. $\lim\limits_{x \to 0^-} (2/7)^{3/x}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $3/x$, goes to negative infinity as $x$ goes to zero from the left.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to negative infinity and the base is between zero and one, we'll apply the property that 

$$\lim_{x\to -\infty} b^x = \infty$$

for $0<b<1$.  Therefore, $\lim\limits_{x \to 0^-} (2/7)^{3/x} = \infty$.
```
---

5. $\lim\limits_{x \to -\infty} 5^{4/x}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $4/x$, goes to zero as $x$ goes to negative infinity.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to zero, we don't need to apply any of the above properties of exponential functions regarding limits at infinity.  Instead, we can make use of the fact that exponential functions are continuous everywhere.  In particular, exponential functions are continuous at zero, which means that 

$$\lim_{x\to 0} b^x = b^0 = 1$$

for all $b>0$.  Therefore, $\lim\limits_{x \to -\infty} 5^{4/x} = 1$.
```
<br>

````