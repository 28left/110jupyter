---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3.9 64-bit
  language: python
  name: python3
---
# Functions, Domain, and Range

## Definitions

```{admonition} Definition
:class: info
A _**function**_ is a rule that assigns to each element in a set $A$ **one and only one** element in a set $B$.
```

It is customary to denote a function by a letter of the alphabet, such as $f$, $g$, $h$, etc.


```{admonition} Definition
:class: info

The set $A$ is called the _**domain**_ of the function. The element in $B$ that $f$ associates with $x$ is written as 

$$f(x)$$ 

(read "$f$ of $x$") and is called the _**value**_ of $f$ at $x$.
```

```{admonition} Definition
:class: info

The set of all possible values of $f(x)$ resulting from all the possible values of $x$ in its domain, is called the _**range**_ of $f(x)$.
```


```{figure} ../images/pic_limits_domainrange.png
---
name: illustration-domain-range
alt: Illustration of domain and range of a function
---
Illustration of the domain and the range of a function
```


```{admonition} Definition
:class: info

Suppose we are given the function $y=f(x)$.  

- The variable $x$ is called the _**independent variable**_.
- The variable $y$, whose value depends on $x$, is called the _**dependent variable**_.
```



## Domain Considerations

To determine the domain of a function, we need to find what restrictions, if any, are to be placed on the independent variable. 

In many practical problems, the domain of a function is dictated by the nature of the problem and any restrictions on the function used in the expression.  In this course, these restrictions will be limited to one or more of the following:

```{admonition} Key restrictions
:class: danger

- **cannot take the square root of a negative number**
- **cannot divide by zero**
- **cannot take the logarithm of zero or a negative number**
```

### Example 1

Determine the domain and range of $f(x) = x^2 - 1$.  


```{dropdown} **Step 1:** Determine the domain of $f$.

Since $f$ does not include any division, square roots, or logarithms, its domain consists of all real numbers, $(-\infty,\infty)$.
```




```{dropdown} **Step 2:** Determine the range of $f$. 

Since $x^2 \geq 0$ for all real $x$, by subtracting $1$ from both sides of the inequality, we obtain $f(x) = x^2 - 1 \geq -1$ for all real $x$.  Therefore, the range of $f$ is $[-1,\infty)$.
```


Another way to determine the domain and range of $f$ is to consider the graph of $y = f(x)$.  For this example, the graph of $y = x^2 - 1$ is a parabola that opens up and is shifted down one unit, as illustrated below.


```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2.0]

%\draw[black,fill=white] (-3,-2) rectangle (3,4);
%\draw[very thin,color=lightgray,step=0.5] (-3.4,-4.9) grid (3.4,0.9);
%\draw[very thin,color=gray,step=2] (-3.5,-5) grid (3.5,1);

\draw[->] (-2.5,0) -- (2.5,0) node[below] {$x$};
\draw[->] (0,-1.5) -- (0,3.5) node[right] {$y$};
       
%s\node[right] at (0.9, -0.5){$y = x^2-4$};

% tick marks
\foreach \x in {-2,-1,1,2} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {-1,1,2,3} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};


\draw[domain=-2.1:2.1,smooth,variable=\x,blue,ultra thick] plot ({\x},{\x*\x- 1});

\end{tikzpicture}
\end{document}
```

- The domain of $f$ consists of all the different $x$-coordinates of points on the graph of $f$, which is $(-\infty,\infty)$.  
- The range of $f$ consists of all the different $y$-coordinates of points on the graph of $f$, which is $[-1,\infty)$. 


### Example 2

Determine the domain of 

$$g(x) = \dfrac{1}{\sqrt{x}}.$$


```{dropdown} **Step 1:** Consider how the square root restricts the domain.

Since $g$ includes the square root function, $\sqrt{x}$, we must assume that $x\geq 0$.
```

```{dropdown} **Step 2:** Consider how division restricts the domain.

Since $g$ includes division, we must exclude any value of $x$ that makes the denominator equal to zero.  In this example, the denominator equals zero only when $x=0$.
```

```{dropdown} **Step 3:** Determine the domain of $g$.

Based on the previous two steps, the domain of $g$ consists of all real numbers greater than zero, which can be written in interval notation as $(0,\infty)$.
```


## Domain Analysis

Let $f$ and $g$ be functions with domains $A$ and $B$, respectively.  The sum, difference, product, and quotient of $f$ and $g$ are functions defined by

\begin{align*}
(f+g)(x) &= f(x) + g(x) && \hbox{Sum}\\
(f-g)(x) &= f(x) - g(x) && \hbox{Difference}\\
(fg)(x) &= f(x) g(x) && \hbox{Product}\\
(f/g)(x) &= \frac{f(x)}{g(x)} && \hbox{Quotient}
\end{align*}

```{admonition} Domains of sums, differences, products, and divisions of functions
:class: info

- The domain of $f+g$, $f-g$, and $fg$ consists of all values of $x$ that appear in both $A$ and $B$, which is called the **intersection** of $A$ and $B$, and is denoted by $A\cap B$.

- The domain of $f/g$ consists of $A\cap B$ excluding all values of $x$ such that $g(x)=0$.
```




### Example 3

Let $f(x) = \sqrt{x + 2}$ and $g(x) = \sqrt{5-x}$.  Determine the domain of $f+g$, $f-g$, $fg$, and $f/g$.  Use interval notation to express each domain.


```{dropdown} **Step 1:** Determine the domain of $f$ and $g$ separately.

- The domain of $f$ consists of all $x$ such that $x+2 \geq 0$, or equivalently, $x \geq -2$.  Therefore, the domain of $f$ is $[-2,\infty)$.

- The domain of $g$ consists of all $x$ such that $5-x \geq 0$, or equivalently, $x \leq 5$.  Therefore, the domain of $g$ is $(-\infty,5]$.
```



```{dropdown} **Step 2:** Determine the domain of $f+g$, $f-g$, and $fg$.

The domain of $f+g$, $f-g$, and $fg$ is the intersection of $[-2,\infty)$ (i.e., $-2 \leq x$) and $(-\infty,5]$ (i.e., $x \leq 5$).  In other words, the domain of all three functions consists of values of $x$ such that $-2 \leq x \leq 5$, or equivalently, $[-2,5]$.
```


```{dropdown} **Step 3:** Determine the values of $x$ such that $g(x) = 0$.

Set $g(x) = 0$.

$$\sqrt{x-5} = 0$$

Solve for $x$ by squaring both sides.

$$x - 5 = 0$$

And finally, adding $5$ to both sides yields $x=5$ (i.e., $g(x) = 0$ only when $x=5$).
```


```{dropdown} **Step 4:** Determine the domain of $f/g$.

The domain of $f/g$ consists of $[-2,5]$, excluding all values of $x$ such that $g(x) = 0$.  In the previous step, we determined that the only value of $x$ that satisfies $g(x) = 0$ is $x=5$.  Therefore, the domain of $f/g$ is $[-2,5)$.
```