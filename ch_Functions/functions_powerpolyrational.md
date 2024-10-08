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
# Power, Polynomial & Rational Functions

## Definitions


```{admonition} Definition
:class: info

A _**power function**_ is a function that can be written in the form

$$ax^r$$

where $a$ and $r$ are constants.
```


```{admonition} Definition
:class: info

A _**polynomial function of degree $n$**_ is a function that can be written in the form

$$a_0 + a_1x + a_2x^2 + \cdots + a_nx^n$$

where $n$ is a nonnegative integer and the constants $a_0, a_1, \ldots, a_n$  ($a_n\neq 0$) are called the _**coefficients**_ of the polynomial.
```


```{admonition} Definition
:class: info

A _**rational function**_ is a function that can be written as the ratio of two polynomials.
```


```{admonition} Polynomials are Rational Functions
:class: note

Any polynomial function, $f(x)$, can also be written as a ratio of polynomials in the following manner:

$$\dfrac{f(x)}{1}$$ 

since the constant $1$ is a polynomial of degree zero.  In other words, every polynomial is also considered to be a rational function.
```



```{admonition} Domain Considerations
:class: info

- The domain of a polynomial function is all real numbers.
- The domain of a rational function, $f(x)/g(x)$, is all real numbers excluding values of $x$ such that $g(x) = 0$.
```


### Example 1

```{admonition} The square root function
:class: tip

The square root function, $\sqrt{x}$, is

- a power function since $\sqrt{x} = x^{1/2}$, but
- is neither a polynomial nor a rational function since it includes a fractional power of $x$.
```

### Example 2

```{admonition} The reciprocal function
:class: tip

The reciprocal function, $\dfrac{1}{x}$, is 

- a power function since $\dfrac{1}{x} = x^{-1}$, and 
- is also a rational function since it is the ratio of two polynomials, but 
- is not a polynomial since it includes a negative power of $x$.
```

### Example 3

```{admonition} The volume of a sphere
:class: tip

The volume of a sphere with radius $r$ is $\dfrac{4}{3}\pi r^3$, which is a power function, a polynomial, and a rational function in the variable $r$.
```

### Example 4

````{admonition} The product of polynomials
:class: tip

Show that $f(x) = (x^2 + 7)(x^3 - 1)$ is a polynomial (and therefore also a rational function) and determine its degree.

```{dropdown} **Step 1:** &nbsp; Expand the product using the FOIL technique.
 
$$(x^2 + 7)(x^3 - 1) = x^5 + 7x^3 - x^2 - 7$$

Since $f$ can be written as a sum of power functions where every power of $x$ is a nonnegative integer, $f$ is a polynomial.
```

```{dropdown} **Step 2:** &nbsp; Determine the degree of &nbsp; $f$.

The degree of $f$ is $5$ since $f$ is a polynomial and the largest power of $x$ is $5$.
```
````



```{admonition} An Observation about the Degree of a Product of Polynomials
:class: note

In the previous example, the degree of the polynomial could have been determined by adding the degrees of the individual factors.  More specifically, $f$ is the product of a polynomial of degree 2 (i.e., $x^2 + 7$) and a polynomial of degree 3 (i.e., $x^3-1$).  Therefore, the degree of $f$ is the sum of $2$ and $3$, which is $5$.

In general, a product of polynomials is also a polynomial and its degree is the sum of the degrees of the polynomial factors.  
```



### Example 5
````{admonition} A rational function
:class: tip

Show that $g(x) = \dfrac{4}{x-1} + \dfrac{5}{x}$ is a rational function (but not a polynomial) and determine its domain.


```{dropdown} **Step 1:** &nbsp; Get a common denominator.

$$\dfrac{4}{x-1} + \dfrac{5}{x} = \frac{4x}{x(x-1)} + \frac{5(x-1)}{x(x-1)}$$
```


```{dropdown} **Step 2:** &nbsp; Add numerators and simplify.

$$\frac{4x + 5(x-1)}{x(x-1)} = \frac{9x-5}{x(x-1)}$$

Since $g(x)$ can be written as a ratio of polynomials, it is also a rational function.
```


```{dropdown} **Step 3:** &nbsp; Determine the domain of &nbsp; $g$.

Since $g$ is the sum of two functions, we begin by considering the domain of each of the two functions.  Specifically, the domain of $4/(x-1)$ consists of all real numbers except $x=1$ and the domain of $5/x$ consists of all real numbers except $x=0$.

Therefore, the domain of $g$ consists of all real numbers except $x=0$ and $x=1$.  In interval notation, this can be written as

$$(-\infty,0)\cup (0,1) \cup (1,\infty).$$
```
````
