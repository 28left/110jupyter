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
  name: python394jvsc74a57bd0085761d8a84a55f3b91b6696b289e6480df59aded311489218ab7e58f5e20cd3
---
# Limits at Infinity of a Function

```{admonition} Definition
:class: info

The function $f(x)$ has the limit $L$ as $x$ increases without bound (as $x$ approaches infinity), 

$$\lim_{x\to \infty} f(x) = L $$ 

if $f(x)$ can be made as close to $L$ by taking $x$ large enough.

Similarly, the function $f(x)$ has the limit $M$ as $x$ decreases without bound (as $x$ approaches negative infinity), 

$$\lim_{x\to -\infty} f(x) = M $$ 

if $f(x)$ can be made as close to $M$ by taking $x$  to be negative and sufficiently large in absolute value.
```

```{admonition} Example
:class: tip

The following graph illustrates a function $f(x)$ that approaches a value of 400 as $x$ increases without bound.  In other words, 

$$\lim\limits_{x\to \infty} f(x) = 400.$$

![The graph approaches the value 400 as x increases without bound](110_02_06_lim_infinity_1.png)
```

## Properties of Limits at Infinity

All previous properties for limits apply when $a$ is replaced with $\infty$ or $-\infty$.  Furthermore, the following additional properties are especially useful when evaluating limits at infinity.  For all $n>0$, we have

- $\lim\limits_{x \to \infty} \dfrac{1}{x^n}=0 $
- $\lim\limits_{x \to -\infty} \dfrac{1}{x^n}=0$, provided that $x^n$ is defined for $x<0$.


```{admonition} Example
:class: tip
Notice how the graph of $y=1/x$ approaches the $x$-axis as $x$ approaches positive and negative infinity.  In other words,

$$\lim_{x\to -\infty} \frac{1}{x} = 0  ~~~~ \hbox{and} ~~~~~ \lim_{x\to \infty} \frac{1}{x} = 0.$$

![The graph of y=1/x](110_02_06_lim_infinity_2.png)
```

```{admonition} Example
:class: tip
Notice how the graph of $y=1/\sqrt{x}$ approaches the $x$-axis as $x$ approaches positive infinity.  In other words,

$$\lim_{x\to \infty} \frac{1}{\sqrt{x}} = 0.$$

Furthermore, there is no discussion of the limit as $x$ approaches negative infinity since $\sqrt{x}$ is not defined for negative values of $x$. 

![The graph of y=1/\sqrt{x}](110_02_06_lim_infinity_3.png)
```

## Limits at Infinity of Rational Functions

For Rational Functions, a limit at infinity, whether it be $\displaystyle\lim_{x\to\infty}$ or $\displaystyle\lim_{x\to -\infty}$, can be determined by comparing the degree of the polynomial in the numerator to the degree of the polynomial in the denominator.

For infinite limits of Rational Functions, if the 
- highest power is in the denominator, then the limit will equal $0$
- highest power in the numerator, then the limit will equal $\pm\infty$ (DNE)
- highest power is the same in both the numerator and denominator, then the limit will equal the ratio of the leading coefficients, i.e. the ratio of the coefficients in front of the highest powers in the numerator and the denominator.

```{admonition} Example
:class: tip
Applying the guidelines:
1. $\displaystyle\lim_{x\to\infty}\frac{x+3}{6x^2+3x+1}$ = 0 (highest power is in denominator)   <br>  &nbsp;

2. $\displaystyle\lim_{x\to-\infty}\frac{6x^{3}+3}{x^{2}+4x-7}$ = $-\infty$ or DNE (highest power is in numerator)  <br>  &nbsp;

3. $\displaystyle\lim_{x\to\infty}\frac{4x^5+3x-8}{9x^5-6x^3}$ = $4/9$ (highest powers are the same)  
```