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
# Algebraic Simplification Techniques

## Simplifying Expressions Involving Fractions

```{admonition} Adding or Subtracting Fractions
:class: info

If the fractions have a common denominator, then they can be combined into a single fraction by adding or subtracting the numerators accordingly.

$$ \frac{A}{B} \pm \frac{C}{B} = \frac{A \pm C}{B} $$

e.g., $\dfrac{2}{3} + \dfrac{5}{3} = \dfrac{7}{3}$

If the fractions do not have a common denominator, then a common denominator can be formed by multiplying the denominators together.

$$ \frac{A}{B} \pm \frac{C}{D} = \frac{AD}{BD} \pm \frac{BC}{BD}  = \frac{AD \pm BC}{BD} $$

e.g., $\dfrac{2}{3} - \dfrac{5}{7} = \dfrac{2\cdot 7- 3\cdot5}{3\cdot 7} = -\dfrac{1}{21}$
```

```{admonition} Multiplying Fractions
:class: info

To multiply two fractions, multiply the numerators and multiply the denominators of the two fractions.

$$
\frac{A}{B} \times \frac{C}{D} = \frac{AC}{BD}
$$

e.g., $\dfrac{2}{3} \times \dfrac{5}{7} = \dfrac{2\cdot 5}{3\cdot 7} = \dfrac{10}{21}$
```

```{admonition} Dividing Fractions
:class: info

To divide two fractions, remember that division is the same as multiplication by the reciprocal.  In other words, dividing by $C/D$ is the same as multiplying by $D/C$. 

$$\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \times \frac{D}{C} = \frac{AD}{BC}$$

e.g., $\dfrac{2}{3} \div \dfrac{5}{7} = \dfrac{2}{3} \times \dfrac{7}{5} = \dfrac{14}{15}$
```



### Example 1

Rewrite $\dfrac{x+1}{x+4} - \dfrac{3x-2}{x+4}$ as a single ratio.

```{admonition} Step 1: Subtract fractions with common denominator.
:class: tip, dropdown

Since the ratios already have the same denominator, we need only apply the formula for subtracting  fractions with a common denominator.
\begin{align*}
  \frac{A}{B} - \frac{C}{B} &= \frac{A-C}{B}
\end{align*}
```

```{admonition} Step 2: Apply the formula from Step 1.
:class: tip, dropdown

Apply the formula from **Step 1** with $A = x+1$, $B=x+4$, and $C = 3x-2$.
\begin{align*}
\dfrac{x+1}{x+4} - \dfrac{3x-2}{x+4}
&= \frac{x+1 - (3x-2)}{x+4} && \hbox{Subtract numerators}\\
&= \frac{x+1 - 3x+2}{x+4}  && \hbox{Distribute the minus sign}\\
&= \frac{3-2x}{x+4} && \hbox{Combine like terms}
\end{align*}
```

### Example 2

Rewrite $\dfrac{3}{x} + \dfrac{4}{x-5}$ as a single ratio.

```{admonition} Step 1: Apply  formula for adding fractions with different denominators.
:class: tip, dropdown

Since the ratios do not have the same denominator, we will apply the formula for adding fractions with different denominators.
\begin{align*}
  \frac{A}{B} + \frac{C}{D} &= \frac{AD}{BD} + \frac{BC}{BD} = \frac{AD+BC}{BD}
\end{align*}
```

```{admonition} Step 1: Apply the formula from Step 1.
:class: tip, dropdown

Apply the formula from {\bf Step 1} with $A = 3$, $B=x$, $C = 4$, and $D = x-5$.
\begin{align*}
\dfrac{3}{x} + \dfrac{4}{x-5}
&= \frac{3(x-5)}{x(x-5)} + \frac{4x}{x(x-5)} && \hbox{Get a common denominator}\\
&= \frac{3(x-5)+4x}{x(x-5)} && \hbox{Add numerators}\\
&= \frac{3x - 15 + 4x}{x(x-5)} && \hbox{Distribute the 3}\\
&= \frac{7x-15}{x(x-5)} && \hbox{Combine like terms}
\end{align*}
```


### Example 3

Simplify 

$$
\cfrac{\left(\cfrac{3p}{\sqrt{180-6p}}\right)}{ \sqrt{180-6p}}.
$$


```{admonition} Step 1: Recall formula for the quotient of fractions.
:class: tip, dropdown

$$
\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \times \frac{D}{C} = \frac{AD}{BC}
$$
```

```{admonition} Step 2: Use formula from Step 1 to rewrite equation.
:class: tip, dropdown

\begin{align*}
\cfrac{\left(\cfrac{3p}{\sqrt{180-6p}}\right)}{ \sqrt{180-6p}}
&= \frac{3p}{\sqrt{180-6p}} \div \sqrt{180-6p} \\ \\
&= \frac{3p}{\sqrt{180-6p}} \times \frac{1}{\sqrt{180-6p}} && \hbox{Division is multiplication by reciprocal}\\  \\
&= \frac{3p}{\sqrt{180-6p}\times \sqrt{180-6p}} && \hbox{Multiply numerators and denominators}\\ \\
&= \frac{3p}{180 - 6p} && \hbox{Simplify}
\end{align*}
```



## Distributive Property of Multiplication

```{admonition} Distributivity 
The distributive property of multiplication can be used to rewrite a product (where at least one factor is a sum) as a sum.

$$
A(B+C) = AB + AC
$$

e.g., $7(3+2) = 7\cdot 3 + 7\cdot 2$
```

### Example 4
Expand $x^2(5x^3 + 7)$.


```{admonition} Step 1: Use distributivity to expand given product.
:class: tip, dropdown

\begin{align*}
x^2(5x^3 + 7)
&= 5x^2x^3 + 7x^2 && \hbox{Distribute $x^2$}\\
&= 5x^5 + 7x^2 && \hbox{Simplify}
\end{align*}
```


## The FOIL Method

The FOIL method is a way to remember how to apply the distributive property of multiplication when expanding the product of two binomial expressions.  FOIL is an acronym for 

```{admonition} F-O-I-L
:class: info

- **F**irst (i.e., multiply the first terms from each binomial)
- **O**uter (i.e., multiply the first term from the first factor and the second term from the second factor)
- **I**nner (i.e., multiply the second term from the first factor and the first term from the second factor)
- **L**ast (i.e., multiply the second terms of each binomial)
\end{itemize}

$$
(a + b)(c + d) = \underbrace{ac}_{\hbox{(F)irst}} + \underbrace{ad}_{\hbox{(O)uter}} + \underbrace{bc}_{\hbox{(I)nner}} + \underbrace{bd}_{\hbox{(L)ast}}
$$
```

### Example 5

Expand $(x+2)(3x-5)$ using the FOIL method.


```{admonition} Step 1: Recall the formula for the FOIL method.
:class: tip, dropdown

\begin{align*}
    (a + b)(c + d) &= ac + ad + bc + bd
\end{align*}
```

```{admonition} Step 2: Use the FOIL method to expand the expression.
:class: tip, dropdown

\begin{align*}
  (x+2)(3x-5) 
  &= x(3x) + x(-5) + 2(3x) + 2(-5) &&\hbox{FOIL}\\
  &= 3x^2 - 5x + 6x - 10 && \text{Simplify each term}\\
  &= 3x^2 + x - 10 && \text{Combine like terms}
\end{align*}
```


## Squaring a Binomial

```{admonition} Applying the FOIL method to a binomial
:class: info

When applying the FOIL method to the square of a binomial (i.e., $(a+b)^2$ or $(a-b)^2$), we arrive at the following formulas:

$$
(a + b)^2 = a^2 + 2ab + b^2
\qquad\qquad
(a - b)^2 = a^2 - 2ab + b^2
$$
```


### Example 6

Expand $(3x-5)^2$ by squaring the binomial.

```{admonition} Step 1: Apply binomial formula.
:class: tip, dropdown

Apply $(a - b)^2 = a^2 - 2ab + b^2$ with $a=3x$ and $b=5$.
\begin{align*}
(3x-5)^2
&= (3x)^2 - 2(3x)(5) + 5^2 && \hbox{Square the binomial} \\ \\ 
&= 3^2x^2 - 30x + 25 && \hbox{Simplify}\\ \\
&= 9x^2 - 30x + 25
\end{align*}
```

### Example 7
Expand $3x^5(4+x)^2$.

```{admonition} Step 1: Apply binomial formula.
:class: tip, dropdown

Apply $(a + b)^2 = a^2 + 2ab + b^2$ with $a=4$ and $b=x$.
\begin{align*}
3x^5(4+x)^2
&= 3x^5(4^2 + 2(4)(x) + x^2) && \hbox{Square the binomial}\\ \\
&= 3x^5(16 + 8x + x^2) && \hbox{Simplify}
\end{align*}
```

```{admonition} Step 2: Use the distributive property of multiplication.
:class: tip, dropdown

\begin{align*}
3x^5(16 + 8x + x^2) 
&= 3x^5(16) + 3x^5(8x) + 3x^5(x^2) && \hbox{Distribute $3x^5$} \\ \\
&= 48x^5 + 24x^6 + 3x^7 && \hbox{Simplify}
\end{align*}
```