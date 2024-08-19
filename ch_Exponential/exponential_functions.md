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
# Exponential and Logarithmic Functions

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



## Definition and Properties of Logarithmic Functions


```{admonition} Definition of a Logarithmic Function
:class: info

For any constant $b>0$ and $b\neq 1$, the _**logarithmic function with base $b$**_, denoted $\log_b(x)$, is defined by

$$y = \log_b(x) ~~~~ \hbox{ if and only if } ~~~~ b^y = x.$$

For example, $\log_2(8) = 3$ since $2^3 = 8$.
```

```{admonition} Properties of Logarithmic Functions
:class: info

For a function $y = \log_{b}(x)$, the following properties hold:

- Its domain is $(0,\infty)$ and range is $(-\infty,\infty)$.
- Its graph passes through the point $(1,0)$ (i.e., $\log_b(1) = 0$).
- It is continuous on $(0,\infty)$.
- If $b>1$
  - $\log_b(x)$ is increasing on $(0,\infty)$
  - $\lim\limits_{x\to 0^+} \log_b(x) = -\infty$  and $\lim\limits_{x\to \infty} \log_b(x) = \infty$ <br><br>
- If $0< b < 1$
  - $\log_b(x)$ is decreasing on $(0,\infty)$
  - $\lim\limits_{x\to 0^+} \log_b(x) = \infty$  and $\lim\limits_{x\to \infty} \log_b(x) = -\infty$
```


```{admonition} A New Domain Restriction
:class: warning

Since the domain of all logarithmic functions is restricted to positive values, whenever we encounter a logarithm, we have to make sure to not take the logarithm of a negative number or of zero.   This is the third restriction on a domain we have encountered this semester.  The first two restrictions being that we cannot divide by zero and we cannot take the square root of a negative number.
```

### Example 4
````{admonition} Graphs of logarithmic functions
:class: tip

On the left image below, the graphs of the logarithmic functions $\log_{5}(x)$, $\log_{2}(x)$, and $\log_{3/2}(x)$ are all displayed.  Since the base associated with each function is greater than one, each of these logarithmic functions is increasing and goes to positive infinity as $x$ goes to infinity. 

On the right image below, the graphs of the logarithmic functions $\log_{1/5}(x)$, $\log_{1/2}(x)$, and $\log_{2/3}(x)$ are all shown below.  Since the base associated with each function is between zero and one, each of these logarithmic functions is decreasing and goes to negative infinity as $x$ goes to infinity. 


::::{grid} 2
:::{grid-item-card}
:columns: 5
:margin: 0 0 4 4
```{image} ../images/pic_exponential_functions_logarithmic_growth.png
:alt: Graphs of various logarithmic functions
:align: center
```
:::

:::{grid-item-card}
:columns: 5
```{image} ../images/pic_exponential_functions_logarithmic_decay.png
:alt: Graphs of various logarithmic functions
:align: center
```
:::
::::
```{dropdown} Long Text Description

Two images containing graphs of logarithmic functions are displayed.

On the first image, the graphs of log base 3/2 of x, log base 2 of x, and log base 5 of x are all shown on the same coordinate axes.  The values 1, 2, 3, and 4 are marked on the x-axis and the values -3, -1, 1, and 3 are marked on the y-axis.

From left-to-right, the graph of y = log base 3/2 of x starts very far below the x-axis and just to the right of the y-axis.  The graph quickly increases to the point (1,0) and continues to increase for values of x greater than one.  The steepness of the curve decreases from left-to-right.

From left-to-right, the graph of y = log base 2 of x starts very far below the x-axis and between the y-axis and the graph of y = log base 3/2 of x .  The graph quickly increases to the point (1,0), where it crosses the graph of y = log base 3/2 of x.  It continues to increase for values of x greater than one, staying below the graph of y = log base 3/2 of x.  The steepness of the curve decreases from left-to-right.

From left-to-right, the graph of y = log base 5 of x starts very far below the x-axis and between the y-axis and the graph of y = log base 2 of x .  The graph quickly increases to the point (1,0), where it crosses the graph of y = log base 2 of x.  It continues to increase for values of x greater than one, staying below the graph of y = log base 2 of x.  The steepness of the curve decreases from left-to-right.


On the second image, the graphs of log base 2/3 of x, log base 1/2 of x, and log base 1/5 of x are all shown on the same coordinate axes.  The values 1, 2, 3, and 4 are marked on the x-axis and the values -3, -1, 1, and 3 are marked on the y-axis.

From left-to-right, the graph of y = log base 2/3 of x starts very far above the x-axis and just to the right of the y-axis.  The graph quickly decreases to the point (1,0) and continues to decrease for values of x greater than 1.  The steepness of the curve decreases from left-to-right.

From left-to-right, the graph of y = log base 1/2 of x starts very far above the x-axis and between the y-axis and the graph of y = log base 2/3 of x.  The graph quickly decreases to the point (1,0), where it crosses the graph of y = log base 2/3 of x.  It continues to decrease for values of x greater than 1, staying above the graph of y = log base 2/3 of x.  The steepness of the curve decreases from left-to-right.

From left-to-right, the graph of y = log base 1/5 of x starts very far above the x-axis and between the y-axis and the graph of y = log base 1/2 of x .  The graph quickly decreases to the point (1,0), where it crosses the graph of y = log base 1/2 of x.  It continues to decrease for values of x greater than one, staying above the graph of y = log base 1/2 of x.  The steepness of the curve decreases from left-to-right.


```
````

<!--

\begin{tikzpicture}[scale=1.4]
\tikzstyle{every node}=[font=\large]
 
% create a white background, with a black frame
%\draw [fill=white] (-7.5,-1.5) rectangle (7.5,3.5); 

% draw a grid
\draw[step=5mm, lightgray, thin] (0,-4.99) grid (4.99,4.99); 
%\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); 

% draw axes
\draw [->,thick] (-0.5,0) -- (5,0) node[below] {$x$}; 
\draw [->,thick] (0,-5) -- (0,5) node[right] {$y$};

% tick marks
\foreach \x in {1,2,3,4} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\foreach \y in {-3,-1,1,3} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\y};

% plot curve
\clip (-1,-5) rectangle (5,5);
\draw[ultra thick,domain=-5:3.96,smooth,samples=100,red] plot ({pow(1.5,\x)},\x) node [above left,fill=white] {$\log_{3/2}(x)$};
\draw[ultra thick,domain=-5:2.316,smooth,samples=100,blue] plot ({pow(2,\x)},\x) node [above left,fill=white] {$\log_2(x)$};
\draw[ultra thick,domain=-5:1,smooth,samples=100] plot ({pow(5,\x)},\x) node [above left,fill=white] {$\log_5(x)$};

\end{tikzpicture}



\begin{tikzpicture}[scale=1.4]
\tikzstyle{every node}=[font=\large]
 
% create a white background, with a black frame
%\draw [fill=white] (-7.5,-1.5) rectangle (7.5,3.5); 

% draw a grid
\draw[step=5mm, lightgray, thin] (0,-4.99) grid (4.99,4.99); 
%\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); 

% draw axes
\draw [->,thick] (-0.5,0) -- (5,0) node[below] {$x$}; 
\draw [->,thick] (0,-5) -- (0,5) node[right] {$y$};

% tick marks
\foreach \x in {1,2,3,4} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\foreach \y in {-3,-1,1,3} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\y};

% plot curve
\clip (-1,-5) rectangle (5,5);
\draw[ultra thick,domain=-5:3.96,smooth,samples=100,red] plot ({pow(1.5,\x)},-\x) node [below left,fill=white] {$\log_{2/3}(x)$};
\draw[ultra thick,domain=-5:2.316,smooth,samples=100,blue] plot ({pow(2,\x)},-\x) node [below left,fill=white] {$\log_{1/2}(x)$};
\draw[ultra thick,domain=-5:1,smooth,samples=100] plot ({pow(5,\x)},-\x)node [below left,fill=white] {$\log_{1/5}(x)$};

\end{tikzpicture}

-->

### Example 5
````{admonition} Domain of a logarithmic function
:class: tip

Determine the domain of $\log_5(3x - 7)$.

```{dropdown} Answer
In general, the domain of $\log_b(f(x))$ consists of all values of $x$ such that $f(x) > 0$.

In this case, the domain of $\log_5(3x - 7)$ consists of all values of $x$ such that $3x-7 > 0$.  Solving for $x$ yields $x > 7/3$.  Therefore, the domain of $\log_5(3x - 7)$ is $(7/3,\infty)$.

For a review of solving inequalities like $f(x) > 0$, see {ref}`solving_inequalities`.
```
````





### Example 6
````{admonition} Limits of logarithmic functions
:class: tip

Evaluate the following limits.

Evaluate the following limits by first evaluating the limit of the inner function and then applying the corresponding limit property of logarithmic functions to evaluate the given limit.

1. $\lim\limits_{x\to 8^+} \log_{3}(x^2-64) $

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the inner function.
 The inner function, $x^2 - 64$, goes to zero from the right as $x$ goes to eight from the right.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since $x^2 - 64$ goes to zero from the right and the base is bigger than one, we'll apply the property that 

$$\lim_{x\to 0^+} \log_{b}(x) = -\infty$$

for $b>1$.  Therefore, $\lim\limits_{x\to 8^+} \log_{3}(x^2-64) = -\infty$.
```
---



2. $\lim\limits_{x\to 5^-} \log_{1/2}\left(\dfrac{1}{5-x}\right) $

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the inner function.
 The inner function, $\dfrac{1}{5-x}$, goes to infinity as $x$ goes to five from the left.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since $\dfrac{1}{5-x}$ goes to infinity and the base is between zero and one, we'll apply the property that 

$$\lim_{x\to \infty} \log_{b}(x) = -\infty$$

for $0<b<1$.  Therefore, $\lim\limits_{x\to 5^-} \log_{1/2}\left(\dfrac{1}{5-x}\right) = -\infty$.
```
---

3. $\lim\limits_{x\to \infty} \log_{1/5}\left(\dfrac{2}{x}\right) $

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the inner function.
 The inner function, $\dfrac{2}{x}$, goes to zero from the right as $x$ goes to infinity.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since $\dfrac{2}{x}$ goes to zero from the right and the base is between zero and one, we'll apply the property that 

$$\lim_{x\to 0^+} \log_{b}(x) = \infty$$

for $0<b<1$.  Therefore, $\lim\limits_{x\to \infty} \log_{1/5}\left(\dfrac{2}{x}\right) = \infty$.
```
---

````




## The Natural Exponential and Logarthimic Functions


```{admonition} Definition
:class: note

The _**natural exponential function**_, denoted $e^x$, is an exponential function with base $e \approx 2.71828$.  The exact value of $e$ can be defined in a variety of different ways, one of which is the following:

$$e = \lim_{n\to \infty} \left(1 + \frac{1}{n}\right)^n$$


The _**natural logarithmic function**_, denoted $\ln(x)$, is the logarithmic function with base $e$ (i.e., $\ln(x) = \log_e(x)$).
```


### Example 7
````{admonition} Graphs of the natural exponential and logarithmic functions
:class: tip

The graphs of $y=e^x$ and $y = \ln(x)$ are shown below.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_exponential_functions_e_ln.png
:alt: Graphs of the natural exponential and logarithmic functions
:width: 500px
```
:::
::::
```{dropdown} Long Text Description
The graph of y = e^x and y = ln(x) are both shown on the same coordinate axes.  The values -3, -1, 1, and 3 are marked on both the x-axis and the y-axis.

From left-to-right, the graph of y = e^x starts very close to and above the x-axis.  The graph increases to the point (0,1) and continues to increase for positive values of x.  The steepness of the curve also increases from left-to-right.

From bottom-to-top, the graph of y = ln(x) starts very close to and to the right of the y-axis.  The graph increases to the point (1,0) and continues to increase for values of x greater than 1.  The steepness of the curve decreases from bottom-to-top.
```
````

<!--
\begin{tikzpicture}[scale=1.4]
\tikzstyle{every node}=[font=\large]
 
% create a white background, with a black frame
%\draw [fill=white] (-7.5,-1.5) rectangle (7.5,3.5); 

% draw a grid
\draw[step=5mm, lightgray, thin] (-4.99,-4.99) grid (4.99,4.99); 
%\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); 

% draw axes
\draw [->,thick] (-5,0) -- (5,0) node[below] {$x$}; 
\draw [->,thick] (0,-5) -- (0,5) node[right] {$y$};

% tick marks
\foreach \x in {-3,-1,1,3} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\foreach \y in {-3, -1,1,3} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\y};

% plot curve
\clip (-5,-5) rectangle (5,5);
\draw[ultra thick,domain=-5:1.6,smooth,samples=100,black] plot (\x,{exp(\x)}) node [below right,fill=white] {$e^x$};
\draw[ultra thick,domain=-5:1.6,smooth,samples=100,black] plot ({exp(\x)},\x) node [above left,fill=white] {$\ln(x)$};

\end{tikzpicture}
-->