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
# Try It Yourself

## Exercise 1
````{admonition} Integral of a product of a power function and an eponential function
:class: tip

Compute $\displaystyle \int xe^{x/3} ~dx$.

```{dropdown} Show answer
Answer: $3(x-3)e^{x/3} + C$
```
````


## Exercise 2
````{admonition} Integral of a product of a power function and a logarithmic function
:class: tip

Compute $\displaystyle \int \sqrt{x}\ln(x) ~dx$.

```{dropdown} Show answer
Answer: $\dfrac{2}{3} x^{3/2} \ln(x) - \dfrac{4}{9}x^{3/2} + C$
```
````



## Exercise 3
````{admonition} Integral of a product of a polynomial and an exponential function
:class: tip

Compute $\displaystyle \int (x^2+2x)e^x ~dx$.  (Hint: Use integration by parts twice.)

```{dropdown} Show answer
Answer: $x^2e^x+C$
```
````


## Exercise 4
````{admonition} Definite integral using integration by parts
:class: tip

Evaluate $\displaystyle \int_1^e (\ln x)^2 ~dx$.  (Hint: Use integration by parts with $u = (\ln x)^2$ and $dv = dx$.)

```{dropdown} Show answer
Answer: $e-2$
```
````


## Exercise 5
````{admonition} Present and future value of an income stream
:class: tip

Suppose an investment is expected to generate income at the rate of $R(t) = 10 + 7t$
thousands of dollars per year for the next 20 years. Find the present and future values from this investment if the prevailing interest rate is 5\% per year compounded continuously.

```{dropdown} Show answer
Answer: Present value: \$866,299.24, Future value: \$2,354,845.49
```
````


## Exercise 6
````{admonition} Improper integral
:class: tip

Evaluate $\displaystyle \int_3^{\infty} e^{-7x} ~dx$, if it exists.

```{dropdown} Show answer
Answer: $\dfrac{1}{7e^{21}}$
```
````


## Exercise 7
````{admonition} Improper integral
:class: tip

Evaluate  $\displaystyle \int_4^{\infty} \frac{e^{-\sqrt{x}}}{\sqrt{x}} ~dx$, if it exists.  (Hint: Use a substitution to compute $\displaystyle \int \frac{e^{-\sqrt{x}}}{\sqrt{x}} ~dx$.)

```{dropdown} Show answer
Answer: $2/e^2$
```
````

## Exercise 8
````{admonition} Improper integral
:class: tip

Evaluate  $\displaystyle \int_2^{\infty} \frac{1}{(2x-3)^{1.5}} ~dx$, if it exists.

```{dropdown} Show answer
Answer: $1$
```
````


## Exercise 9
````{admonition} Improper integral
:class: tip

Evaluate  $\displaystyle \int_6^{\infty}  \frac{1}{(6x-35)^{0.5}} ~dx $, if it exists.

```{dropdown} Show answer
Answer: Does not exist
```
````


## Exercise 10
````{admonition} Present value of a perpetuity
:class: tip

In order to create an endowment which pays \$100 per week, in perpetuity, how much money must be invested today if the annual interest rate is 5\% compounded continuously?

```{dropdown} Show answer
Answer: \$104,000
```
````
