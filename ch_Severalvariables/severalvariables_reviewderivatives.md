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


# Review of Differentiation of Functions of One Variable

## Formulas and Rules of Differentiation

```{admonition} Formulas of Differentiation
:class: info

The following is a list of derivatives of commonly used functions.  

\begin{align*}
&\text{Derivative of a Constant} && \frac{d}{dx} c = 0  ~~~ \text{for any constant $c$}\\ \\ 
&\text{Derivative of a Power Function} && \frac{d}{dx}x^n = nx^{n-1} ~~~ \text{for any constant $n$} \\ \\
&\text{Derivative of $e^x$} && \frac{d}{dx}e^x = e^x \\ \\
&\text{Derivative of $\ln(x)$} && \frac{d}{dx}\ln(x) = \frac{1}{x}
\end{align*}
```


### Example 1
````{admonition} Derivative of power functions
:class: tip
<br>

```{dropdown} Compute the derivative of $x^5$.

\begin{align*}
\frac{d}{dx}x^5 
&= 5x^{5-1} \\
&= 5x^4
\end{align*}
```

```{dropdown} Compute the derivative of $x^{-3/4}$.

\begin{align*}
\frac{d}{dx}x^{-3/4}
&= -\frac{3}{4}x^{-3/4-1} \\
&= -\frac{3}{4}x^{-7/4}
\end{align*}
```


```{dropdown} Compute the derivative of $\sqrt{x}$.

\begin{align*}
\frac{d}{dx}\sqrt{x} 
&= \frac{d}{dx}x^{1/2} \\
&= \frac{1}{2}x^{-1/2} \\
&= \frac{1}{2\sqrt{x}} 
\end{align*}
```

```{dropdown} Compute the derviative of $1/x$.

\begin{align*}
\frac{d}{dx}\frac{1}{x} 
&= \frac{d}{dx}x^{-1} \\
&= (-1)x^{-2} \\
&= -\frac{1}{x^2} 
\end{align*}
```
````


## Basic Rules of Differentiation


```{admonition} The Derivative of a Sum, Difference, Product and Quotient
:class: info

The following is a list of rules of differentiation that can be applied to the sum, difference, product, and quotient of $f$ and $g$, assuming that both $f$ and $g$ are differentiable.

\begin{align*}
&\text{Constant Multiple Rule} && \frac{d}{dx}[cf(x)] = cf'(x) ~~~ \text{for any constant $c$}\\ \\
&\text{Sum/Difference Rule} && \frac{d}{dx}[f(x)\pm g(x)] = f'(x) \pm g'(x)\\ \\
&\text{Product Rule} && \frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)\\ \\
&\text{Quotient Rule} && \frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}
\end{align*}
```

### Example 2

````{admonition} Derivative of a polynomial
:class: tip

Compute the derivative of $3x^4 + 5x^2 - 7x + 6$

```{dropdown} **Step 1:** &nbsp; Apply the sum and difference rules.

$$\frac{d}{dx} (3x^4 + 5x^2 - 7x + 6) = \frac{d}{dx}3x^4 + \frac{d}{dx}5x^2 - \frac{d}{dx}7x + \frac{d}{dx}6$$

```

```{dropdown} **Step 2:** &nbsp; Apply the constant multiple rule.

$$\frac{d}{dx} (3x^4 + 5x^2 - 7x + 6) =  3\frac{d}{dx}x^4 + 5\frac{d}{dx}x^2 - 7\frac{d}{dx}x + \frac{d}{dx}6$$

```

```{dropdown} **Step 3:** &nbsp; Apply the formula for the derivative of a power function and a constant.

$$\frac{d}{dx} (3x^4 + 5x^2 - 7x + 6) =  3(4)x^3 + 5(2)x^1 - 7(1) + 0$$

```

```{dropdown} **Step 4:** &nbsp; Simplify.

$$\frac{d}{dx} (3x^4 + 5x^2 - 7x + 6) =  12x^3 + 10x - 7$$

```

````

### Example 3

````{admonition} Product rule
:class: tip

Compute the derivative of $f(x) = \left(5x^2 + 1\right)(4\sqrt{x} - 6x)$ at $x=1$.

```{dropdown} **Step 1:** &nbsp; Apply the product rule.

\begin{align*}
f'(x)
&= \left[\frac{d}{dx} \left(5x^2 + 1\right)\right](4\sqrt{x} - 6x) + \left(5x^2 + 1\right)\left[\frac{d}{dx}(4\sqrt{x} - 6x)\right] \\ \\
&= 10x(4\sqrt{x} - 6x) + \left(5x^2 + 1\right)\left(4\frac{1}{2\sqrt{x}} - 6\right)
\end{align*}
```

```{dropdown} **Step 1:** &nbsp; Plug in $x=1$.

\begin{align*}
f'(1)
&= 10(1)(4\sqrt{1} - 6(1)) + \left(5(1^2) + 1\right)\left(4\frac{1}{2\sqrt{1}} - 6\right) \\
&= 10(-20) + (6)(-4) \\
&= -224
\end{align*}
```

````

### Example 4

````{admonition} Quotient rule
:class: tip

Compute the derivative of $\dfrac{1 + x^4}{1 - x^5}$.

```{dropdown} **Step 1:** &nbsp; Apply the quotient rule.

\begin{align*}
\frac{d}{dx} \dfrac{1 + x^4}{1 - x^5} 
&= \frac{\left[\frac{d}{dx} (1 + x^4)\right](1-x^5) - (1 + x^4)\left[\frac{d}{dx}(1-x^5)\right]}{(1-x^5)^2} \\ \\
&= \frac{4x^3(1 - x^5) - (1 + x^4)(-5x^4)}{(1 - x^5)^2}
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Simplify the numerator.

\begin{align*}
\frac{d}{dx} \dfrac{1 + x^4}{1 - x^5} 
&= \frac{x^3[4(1 - x^5) - (1 + x^4)(-5x)]}{(1 - x^5)^2} && \text {pull out common factors}\\ \\
&= \frac{x^3(4 - 4x^5 + 5x + 5x^5)}{(1 - x^5)^2} && \text{expand inside []} \\ \\
&= \frac{x^3(4 + 5x + x^5)}{(1 - x^5)^2} && \text{combine like terms}\\
\end{align*}
```

````


## The Chain Rule of Differentiation


```{admonition} The Derivative of a Composition of Functions
:class: info

The Chain Rule is a rule of differentiation that can be applied to the composition $g\circ f$, assuming both $f$ and $g$ are differentiable.  The last three rules are specific cases of the Chain Rule, where $g(x) = x^n$, $g(x) = e^x$, and $g(x) = \ln(x)$, respectively.

\begin{align*}
&\text{Chain Rule} && \frac{d}{dx}\left[g(f(x))\right] = g'(f(x))f'(x) \\ \\
&\text{General Power Rule} && \frac{d}{dx}[f(x)]^n = n[f(x)]^{n-1}f'(x) ~~~ \text{for any constant $n$} \\ \\
&\text{Derivative of $e^{f(x)}$} && \frac{d}{dx}e^{f(x)} = e^{f(x)} f'(x) \\ \\
&\text{Derivative of $\ln(f(x)$)} && \frac{d}{dx}\ln(f(x)) = \frac{1}{f(x)} f'(x)
\end{align*}
```


### Example 5

````{admonition} General power rule
:class: tip

Compute the derivative of $(x^3 + 7x - 1)^4$.

```{dropdown} Apply the general power rule.

\begin{align*}
\frac{d}{dx} (x^3 + 7x - 1)^4 
&= 4(x^3 + 7x - 1)^3\frac{d}{dx}(x^3 + 7x -1)  \\ \\
&= 4(x^3 + 7x - 1)^3(3x^2+7)
\end{align*}
```
````

### Example 6

````{admonition} General power rule
:class: tip

Compute the derivative of $\sqrt{y^2 - 5}$.

```{dropdown} Apply the general power rule.

\begin{align*}
\frac{d}{dy} \sqrt{y^2 - 5}
&= \frac{d}{dy} (y^2 - 5)^{1/2} \\ \\
&= \frac{1}{2}(y^2 - 5)^{-1/2}\frac{d}{dy}(y^2 - 5) \\ \\
&= \frac{1}{2}(y^2 - 5)^{-1/2}2y \\ \\
&= \frac{y}{\sqrt{y^2 - 5}} 

\end{align*}
```
````

### Example 7

````{admonition} Derivative of $e^{f(x)}$
:class: tip

Compute the derivative of $e^{7x^2}$.

```{dropdown} Apply the formula for the derivative of $e^{f(x)}$.

\begin{align*}
\frac{d}{dx} e^{7x^2}
&= e^{7x^2} \frac{d}{dx} (7x^2) \\ \\
&= 14xe^{7x^2}

\end{align*}
```
````

### Example 8

````{admonition} Product rule
:class: tip

Compute the derivative of $y^2e^{3y}$.

```{dropdown} Apply the product rule.

\begin{align*}
\frac{d}{dy} y^2e^{3y} 
&= \left(\frac{d}{dy}y^2 \right)e^{3y}  + y^2\left(\frac{d}{dy}e^{3y} \right) \\ \\
&= 2ye^{3y}  + y^2e^{3y}\left(\frac{d}{dy}3y \right) \\ \\
&= 2ye^{3y}  + 3y^2e^{3y} \\ \\
&= ye^{3y}(2  + 3y)

\end{align*}
```
````

### Example 9

````{admonition} Derivative of $\ln(f(x))$
:class: tip

Compute the derivative of $\ln(z^3 + 5z)$.


```{dropdown} Apply the formula for the derivative of $\ln(f(x))$.

\begin{align*}
\frac{d}{dz} \ln(z^3 + 5z) 
&= \frac{1}{z^3 + 5z} \frac{d}{dz}(z^3 + 5z) \\ \\
&= \frac{3z^2 + 5}{z^3 + 5z}
\end{align*}
```

````




```{admonition} More Practice
:class: important

For more examples of the rules of differentiation, see

- {ref}`derivative:diff_rules`
- {ref}`exponential:laws`

```


