---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3.9.6 64-bit
  language: python
  name: python3
---
# Implicit Differentiation

## The Rules

```{admonition} Explicit versus Implicit Functions
:class: info

Suppose we have an equation relating two variables: $x$ and $y$.  If $y$ is isolated on one side of the equation, we say that $y$ is **explicitly defined** as a function of $x$, or simply, $y$ is a function of $x$. If $y$ is not isolated on one side of the equation, we say that $y$ is **defined implicitly** in terms of $x$, or $y$ is an implicit function of $x$.

**Explicit Functions**
- $y = x^2 - 3$
- $y = \sqrt{x + 7}$

**Implicit Functions**
- $x^2 + xy - y = 1$
- $x^3 + y^3 + yx - 4 = 0$

```

```{admonition} Computing Derivatives Implicitly
:class: info

When computing the derivative of a function involving $x$ and $y$ (where we treat $y$ as a function of $x$), it may be helpful to replace $y$ with $f(x)$ and recall the general power rule:

$$\frac{d}{dx} [f(x)]^n = n[f(x)]^{n-1} f'(x)$$

```

(05_01_example1)=
### Example 1

Compute the derivative of $x^2 y^3$ with respect to $x$ by treating $y$ as a function of $x$.


```{dropdown} **Step 1:** Replace $y$ with $f(x)$.

Since we are treating $y$ as a function of $x$, we can rewrite $x^2 y^3$ as 

$$x^2 [f(x)]^3.$$
```

```{dropdown} **Step 2:** Differentiate with respect to $x$.

Since $x^2[f(x)]^3$ is a product of two functions of $x$, namely $x^2$ and $[f(x)]^3$, we begin by using the product rule.

\begin{align*}
\frac{d}{dx} x^2 [f(x)]^3  
&= \left[\frac{d}{dx}x^2\right][f(x)]^3 + x^2 \left[\frac{d}{dx}[f(x)]^3\right] && \hbox{Product Rule}\\ \\
%&= 2x[f(x)]^3 + x^2 \left[\frac{d}{dx}[f(x)]^3\right] && \hbox{Power \& General Power rules}\\
&= 2x[f(x)]^3 + x^2 3[f(x)]^2f'(x) && \hbox{Power & General Power Rules}\\
%&= 2x[f(x)]^3 + x^2 3[f(x)]^2f'(x) && \hbox{General Power Rule}\\
\end{align*}
```

```{dropdown} **Step 3:** And finally, replace $f(x)$ with $y$ and $f'(x)$ with $y'$.

$$\frac{d}{dx} x^2y^3 = 2xy^3 + 3x^2y^2y'$$
```

```{admonition} Derivative of a Constant Multiple of a Function
:class: info

Suppose we are given an equation relating the variables $x$ and $y$.  We can compute the derivative of $y$ with respect to $x$ using the following technique.

1. Differentiate both sides of the equation with respect to $x$.
2. If given, plug in specific values of $x$ and $y$ into the resulting equation.
3. Solve for $y'$ in terms of $x$ and $y$.
    1. Put all terms with a factor of $y'$ on the left side of the equation and everything else on the side of the equation.
    2. Factor out $y'$ from each term on the left side of the equation.
    3. Divide both sides by the appropriate factor to solve for $y'$.
```

### Example 2

Find $\dfrac{dy}{dx}$ where $y$ is defined implicitly by
${x^2}y - x^4 + y^3 = 1$.

```{dropdown} **Step 1:** Replace $y$ with $f(x)$.

$$x^2f(x) - x^4 + [f(x)]^3 = 1.$$
```

```{dropdown} **Step 2:** Differentiate both sides with respect to $x$.

$$[2xf(x) + x^2f'(x)] - 4x^3 + 3[f(x)]^2f'(x) = 0 $$
Notice the use of the product rule to compute the derivative of $x^2f(x)$ and the general power rule to compute the derivative of $[f(x)]^3$.
```

```{dropdown} **Step 3:** Rearrange terms so that only terms involving $f'(x)$ are on the left side.

$$x^2f'(x) + 3[f(x)]^2f'(x) = 4x^3 - 2xf(x).$$
```

```{dropdown} **Step 4:** Factor out $f'(x) on the left side of the equation.

$$(x^2 + 3[f(x)]^2)f'(x) = 4x^3 - 2xf(x).$$
```

```{dropdown} **Step 5:** Solve for $f'(x)$.

$$f'(x) = \frac{4x^3 - 2xf(x)}{x^2 + 3[f(x)]^2}.$$
```

```{dropdown} **Step 6:** And finally, replace $f(x)$ with $y$ and $f'(x)$ with $y'$ (or $\frac{dy}{dx}$).

$$\frac{dy}{dx} = \frac{4x^3 - 2xy}{x^2 + 3y^2}.$$
```

```{admonition} Observation
:class: warning

Once we get used to the idea of thinking of $y$ as a function of $x$, it's not necessary to replace $y$ with $f(x)$.  Instead, we can use the general power rule written in the following form:

\begin{align*}
\frac{d}{dx} y^n 
&= n y^{n-1} y'\\
&= n y^{n-1} \frac{dy}{dx}.
\end{align*}
```

### Example 3

Find the equation of the line tangent to the curve defined implicitly by

$$ x^2 y^3 - y^2 + xy = 5 $$

at the point  $(2,1)$.

```{dropdown} **Step 1:** 

Differentiate both sides with respect to $x$.

$$\left[ 2xy^3 + x^2 3y^2\frac{dy}{dx}\right] - 2y\frac{dy}{dx} + \left[y + x\frac{dy}{dx}\right] = 0$$

See [Implicit Differentiation, Example 1](05_01_example1) above for how to differentiate $x^2y^3$ implicitly.

```
```{dropdown} **Step 2:** Plug in specific values of $x$ and $y$.

Since we want to find the slope of the line tangent to the curve at the point $(2,1)$, plug in $x=2$ and $y=1$.

$$4 + 12\frac{dy}{dx} - 2\frac{dy}{dx} + 1 + 2\frac{dy}{dx} = 0.$$
```

```{dropdown} **Step 3:** Simplify and rearrange terms.

$$12\frac{dy}{dx} = -5.$$
```

```{dropdown} **Step 4:** Solve for $\dfrac{dy}{dx}$.

$$\frac{dy}{dx} = -\frac{5}{12}.$$
```

```{dropdown} **Step 5:** Use the point-slope equation of a line: $y - b = m(x-a)$.

The equation of the line tangent of the curve at the point $(2,1)$ is

$$y - 1 = -\frac{5}{12}(x-2).$$
```

### Example 4

Find $\dfrac{dy}{dx}$ at $(2,0)$ where $y$ is defined implicitly by

$$xy + x = \sqrt{2x + 7y}.$$

```{dropdown} **Step 1:** Differentiate both sides with respect to $x$.

Left Hand Side:
$$\displaystyle \frac{d}{dx}(xy + x) = y + x\frac{dy}{dx} + 1$.$

Right Hand Side: 
\begin{align*}
\displaystyle\frac{d}{dx}\sqrt{2x + 7y} &= \frac{d}{dx}(2x + 7y)^{1/2}\\
&= \frac{1}{2}(2x + 7y)^{-1/2}\frac{d}{dx}(2x + 7y)\\
&= \frac{1}{2\sqrt{2x + 7y}}\left(2 + 7\frac{dy}{dx}\right).
\end{align*}

Therefore,

$$y + x\frac{dy}{dx} + 1 = \frac{1}{2\sqrt{2x + 7y}}\left(2 + 7\frac{dy}{dx}\right).$$

```

```{dropdown} **Step 2:** Plug in the values $x=2$ and $y=0$.

$$2\frac{dy}{dx} + 1 = \frac{1}{4}\left(2 + 7\frac{dy}{dx}\right).$$
```

```{dropdown} **Step 3:** Expand both sides of the equation so that each side is written as a sum.

$$2\frac{dy}{dx} + 1 = \frac{1}{2} + \frac{7}{4}\frac{dy}{dx}.$$
```

```{dropdown} **Step 4:** Rearrange terms (i.e., subtract $1$ from both sides and subtract $\dfrac{7}{4}\dfrac{dy}{dx}$ from both sides).

$$\frac{1}{4}\frac{dy}{dx} = -\frac{1}{2}.$$
```

```{dropdown} **Step 5:** Solve for $\dfrac{dy}{dx}$ (i.e., multiply both sides by $4$).

$$\frac{dy}{dx} = -2.$$
```

```{admonition} Observation
:class: warning

Alternatively, we could multiply both sides of the equation in Step 2 by $4$ to get 

$$8\frac{dy}{dx} + 4 = 2 + 7\frac{dy}{dx}.$$

Now rearranging terms is a little easier since we don't have to deal with any fractions.
```

### Example 5

The demand equation for Dr. Hager's *Make Math Great Again* video series is given by

$$p = -4x^2 - 2x + 30$$

where $p$ is the wholesale unit price in dollars and $x$ is the quantity demanded in units of a thousand.  Compute the elasticity of demand when $x=2$.

```{admonition} Observation
:class: warning

Ordinarily when we compute elasticity of demand, the first thing we do is  find $x = f(p)$ by solving for $x$ in terms of $p$ in the given demand equation.  However in this case, solving for $x$ is easier said than done.  So instead, we will use implicit differentiation to compute $f'(p)$ when the time comes.
```

```{dropdown} **Step 1:** Compute the unit price $p$ when $x=2$.

\begin{align*}
p 
&= -4(2^2) - 2(2) + 30 & \hbox{since $p = -4x^2 - 2x + 30$} \\
&= -16 - 4 + 30 \\
&= 10
\end{align*} 
```

```{dropdown} **Step 2:** Compute $f(10)$.

Recall that $x=f(p)$ is the quantity demanded (in thousands) when the unit price is $p$ dollars.  We were given $x=2$ (and used that to determine $p=10$ in Step 1), which is equivalent to saying $f(10) = 2$.
```

```{dropdown} **Step 3:** Compute $f'(10)$

Compute the derivative of both sides of the demand equation ($p = -4x^2 - 2x + 30$) with respect to $p$.  Here is where we use implicit differentiation by thinking of $x$ as a function of $p$ (i.e., $x=f(p)$).

\begin{align*}
1 
&= \frac{d}{dp}(-4x^2 - 2x + 30) && \hbox{since $\dfrac{d}{dp}p = 1$}\\
&= -8xx' - 2x'
\end{align*}

Now plug in $x=2$ to get 

$$1 = -16x' - 2x' = -18x'$$

and therefore $x' = f'(10) = -1/18$.
```

```{dropdown} **Step 4:** Compute elasticity of demand using the values $p=10$, $f(10) = 2$, and $f'(10) = -1/18$.

\begin{align*}
E(10)
&= -\frac{10\cdot (-1/18)}{2} && \hbox{since $E(p) = -\dfrac{p\cdot f'(p)}{f(p)}$} \\
&= \frac{10}{2}\cdot \frac{1}{18} \\
&= \frac{5}{18}
\end{align*}
```