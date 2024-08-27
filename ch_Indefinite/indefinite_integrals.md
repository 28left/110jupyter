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
# Indefinite Integrals

## The Antiderivative



```{admonition} Definition
:class: info

A function $F$ is an _**antiderivative**_ of $f$ on an interval $I$ if 

$$F'(x) = f(x)$$ 

for all $x$ in $I$.

In other words, the phrase "*$F$ is an antiderivative of $f$*" means the same thing as the phrase "*$f$ is the derivative of $F$*."
```


### Example 1
````{admonition} Verify a function is an antiderivative
:class: tip

Show that $F(x) = 3x^5 + 4x^3 + 7x$ is an antiderivative of $f(x) = 15x^4+12x^2+7$.

```{dropdown} **Step 1:** &nbsp; Verify that $F'(x) = f(x)$.

\begin{align*}
  F'(x) &= \frac{d}{dx}\left( 3x^5 + 4x^3 + 7x \right)  \\
  &= 3 \cdot 5 x^4+ 4\cdot 3x^2 + 7\\
  & = 15x^4+12x^2+7 \\
  & = f(x)
\end{align*}

Because $F'(x) = f(x)$, $F$ is an antiderivative of $f$.
```
````


### Example 2
````{admonition} Verify a function is an antiderivative
:class: tip

Show that $G(x) = 3x^5 + 4x^3 + 7x + 71$ is an antiderivative of $f(x) = 15x^4+12x^2+7$.

```{dropdown} **Step 1:** &nbsp; Verify that $G'(x) = f(x)$.

\begin{align*}
  G'(x) &= \frac{d}{dx}\left( 3x^5 + 4x^3 + 7x + 71\right)  \\
  &= 3 \cdot 5 x^4+ 4\cdot 3x^2 + 7 + 0\\
  & = 15x^4+12x^2+7 \\
  & = f(x)
\end{align*}

Because $G'(x) = f(x)$, $G$ is an antiderivative of $f$.
```
````


```{admonition} Observation
:class: important

In the previous two examples, the functions $F(x)$ and $G(x)$ were both shown to be antiderivatives of $f(x) = 15x^4+12x^2+7$.  This implies that antiderivatives are not unique.  Also notice that $G(x) = F(x) + 71$ and adding a constant to a function doesn't change its derivative since the derivative of a constant is zero.  So once we knew that $F(x)$ was an antiderivative of $f(x)$, we didn't need to verify that $G(x)$ was also an antiderivative of $f(x)$ since it only differs from $F(x)$ by a constant.

In general, if $F$ is an antiderivative of $f$, then $F(x) + C$, where $C$ is any constant, is also an antiderivative of $f$.  Furthermore, every antiderivative of $f$ must be of the form $F(x) + C$ for some constant $C$.

```

## The Indefinite Integral

```{admonition} Definition and Notation
:class: info

The _**indefinite integral of $f(x)$ with respect to $x$**_, denoted

$$\int f(x) ~dx$$

represents the most general antiderivative of $f$. 

The symbol $\displaystyle \int$ is called an _**integral sign**_ and the symbol $dx$ is called a _**differential**_, which indicates the variable of integration. 
```


```{admonition} The Most General Antiderivative
:class: info
If $F$ is an antiderivative of $f$, then the most general antiderivative of $f$ is given by

$$\int f(x) ~dx = F(x) + C$$

where $C$ is an arbitrary constant referred to as the _**constant of integration**_.
```





### Example 3
````{admonition} Indefinite integral
:class: tip

Compute $\displaystyle \int 15x^4+12x^2+7 ~dx.$

```{dropdown} **Answer**

From Example 1 above, we know that $3x^5 + 4x^3 + 7x$ is an antiderivative of $15x^4+12x^2+7$.  Therefore,

$$ \int 15x^4+12x^2+7 ~dx = 3x^5 + 4x^3 + 7x + C.$$

Therefore, every antiderivative of $15x^4+12x^2+7$ can be written as $3x^5 + 4x^3 + 7x + C$ for some constant $C$.
```
````
