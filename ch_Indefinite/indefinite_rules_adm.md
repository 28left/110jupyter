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
# Basic Rules of Integration

```{admonition} Integral of a Costant
:class: info

For any real number $k$,

$$\int k ~dx = kx + C$$
```

```{admonition} The Power Rule
:class: info

For any real number $n\neq -1$,

$$\int x^n ~dx = \frac{x^{n+1}}{n+1} + C$$
```

```{admonition} The Constant Multiple Rule
:class: info

For any real number $k$,

$$\int kf(x) ~dx = k\int f(x) ~dx$$
```

```{admonition} The Sum Rule
:class: info

$$\int f(x)\pm g(x) ~dx = \int f(x) ~dx \pm \int g(x) ~dx$$
```

```{admonition} Integral of $e^x$
:class: info

For any real number $a\neq 0$,

$$\int e^x ~dx = e^x + C$$

and

$$\int e^{ax} ~dx = \frac{e^{ax}}{a} + C$$
```

```{admonition} Integral of $1/x$
:class: info

$$\int \frac{1}{x} ~dx = \ln|x| + C$$
```

```{admonition} The Substitution Rule
:class: info

If $u=g(x)$ and $du = g'(x) ~dx$ then

$$\int f(g(x))g'(x) ~dx = \int f(u) ~du$$
```

## Example 2

Compute $\displaystyle \int 13 ~dz$.

```{dropdown} **Step 1:** Notice the differential $dz$.

This indicates that we are looking for a function of $z$, $f(z)$, such that $f'(z) = 13$.
```

```{dropdown} **Step 2:** Recall the formula for the integral of a constant.

$$\int k ~dx = kx + C$$
```

```{dropdown} **Step 3:** Apply the rule with $k = 13$.

Therefore,

$$\int 13 ~dz = 13z + C$$
```

## Example 3

Compute $\displaystyle \int  x^7 ~dx$.

```{dropdown} **Step 1:** Recall the power rule.

For any real number $n\neq -1$,

$$\int x^n ~dx = \frac{x^{n+1}}{n+1} + C$$
```

```{dropdown} **Step 2:** Apply the power rule with $n = 7$.

\begin{align*}
  \int x^7  dx 
  &= \frac{x^{7+1}}{7+1} + C \\
  &= \frac{x^8}{8} + C 
\end{align*}
```

## Example 4

Compute $\displaystyle \int \frac{1}{\sqrt{y}} ~dy$.

```{dropdown} **Step 1:** Rewrite the integrand in the appropriate form to apply the power rule.

$$\int  \frac{1}{\sqrt{y}} ~dy = \int  y^{-1/2} ~dy$$
```

```{dropdown} **Step 2:** Apply the power rule with $n = -1/2$.

\begin{align*}
  \int  y^{-1/2} ~dy 
  &=  \frac{y^{-1/2 + 1}}{-1/2 + 1} + C \\
  &=  \frac{y^{1/2}}{1/2} + C \\
  &= 2\sqrt{y} + C
\end{align*}
```

## Example 5

Compute $\displaystyle \int  4x^{7/3} ~dx$.

```{dropdown} **Step 1:** Recall the constant multiple rule.

For any real number $k$,

$$\int kf(x) ~dx = k\int f(x) ~dx$$
```

```{dropdown} **Step 2:** Apply the constant multiple rule with $k=4$.

\begin{align*}
  \int 4x^{7/3}  ~dx 
  &= 4\int x^{7/3} ~dx \\
  &= 4 \left(\frac{x^{7/3+1}}{7/3+1}\right) + C && \text{Power rule with $n=7/3$}\\
  &= 4 \left( \frac{x^{10/3}}{10/3}\right) + C && \hbox{Simplify} \\
  &= 4 \cdot \frac{3}{10} x^{10/3} + C \\
  &=  \frac{6}{5} x^{10/3} + C 
\end{align*}
```

## Example 6

Compute $\displaystyle \int 5t^3-\frac{10}{t^{6}}+4\sqrt{t} ~dt$.

```{dropdown} **Step 1:** Recall the sum rule.

$$\int f(x)\pm g(x) ~dx = \int f(x) ~dx \pm \int g(x) ~dx$$
```

```{dropdown} **Step 2:** Apply the sum and constant multiple rules and then integrate each term.

\begin{align*}
  \int 5t^3-\frac{10}{t^{6}}+4\sqrt{t}  ~dt
  &= \int 5t^3 ~dt - \int \frac{10}{t^{6}} ~dt + \int 4\sqrt{t}  ~dt && \text{Sum rule}\\
  &= 5\int t^3 ~dt - 10\int \frac{1}{t^{6}} ~dt + 4\int \sqrt{t}  ~dt && \text{Constant multiple rule}\\
  &= 5\int t^3 ~dt - 10\int t^{-6} ~dt + 4\int t^{1/2} ~dt  \\
  &= 5\cdot \frac{t^4}{4} - 10\cdot \frac{t^{-5}}{-5} + 4\frac{t^{3/2}}{3/2} + C  && \hbox{Power rule}\\
  &= \frac{5}{4}t^4 + 2t^{-5} + \frac{8}{3}t^{3/2} + C  && \hbox{Simplify}
\end{align*}
```

## Example 7

Compute $\displaystyle \int \frac{4x^9 - 15x^4 + 7x^3}{x^4} ~dx$.

```{dropdown} **Step 1:** Rewrite the integrand as a sum.

\begin{align*}
  \frac{4x^9-15x^4 + 7x^3}{x^4}
  &= \frac{4x^9}{x^4} -  \frac{15x^4}{x^4} + \frac{7x^3}{x^4}\\
  &= 4x^5 - 15 + \frac{7}{x}
\end{align*}
```

```{dropdown} **Step 2:** Apply the sum and constant multiple rules and then integrate each term.

\begin{align*}
  \int \frac{4x^9 - 15x^4 + 7x^3}{x^4} ~dx 
  &= \int 4x^5 - 15 + \frac{7}{x} ~dx \\ \\
  &= \int 4x^5 ~dx - \int 15 ~dx + \int \frac{7}{x}~dx && \hbox{Sum rule}\\ \\
  &= 4\int x^5 ~dx - \int 15 ~dx + 7\int \frac{1}{x}~dx && \hbox{Constant multiple rule}\\ \\
  &= \frac{4x^6}{6} - 15x + 7\ln|x| + C && \text{Integrate each term}\\ \\
  &= \frac{2x^6}{3} - 15x + 7\ln|x| + C && \text{Simplify}\\
\end{align*}
```

## Example 8

Compute $\displaystyle \int e^{2x/5}dx$.

```{dropdown} **Step 1:** Recall the formula for the integral of $e^{ax}$ for $a\neq 0$.

$$\int e^{ax} ~dx = \frac{e^{ax}}{a} + C$$
```

```{dropdown} **Step 2:** Apply the formula for the integral of $e^{ax}$ with $a=2/5$.

\begin{align*}
  \int e^{2x/5} ~dx 
  &= \frac{e^{2x/5}}{2/5} + C\\ \\
  &= \frac{5}{2}e^{2x/5} + C
\end{align*}
```

## Example 9

Compute $\displaystyle \int 3e^{2x}+\frac{8}{x}+\frac{4}{x^3} ~dx$.

```{dropdown} **Step 1:** Apply the sum and constant multiple rules and then integrate each term.

\begin{align*}
  \int 3e^{2x}+\frac{8}{x}+\frac{4}{x^3} ~dx 
  &= \int 3e^{2x} ~dx + \int \frac{8}{x} ~dx + \int 4x^{-3}~dx  && \hbox{Sum rule}\\ \\
  &= 3\int e^{2x} ~dx + 8\int \frac{1}{x} ~dx + 4\int x^{-3}~dx  && \hbox{Constant multiple rule}\\ \\
  &= 3\frac{e^{2x}}{2} + 8\int \frac{1}{x} ~dx + 4\int x^{-3}dx && \text{Integral of $e^{ax}$}\\ \\
  &= 3\frac{e^{2x}}{2} + 8\ln|x| + 4\int x^{-3}dx && \text{Integral of $1/x$}\\ \\
  &= 3\frac{e^{2x}}{2} + 8\ln|x| + \frac{4x^{-2}}{-2}+C && \text{Power rule}\\ \\
  &=\frac{3}{2}e^{2x} + 8\ln|x| - \frac{2}{x^{2}}+C && \text{Simplify}\\
\end{align*}
```

## Example 10

Compute $\displaystyle \int (e^{3x} + 1)(e^{-3x} - 1) ~dx$.

```{dropdown} **Step 1:** Rewrite the integrand as a sum.

\begin{align*}
  (e^{3x} + 1)(e^{-3x} - 1)
  &= e^{3x}e^{-3x} + e^{-3x} - e^{3x} - 1 && \hbox{Expand product}\\
  &= e^{3x-3x} + e^{-3x} - e^{3x} - 1 && \hbox{Since $e^a e^b = e^{a+b}$}\\
  &= e^{0} + e^{-3x} - e^{3x} - 1\\
  &= 1 + e^{-3x} - e^{3x} - 1 && \hbox{Since $e^0 = 1$}\\
  &= e^{-3x} - e^{3x} && \hbox{Simplify}
\end{align*}
```

```{dropdown} **Step 2:** Apply the sum rule and then integrate each term.

\begin{align*}
  \int (e^{3x} + 1)(e^{-3x} - 1) ~dx
  &= \int e^{-3x} - e^{3x} ~dx \\
  &= \int e^{-3x} ~dx  - \int e^{3x} ~dx \\
  &= \frac{1}{-3} e^{-3x}  - \frac{1}{3} e^{3x} + C && \text{Integral of $e^{ax}$}\\
  &= -\frac{1}{3}(e^{-3x} + e^{3x}) + C && \text{Simplify}
\end{align*}
```