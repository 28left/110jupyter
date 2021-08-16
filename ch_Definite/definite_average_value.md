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
# Average Value of a Function

## Computing the Average Value of a Continuous Function

```{admonition} Definition
:class: info

If $f$ is integrable on $[a, b]$, then the average value of $f$ over $[a, b]$ is given by

$$\frac{1}{b-a}\int_a^b f(x)dx.$$
```

## Example 10

Find the average value of $f(x) = 3x^2 + 4x^3$ over the interval $[-1, 1]$.

```{admonition} Step 1: The average value is given by
:class: tip, dropdown

\begin{align*}
    \frac{1}{1-(-1)} \int_{-1}^1 3x^2 + 4x^3 ~dx 
    &= \frac{1}{2} \int_{-1}^1 3x^2 + 4x^3 ~dx \\
    &= \frac{1}{2}\left(x^3+x^4\right)\Big|_{-1}^1 \\
    &= \frac{1}{2}\left[(1^3 + 1^4) - ((-1)^3+(-1)^4)\right]\\
    &= \frac{1}{2}(2-0)  \\
    &= 1
\end{align*}
```

## Example 11

Find the average value of $f(x) = \dfrac{12}{x}$ over the interval $[-9, -3]$.

```{admonition} Step 1: The average value is given by
:class: tip, dropdown

\begin{align*}
  \frac{1}{-3-(-9)} \int_{-9}^{-3} \frac{12}{x} ~dx 
  &= \frac{12}{6} \int_{-9}^{-3} \frac{1}{x} ~dx \\
  &= 2\ln|x|\Biggr|_{-9}^{-3} \\
  &= 2[\ln|-3| - \ln|-9|]\\ \\
  &= 2[\ln(3) - \ln(9)]\\ \\
  &= 2\ln(3/9) && \hbox{Since $\ln(m/n) = \ln(m) - \ln(n)$}\\ \\
  &= 2\ln(3^{-1}) \\ \\
  &= -\ln(9) && \hbox{Since $m\ln(n) = \ln(n^m)$}
\end{align*}
```

## Example 12

Sales of the Penn State Learning Calculus tutorial software packages are approximated by

$$f(t) = \frac{t^2}{(t^3+5)^2},$$

where $t$ is in years and $f(t)$ is in millions of software packages. What are the average sales over the time interval $0 \leq t \leq 3$ years?

```{admonition} Step 1: Use the definition of average value.
:class: tip, dropdown

The average value is given by

$$\frac{1}{3-0}\int_0^3 \frac{t^2}{(t^3+5)^2}~dt = \frac{1}{3}\int_0^3 \frac{t^2}{(t^3+5)^2}~dt.$$
```

```{admonition} Step 2: Identify a suitable substitution.
:class: tip, dropdown

Based on rewriting the integral in the following form

$$\frac{1}{3}\int_{t=0}^{t=3} (t^3+5)^{-2}~t^2 ~dt$$

let $u = t^3 + 5$ and $du = 3t^2 ~dt$, or equivalently $\dfrac{1}{3} du = t^2 ~dt$.
```

```{admonition} Step 3: Determine the new limits of integration using the substitution $u = t^3 + 5$.
:class: tip, dropdown

\begin{align*}
\text{When } t=3 ~~&\Longrightarrow~~ u = 3^3 + 5 = 32\\
\text{When } t=0 ~~&\Longrightarrow~~ u = 0^3 + 5 = 5
\end{align*}
```

```{admonition} Step 4: Rewrite the integral in terms of $u$ and $du$.
:class: tip, dropdown

\begin{align*}
  \frac{1}{3}\int_{t=0}^{t=3} (t^3+5)^{-2}~t^2 ~dt
  &= \frac{1}{3} \int_{u=5}^{u=32} u^{-2} ~ \frac{1}{3} du\\
  &= \frac{1}{9} \int_{u=5}^{u=32} u^{-2} ~du
\end{align*}
```

```{admonition} Step 5: Evaluate the integral.
:class: tip, dropdown

\begin{align*}
  \frac{1}{9} \int_{u=5}^{u=32} u^{-2} ~du 
  &= \frac{1}{9}(-u^{-1}) \Big|_{5}^{32}  && \hbox{Since $\dfrac{u^{-1}}{-1}$ is an antiderivative of $u^{-2}$}\\
  &= \frac{1}{9}\left[\left( -\frac{1}{32}\right)- \left(-\frac{1}{5}\right)\right] && \hbox{Plug in limits of integration}\\
  &= \frac{1}{9}\left(\frac{1}{5} - \frac{1}{32}\right) && \hbox{Simplify}\\
  &= 3/160
\end{align*}

Therefore, the average sales over the time interval $0\leq t \leq 3$ is $3/160$ millions of software packages per year.
```