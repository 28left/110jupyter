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
# Application of Integration by Parts

## Income Streams

An **income stream** refers to income that is generated continuously and transferred into an account that earns interest at a fixed rate. Interest is assumed to be compounded continuously.

````{panels}

The **future value** of an income stream is the total of all of the money transferred plus all of the interest earned.

---

The **present value** of an income stream is the principal investment, $P$, that yields the same future/accumulated value as the income stream when $P$ is invested for a period of $T$ years at the same rate of interest.
````


- $R(t)$ = rate at which income is generated (in dollars per year)
- $T$ = length of time (in years) of the income stream    
- $r$ = annual interest rate (compounded continuously)

```{admonition} Future Value Formula
:class: info

$$A = e^{rT}\int_0^T R(t) e^{-rt} ~dt$$
```

```{admonition} Present Value Formula
:class: info

$$PV = \int_0^T R(t) e^{-rt} ~dt$$
```

## Example 1

```{admonition} Compute future and present value of an investment
:class: tip

Suppose an investment is expected to generate income at the rate of 

$$R(t) = 5 + 3t$$

thousands of dollars per year for the next 10 years. Find the present and future values from this investment if the prevailing interest rate is 2\% per year compounded continuously.
```

```{dropdown} **Step 1:** Write the present and future values of the income stream as definite integrals.

$$PV = \int^{10}_0 \left( 5 + 3t \right)e^{-0.02t} ~dt ~~~~~~~ A = e^{0.2}\int^{10}_0 \left( 5 + 3t \right)e^{-0.02t} ~dt$$
```

```{dropdown} **Step 2:** Compute $\displaystyle \int \left( 5 + 3t \right)e^{-0.02t}~dt$ using integration by parts.

Pick $u$ and $dv$ and compute $du$ and $v$. (Recall $\int e^{ax} ~dx = \frac{1}{a}e^{ax}+C$.) 

\begin{align*}
  u &= 5 + 3t & dv &= e^{-0.02t}~dt \\
  du &= \frac{d}{dt}(5 + 3t) ~dt = 3~dt & v &= \int e^{-0.02t}~dt = -\frac{1}{0.02}e^{-0.02t} = -50e^{-0.02t}
\end{align*}

\begin{align*}
  \int \left( 5 + 3t \right)e^{-0.02t}~dt
  &= uv-\int v~du\\
  &= (5+3t)(-50e^{-0.02t}) - \int (-50 e^{-0.02t})3~dt\\
  &= -50(5+3t)e^{-0.02t} + 150\int e^{-0.02t}~dt && \hbox{simplify}\\
  &= -50(5+3t)e^{-0.02t} + 150(-50e^{-0.02t}) + C\\
  &= -50(155 + 3t)e^{-0.02t}+C
\end{align*}
```

```{dropdown} **Step 3:** Compute the present value using the answer to Step 2.

\begin{align*}
  PV 
  &= \int^{10}_0 \left( 5 + 3t \right)e^{-0.02t}dt\\
  &= -50(155 + 3t)e^{-0.02t}\Big|^{10}_{0} && \hbox{using Step 2}\\
  &= -50(185) e ^{-0.2} - (-50(155)e^{0})\\
  &= -9250e^{-0.2} + 7750 &&\hbox{since $e^0 = 1$}\\
  &\approx 176.74053  && \hbox{in thousands of dollars}
\end{align*}

Therefore, the present value of this income stream is approximately \$176,740.53.
```

```{dropdown} **Step 4:** Compute the future value using the answer to Step 3.

\begin{align*}
  A 
  &= e^{0.2}\int^{10}_0 \left( 5 + 3t \right)e^{-0.02t}dt\\
  &= e^{0.2}(-9250e^{-0.2} + 7750) && \hbox{using Step 3}\\
  &= -9250e^{0.2-0.2} + 7750e^{0.2}\\
  &= -9250e^{0} + 7750e^{0.2}\\
  &= -9250 + 7750e^{0.2} &&\hbox{since $e^0 = 1$}\\
  &\approx 215.87138 && \hbox{in thousands of dollars}
\end{align*}

Therefore, the future value of this income stream is approximately \$215,871.38.
```