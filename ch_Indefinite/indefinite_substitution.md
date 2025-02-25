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

(indefinite:substitution)=
# Integration by Substitution

## Method of Integration by Substitution

```{admonition} Method of Integration by Substitution
:class: info

1. Write the given integral in one of the following two forms:

    $$\int [g(x)]^n g'(x) ~dx \qquad \text{or} \qquad \int e^{g(x)} g'(x) ~dx$$

2. Let $u=g(x)$ and compute the corresponding differential $du = g'(x) dx$.

3. Rewrite the integral in terms of $u$ and $du$.  To complete the substitution, it may be helpful to divide both sides of $du= g'(x) ~dx$ by a constant and/or to solve for $x$ in terms of $u$ in the equation $u=g(x)$.

4. Evaluate the integral in terms of the variable $u$.

5. Replace $u$ with $g(x)$.
```


### Example 1
````{admonition} Integration by substitution
:class: tip

Compute $\displaystyle \int 20x^3 \sqrt{5x^4+7} ~dx$.

```{dropdown} **Step 1:** &nbsp; Identify a suitable substitution.

Based on rewriting the integral in the following form

$$\int (5x^4+7)^{1/2} ~20x^3  ~dx$$

Let $u=5x^4 + 7$ and therefore, $du = 20x^3 ~dx$.
```

```{dropdown} **Step 2:** &nbsp; Rewrite the integral in terms of $u$ and $du$.

$$\int (5x^4+7)^{1/2} ~20x^3  ~dx = \int u^{1/2} ~du$$
```

```{dropdown} **Step 3:** &nbsp; Evaluate the integral in terms of $u$.

\begin{align*}
  \int u^{1/2} ~du
  &= \frac{u^{1/2+1}}{1/2+1} + C &&\text{power rule}\\
  &= \frac{u^{3/2}}{3/2} + C &&\text{simplify}\\
  &= \frac{2}{3}u^{3/2} + C && \text{simplify}
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Replace $u$ with $5x^4 + 7$.

$$ \int 20x^3 \sqrt{5x^4+7} ~dx ~=~ \frac{2}{3}(5x^4 + 7)^{3/2} + C $$
```
````


### Example 2
````{admonition} Integration by substitution
:class: tip

Compute $\displaystyle \int 7x^2e^{4x^3+5} ~dx$.

```{dropdown} **Step 1:** &nbsp; Identify a suitable substitution.

Based on rewriting the integral in the following form

$$7\int e^{4x^3+5} ~x^2 ~dx$$

Let $u=4x^3 + 5$ and therefore, $du = 12x^2 ~dx$, or equivalently $\dfrac{1}{12}du = x^2 ~dx$.
```

```{dropdown} **Step 2:** &nbsp; Rewrite the integral in terms of $u$ and $du$.

\begin{align*}
  7\int e^{4x^3+5} ~x^2 ~dx
  &= 7\int e^{u} \frac{1}{12} ~du \\
  &= \frac{7}{12}\int e^{u}  ~du 
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Evaluate the integral in terms of $u$.

\begin{align*}
  \frac{7}{12}\int e^{u}  ~du
  &= \frac{7}{12}e^u + C 
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Replace $u$ with $4x^3 + 5$.

$$ \int 7x^2e^{4x^3+5} ~dx ~=~ \frac{7}{12}e^{4x^3 + 5} + C $$
```
````

### Example 3
````{admonition} Integration by substitution
:class: tip

Compute $\displaystyle \int \frac{(\ln x)^2}{x}~dx$.

```{dropdown} **Step 1:** &nbsp; Identify a suitable substitution.

Based on rewriting the integral in the following form

$$\int (\ln x)^2\frac{1}{x} ~dx$$

Let $u=\ln x$ and therefore, $du = \dfrac{1}{x} ~dx$.
```

```{dropdown} **Step 2:** &nbsp; Rewrite the integral in terms of $u$ and $du$.

\begin{align*}
  \int (\ln x)^2\frac{1}{x} ~dx
  &= \int u^2  ~du 
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Evaluate the integral in terms of $u$.

\begin{align*}
  \int u^2  ~du
  &= \frac{1}{3}u^3 + C
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Replace $u$ with $\ln x$.

$$ \int \frac{(\ln x)^2}{x}~dx ~=~ \frac{1}{3}(\ln x)^3 + C $$
```
````


### Example 4
`````{admonition} Integration by substitution
:class: tip

Compute $\displaystyle \int \frac{x}{x+4} ~dx$.

```{dropdown} **Step 1:** &nbsp; Identify a suitable substitution.

Based on rewriting the integral in the following form

$$\int (x+4)^{-1} x ~dx$$

Let $u=x+4$ and therefore, $du = dx$.
```

```{dropdown} **Step 2:** &nbsp; Rewrite the integral in terms of $u$ and $du$.

In this case, it is necessary to solve for $x$ in terms of $u$ in the equation $u = x+4$ (i.e., $x = u-4$) to complete the substitution.

\begin{align*}
  \int (x+4)^{-1} x ~dx
  &= \int u^{-1} (u-4) ~du \\
  &= \int \frac{u-4}{u} ~du 
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Evaluate the integral in terms of $u$.

\begin{align*}
  \int \frac{u-4}{u} ~du 
  &= \int \frac{u}{u}- \frac{4}{u} ~du && \hbox{rewrite integrand as a sum}\\
  &= \int 1- \frac{4}{u} ~du && \hbox{simplify}\\
  &= \int 1 ~du - 4\int \frac{1}{u} ~du && \hbox{sum & constant multiple rules}\\
  &= u - 4\ln|u| + C && \hbox{integrate each term}
\end{align*}
```

````{dropdown} **Step 4:** &nbsp; Replace $u$ with $x+4$.

\begin{align*}
  \int \frac{x}{x+4} ~dx 
  &= x+4 - 4\ln|x+4| +C \\
  &= x - 4\ln|x+4| +C + 4 \\
  &= x - 4\ln|x+4| +C 
\end{align*}

```{admonition} Observation
:class: warning

The last line follows from the observation that if $C$ is an arbitrary constant, then so is $C+4$. In other words, the $+4$ can be absorbed into the arbitrary constant $C$, and is not needed. We can verify this final answer by computing its derivative.

\begin{align*}
  \frac{d}{dx}(x - 4\ln|x+4|)
  &= 1 - 4\frac{1}{x+4} \\
  &= \frac{x+4}{x+4} - \frac{4}{x+4} && \hbox{get a common denominator}\\
  &= \frac{x+4 - 4}{x+4}&& \hbox{combine numerators} \\
  &= \frac{x}{x+4} && \hbox{simplify}
\end{align*}

Therefore, $x - 4\ln|x+4|$ is an antiderivative of $\dfrac{x}{x+4}$. 
```
````


`````