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
# The Natural Exponential and Logarithmic Functions

## Definitions and Properties



```{admonition} Definition
:class: note

The _**natural exponential function**_, denoted $e^x$, is an exponential function with base $e \approx 2.71828$.  The exact value of $e$ can be defined in a variety of different ways, one of which is the following:

$$e = \lim_{n\to \infty} \left(1 + \frac{1}{n}\right)^n$$


The _**natural logarithmic function**_, denoted $\ln(x)$, is the logarithmic function with base $e$ (i.e., $\ln(x) = \log_e(x)$).
```


```{admonition} Limit Properties of the Natural Exponential and Logarithmic Functions
:class: note

The functions $e^x$ and $\ln(x)$ satisfy the corresponding properties listed above for all exponential and logarithmic functions.  And in particular, since $e>1$, we have the following.

  - $e^x$ is increasing on $(-\infty,\infty)$
  - $\lim\limits_{x\to -\infty} e^x = 0$  and $\lim\limits_{x\to \infty} e^x = \infty$ <br><br>


  - $\ln(x)$ is increasing on $(0,\infty)$
  - $\lim\limits_{x\to 0^+} \ln(x) = -\infty$  and $\lim\limits_{x\to \infty} \ln(x) = \infty$ <br><br>
```



### Example 1
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


### Example 2
````{admonition} Limits of $e^x$ and $\ln(x)$
:class: tip

Evaluate the following limits.

1. $\lim\limits_{x \to \infty} e^{-x^7}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $-x^7$, goes to negative infinity as $x$ goes to positive infinity.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to negative infinity, we'll apply the property that 

$$\lim_{x\to -\infty} e^x = 0$$

Therefore, $\lim\limits_{x \to \infty} e^{-x^7} = 0$.
```
---


2. $\lim\limits_{x \to -\infty} e^{-x^2}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $-x^2$, goes to negative infinity as $x$ goes to negative infinity.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to negative infinity, we'll apply the property that 

$$\lim_{x\to -\infty} e^x = 0$$

Therefore, $\lim\limits_{x \to \infty} e^{-x^2} = 0$.
```
---


3. $\lim\limits_{x \to 0^+} e^{5/x}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $5/x$, goes to positive infinity as $x$ goes to zero from the right.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to positive infinity, we'll apply the property that 

$$\lim_{x\to \infty} e^x = \infty$$

Therefore, $\lim\limits_{x \to 0^+} e^{5/x} = \infty$.
```
---

4. $\lim\limits_{x \to 0^-} e^{3/x}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $3/x$, goes to negative infinity as $x$ goes to zero from the left.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to negative infinity, we'll apply the property that 

$$\lim_{x\to -\infty} e^x = 0$$

Therefore, $\lim\limits_{x \to 0^-} e^{3/x} = 0$.
```
---

5. $\lim\limits_{x \to -\infty} e^{4/x}$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the exponent.
 The exponent, $4/x$, goes to zero as $x$ goes to negative infinity.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since the exponent goes to zero, we don't need to apply any of the above properties of exponential functions regarding limits at infinity.  Instead, we can make use of the fact that $e^x$ is continuous everywhere.  In particular, $e^x$ is continuous at zero, which means that 

$$\lim_{x\to 0} e^x = e^0 = 1$$

Therefore, $\lim\limits_{x \to -\infty} e^{4/x} = 1$.
```
---


6. $\lim\limits_{x\to 1^-} \ln(1-x^2)$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the inner function.
 The inner function, $1-x^2$, goes to zero from the right as $x$ goes to one from the left.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since $1-x^2$ goes to zero from the right, we'll apply the property that 

$$\lim_{x\to 0^+} \ln(x) = -\infty$$

Therefore, $\lim\limits_{x\to 1^-} \ln(1 - x^2) = -\infty$.
```
---


7. $\lim\limits_{x\to 3^+} \ln\left(\dfrac{1}{x - 3}\right) $

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the inner function.
 The inner function, $\dfrac{1}{x-3}$, goes to infinity as $x$ goes to three from the right.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since $\dfrac{1}{x-3}$ goes to infinity, we'll apply the property that 

$$\lim_{x\to \infty} \ln(x) = \infty$$

Therefore, $\lim\limits_{x\to 3^+} \ln\left(\dfrac{1}{x-3}\right) = \infty$.
```
---

8. $\lim\limits_{x\to \infty} \ln\left(\dfrac{2}{x}\right)$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the inner function.
 The inner function, $\dfrac{2}{x}$, goes to zero from the right as $x$ goes to infinity.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since $\dfrac{2}{x}$ goes to zero from the right, we'll apply the property that 

$$\lim_{x\to 0^+} \ln(x) = -\infty$$

Therefore, $\lim\limits_{x\to \infty} \ln\left(\dfrac{2}{x}\right) = -\infty$.
```


9. $\lim\limits_{x\to -\infty} \ln\left(\dfrac{5x^2 + 3}{7x^2 - 1}\right)$

```{dropdown} **Step 1:** &nbsp; Evaluate the limit of the inner function.
 The inner function, $\dfrac{5x^2 + 3}{7x^2 - 1}$, goes to $5/7$ as $x$ goes to negative infinity.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the given limit.
Since $\dfrac{5x^2 + 3}{7x^2 - 1}$ goes to $5/7$, we don't need to apply any of the above properties of logarithmic functions regarding infinite limits.  Instead, we can make use of the fact that $\ln(x)$ is continuous on $(0,\infty)$.  In particular, $\ln(x)$ is continuous at $5/7$, which means that 

$$\lim_{x\to 5/7} \ln(x) = \ln(5/7)$$

Therefore, $\lim\limits_{x\to -\infty} \ln\left(\dfrac{5x^2 + 3}{7x^2 - 1}\right) = \ln(5/7)$.
```
````
