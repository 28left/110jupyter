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
# Laws of Exponential and Logarithmic Functions

## Laws, Properties, and Derivatives

````{admonition} Laws of Exponential and Logarithmic Functions
:class: info
Let $a$ and $b$ be positive numbers and $x$ and $y$ be real numbers. Let $m$ and $n$ be positive numbers.

::::{grid} 2
:::{grid-item-card} Exponential
- **Addition of Exponents Law**

  $$b^x b^y = b^{x + y}$$

- **Difference of Exponents Law**

  $$\frac{b^x}{b^y} = b^{x - y}$$

- **Exponentiation Law**

  $$\left( b^x \right)^y = b^{xy}$$

- **Product Distribution Law**

  $$(ab)^x = a^xb^x$$

- **Fractional Distribution Law**

  $$\left(\frac{a}{b}\right)^x = \frac{a^x}{b^x}$$
:::

:::{grid-item-card} Logarithmic
- **Logarithmic Addition Law** 
  
  $$\log_{b}(mn) = \log_b(m) + \log_b(n)$$

- **Logarithmic Subtraction Law**

  $$\log_{b}\left( \frac{m}{n} \right) = \log_b(m) - \log_b(n)$$

- **Logarithm of a Power**

  $$\log_b(m^n) = n \log_b(m)$$

- **Logarithm of 1**

  $$\log_b(1) = 0 ~~\&~~ \ln(1) = 0$$

- **Logarithm of the Base**

  $$\log_b(b) = 1 ~~\&~~ \ln(e) = 1$$
:::
::::
````


````{admonition} Cancellation Properties of $e^x$ and $\ln(x)$
:class: info 

::::{grid} 2
:::{grid-item-card} 

- For all $x>0$  
  
  $$e^{\ln(x)} = x$$
:::

:::{grid-item-card} 
- For all $x$ 

  $$\ln(e^x) = x$$
:::
::::
````

````{admonition} Derivatives of $e^x$ and $\ln(x)$
:class: info 

::::{grid} 2
:::{grid-item-card}

- **Derivative of $e^x$**

  $$\frac{d}{dx}e^x = e^x$$

- **Derivative of $e^{f(x)}$**

  $$\frac{d}{dx}e^{f(x)} = e^{f(x)} f'(x)$$
:::

:::{grid-item-card}
- **Derivative of $\ln(x)$**

  $$\frac{d}{dx}\ln(x) = \frac{1}{x}$$

- **Derivative of $\ln(f(x))$**

  $$\frac{d}{dx}\ln(f(x)) = \frac{1}{f(x)} f'(x)$$

:::
::::
````


### Example 1
````{admonition} Solve for unknown value in the exponent
:class: tip

Find all values of $x$ such that $\displaystyle 4^{x-x^2} = \frac{1}{16^x}$.

```{dropdown} **Step 1:** &nbsp; Write both sides of the equation as a power of &nbsp; $4$.
:color: light
:animate: fade-in

Since the left-hand side is already written as a power of $4$, focus on the right-hand side.

\begin{align*}
  \frac{1}{16^x} 
  &= 16^{-x} \\
  &= (4^2)^{-x}  && \hbox{since $16 = 4^2$}\\
  &= 4^{-2x} && \hbox{since $(b^x)^y = b^{xy}$}
\end{align*}

Therefore, the original equation can be rewritten in the following manner:

$$4^{x-x^2} = 4^{-2x}.$$
```


```{dropdown} **Step 2:** &nbsp; Set the exponents equal to each other, and solve for &nbsp; $x$.
:color: light
:animate: fade-in

\begin{align*}
  x-x^2 &= -2x && \\
  3x-x^2 &= 0 && \text{move all variables to one side}\\
  x(3-x) &= 0 && \text{factor}\\
  x = 0&, x = 3 && \text{folve for $x$ by setting each factor equal to $0$}
\end{align*}
```
````

### Example 2
````{admonition} Solve for unknown value in the exponent
:class: tip

Find all values of $x$ such that: 

$$2^{2x}-40\cdot 2^x +256 = 0.$$

```{dropdown} **Step 1:** &nbsp; Rewrite the equation in terms of &nbsp; $2^x$.
:color: light
:animate: fade-in

$$(2^x)^2 -40\cdot 2^x+256 = 0.$$
```

```{dropdown} **Step 2:** &nbsp; Let &nbsp; $u = 2^x$.
:color: light
:animate: fade-in

$$u^2-40u+256 =0.$$
```

```{dropdown} **Step 3:** &nbsp; Factor and solve for &nbsp; $u$.
:color: light
:animate: fade-in

$$(u-8)(u-32) = 0.$$

$$u=8 ~~~~ \hbox{ or } ~~~~ u=32.$$
```

```{dropdown} **Step 4:** &nbsp; Substitute &nbsp; $2^x$ &nbsp; back in for &nbsp; $u$ &nbsp; and solve for &nbsp; $x$.
:color: light
:animate: fade-in

\begin{align*}
  2^x &= 8 & 2^x &= 32\\
  x&=3 & x&=5
\end{align*}
```
````

### Example 3
````{admonition} Solve for unknown value in the exponent
:class: tip

Find all values of $t$ such that $\dfrac{360}{1+9e^{-2t}} = 90$.

```{dropdown} **Step 1:** &nbsp; Isolate &nbsp; $e^{-2t}$ &nbsp; using the following steps.
:color: light
:animate: fade-in

\begin{align*}
  360 &= 90(1+9e^{-2t}) && \text{multiply both sides by the denominator} \\ \\
  4 &= 1+9e^{-2t} && \text{divide both sides by 90} &&\\ \\
  3 &= 9e^{-2t} && \text{subtract 1 from both sides}&&\\ \\
  1/3 &= e^{-2t} && \text{divide both sides by 9}&&
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Take the natural logarithm of both sides.
:color: light
:animate: fade-in

\begin{align*}
  \ln \left(\frac{1}{3} \right) 
  &= \ln(e^{-2t}) \\ 
  &= -2t && \hbox{cancellation property $\ln(e^x) = x$}
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Solve for &nbsp; $t$.
:color: light
:animate: fade-in

\begin{align*}
  t 
  &= -\frac{1}{2}  \ln \left( \frac{1}{3}\right)\\
  &= \frac{1}{2}\ln(3)  && \hbox{since $\ln(1/3) = \ln(3^{-1}) = -\ln(3)$}
\end{align*}
```
````

### Example 4
````{admonition} Expand using properties of logarithms
:class: tip

Expand the following expression:

$$\ln \left(\frac{\sqrt[3]{(x+1)^2}\cdot e^{5x}}{x}\right).$$

```{dropdown} **Step 1:** &nbsp; Use the laws of logarithms to expand the given expression.
:color: light
:animate: fade-in

\begin{align*}
  \ln \left(\frac{\sqrt[3]{(x+1)^2}\cdot e^{5x}}{x}\right) 
  &= \ln(\sqrt[3]{(x+1)^2}\cdot e^{5x}) - \ln(x) && \text{since $\ln(m/n) = \ln(m) - \ln(n)$} \\ \\
  &= \ln(\sqrt[3]{(x+1)^2}) + \ln(e^{5x}) - \ln(x) && \text{since $\ln(mn) = \ln(m) + \ln(n)$}\\ \\
  %&= \ln((x+1)^{2/3}) + \ln(e^{5x}) - \ln(x)\\ \\
  &= \frac{2}{3} \ln(x+1) + 5x \ln(e) - \ln(x) && \text{sine $\ln(m^n) = n\ln(m)$}\\ \\
  &= \frac{2}{3} \ln(x+1) + 5x - \ln(x) && \text{since $\ln(e) = 1$.}
\end{align*}
```
````

### Example 5
````{admonition} Equation of the tangent line
:class: tip

Find the tangent line to $y=\dfrac{e^{27x}}{x^9}$ at the point $(1,e^{27})$.

```{dropdown} **Step 1:** &nbsp; Recall the point-slope equation of a line.
:color: light
:animate: fade-in

Point-Slope: 

$$y = m(x-a) + b,$$

where $m$ is the slope of the line and $(a,b)$ is a point on the line.
```

```{dropdown} **Step 2:** &nbsp; Compute the slope of the line by using the derivative. 
:color: light
:animate: fade-in

Recall $\dfrac{d}{dx}e^{f(x)} = e^{f(x)} f'(x)$.

$$y' = \frac{e^{27x}\cdot 27 \cdot x^9 - e^{27x}\cdot 9x^8}{x^{18}}.$$

Since the given point is $(1,e^{27})$, plug in $x=1$ into the derivative to find the slope of the tangent line.

\begin{align*}
  m
  &= y'(1) \\
  &= \frac{e^{27}\cdot 27 - e^{27}\cdot 9}{1}\\
  &= 18e^{27}.
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Write down the equation of the tangent line.
:color: light
:animate: fade-in

Since we were given the point $(1,e^{27})$ (i.e., $a=1$ and $b=e^{27}$) and we found the slope ($m=18e^{27}$), we can now write down the equation of the tangent line using the point-slope equation of a line. 

$$y = 18e^{27}(x-1) + e^{27}.$$
```
````


### Example 6
````{admonition} Marginal revenue function
:class: tip

Suppose the unit selling price $p(x)$ and the quantity supplied $x$ of a certain product is given by 

$$p(x) = x^3e^{5x}+12.$$


Find the marginal revenue function $R'(x)$.

```{dropdown} **Step 1:** &nbsp; Find the revenue function, &nbsp; $R(x)$, using the formula &nbsp; $R(x) = x\cdot p(x)$.
:color: light
:animate: fade-in

$$R(x) = x^4e^{5x} +12x.$$
```

```{dropdown} **Step 2:** &nbsp; Compute the derivative of &nbsp; $R(x)$. 
:color: light
:animate: fade-in

Recall $\dfrac{d}{dx}e^{f(x)} = e^{f(x)} f'(x)$.

\begin{align*}
  R'(x) 
  &= 4x^3(e^{5x})+x^4(e^{5x}\cdot 5) + 12 && \text{using product rule}\\
  &= x^3 e^{5x}(4+5x) + 12.
\end{align*}
```
````


### Example 7
````{admonition} Derivative of a logarithmic function
:class: tip

Compute the derivative of $f(x) = \ln\left(\dfrac{\sqrt{6x+1}}{5x}\right)$.

```{dropdown} **Step 1:** &nbsp; Expand &nbsp; $f(x)$ &nbsp; using laws of logarithms.
:color: light
:animate: fade-in

\begin{align*}
  \ln\left(\dfrac{\sqrt{6x+1}}{5x}\right)
  &= \ln(\sqrt{6x+1}) - \ln(5x) && \hbox{since $\ln(m/n) = \ln(m) - \ln(n)$} \\ \\
  &= \ln((6x+1)^{1/2}) - [\ln(5) + \ln(x)] && \hbox{since $\ln(mn) = \ln(m) + \ln(n)$} \\ \\
  &= \frac{1}{2}\ln(6x+1) - \ln(5) - \ln(x) && \hbox{since $\ln(m^n) = n\ln(m).$}
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Compute the derivative. 
:color: light
:animate: fade-in

Recall $\dfrac{d}{dx}\ln(f(x)) = \dfrac{1}{f(x)} f'(x)$.
 
\begin{align*}
  \frac{d}{dx}\left(\frac{1}{2}\ln(6x+1) - \ln(5) - \ln(x)\right)
  &= \frac{1}{2}\cdot \frac{1}{6x+1}\cdot 6 - 0 - \frac{1}{x} \\
  &= \frac{3}{6x+1} - \frac{1}{x}.
\end{align*}
```
````


### Example 8
````{admonition} Implicit differentiation
:class: tip

Let $\ln(xy)+y^7 = x^3 + 2x$. Find $\dfrac{dy}{dx}$.

```{dropdown} **Step 1:** &nbsp; Differentiate both sides using implicit differentiation.
:color: light
:animate: fade-in

$$\frac{1}{xy} (y +xy') + 7y^6y' = 3x^2+2.$$
```

```{dropdown} **Step 2:** &nbsp; Multiply both sides by &nbsp; $xy$.
:color: light
:animate: fade-in

\begin{align*}
  xy\left[ \frac{1}{xy} (y +xy') + 7y^6y' \right]
  &= xy\frac{1}{xy} (y +xy') + xy\cdot 7y^6y' \\
  &= (y+xy') + 7xy^7y'\\
  \\
  xy\left[ 3x^2 + 2 \right]
  &= 3x^3y + 2xy.
\end{align*}

Therefore, 

$$y+xy' + 7xy^7y' = 3x^3y + 2xy.$$
```

```{dropdown} **Step 3:** &nbsp; Rearrange terms.
:color: light
:animate: fade-in

Rearrange terms so that any term with a factor of &nbsp; $y'$ &nbsp; is on the left-hand side of the equation and all other terms are on the right-hand side.

$$xy' + 7xy^7y' = 3x^3y + 2xy - y.$$
```

```{dropdown} **Step 4:** &nbsp; Factor out &nbsp; $y'$ &nbsp; on the left-hand side.
:color: light
:animate: fade-in

$$y'(x + 7xy^7) = 3x^3y + 2xy - y.$$
```

```{dropdown} **Step 5:** &nbsp; Solve for &nbsp; $y'$.
:color: light
:animate: fade-in

$$y' = \frac{3x^3y + 2xy - y}{x + 7xy^7}.$$
```
````