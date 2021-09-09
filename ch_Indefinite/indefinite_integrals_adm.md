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

A function $F$ is an **antiderivative** of $f$ on an interval $I$ if 

$$F'(x) = f(x)$$ 

for all $x$ in $I$.
```

In other words, the phrase "*$F$ is an antiderivative of $f$*" means the same thing as the phrase "*$f$ is the derivative of $F$*."

## Example 1

Show that $F(x) = 3x^5 + 4x^3 + 7x$ is an antiderivative of $f(x) = 15x^4+12x^2+7$.

```{dropdown} **Step 1:** Verify that $F'(x) = f(x)$.

\begin{align*}
  F'(x) &= \frac{d}{dx}\left( 3x^5 + 4x^3 + 7x \right)  \\
  &= 3 \cdot 5 x^4+ 4\cdot 3x^2 + 7\\
  & = 15x^4+12x^2+7 \\
  & = f(x)
\end{align*}

Because $F'(x) = f(x)$, $F$ is an antiderivative of $f$.
```

## The Indefinite Integral

```{admonition} Definition
:class: info

The indefinite integral of $f(x)$ with respect to $x$, denoted

$$\int f(x) ~dx$$

represents the most general antiderivative of $f$.
```

In other words, if $F$ is an antiderivative of $f$, then

$$\int f(x) ~dx = F(x)+C.$$