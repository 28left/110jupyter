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
# Indeterminate Forms

## Definition

```{admonition} Definition
:class: info

If $\lim\limits_{x\to a} f(x) = 0$ and $\lim\limits_{x\to a}g(x) = 0$, then 

$$\lim_{x\to a}\frac{f(x)}{g(x)}$$

is called an _**indeterminate form of type $0/0$**_.  
```

```{admonition} How to Evaluate an Indeterminate Form of Type $0/0$
:class: info

To evaluate an indeterminate form, simplify the ratio $f(x)/g(x)$ by factoring or rationalizing the expression and then canceling out common factors.
```

### Example 1
````{admonition} An indeterminate form involving a rational function
:class: tip

Evaluate $\lim\limits_{x\to 5} \dfrac{x-5}{x^2-25}.$


```{dropdown} **Step 1:** &nbsp; Evaluate the limit of numerator and denominator.

We evaluate these limits by plugging in $x=5$:

$$\lim_{x\to 5} x-5 = 5 - 5 = 0 ~~~~ \text{and} ~~~~~ \lim_{x\to 5} x^2 - 25 = 5^2-25 = 0$$

This means that the given limit is an indeterminate form of type $0/0$, so we need to simplify the function before we can evaluate the limit.
```

```{dropdown} **Step 2:** &nbsp; Factor numerator and/or denominator and simplify.

\begin{align*}
\frac{x-5}{x^2-25}
&= \frac{x-5}{(x-5)(x+5)} && \text{since $A^2 - B^2 = (A-B)(A+B)$}\\ \\
&= \frac{1}{x+5} && \text{assuming $x \neq 5$}
\end{align*}

When computing the limit as $x$ approaches $5$, we are initially assuming that $x$ is not equal to $5$.  This means that we can replace $\dfrac{x-5}{x^2-25}$ with $\dfrac{1}{x+5}$ when computing the limit, as shown in the next step.
```

```{dropdown} **Step 3:** &nbsp; Evaluate the limit using the simplified function.

\begin{align*}
\lim_{x\to 5}\frac{x-5}{x^2-25}
&= \lim_{x\to 5} \frac{1}{x+5} \\ \\
&= \frac{1}{5+5}  && \text{plug in $x=5$}\\ \\
&= \frac{1}{10} && \text{simplify}
\end{align*}
```
````


### Example 2
````{admonition} An indeterminate form involving a square root function
:class: tip

Evaluate $\lim\limits_{x\to 10} \dfrac{\sqrt{x-6}-2}{x-10}$.


```{dropdown} **Step 1:** &nbsp; Evaluate the limit of numerator and denominator.

Plug in $x=10$:

$$\lim_{x\to 10} \sqrt{x-6}-2 = \sqrt{10-6} - 2 = 0 ~~~~ \hbox{and} ~~~~~ \lim_{x\to 10} x-10 = 10-10 = 0$$

This means that the given limit is an indeterminate form of type $0/0$, so we need to simplify the function before we can evaluate the limit.
```

```{dropdown} **Step 2:** &nbsp; Simplify the function.

We simplify the function by multiplying and dividing by $\sqrt{x-6} + 2$, which is the conjugate of $\sqrt{x-6} - 2$.

\begin{align*}
\frac{\sqrt{x-6}-2}{x-10} \cdot \frac{\sqrt{x-6} + 2}{\sqrt{x-6} + 2}
&= \frac{(\sqrt{x-6}-2)(\sqrt{x-6}+2)}{(x-10)(\sqrt{x-6}+2)}\\ \\
&= \frac{\sqrt{x-6}\sqrt{x-6} + 2\sqrt{x-6} - 2\sqrt{x-6} - 4}{(x-10)(\sqrt{x-6}+2)} && \text{FOIL}\\ \\
&= \frac{x-6 + \cancel{2\sqrt{x-6}} - \cancel{2\sqrt{x-6}} - 4}{(x-10)(\sqrt{x-6}+2)}&& \text{simplify}\\ \\
&= \frac{x- 6 - 4}{(x-10)(\sqrt{x-6}+2)}\\ \\
&= \frac{x- 10}{(x-10)(\sqrt{x-6}+2)}\\ \\
&= \frac{1}{\sqrt{x-6}+2} && \text{if $x\neq 10$}
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Evaluate the limit using the simplified function.

\begin{align*}
\lim_{x\to 10} \frac{\sqrt{x-6}-2}{x-10} 
&= \lim_{x\to 10} \frac{1}{\sqrt{x-6}+2}\\ \\
&= \frac{1}{\sqrt{10-6}+2} && \text{plug in $x=10$}\\ \\
&= \frac{1}{\sqrt{4}+2} && \text{simplify}\\ \\
&= \frac{1}{4}
\end{align*}
```
````
