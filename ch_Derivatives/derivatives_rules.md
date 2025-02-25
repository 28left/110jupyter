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

(derivative:diff_rules)=
# Basic Rules of Differentiation

## The Rules

```{admonition} Formulas of Differentiation
:class: info

\begin{align*}
&\text{Derivative of a Constant} && \frac{d}{dx} c = 0  ~~~ \text{for any constant $c$}\\ \\ 
&\text{Derivative of a Power Function} && \frac{d}{dx}x^n = nx^{n-1} ~~~ \text{for any constant $n$}
\end{align*}
```

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

```{admonition} The Derivative of a Composition of Functions
:class: info

The Chain Rule is a rule of differentiation that can be applied to the composition $g\circ f$, assuming both $f$ and $g$ are differentiable.  The General Power Rule is a specific case of the Chain Rule, where $g(x) = x^n$.

\begin{align*}
&\text{Chain Rule} && \frac{d}{dx}\left[g(f(x))\right] = g'(f(x))f'(x) \\ \\
&\text{General Power Rule} && \frac{d}{dx}[f(x)]^n = n[f(x)]^{n-1}f'(x) ~~~ \text{for any constant $n$}
\end{align*}
```


<!--
```{admonition} Derivative of a Constant
:class: info
For any real number $c$, 

$$
\frac{d}{dx}(c) = 0
$$
```

```{admonition} The Power Rule
:class: info

For any real number $n$, 

$$
\frac{d}{dx}(x^n) = nx^{n-1}
$$
```

```{admonition} The Constant Multiple Rule
:class: info

For any real number $c$, 

$$
\frac{d}{dx}[cf(x)] = cf'(x)
$$
```

```{admonition} The Sum/Difference Rule
:class: info

$$
\frac{d}{dx}[f(x)\pm g(x)] = f'(x) \pm g'(x)
$$
```

```{admonition} The Product Rule
:class: info

$$
\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
$$
```

```{admonition} The Quotient Rule
:class: info

If $g(x)\neq 0$, 

$$
\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}
$$
```

```{admonition} The Chain Rule
:class: info

$$
\frac{d}{dx}\left[g(f(x))\right] = g'(f(x))f'(x)
$$
```

```{admonition} The General Power Rule
:class: info

$$
\frac{d}{dx}[f(x)]^n = n[f(x)]^{n-1}f'(x)
$$

This is a special case of the Chain Rule with $g(x) = x^n$.
```
-->


### Example 1

````{admonition} Sum and Constant Multiple Rule
:class: tip

Compute the derivative of $f(x) = 5x^2 - 4x + 2 + \dfrac{3}{x^4}$ using the basic rules of differentiation.


```{dropdown} **Step 1:** &nbsp; Remember the sum rule.

Since $f(x)$ is the sum of functions, remember the sum rule for derivatives.

$$
\frac{d}{dx}[f(x)\pm g(x)] = \frac{d}{dx}[f(x)]\pm \frac{d}{dx}[g(x)]
$$
```

```{dropdown} **Step 2:** &nbsp; Apply the sum rule.

\begin{align*}
f'(x)
&= \frac{d}{dx}\left(5x^2-4x+2 +\frac{3}{x^4}\right) \\
&=\frac{d}{dx}\left(5x^2\right)-\frac{d}{dx}\left(4x^1\right)+\frac{d}{dx}\left(2\right)+\frac{d}{dx}\left(3x^{-4}\right)
\end{align*}
```


```{dropdown} **Step 3:** &nbsp; Remember the constant multiple rule.

Since several terms of $f(x)$ are a constant times a function, remember the constant multiple rule for derivatives.

$$
\frac{d}{dx}[cf(x)] = c\frac{d}{dx}[f(x)]
$$
```

```{dropdown} **Step 4:** &nbsp; Apply the constant multiple rule.

\begin{align*}
f'(x)
&= 5\frac{d}{dx}\left(x^2\right) - 4\frac{d}{dx}\left(x^1\right) + \frac{d}{dx}\left(2\right) + 3\frac{d}{dx}\left(x^{-4}\right)
\end{align*}
```

```{dropdown} **Step 5:** &nbsp; Compute the derivative of each term.

Remember $x^0=1$.

\begin{align*}
f'(x) 
&= 5\frac{d}{dx}\left(x^2\right)-4\frac{d}{dx}\left(x^1\right)+0+3\frac{d}{dx}\left(x^{-4}\right) && \hbox{$\dfrac{d}{dx}(c) = 0$ for any constant $c$}\\ \\ 
&= 5 \cdot 2x^{2-1} -  4\cdot1x^{1-1} + 3\cdot (-4)x^{-4-1} && \hbox{power rule, $\dfrac{d}{dx}x^n = nx^{n-1}$}\\ \\
&= 10x^1 - 4x^0 - 12x^{-5} && \hbox{simplify}\\
%&= 10x - 4 - \frac{12}{x^5}
\end{align*}

Therefore,

$$f'(x) = 10x - 4 - \frac{12}{x^5}$$
```
````


### Example 2
````{admonition} Product Rule
:class: tip

Compute the derivative of $h(x)=(3x^2+1)(x^2+x+1)$ using the basic rules of differentiation.


```{dropdown} **Step 1:** &nbsp; Remember the product rule.

Since $h(x)$ is the product of two functions, remember the product rule for derivatives.

$$
\frac{d}{dx}[f(x)g(x)]=f'(x)g(x)+f(x)g'(x)
$$
```

```{dropdown} **Step 2:** &nbsp; Identify the two functions being multiplied.

$$ f(x)=3x^2+1 ~~~\text{  and  }~~~ g(x)=x^2+x+1$$
```

```{dropdown} **Step 3:** &nbsp; Compute the derivative of each function.

\begin{align*}
f'(x) 
&= \frac{d}{dx}(3x^2 + 1) \\
&= \frac{d}{dx}(3x^2) + \frac{d}{dx}(1) && \hbox{sum rule}\\
&= 3\cdot 2x + 0 && \hbox{power Rule & $\dfrac{d}{dx}(c) = 0$} \\
&= 6x \\ \\
g'(x) 
&= \frac{d}{dx}(x^2+x+1)\\
&= \frac{d}{dx}(x^2) + \frac{d}{dx}(x) + \frac{d}{dx}(1) && \hbox{sum rule}\\
&= 2x + 1 + 0 && \hbox{power rule & $\dfrac{d}{dx}(c) = 0$} \\
&= 2x + 1
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Compute &nbsp; $h'(x)$.

\begin{align*}
h'(x) &= f'(x)g(x)+f(x)g'(x) && \hbox{product rule}\\ \\
&= (6x)(x^2+x+1) + (3x^2+1)(2x+1) && \hbox{using Steps 2 & 3}\\ \\
&= 6x^3+6x^2+6x+6x^3+3x^2+2x+1 && \hbox{expand}\\ \\
&=12x^3+9x^2+8x+1 && \hbox{combine like terms}
\end{align*}
```
````

### Example 3 
````{admonition} Quotient Rule
:class: tip

Compute the derivative of $h(x)=\dfrac{x^3-7x+10}{x^2+4}$ using the basic rules of differentiation and then evaluate $h'(2)$.


```{dropdown} **Step 1:** &nbsp; Remember the quotient rule.

Since $h(x)$ is the quotient of two functions, remember the quotient rule for derivatives.

$$
\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right]=\frac{f'(x)g(x)-f(x)g'(x)}{[g(x)]^2}
$$
```

```{dropdown} **Step 2:** &nbsp; Apply the quotient rule to the given function.

\begin{align*}
h'(x)
& =\frac{\left[\frac{d}{dx}(x^3-7x+10)\right](x^2+4)-(x^3-7x+10)\left[\frac{d}{dx}(x^2+4)\right]}{(x^2+4)^2} \\ 
&= \frac{(3x^2-7)(x^2+4)-(x^3-7x+10)(2x)}{(x^2+4)^2} 
\end{align*}
```


```{dropdown} **Step 3:** &nbsp; Simplify.

\begin{align*}
h'(x)
&=\frac{(3x^4+5x^2-28)-(2x^4-14x^2+20x)}{(x^2+4)^2} && \hbox{expand numerator}\\ 
&=\frac{x^4+19x^2-20x-28}{(x^2+4)^2} && \hbox{combine like terms}
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Evaluate $h'(2)$.

\begin{align*}
h'(2) &= \frac{2^4+19\cdot2^2-20\cdot2-28}{(2^2+4)^2}\\ \\
&=\frac{16+19\cdot 4-20\cdot 2-28}{(4+4)^2}\\ \\
&=\frac{16+76-40-28}{8^2}\\ \\
&=\frac{24}{64}\\ \\
&=\frac{3}{8}
\end{align*}
```

```{admonition} Good to know
:class: warning

Keep in mind that if the only goal is to compute $h'(2)$, then Step 3 can be skipped and $x=2$ can be plugged in immediately after computing the derivative in Step 2.  This will reduce the number of computations and help avoid some possible algebraic mistakes while simplifying.
```
````

### Example 4 
````{admonition} General Power Rule
:class: tip

Compute the derivative of $h(x) = \sqrt{3x^2 - 4x + 2}$ using the basic rules of differentiation.


```{dropdown} **Step 1:** &nbsp; Remember the general power rule.

Since $h(x)$ can be rewritten as $(3x^2 - 4x + 2)^{1/2}$, remember the general power rule.

$$
\frac{d}{dx}[f(x)]^n = n[f(x)]^{n-1}f'(x)
$$
```

```{dropdown} **Step 2:** &nbsp; Apply the rule and simplify.

Apply the general power rule with $n=1/2$ and $f(x) = 3x^2 - 4x + 2$ and then simplify.

\begin{align*}
h'(x) &= \frac{d}{dx} (3x^2 - 4x + 2)^{1/2}\\ \\
&= \frac{1}{2}(3x^2 - 4x + 2)^{1/2 - 1}  \frac{d}{dx}(3x^2 - 4x + 2) && \hbox{general power rule}\\ \\
&= \frac{1}{2}(3x^2 - 4x + 2)^{-1/2}  (3\cdot 2x^{2-1} - 4x^{1-1} + 0)\\ \\
&= \frac{1}{2}(3x^2 - 4x + 2)^{-1/2}  (6x - 4)\\ \\
&= \frac{2(3x-2)}{2(3x^2-4+2)^{1/2}} &&\hbox{simplify}\\ \\
&= \frac{3x-2}{\sqrt{3x^2-4+2}}
\end{align*}
```
````

### Example 5 
````{admonition} Product and General Power Rule
:class: tip

Compute the derivative of $h(x) = (4x+1)^3(2x-5)^4$ using the basic rules of differentiation.


```{dropdown} **Step 1:** &nbsp; Remember the product rule.

Since $h(x)$ is the product of two functions, remember the product rule for derivatives.

$$
\frac{d}{dx}[f(x)g(x)]=f'(x)g(x)+f(x)g'(x)
$$
```

```{dropdown} **Step 2:** &nbsp; Apply the product rule.

Apply the product rule with $f(x) = (4x+1)^3$ and $g(x) = (2x-5)^4$.

\begin{align*}
h'(x) 
&= \left[\frac{d}{dx}(4x+1)^3\right](2x-5)^4 + (4x+1)^3\left[\frac{d}{dx}(2x-5)^4\right]\\ \\
&= \left[3(4x+1)^2\cdot 4\right](2x-5)^4 + (4x+1)^3\left[4(2x-5)^3\cdot 2\right] 
\end{align*}

Notice how the general power rule was used to compute the derivative of both $(4x+1)^3$ and $(2x-5)^4$.
```

```{dropdown} **Step 3:** &nbsp; Pull out common factors.

\begin{align*}
h'(x) &= 4(4x+1)^2(2x-5)^3\left[3(2x-5) + 2(4x+1)\right]
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Simplify.

\begin{align*}
h'(x) &= 4(4x+1)^2(2x-5)^3\left[6x-15 + 8x+2\right]\\ \\
&= 4(4x+1)^2(2x-5)^3(14x-13)
\end{align*}
```
````


### Example 6 
````{admonition} Quotient and General Power Rule
:class: tip

Compute the derivative of $h(x) = \dfrac{x^5}{(4x-7)^3}$ using the basic rules of differentiation.


```{dropdown} **Step 1:** &nbsp; Remember the quotient rule.

Since $h(x)$ is the quotient of two functions, remember the quotient rule for derivatives.

$$
\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right]=\frac{f'(x)g(x)-f(x)g'(x)}{[g(x)]^2}
$$
```

```{dropdown} **Step 2:** &nbsp; Apply the quotient rule.

Apply the quotient rule with $f(x) = x^5$ and $g(x) = (4x-7)^3$.

\begin{align*}
h'(x) 
&= \frac{\left[\frac{d}{dx}x^5\right](4x-7)^3 - x^5 \left[\frac{d}{dx}(4x-7)^3\right]}{[(4x-7)^3]^2} \\ \\
&= \frac{\left[5x^4\right](4x-7)^3 - x^5 \left[3(4x-7)^2 4\right]}{[(4x-7)^3]^2} && \hbox{power rule & general power rule}\\ \\
&= \frac{5x^4(4x-7)^3 - 12x^5 (4x-7)^2}{(4x-7)^6}  && \hbox{simplify}
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Pull out common factors from the numerator.

\begin{align*}
h'(x) &= \frac{x^4(4x-7)^2[5(4x-7) - 12x ]}{(4x-7)^6} 
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Simplify.

\begin{align*}
h'(x) &= \frac{x^4\cancel{(4x-7)^2}[20x-35 - 12x]}{(4x-7)^{\cancel{6}4}} \\ \\
&= \frac{x^4(8x-35)}{(4x-7)^4} 
\end{align*}
```
````

## An Applied Example

### Example 7 
````{admonition} Rate of Change of Unit Price
:class: tip

Penn State Learning has a weekly demand function for their calculators which is given by

$$p = d(x) = 300 - 2x^2$$

where $p$ is measured in dollars and $x$ is measured in thousands of calculators. What is the instantaneous rate of change of the unit price when the quantity demanded is $5000$ calculators?


```{dropdown} **Step 1:** &nbsp; Determine &nbsp; $x$.

Notice that $x = 5$ because units are in thousands of calculators demanded.
```

```{dropdown} **Step 2:** &nbsp; Compute the derivative.

In order to compute the instantaneous rate of change, we need to compute the derivative, $d'(x)$. 

\begin{align*}
d'(x) &= \frac{d}{dx}(300 - 2x^2)\\ \\
&= \frac{d}{dx}300 - \frac{d}{dx}2x^2 && \hbox{difference rule}\\ \\
&= 0 - 2\frac{d}{dx}x^2 && \hbox{$\dfrac{d}{dx}c = 0$ & constant multiple rule} \\ \\
&= - 2\cdot 2x && \hbox{power rule}\\ \\
&= -4x
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Plug in &nbsp; $x=5$.

Lastly, substitute $x = 5$ into $d'(x)$.

$$d'(5) = -4\cdot5 = -20$$

Therefore, the instantaneous rate of change of the unit price is $-20$ dollars per thousand calculators when the quantity demanded is 5000 calculators.  This means that the unit price would decrease by approximately 20 dollars if the demand increased from 5000 to 6000 calculators.
```
````

## Using the Derivative to Compute Limits

### Example 8
````{admonition} Evaluate a Limit using a Derivative
:class: tip

Use the limit definition of the derivative to evaluate 

$$\lim_{h\to 0}\dfrac{(x+h)^2-5(x+h)-(x^2-5x)}{h}.$$


```{dropdown} **Step 1:** &nbsp; Recall the limit definition of the derivative.

Begin with the limit definition of the derivative. 

$$
f'(x) = \lim_{h\to 0} \frac{f(x+h) - f(x)}{h}
$$
```

```{dropdown} **Step 2:** &nbsp; Identify &nbsp; $f(x)$.

Identify the $f(x)$ in the limit definition of $f'(x)$ for our problem.  If we focus on the $f(x)$ that is being subtracted in the numerator of the limit definition of $f'(x)$, this appears to coincide with the $(x^2-5x)$ that is being subtracted in the numerator of our limit.  So we hypothesize that 

$$f(x) = x^2 - 5x.$$
```

```{dropdown} **Step 3:** &nbsp; Verify choice of &nbsp; $f(x)$.

Verify that the given limit is equal to the limit definition of the derivative of $f(x) = x^2-5x$. 

If $f(x) = x^2-5x$ then $f(x+h) = (x+h)^2 - 5(x+h)$ and therefore 

$$\lim_{h\to 0}\dfrac{(x+h)^2-5(x+h)-(x^2-5x)}{h} = \lim_{h\to 0} \frac{f(x+h) - f(x)}{h} = f'(x)$$

Since the given limit is equal to the derivative of $x^2-5x$, we can evaluate the limit by computing the derivative of $x^2-5x$ instead of algebraically simplifying it.
```

```{dropdown} **Step 4:** &nbsp; Evaluate the limit by computing the derivative.

Evaluate the given limit by computing the derivative of $f(x) = x^2-5x$ using the basic rules of differentiation.

\begin{align*}
\lim_{h\to 0}\dfrac{(x+h)^2-5(x+h)-(x^2-5x)}{h} 
&= \frac{d}{dx}(x^2-5x)\\ \\
&= \frac{d}{dx}x^2 - \frac{d}{dx}5x && \hbox{difference rule}\\ \\
&= 2x - 5
\end{align*}
```
````

### Example 9
````{admonition} Evaluate a Limit using a Derivative
:class: tip

Use the limit definition of the derivative to evaluate 

$$\lim_{h\to 0}\dfrac{(2+h)^3-8}{h}.$$


```{dropdown} **Step 1:** &nbsp; Recall the limit definition of the derivative.

$$
f'(x) = \lim_{h\to 0} \frac{f(x+h) - f(x)}{h}
$$
```

```{dropdown} **Step 2:** &nbsp; Identify &nbsp; $f(x)$.

Identity the $f(x)$ in the limit definition of $f'(x)$ for our problem.  If we focus on the $f(x+h)$ in the numerator of the limit definition of $f'(x)$, this appears to coincide with the $(2+h)^3$ in the numerator of our limit.  So we hypothesize that 

$$f(x) = x^3 ~~~~\hbox{ and } ~~~~ x = 2.$$
```

```{dropdown} **Step 3:** &nbsp; Verify choice of &nbsp; $f(x)$.

Verify that the given limit is equal to the limit definition of the derivative of the function $f(x) = x^3$ at $x=2$. 

If $f(x) = x^3$ then $f(2+h) = (2+h)^3$ and $f(2) = 2^3 = 8$. Therefore 

$$\lim_{h\to 0}\dfrac{(2+h)^3-8}{h} = \lim_{h\to 0} \frac{f(2+h) - f(2)}{h} = f'(2)$$

Since the given limit is equal to the derivative of $x^3$ at $x=2$, we can evaluate the limit by computing the derivative of $x^3$ instead of algebraically simplifying it.
```



```{dropdown} **Step 4:** &nbsp; Evaluate the limit by computing the derivative.

Evaluate the given limit by computing the derivative of $f(x) = x^3$ and then plugging in $x=2$.

\begin{align*}
\lim_{h\to 0}\dfrac{(2+h)^3-8}{h} 
&= f'(2) \\ \\
&= 3\cdot 2^2  && \hbox{since $f'(x) = 3x^2$}\\ \\
&= 12
\end{align*}
```
````
