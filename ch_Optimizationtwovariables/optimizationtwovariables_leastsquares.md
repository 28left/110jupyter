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

# Least Squares

## Solving a System of Linear Equations

### Example

## The Least-Squares Line

```{admonition} The Method of Least Squares
:class: info

Suppose we are given the following $n$ data points:

$$(x_1,y_1), (x_2,y_2), (x_3,y_3), \ldots, (x_n,y_n)$$

The _**least-squares line**_ or _**regression line**_ for the data is the line that best fits the data points and is determined by the _**method of least squares**_.  More specifically, the least-squares line is given by

$$y = mx + b$$

where $m$ and $b$ are the unique solutions to the equations

\begin{align*}
\left(\Sigma x^2\right) m + \left(\Sigma x\right) b &= \Sigma xy \\
\left(\Sigma x\right) m + n b &= \Sigma y 
\end{align*}

and

\begin{align*}

\Sigma x &= x_1 + x_2 + x_3 + \cdots + x_n \\
\Sigma y &= y_1 + y_2 + y_3 + \cdots + y_n \\
\Sigma x^2 &= x_1^2 + x_2^2 + x_3^2 + \cdots + x_n^2 \\
\Sigma xy &= x_1y_1 + x_2y_2 + x_3y_3 + \cdots + x_ny_n

\end{align*}

```


### Example

````{admonition} Sales in millions
:class: tip


::::{grid} auto
:::{grid-item-card}
:margin: auto
| Year, $x$   | 0   | 1   | 2   | 3   | 
|-------|-----|-----|-----|-----|
| **Sales**, $y$ | 0.4 | 1.4 | 1.0 | 2.2 |
:::
::::




```{dropdown} **Step 1:** &nbsp; Calculate $\Sigma x^2$, $\Sigma x$, $\Sigma xy$ and $\Sigma y$.


::::{grid} auto
:::{grid-item-card}
:margin: auto
| $x$   | 0   | 1   | 2   | 3   | $\Sigma x = 6$   |
|-------|-----|-----|-----|-----|------------------|
| $y$ | 0.4 | 1.4 | 1.0 | 2.2 | $\Sigma y = 5.0$ |
| $x^2$ | 0 | 1 | 4 | 9 | $\Sigma x^2 = 14$ |
| $xy$  | 0 | 1.4 | 2.0 | 6.6 | $\Sigma xy = 10.0$ |
:::
::::


```

```{dropdown} **Step 2:** &nbsp; Set up system of equations.

Based on the values computed in **Step 1**, the slope $m$ and the $y$-intercept $b$ corresponding to the least-squares line $y=mx+b$ are the unique solution to 

\begin{align*}
14 m + 6 b &= 10\\
6 m + 4 b &= 5
\end{align*}

```

```{dropdown} **Step 3:** &nbsp; Solve system of equations.

````





