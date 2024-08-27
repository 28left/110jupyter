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
# Substitution for Definite Integrals

## Changing the Limits of Integration via Substitution



```{admonition} Substitution Rule for Definite Integrals
:class: info

When evaluating the definite integral $\displaystyle \int_a^b f(x) ~dx$, the limits of integration are assumed to be in terms of the variable $x$ (i.e., we are integrating from $x = a$ to $x = b$). If we change the variable by applying the substitution $u = g(x)$, then we also need to change the limits of integration so that they are in terms of the new variable $u$. The substitution rule for definite integrals, as stated below, tells us exactly how to do that. 

$$\int_{x=a}^{x=b} f(g(x))g'(x)~dx = \int_{u=g(a)}^{u=g(b)} f(u) ~du$$

where $u=g(x)$ and $du = g'(x) ~dx$.
```

```{admonition} Method of Integration by Substitution for Definite Integrals
:class: info

1. Write the given integral in one of the following two forms:

    $$\int_{x=a}^{x=b} [g(x)]^n g'(x) ~dx \qquad \text{or} \qquad \int_{x=a}^{x=b} e^{g(x)} g'(x) ~dx$$

2. Let $u=g(x)$ and compute the corresponding differential $du = g'(x) dx$.

3. Rewrite the integral in terms of $u$ and $du$.  This includes changing the limits of integration so that the new lower limit of integration is $g(a)$ and the new upper limit of integration is $g(b)$.

4. Evaluate the integral in terms of the variable $u$.

5. Plug in the new limits of integration, $g(b)$ and $g(a)$.
```



### Example 1

````{admonition} Using substitution to integrate rational functions
:class: tip

Evaluate $\displaystyle \int_{1}^{2} \frac{6x^2}{2x^3 + 1}~dx$. 

```{dropdown} **Step 1:** &nbsp; Identify a suitable substitution.

Based on rewriting the integral in the following form

$$\int_{x=1}^{x=2} (2x^3+1)^{-1} 6x^2 ~dx$$

let $u = 2x^3+1$ and $du = 6x^2 ~du$.
```

```{dropdown} **Step 2:** &nbsp; Determine the new limits of integration.

If $u = 2x^3+1$, then
\begin{align*}
  \text{when } x=2 ~~&\Longrightarrow~~ u = 2(2)^3 + 1 = 17 \\
  \text{when } x=1 ~~&\Longrightarrow~~ u = 2(1)^3 + 1 = 3 
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Rewrite the integral in terms of $u$ and $du$.

$$\int_{x=1}^{x=2} (2x^3+1)^{-1} 6x^2 ~dx = \int_{u=3}^{u=17} u^{-1} ~du$$
```

```{dropdown} **Step 4:** &nbsp; Evaluate the integral.

\begin{align*}
  \int_{u=3}^{u=17} \frac{1}{u}~du 
  &= \ln|u| \Big|_3^{17} && \text{since $\ln|u|$ is an antiderivative of $\dfrac{1}{u}$}\\
  &= \ln(17) - \ln(3) && \text{plug in limits of integration}\\
  &= \ln(17/3) && \text{since $\ln(m/n) = \ln(m) - \ln(n)$}
\end{align*}

Therefore,

$$\int_{1}^{2} \frac{6x^2}{2x^3 + 1}~dx = \ln(17/3).$$
```
````

### Example 2

````{admonition} Finding the area under a graph
:class: tip

Find the area of the region under the graph of $f(x) = e^{-3x/2}$ between $x = -2$ and $x = 6$.

```{dropdown} **Step 1:** &nbsp; Find the definite integral that corresponds to the area of the given region.

Since $e^{-3x/2} \geq 0$ for all $x$, the area under the graph of $f$ on $[-2,6]$ is given by

$$ \int_{x=-2}^{x=6} e^{-3x/2} ~dx.$$
```

```{dropdown} **Step 2:** &nbsp; Identify a suitable substitution.

Let $u = -3x/2$  and $du = -\dfrac{3}{2}~dx$, or equivalently $-\dfrac{2}{3} ~du = dx$.
```

```{dropdown} **Step 3:** &nbsp; Determine the new limits of integration.

If $u = -3x/2$, then
\begin{align*}
  \text{when } x=6 ~~&\Longrightarrow~~ u = -3(6)/2 = -9 \\
  \text{when } x=-2 ~~&\Longrightarrow~~ u = -3(-2)/2  = 3 
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Rewrite the integral in terms of $u$ and $du$.

\begin{align*}
  \int_{x=-2}^{x=6} e^{-3x/2} ~dx 
  &= \int_{u=3}^{u=-9} e^{u} \left(-\frac{2}{3}\right)~du \\
  &= -\frac{2}{3}\int_{u=3}^{u=-9} e^{u} ~du 
\end{align*}

Notice that the new lower limit of integration ($u=3$) is larger than the new upper limit ($u=-9$). There is nothing wrong with this and we will continue the calculation in the next step as is. However, it is possible to switch limits of integration using the second {ref}`def_int:properties`. Specifically,

$$ -\frac{2}{3}\int_{u=3}^{u=-9} e^{u} ~du = \frac{2}{3}\int_{u=-9}^{u=3} e^{u} ~du.$$ 
```

```{dropdown} **Step 5:** &nbsp; Evaluate the integral.

\begin{align*}
  -\frac{2}{3}\int_{u=3}^{u=-9} e^{u} ~du
  &= -\frac{2}{3} e^{u} \Biggr|_{u=3}^{u=-9} \\
  &= -\frac{2}{3}(e^{-9} - e^3) \\
  &= \frac{2}{3}(e^{3} - e^{-9}) 
\end{align*}

Therefore, the area under the graph of $f$ on $[-2,6]$ is given by $\dfrac{2}{3}\left(e^3 - e^{-9}\right)$.
```

```{admonition} Observation
:class: warning

The integral in Step 1 can be evaluated without using substitution. Try using the following formula instead.

$$ \int e^{ax} ~dx = \frac{1}{a}e^{ax} + C ~~~~~ \hbox{for } a\neq 0.$$
```
````


### Example 3

````{admonition} Using substitution
:class: tip

Evaluate $\displaystyle \int_{1}^{3} x\sqrt{3x^2-2}~dx$.

```{dropdown} **Step 1:** &nbsp; Identify a suitable substitution.

Based on rewriting the integral in the following form

$$\int_{x=1}^{x=3} (3x^2-2)^{1/2} ~x ~dx$$

let $u = 3x^2-2$ and $du = 6x ~dx$, or equivalently $\dfrac{1}{6} du = x ~dx$.
```

```{dropdown} **Step 2:** &nbsp; Determine the new limits of integration.

If $u = 3x^2-2$, then
\begin{align*}
  \text{when } x=3 ~~&\Longrightarrow~~ u = 3(3)^2 - 2 = 25 \\
  \text{when } x=1 ~~&\Longrightarrow~~ u = 3(1)^2 - 2 = 1
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Rewrite the integral in terms of $u$ and $du$.

\begin{align*}
  \int_{x=1}^{x=3} (3x^2-2)^{1/2} ~x ~dx 
  &= \int_{u=1}^{u=25} u^{1/2} \frac{1}{6}~du\\
  &= \frac{1}{6}\int_{u=1}^{u=25} u^{1/2} ~du
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Evaluate the integral.

\begin{align*}
  \frac{1}{6}\int_{u=1}^{u=25} u^{1/2} ~du 
  &= \frac{1}{6}\cdot\frac{2}{3}u^{3/2}\Biggr|_1^{25} && \text{power rule}\\
  &= \frac{1}{9}u^{3/2}\Biggr|_1^{25} && \text{simplify}\\
  &= \frac{1}{9}(25^{3/2} - 1^{3/2}) && \text{plug in limits of integration}\\
  &= \frac{1}{9}(5^{3} - 1) && \text{since $25^{3/2} = (25^{1/2})^3 = 5^3$}\\
  &= 124/9
\end{align*}

Therefore,

$$\int_{1}^{3} x\sqrt{3x^2-2}~dx = 124/9.$$
```
````


### Example 4

````{admonition} Using substitution
:class: tip

Evaluate $\displaystyle \int_{0}^{2} \frac{e^x}{1+e^x} ~dx$.


```{dropdown} **Step 1:** &nbsp; Identify a suitable substitution.

Based on rewriting the integral in the following form

$$\int_{x=0}^{x=2} (1+e^x)^{-1} ~e^x ~dx$$

let $u = 1+e^x$ and $du = e^x ~dx$.
```

```{dropdown} **Step 2:** &nbsp; Determine the new limits of integration.

If $u = 1+e^x$, then
\begin{align*}
  \text{when } x=2 ~~&\Longrightarrow~~ u = 1+e^2 \\
  \text{when } x=0 ~~&\Longrightarrow~~ u = 1+e^0 = 2
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Rewrite the integral in terms of $u$ and $du$.

\begin{align*}
  \int_{x=0}^{x=2} (1+e^x)^{-1} ~e^x ~dx
  &= \int_{u=2}^{u=1+e^2} u^{-1} ~du\\
  &= \int_{u=2}^{u=1+e^2} \frac{1}{u} ~du
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Evaluate the integral.

\begin{align*}
  \int_{u=2}^{u=1+e^2} \frac{1}{u} ~du 
  &= \ln|u| \Big|_2^{1+e^2} \\
  &=  \ln(1+e^2)-\ln(2) && \text{plug in limits of integration}\\
  &= \ln\left(\frac{1+e^2}{2}\right)&& \text{since $\ln(m/n) = \ln(m) - \ln(n)$}
\end{align*}

Therefore,

$$\int_{0}^{2} \frac{e^x}{1+e^x} ~dx = \ln\left(\frac{1+e^2}{2}\right).$$
```
````