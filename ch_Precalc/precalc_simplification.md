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

For example, $\dfrac{2}{3} + \dfrac{5}{3} = \dfrac{7}{3}$.

If the fractions do not have a common denominator, then a common denominator can be formed by multiplying the denominators together.

$$ \frac{A}{B} \pm \frac{C}{D} = \frac{AD}{BD} \pm \frac{BC}{BD}  = \frac{AD \pm BC}{BD} $$

For example, $\dfrac{2}{3} - \dfrac{5}{7} = \dfrac{2\cdot 7- 3\cdot5}{3\cdot 7} = -\dfrac{1}{21}$.
```


```{admonition} Multiplying Fractions
:class: info

To multiply two fractions, multiply the numerators and multiply the denominators of the two fractions.

$$\frac{A}{B} \times \frac{C}{D} = \frac{AC}{BD}$$

For example, $\dfrac{2}{3} \times \dfrac{5}{7} = \dfrac{2\cdot 5}{3\cdot 7} = \dfrac{10}{21}$.
```


```{admonition} Dividing Fractions
:class: info

To divide two fractions, remember that division is the same as multiplication by the reciprocal.  In other words, dividing by $C/D$ is the same as multiplying by $D/C$. 

$$\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \times \frac{D}{C} = \frac{AD}{BC}$$

For example, $\dfrac{2}{3} \div \dfrac{5}{7} = \dfrac{2}{3} \times \dfrac{7}{5} = \dfrac{14}{15}$.
```

<!--
```{code-cell}
:tags: [remove-input]


from IPython.display import IFrame
IFrame("https://www.youtube.com/embed/LyMESqKEVnY?rel=0&amp;controls=1&amp;showinfo=0", '100%', '200px')
```
-->

````{admonition} Video Resource
:class: important

::::{grid} 2
:::{grid-item}
:columns: 1
:padding: 1
```{image} ../images/UnderstandTheMath.png
:alt: UnderstandTheMath
```
:::
:::{grid-item}
:columns: 10
<a href="https://youtu.be/YV0wFncCTGw" target="_blank">Order of Operations</a> (Links to an external site) <br>
A review of how to evaluate expressions involving parentheses, exponents, multiplication, division, addition, and/or subtraction. 
:::
::::
````



````{admonition} Video Resource
:class: important

::::{grid} 2
:::{grid-item}
:columns: 1
:padding: 1
```{image} ../images/UnderstandTheMath.png
:alt: UnderstandTheMath
```
:::
:::{grid-item}
:columns: 10
<a href="https://youtu.be/LyMESqKEVnY" target="_blank">Understand Fractions in Minutes</a> (Links to an external site) <br>
A review of how to add, subtract, multiply and divide fractions. 
:::
::::
````



```{admonition} Important
:class: note

In the previous examples of combining fractions, only numerical values appeared in the numerators and denominators.  However, the same formulas can be used to simplify expressions where the numerators and/or denominators contain functions.
```


### Example 1

````{admonition} Subtracting fractions with the same denominator
:class: tip

Rewrite $\dfrac{x+1}{x+4} - \dfrac{3x-2}{x+4}$ as a single ratio.


```{dropdown} **Step 1:**&nbsp; Subtract fractions with common denominator.

Since the ratios already have the same denominator, we need only apply the formula for subtracting  fractions with a common denominator.
\begin{align*}
  \frac{A}{B} - \frac{C}{B} &= \frac{A-C}{B}
\end{align*}
```

```{dropdown} **Step 2:**&nbsp; Apply the formula from Step 1.

Apply the formula from **Step 1** with $A = x+1$, $B=x+4$, and $C = 3x-2$.

\begin{align*}
\dfrac{x+1}{x+4} - \dfrac{3x-2}{x+4}
&= \frac{x+1 - (3x-2)}{x+4} && \text{subtract numerators}
\end{align*}
Note the use of parantheses around $3x-2$.  Since we are subtracting $3x-2$, the parantheses are needed to make sure we distribute the minus sign to both terms of $3x-2$, which we will do in the next step.
```

```{dropdown} **Step 3:**&nbsp; Simplify the numerator.

\begin{align*}
\frac{x+1 - (3x-2)}{x+4}
&= \frac{x+1 - 3x+2}{x+4}  && \text{distribute the minus sign}\\
&= \frac{3-2x}{x+4} && \text{combine like terms in the numerator}
\end{align*}
```
````


### Example 2

````{admonition} Adding fractions with different denominators
:class: tip

Rewrite $\dfrac{3}{x} + \dfrac{4}{x-5}$ as a single ratio.


```{dropdown} **Step 1:** &nbsp; Apply  formula for adding fractions with different denominators.

Since the ratios do not have the same denominator, we will apply the formula for adding fractions with different denominators.
\begin{align*}
  \frac{A}{B} + \frac{C}{D} &= \frac{AD}{BD} + \frac{BC}{BD} = \frac{AD+BC}{BD}
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Apply the formula from Step 1.

Apply the formula from **Step 1** with $A = 3$, $B=x$, $C = 4$, and $D = x-5$.
\begin{align*}
\dfrac{3}{x} + \dfrac{4}{x-5}
&= \frac{3(x-5)}{x(x-5)} + \frac{4x}{x(x-5)} && \text{get a common denominator}\\
&= \frac{3(x-5)+4x}{x(x-5)} && \text{add numerators}
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Simplify the numerator.

\begin{align*}
\frac{3(x-5)+4x}{x(x-5)} 
&= \frac{3x - 15 + 4x}{x(x-5)} && \text{distribute the 3}\\
&= \frac{7x-15}{x(x-5)} && \text{combine like terms in the numerator}
\end{align*}
```
````


### Example 3

````{admonition} Simplifying quotients of fractions
:class: tip

Simplify 
$
\cfrac{\left(\cfrac{3p}{\sqrt{180-6p}}\right)}{ \sqrt{180-6p}}.
$


```{dropdown} **Step 1:** &nbsp; Recall formula for the quotient of fractions.

$$
\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \times \frac{D}{C} = \frac{AD}{BC}
$$
```

```{dropdown} **Step 2:** &nbsp; Use formula from Step 1 to rewrite equation.

\begin{align*}
\cfrac{\left(\cfrac{3p}{\sqrt{180-6p}}\right)}{ \sqrt{180-6p}}
&= \frac{3p}{\sqrt{180-6p}} \div \sqrt{180-6p} \\ \\
&= \frac{3p}{\sqrt{180-6p}} \times \frac{1}{\sqrt{180-6p}} && \text{division is multiplication by reciprocal}\\  \\
&= \frac{3p}{\sqrt{180-6p}\times \sqrt{180-6p}} && \text{multiply numerators and denominators}
\end{align*}
```


```{dropdown} **Step 3:** &nbsp; Simplify the denominator.

\begin{align*}
\frac{3p}{\sqrt{180-6p}\times \sqrt{180-6p}}
&= \frac{3p}{180 - 6p}
\end{align*}
```
````


## Distributive Property of Multiplication

```{admonition} Distributivity 
The distributive property of multiplication can be used to rewrite a product (where at least one factor is a sum) as a sum.

$$
A(B+C) = AB + AC
$$

For example, $7(3+2) = 7\cdot 3 + 7\cdot 2$.
```

```{admonition} Important
:class: note

In the above example of the distributive property of multiplication, only numerical values were used.  However, the distributive property can also be used to expand products of functions.
```



````{admonition} Video Resource
:class: important

::::{grid} 2
:::{grid-item}
:columns: 1
:padding: 1
```{image} ../images/UnderstandTheMath.png
:alt: UnderstandTheMath
```
:::
:::{grid-item}
:columns: 10
<a href="https://youtu.be/_5A7bGr2vjA" target="_blank">Multiplying Polynomials</a> (Links to an external site) <br>
A review of how to use the distributive property to expand the product of polynomials.
:::
::::
````


### Example 4

````{admonition} Expanding a product of polynomials
:class: tip

Expand $x^2(5x^3 + 7)$.


```{dropdown} **Step 1:** &nbsp; Use distributivity to expand the given product.

\begin{align*}
x^2(5x^3 + 7)
&= 5x^2x^3 + 7x^2 && \text{distribute $x^2$}
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Simplify each term.

\begin{align*}
5x^2x^3 + 7x^2 &= 5x^5 + 7x^2 
\end{align*}
```
````



## The FOIL Method
```{admonition} F-O-I-L
:class: info

The FOIL method is a way to remember how to apply the distributive property of multiplication when expanding the product of two binomial expressions.  FOIL is an acronym for 

- **F**irst (i.e., multiply the first terms from each binomial)
- **O**uter (i.e., multiply the first term from the first factor and the second term from the second factor)
- **I**nner (i.e., multiply the second term from the first factor and the first term from the second factor)
- **L**ast (i.e., multiply the second terms of each binomial)

$$
(a + b)(c + d) = \underbrace{ac}_{\text{(F)irst}} + \underbrace{ad}_{\text{(O)uter}} + \underbrace{bc}_{\text{(I)nner}} + \underbrace{bd}_{\text{(L)ast}}
$$
After expanding the product using the FOIL method, combine like terms, if possible.
```


````{admonition} Video Resource
:class: important

::::{grid} 2
:::{grid-item}
:columns: 1
:padding: 1
```{image} ../images/UnderstandTheMath.png
:alt: UnderstandTheMath
```
:::
:::{grid-item}
:columns: 10
<a href="https://youtu.be/P_B6YBGKwVU" target="_blank">The FOIL Method</a> (Links to an external site) <br>
A review of how to expand the product of two binomial expressions.
:::
::::
````


### Example 5
````{admonition} Applying the FOIL method
:class: tip

Expand $(x+2)(3x-5)$ using the FOIL method.


```{dropdown} **Step 1:** &nbsp; Recall the formula for the FOIL method.

\begin{align*}
    (a + b)(c + d) &= ac + ad + bc + bd
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Use the FOIL method to expand the expression.

\begin{align*}
  (x+2)(3x-5) 
  &= x(3x) + x(-5) + 2(3x) + 2(-5) &&\text{FOIL}\\
  &= 3x^2 - 5x + 6x - 10 && \text{simplify each term}
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Combine like terms.

\begin{align*}
  3x^2 - 5x + 6x - 10 
  &= 3x^2 + x - 10
\end{align*}
```
````


## Squaring a Binomial

```{admonition} Applying the FOIL Method to the Square of a Binomial
:class: info

When applying the FOIL method to the square of a binomial (i.e., $(a+b)^2$ or $(a-b)^2$), we arrive at the following formulas:

$$
(a + b)^2 = a^2 + 2ab + b^2
\qquad\qquad
(a - b)^2 = a^2 - 2ab + b^2
$$
```


````{admonition} Video Resource
:class: important

::::{grid} 2
:::{grid-item}
:columns: 1
:padding: 1
```{image} ../images/UnderstandTheMath.png
:alt: UnderstandTheMath
```
:::
:::{grid-item}
:columns: 10
<a href="https://youtu.be/QlWekLztefU" target="_blank">Squaring a Binomial</a> (Links to an external site) <br>
A review of how to square a binomial expression using the FOIL method or using the above formulas.
:::
::::
````



### Example 6

````{admonition} Expanding the square of a binomial
:class: tip

Expand $(3x-5)^2$ by squaring the binomial.


```{dropdown} **Step 1:** &nbsp; Apply the appropriate binomial formula.

Apply $(a - b)^2 = a^2 - 2ab + b^2$ with $a=3x$ and $b=5$.
\begin{align*}
(3x-5)^2
&= (3x)^2 - 2(3x)(5) + 5^2 
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Simplify each term.

\begin{align*}
(3x)^2 - 2(3x)(5) + 5^2  &= 9x^2 - 30x + 25
\end{align*}
```
````


### Example 7
````{admonition} Expanding a product of a monomial and the square of a binomial
:class: tip

Expand $3x^5(4+x)^2$.


```{dropdown} **Step 1:** &nbsp; Apply the appropriate binomial formula.

Apply $(a + b)^2 = a^2 + 2ab + b^2$ with $a=4$ and $b=x$.
\begin{align*}
3x^5(4+x)^2 &= 3x^5(4^2 + 2(4)(x) + x^2) 
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Simplify each term.

\begin{align*}
3x^5(4^2 + 2(4)(x) + x^2) &= 3x^5(16 + 8x + x^2) 
\end{align*}
```


```{dropdown} **Step 3:** &nbsp; Distribute the factor of $3x^5$ and simplify again.

\begin{align*}
3x^5(16 + 8x + x^2) 
&= 3x^5(16) + 3x^5(8x) + 3x^5(x^2) && \text{distribute $3x^5$} \\ \\
&= 48x^5 + 24x^6 + 3x^7 && \text{simplify each term}
\end{align*}
```
````