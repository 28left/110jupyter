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
# Logarithmic Differentiation

```{admonition} Compute Derivatives using Logarithmic Differentiation
:class: info

The process of logarithmic differentiation can be used to compute the derivative of any function, but is particularly useful when the function involves products, quotients, and/or powers that can be expanded using laws of logarithms.  Starting with:

$$y = f(x)$$

the process of logarithmic differentiation is carried out in the following manner.

1. Take the natural logarithm of both sides of the above equation and use the properties of logarithms to expand $\ln(f(x))$. 

2. Differentiate both sides (implicitly on the left-hand side, explicitly on the right-hand side) of the equation with respect to $x$. In particular, notice that:

    $$\frac{d}{dx} \ln(y) = \frac{y'}{y}.$$
3. Solve the resulting equation for $y'$ (by multiplying both sides by $y$) and then replace $y$ with $f(x)$.
```

## Example 9

Compute the derivative of $f(x) = \dfrac{(5x+1)^7}{x^4\sqrt{x^3+4}}$.

```{admonition} Step 1: Observe that $f(x)$ involves products, quotients, and powers.
:class: tip, dropdown

While $f'(x)$ could be computed using the product, quotient, and general power rules of differentiation, it is a good candidate for logarithmic differentiation.
```

```{admonition} Step 2: Take the natural logarithm of both sides of $y=f(x)$ and expand $\ln(f(x))$ using laws of logarithms.
:class: tip, dropdown

\begin{align*}
    \ln(y) 
    &= \ln\left( \dfrac{(5x+1)^7}{x^4\sqrt{x^3+4}}\right) \\ \\
    &= \ln((5x+1)^7) - \ln(x^4\sqrt{x^3+4}) && \hbox{since $\ln(m/n) = \ln(m) - \ln(n)$} \\ \\
    &= \ln((5x+1)^7) - [\ln(x^4) + \ln(\sqrt{x^3+4})]&& \hbox{since $\ln(mn) = \ln(m) + \ln(n)$} \\ \\
    &= \ln((5x+1)^7) - \ln(x^4) - \ln((x^3+4)^{1/2}) \\ \\
    &= 7\ln(5x+1) - 4\ln(x) - \frac{1}{2}\ln(x^3+4) && \hbox{since $\ln(m^n) = n\ln(m)$.}
\end{align*}
```

```{admonition} Step 3: Differentiate both sides. Recall $\dfrac{d}{dx}\ln(f(x)) = \dfrac{1}{f(x)} f'(x)$.
:class: tip, dropdown

\begin{align*}
    \frac{y'}{y} 
    &= \frac{d}{dx}\left[7\ln(5x+1) - 4\ln(x) - \frac{1}{2}\ln(x^3+4) \right]\\ \\
    &= 7\frac{1}{5x+1}\cdot 5 - 4\frac{1}{x} - \frac{1}{2} \cdot \frac{1}{x^3+4}\cdot 3x^2\\ \\
    &= \frac{35}{5x+1} - \frac{4}{x} - \frac{3x^2}{2(x^3+4).}
\end{align*}
```

```{admonition} Step 4: Solve for $y'$ (by multiplying both sides by $y$) and replace $y$ with $f(x)$.
:class: tip, dropdown

\begin{align*}
    y'
    &= y \left[ \frac{35}{5x+1} - \frac{4}{x} - \frac{3x^2}{2(x^3+4)} \right] \\ \\
    &= \dfrac{(5x+1)^7}{x^4\sqrt{x^3+4}} \left[ \frac{35}{5x+1} - \frac{4}{x} - \frac{3x^2}{2(x^3+4)} \right]. 
\end{align*}
```

## Example 10

Compute the derivative of $f(x) = \left(3x+5\right)^{x^2}$.

```{admonition} Step 1: Recognize the form of $f(x)$.
:class: tip, dropdown

Observe that $f(x)$ is a function of $x$ (i.e., $3x+5$) raised to another function of $x$ (i.e., $x^2$). Logarithmic differentiation is the only technique of differentiation that can be applied to functions of the form $h(x)^{g(x)}$, as is the case here.
```

```{admonition} Step 2: Take the natural logarithm of both sides of $y=f(x)$ and expand $\ln(f(x))$ using laws of logarithms.
:class: tip, dropdown

\begin{align*}
    \ln(y) 
    &= \ln \left( (3x+5)^{x^2}\right) \\ \\
    &= x^2 \ln(3x+5) && \hbox{since $\ln(m^n) = n\ln(m)$.}
\end{align*}
```

```{admonition} Step 3: Differentiate both sides. 
:class: tip, dropdown

Recall $\dfrac{d}{dx}\ln(f(x)) = \dfrac{1}{f(x)} f'(x)$.

\begin{align*}
    \frac{y'}{y} 
    &= 2x \ln(3x+5) + x^2 \frac{1}{3x+5}\cdot 3  & \hbox{using the Product Rule}\\ \\
    &= 2x \ln(3x+5) +  \frac{3x^2}{3x+5}.
\end{align*}
```

```{admonition} Step 4: Solve for $y'$ (by multiplying both sides by $y$) and replace $y$ with $f(x)$.
:class: tip, dropdown

\begin{align*}
    y'
    &= y \left[ 2x \ln(3x+5) +  \frac{3x^2}{3x+5} \right] \\ \\
    &= \left( 3x+5\right)^{x^2} \left[ 2x \ln(3x+5) +  \frac{3x^2}{3x+5} \right]. 
\end{align*}
```