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
# Piecewise Functions

## Definition

```{admonition} Definition
:class: info

A _**piecewise function**_ is a function whose domain is broken up into several subintervals and a different rule is used to define the function on each subinterval. 
```

### Example 1
```{admonition} A piecewise defined function
:class: tip

 Movie theaters frequently offer discounted ticket prices for shows that start before 4:00 pm.  If we let $p(t)$ represent the price of a ticket for a movie that starts at time $t$, then we could use the following notation to describe the scenario where a ticket costs 6 dollars if the movie starts before 4:00 pm and costs 10 dollars if the movie starts at 4:00 pm or later.

$$
p(t) = 
\begin{cases}
\$6 & \hbox{if $t<$ 4:00 pm} \\
\$10 & \hbox{if $t\geq $ 4:00 pm}
\end{cases}
$$
```


### Example 2
````{admonition} Evaluate a piecewise function
:class: tip

Evaluate the following piecewise function at $-1$, $0$ and $1$.

$$
f(x) = 
\begin{cases}
x^2 + 1 & \hbox{if $x < 0$} \\
3 & \hbox{if $x = 0$} \\
\sqrt{x+4} & \hbox{if $x > 0$} 
\end{cases}
$$


```{dropdown} **Step 1:** &nbsp; Evaluate $f(-1)$.

Since $-1 < 0$, use $f(x) = x^2 + 1$ to evaluate $f(-1)$.

$$f(-1) = (-1)^2 + 1 = 2$$
```

```{dropdown} **Step 2:**  &nbsp; Evaluate $f(0)$.
Since $x = 0$, $f(0) = 3$.
```

```{dropdown} **Step 3:**  &nbsp; Evaluate $f(1)$.

Since $1 > 0$, use $f(x) = \sqrt{x+4}$ to evaluate $f(1)$.

$$f(1) = \sqrt{1+4} = \sqrt{5}$$
```
````



### Example 3
````{admonition} Evaluate a piecewise function
:class: tip

Evaluate the following piecewise function at $4$, $5$ and $6$.

$$
g(x) = 
\begin{cases}
\dfrac{x^2 - 25}{x-5} & \hbox{if $x\neq 5$} \\
0 & \hbox{if $x = 5$} 
\end{cases}
$$



```{dropdown} **Step 1:** &nbsp; Evaluate $g(4)$.

Since $4 \neq 5$, use $g(x) = \dfrac{x^2 - 25}{x-5}$ to evaluate $g(4)$.

$$g(4) = \frac{4^2 - 25}{4-5} = 9$$
```



```{dropdown} **Step 2:** &nbsp; Evaluate $g(5)$.

Since $x = 5$, $g(5) = 0$.
```


```{dropdown} **Step 3:** &nbsp; Evaluate $g(6)$.

Since $6 \neq 5$, use $g(x) = \dfrac{x^2 - 25}{x-5}$ to evaluate $g(6)$.

$$g(6) = \frac{6^2 - 25}{6-5} = 11$$
```
````
