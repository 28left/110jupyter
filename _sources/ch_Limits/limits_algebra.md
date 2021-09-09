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

# Examples: Computing Limits Algebraically

## Example: Constant Function

If $f(x) = 2$, find $\lim\limits_{x\to 1^{-}}f(x)$.

```{admonition} Solution
:class: tip, dropdown

$f$ is a constant function, hence a polynomial. Therefore, by Property 7 of {ref}`lim:prop_lim`, $\lim\limits_{x\to 1} f(x) = f(1) = 2$. Since the limit exists, the one-sided limits exist, too and coincide with the limit. Thus, $\lim\limits_{x\to 1^{-}}f(x) = 2$.
```

## Example: Rational Function (1)

Evaluate 

$$\lim\limits_{x\to -1} \dfrac{x^3 +4x^2-x-3}{2x^2+1}.$$

```{admonition} Solution
:class: tip, dropdown

The function 

$$ g(x) = \dfrac{x^3 +4x^2-x-3}{2x^2+1}$$

is a rational function, and since $2(-1)^2 + 1 = 3 \neq 0$, it follows that $-1$ is in the domain of $g$. 
Again by Property 7 of {ref}`lim:prop_lim`, $\lim\limits_{x\to -1} g(x)$ exists and equals 

$$g(-1) = \frac{(-1)^3 + 4(-1)^2 - (-1) -3}{2(-1)^2+1} = \frac{1}{3}.$$
```

## Example: Rational Function (2)

Evaluate 

$$\lim\limits_{x\to 2} \dfrac{x^2 +4x-1}{x-2}.$$

```{admonition} Solution
:class: tip, dropdown

For $x=2$, the denominator of the expression above is zero, so we cannot apply Property 7 of {ref}`lim:prop_lim` in this case. We observe that, as $x$ gets closer to $2$, the values of the denominator get closer to $0$, while the values of the numerator approach $11$. 

Moreover, if we approach $2$ from the left, the values of $(x^2 +4x-1)/(x-2)$ will be negative and approach $-\infty$, while if we approach from the right, the values are positive and approach $+\infty$. 

Therefore, neither the left-hand limit nor the right-limit exists, and hence $\lim\limits_{x\to 2} \dfrac{x^2 +4x-1}{x-2}$ does not exist either. 
```

## Example: Piecewise Polynomial Function

Evaluate $\displaystyle\lim_{x\to 6} h(x)$, where

\begin{equation*}
h(x)=
\begin{cases} 
x^2-4x-12 & \hbox{if } x<6 \\
8 & \hbox{if } x=6 \\
x^2-5x-6 & \hbox{if } x>6 \\  
\end{cases}
\end{equation*}

```{dropdown} **Step 1:** Find the limit from the left.

In this case, since we are approaching 6 from the left, we can assume that $x<6$, and therefore $h(x) = x^2-4x-12$.
\begin{align*}
\lim_{x\to 6^{-}} h(x) 
&= \lim_{x\to 6^-} x^2-4x-12\\ \\
&= 6^2-4(6)-12 && \text{Plug in $x=6$ (Property 7)}\\ \\
&= 36-24-12 && \text{Simplify}\\ \\
&= 0
\end{align*}
```

```{dropdown} **Step 2:** Find the limit from the right. 

In this case, since we are approaching 6 from the right, we can assume that $x>6$, and therefore $h(x) = x^2-5x-6$.
\begin{align*}
\lim_{x\to 6^{+}} h(x) 
&= \lim_{x\to 6^+} x^2-5x-6\\ \\
&= 6^2-5(6)-6  && \text{Plug in $x=6$ (Property 7)}\\ \\
&= 36-30-6 && \text{Simplify}\\ \\
&= 0
\end{align*}
```

```{dropdown} **Step 3:** Check to see if the two limits are equal.

Since $\displaystyle \lim_{x\to 6^-} h(x) = \lim_{x\to 6^+} h(x) = 0$, we conclude that the limit exists and

$$\lim_{x\to 6} h(x) = 0.$$
```

```{warning} 
Keep in mind that just because $\displaystyle\lim_{x\to 6} h(x) \neq h(6) = 8$, this does not mean that the limit does not exist.
```




