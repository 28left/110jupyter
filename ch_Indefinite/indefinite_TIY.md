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
````{admonition} Integral of a constant
:class: tip

Compute $\displaystyle \int 2e ~dy$.  Verify your answer by computing its derivative.

```{dropdown} Show answer
Answer: $2ey + C$
```
````


## Exercise 2
````{admonition} Integral of a sum of power functions
:class: tip

Compute  $\displaystyle \int 3 x^{5/4} + \frac{7}{\sqrt{x}}+ \frac{1}{6x^5} ~dx$. Verify your answer by computing its derivative.

```{dropdown} Show answer
Answer: $\dfrac{4}{3}x^{9/4} + 14\sqrt{x} - \dfrac{1}{24x^4} + C$
```
````

## Exercise 3
````{admonition} Integral of a product
:class: tip

Compute $\displaystyle \int (e^{3x} + 4)(e^{-5x} - 20) ~dx$. Verify your answer by computing its derivative.

```{dropdown} Show answer
Answer: $-\dfrac{1}{2}e^{-2x} - \dfrac{20}{3}e^{3x} - \dfrac{4}{5}e^{-5x} - 80x + C$
```
````

## Exercise 4
````{admonition} Integral of a polynomial divided by a power function
:class: tip

Compute $\displaystyle \int \frac{10x^3 - 2x^2 + 3x-25 }{x} ~dx$. Verify your answer by computing its derivative.

```{dropdown} Show answer
Answer: $\dfrac{10}{3}x^3 - x^2 + 3x - 25\ln|x| + C$
```
````


## Exercise 5
````{admonition} Initial value problem
:class: tip

Find $f(x)$ such that $ f'(x) = e^{7x} + 2x^3 +3 $ and $f(0)=2$.  Verify your answer by computing its derivative.

```{dropdown} Show answer
Answer: $\dfrac{1}{7}e^{7x} + \dfrac{1}{2}x^4 + 3x + \dfrac{13}{7}$
```
````


## Exercise 6
````{admonition} Total cost
:class: tip

The marginal cost function associated with producing $x$ croissants is given by 

$$C'(x) = -0.5x +60 $$ 

where $C'(x)$ is measured in dollars/unit and $x$ denotes the number of croissants. 

If the daily fixed costs incurred in the production is $\$400$, find the total cost $C(x)$ incurred in producing the first 100 units of the day.

```{dropdown} Show answer
Answer: \$3900
```
````


## Exercise 7
````{admonition} Integration by substitution
:class: tip

Compute $\displaystyle \int \frac{5x-3}{(5x^2-6x+15)^4} ~dx$. Verify your answer by computing its derivative.

```{dropdown} Show answer
Answer: $-\dfrac{1}{6(5x^2 - 6x + 15)^3} + C$
```
````

## Exercise 8
````{admonition} Integration by substitution
:class: tip

Compute $\displaystyle \int \frac{x}{x-2} ~dx$. Verify your answer by computing its derivative.

```{dropdown} Show answer
Answer: $x + 2\ln|x-2| + C$
```
````


## Exercise 9
````{admonition} Integration by substitution
:class: tip

Compute $\displaystyle \int \frac{e^{3x}}{e^{3x}-4} ~dx$.  Verify your answer by computing its derivative.


```{dropdown} Show answer
Answer: $\dfrac{1}{3}\ln|e^{3x}-4| + C$

```
````

## Exercise 10
````{admonition} Initial value problem
:class: tip

Find $f(x)$ such that $f'(x) = (5x+1)(5x^2+2x-1)^2$ and $f(1) = 15$. Verify your answer by computing its derivative.


```{dropdown} Show answer
Answer: $\dfrac{1}{6}(5x^2+2x-1)^3 - 21$
```
````


## Exercise 11
````{admonition} Integration by substitution
:class: tip

Compute $\displaystyle \int 3x ~\sqrt[]{x^2+10} ~dx$. Verify your answer by computing its derivative.


```{dropdown} Show answer
Answer: $(x^2+10)^{3/2} + C$
```
````


## Exercise 12
````{admonition} Integration by substitution
:class: tip

Compute $\displaystyle \int 15x^3 ~\sqrt[]{x^2+10} ~dx$.  Verify your answer by computing its derivative.


```{dropdown} Show answer
Answer: $3(x^2+10)^{5/2} - 50(x^2+10)^{3/2} + C$

```
````
