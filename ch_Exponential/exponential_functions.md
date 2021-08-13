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
# Exponential and Logarithmic Functions

```{admonition} Definition of an Exponential Function
:class: info

The function defined by

$$f(x) = b^x \qquad (b > 0, b \neq 1)$$

is called an **exponential function with base $b$ and exponent $x$**.

```

```{admonition} Properties of Exponential Functions
:class: info

For a function $y = b^x$, the following properties hold:

- Its domain is $(-\infty,\infty)$.
- Its range is $(0,\infty)$.
- Its graph passes through the point $(0,1)$ (i.e., $b^0 = 1$).
- It is continuous on $(-\infty,\infty)$.
- It is increasing on $(-\infty,\infty)$ if $b>1$ and decreasing on  $(-\infty,\infty)$ if $0<b<1$.
```

```{admonition} Definition of a Logarithmic Function
:class: info

\begin{align*}
f(x) = \log_b(x) & \qquad  (b>0,b \neq 1) 
\end{align*}

is called the **logarithmic function with base $b$** and is defined by

$$y = \log_b(x) ~~~~ \hbox{ if and only if } ~~~~ x = b^y.$$
```

```{admonition} Properties of Logarithmic Functions
:class: info

For a function $y = \log_{b}(x)$, the following properties hold:

- Its domain is $(0,\infty)$.
- Its range is $(-\infty,\infty)$.
- Its graph passes through the point $(1,0)$ (i.e., $\log_b(1) = 0$).
- It is continuous on $(0,\infty)$.
- It is increasing on $(0,\infty)$ if $b>1$ and decreasing on $(-\infty,\infty)$ if $0<b<1$.

```