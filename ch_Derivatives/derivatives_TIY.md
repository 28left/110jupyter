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
````{admonition} Compute derivative using the limit definition
:class: tip

Compute the derivative of $f(x) = 5x^2 - 2x$ using the limit definition of the derivative.

```{dropdown} Show answer
Answer: $10x - 2$
```
````

## Exercise 2
````{admonition} Compute derivative using rules of differentiation
:class: tip

Compute the derivative of $f(x)= 3x^2 + 5x^{-2} + 7\sqrt{x}$ using the basic rules of differentiation.

```{dropdown} Show answer
Answer: $6x - 10x^{-3} + \frac{7}{2}x^{-1/2}$
```
````

## Exercise 3
````{admonition} Compute the derivative
:class: tip

Compute the derivattive of $f(x)= \dfrac{7}{x^7} + \dfrac{5}{x^5} + \dfrac{3}{x^3}$.

Hint: Avoid using the quotient rule by rewriting each term so that it involves multplying by a negative power of $x$.

```{dropdown} Show answer
Answer: $-49x^{-8} - 25x^{-6} - 9x^{-4}$
```
````

## Exercise 4
````{admonition} Equation of a tangent line
:class: tip

Find the equation of the line tangent to $f(x)=\dfrac{x^{3/2}+x^{1/2}+1}{x^2}$ at $x=4$.  

Hint: Avoid using the quotient rule by dividing each term of the numerator by $x^2$ and then simplifying.

```{dropdown} Show answer
Answer: $y = -\frac{9}{64}(x-4) + \frac{11}{16}$
```
````

## Exercise 5
````{admonition} Compute the derivative
:class: tip

Compute the derivative of $f(x)= (x^3+6)(x-2)(x+2)$.

Hint: Expand $(x-2)(x+2)$ and then apply the product rule.

```{dropdown} Show answer
Answer: $5x^4 - 12x^2 + 12x$
```
````

## Exercise 6
````{admonition} Compute the derivative
:class: tip

Compute the derivative of $f(x)= \sqrt{\dfrac{x^2-1}{x+1}}$.

Hint: Simplify the function before computing the derivative.

```{dropdown} Show answer
Answer: $\dfrac{1}{2\sqrt{x-1}}$
```
````

## Exercise 7
````{admonition} Compute the derivative
:class: tip

Compute the derivative of $f(x)=\dfrac{17}{(3x+4)^2}$.

Hint: Rewrite the function before differentiating in order to avoid using the quotient rule.

```{dropdown} Show answer
Answer: $-\dfrac{102}{(3x+4)^3}$
```
````

## Exercise 8
````{admonition} Compute the derivative
:class: tip

Compute the derivative of $f(x)=5x^4(x^3+6)^{7}$ and simplify your answer.

```{dropdown} Show answer
Answer: $5x^3(x^3+6)^6(25x^3 + 24)$
```
````

## Exercise 9
````{admonition} Compute the derivative
:class: tip

Compute the derivative of $f(x)=\dfrac{(x^2+4)^5}{(x^6+ 1)^3}$ and simplify your answer.

```{dropdown} Show answer
Answer: $\dfrac{2x(x^2+4)^4(-4x^6-36x^4+5)}{(x^6+1)^4}$
```
````

## Exercise 10
````{admonition} Evaluate a limit
:class: tip

Evaluate $\displaystyle\lim_{h\to 0}\dfrac{(1+h)^5-1}{h}$.

```{dropdown} Show answer
Answer: $5$
```
````

## Exercise 11
````{admonition} Continuous but not differentiable
:class: tip

Draw the graph of a function $f(x)$ that is continuous at $x=a$ but not differentiable at $x=a$. Explain why the function is continuous but not differentiable at this point.

```{dropdown} Show answer
Answer: Consider a graph with a corner or a vertical tangent line at $x=a$.  See {ref}`der:diff_example_2` in Differentiability.
```
````
