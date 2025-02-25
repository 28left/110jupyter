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
# The Fundamental Theorem of Calculus

## How to Use Antiderivatives to Evaluate Definite Integrals

```{admonition} The Fundamental Theorem of Calculus
:class: info

Let $f$ be a continuous function on $[a, b]$. Then

$$ \int_a^b f(x) ~dx = F(b) - F(a) $$

where $F$ is any antiderivative of $f$.
```

```{admonition} Notation
:class: note

$$F(x) \Big|_a^b = F(b) - F(a)$$
```

### Example 1

````{admonition} Area under a graph
:class: tip

Write the area under the graph of $y=x^2$ on $[1,3]$ as a definite integral and then use the Fundamental Theorem of Calculus to evaluate it. Compare the result with the approximations found in {ref}`def_int:example_1` of the previous section.


```{dropdown} **Step 1:** &nbsp; Write the area under the graph of $y=x^2$ on $[1,3]$ as a definite integral.

$$\int_1^3 x^2 ~dx$$
```

```{dropdown} **Step 2:** &nbsp; Find an antiderivative of $x^2$.

\begin{align*}
  \int x^2~dx &= \frac{1}{3}x^3 + C && \text{power rule}
\end{align*}

Therefore, $x^3/3$ is an antiderivative of $x^2$, and can be used to evaluate the definite integral from Step 1.
```

```{dropdown} **Step 3:** &nbsp; Apply the Fundamental Theorem of Calculus.

\begin{align*}
  \int_1^3 x^2dx &= \frac{1}{3}x^3 \Biggr|_1^3 && \text{since $\frac{1}{3}x^3$ is an antiderivative of $x^2$} \\
  &= \frac{1}{3}3^3 - \frac{1}{3}1^3 && \text{plug in the limits of integration} \\
  &= \frac{27}{3} - \frac{1}{3} && \text{simplify} \\
  &= 26/3
\end{align*}

Therefore, the area under the graph of $y=x^2$ on $[1,3]$ is $26/3 = 8.\overline{6}$.
```

```{dropdown} **Step 4:** &nbsp; Compare the result from Step 3 to the approximations found in Example 1.

The above calculations show that the area of the region is exactly $8.\overline{6}$. The approximations we calculated in {ref}`def_int:example_1` of the previous section were $10.75$ (using right Riemann sum), $6.75$ (using left Riemann sum), and $8.625$ (using the Midpoint Rule).
```
````


### Example 2

````{admonition} Evaluating a definite integral
:class: tip

Evaluate $\displaystyle \int_1^2 \frac{x^2 + 4x^4}{x^3} ~dx$.


```{dropdown} **Step 1:** &nbsp; Simplify the integrand by writing it as a sum.

\begin{align*}
\frac{x^2 + 4x^4}{x^3} 
&= \frac{x^2}{x^3} + \frac{4x^4}{x^3} \\
&=  \frac{1}{x} + 4x
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Find an antiderivative of $\dfrac{1}{x} + 4x$.

\begin{align*}
  \int \frac{1}{x} + 4x ~dx
  &= \ln|x| + \frac{4x^2}{2} + C \\
  &= \ln|x| + 2x^2 + C
\end{align*}

Therefore, $\ln|x| + 2x^2 $ is an antiderivative of $\dfrac{1}{x} + 4x$, and can be used to evaluate the given definite integral.
```

```{dropdown} **Step 3:** &nbsp; Apply the Fundamental Theorem of Calculus.

\begin{align*}
\int_1^2 \frac{x^2 + 4x^4}{x^3} ~dx
  &= \int_1^2 \frac{1}{x} + 4x  ~dx \\
  &= \ln|x| + 2x^2 \Big|_1^2 && \hbox{since $\ln|x| + 2x^2$ is an antiderivative}\\
  &= (\ln|2| + 2(2)^2) - (\ln|1| + 2(1)^2) && \text{plug in limits of integration}\\
  &= \ln(2) + 8 - 0 - 2 && \hbox{since $\ln(1) = 0$}\\
  &= 6 + \ln(2).
\end{align*}
```
````


### Example 3

````{admonition} Evaluating a definite integral
:class: tip

Evaluate $\displaystyle \int_{0}^{4} e^x ~dx$. 

```{dropdown} **Step 1:** &nbsp; Apply the Fundamental Theorem of Calculus.

\begin{align*}
  \int_{0}^{4} e^x ~dx
  &= e^x \Big|_0^4 && \hbox{since $e^x$ is an antiderivative of $e^x$}\\
  &= e^4 - e^0 && \text{plug in limits of integration}\\
  &= e^4 - 1 && \hbox{since $e^0 = 1$}\\
\end{align*}
```
````


### Example 4

````{admonition} Computing total revenue from marginal revenue
:class: tip

The daily marginal revenue function associated with selling $m$ gadgets is given by $R'(m)=0.2m + 50$, where $R'(m)$ is given in dollars per unit.

- Find the daily total revenue realized from the sale of the first 20 gadgets.
- Find the additional revenue realized from the sale of the 21st through 50th gadgets.


```{dropdown} **Step 1:** &nbsp; Apply the Fundamental Theorem of Calculus for the first case.

By the Fundamental Theorem of Calculus, the total revenue from the sale of the first 20 gadgets is given by

\begin{align*}
  R(20) 
  &= R(20) - R(0) && \hbox{since $R(0) = 0$} \\
  &= \int_0^{20} R'(m)~dm && \hbox{Fundamental Theorem of Calculus}\\
  &= \int_0^{20} \frac{2}{10}m + 50 ~dm.
\end{align*}

We evaluate the integral to get

\begin{align*}
  \frac{2}{10}\cdot \frac{m^2}{2} + 50m \Biggr|_0^{20} 
  &= \frac{m^2}{10} + 50m \Biggr|_0^{20} \\
  &= \left(\frac{20^2}{10} + 50(20)\right)-\left(\frac{0^2}{10} + 50(0)\right)\\
  &= 40+1000 - 0\\
  &=1040.
\end{align*}

Therefore, the total revenue from the sale of the first 20 gadgets is $\$1,040$.
```

```{dropdown} **Step 2:** &nbsp; Apply the Fundamental Theorem of Calculus for the second case.

Note that the additional revenue realized from the sale of the 21st through 50th gadgets is given by $R(50) - R(20)$.  This is because $R(50)$ corresponds to the revenue generated from the sale of gadgets 1 through 50 and $R(20)$ corresponds to the revenue generated from the sale of gadgets 1 through 20.  When we subtract the two values, what remains corresponds to the revenue associated with gadgets 21 through 50.

By the Fundamental Theorem of Calculus, we have

\begin{align*}
  R(50) - R(20) 
  &= \int_{20}^{50} R'(m)~dm \\
  &= \int_{20}^{50} \frac{2}{10}m + 50 ~dm.
\end{align*}

Evaluating the integral, we get

\begin{align*}
  \frac{2}{10}\cdot \frac{m^2}{2} + 50m \Biggr|_{20}^{50} 
  &= \frac{m^2}{10} + 50m \Biggr|_{20}^{50} \\
  &=  \left(\frac{50^2}{10} + 50(50)\right) - \left( \frac{20^2}{10} + 50(20)\right)\\
  &=(250+2500)-(40+1000)\\
  &=2750-1040 \\
  &=1710.
\end{align*}

Therefore, the sale of gadgets 21 through 50 generate an additional revenue of $\$1,710.$
```
````