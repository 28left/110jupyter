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
# Income Streams & Annuities

## Income Streams

An **income stream** refers to income that is generated continuously and transferred into an account that earns interest at a fixed rate. Interest is assumed to be compounded continuously.

```{panels}

The **future value** of an income stream is the total of all of the money transferred plus all of the interest earned.

---

The **present value** of an income stream is the principal investment, $P$, that yields the same future/accumulated value as the income stream when $P$ is invested for a period of $T$ years at the same rate of interest.
```

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

## Annuities

````{panels}

An **annuity** is a sequence of payments made at regular intervals. 

- $P=$ the size of each payment
- $T=$ length of time (in years) that payments are made
- $r$ = annual interest rate (compounded continuously)
- $m=$ the number of payments per year

---

|Annually|Semiannually|Quarterly|
| :---: | :---: | :---: |
|$m=1$|$m=2$|$m=4$|

|Monthly|Weekly|Daily|
| :---: | :---: | :---: |
|$m=12$|$m=52$|$m=365$|

````


The following formulas for the amount and present value of an annuity are based on treating an annuity as an income stream where $R(t) = mP$.

```{admonition} Amount of an Annuity
:class: info

$$A = \frac{mP}{r}\left(e^{rT} - 1\right)$$
```

```{admonition} Present Value of an Annuity
:class: info

$$PV = \frac{mP}{r}\left(1 - e^{-rT}\right)$$
```

## Example 1

```{admonition} Future value of an income stream
:class: tip

Penn State Learning is expected to generate \$3,000 a year for the next 2 years from the sales of its *Calculus on Demand* iOS app.  Assuming the income is invested at an interest rate of 5\%, what is the future value of this income stream?
```

```{dropdown} **Step 1:** Recall the formula for the future value of an income stream.

$$A = e^{rT} \int_0^T R(t) e^{-rt} ~dt$$
```

```{dropdown} **Step 2:** Plug in the given values: $R(t)=3000$, $r=0.05$, and $T=2$. 

\begin{align*}
  e^{0.05(2)}\int_0^2 3000e^{-0.05t}~dt
  &= 3000 e^{0.1}\int_0^2 e^{-0.05t}~dt && \hbox{Constant multiple rule}\\
  &= 3000 e^{0.1} \left(\frac{e^{-0.05t}}{-0.05}\right)\Biggr|^{2}_{0} && \hbox{Since $\displaystyle \int e^{ax} ~dx  = \dfrac{e^{ax}}{a} + C$} \\
  &= 3000 e^{0.1} \left(\frac{e^{-0.05(2)}}{-0.05} - \frac{e^{-0.05(0)}}{-0.05}\right) && \hbox{Plug in limits of integration}\\
  &= 3000 e^{0.1} \left(\frac{e^{-0.1}}{-0.05} + \frac{1}{0.05}\right) && \hbox{Since $e^0 = 1$}\\
  &= 60000 e^{0.1} \left(1- e^{-0.1}\right) && \hbox{Since $\frac{1}{0.05} = \frac{1}{5/100} = \frac{100}{5} = 20$}\\
  &\approx \$6,310.26 
\end{align*}
```

## Example 2

```{admonition}  Present value of an investment
:class: tip

An investment is expected to generate income at a rate of \$300,000 per year for the next 6 years. Find the present value of this investment if the interest rate is 10\% compounded continuously. 
```

```{dropdown} **Step 1:** Recall the formula for the present value of an income stream.

$$PV = \int_0^T R(t) e^{-rt} ~dt$$
```

```{dropdown} **Step 2:** Plug in the given values: $R(t)=300000$, $r=0.1$, and $T=6$. 

\begin{align*}
  \int_0^6 300000e^{-0.1t} ~dt
  &= 300000 \int_0^6 e^{-0.1t} ~dt && \hbox{Constant multiple rule}\\
  &= 300000 \left(\frac{e^{-0.1t}}{-0.1}\right)\Biggr|^6_0 && \hbox{Since $\displaystyle \int e^{ax} ~dx  = \dfrac{e^{ax}}{a} + C$}\\
  &= 300000 \left(\frac{e^{-0.1(6)}}{-0.1}-\frac{e^{-0.1(0)}}{-0.1}\right) && \hbox{Plug in limits of integration}\\
  &= 300000 \left(\frac{e^{-0.6}}{-0.1}+\frac{1}{0.1}\right) && \hbox{Since $e^0 = 1$}\\
  &= 3000000\left(1- e^{-0.6}\right) && \hbox{Since $\frac{1}{0.1} = \frac{1}{1/10}=10$}\\
  &\approx \$1,353,565.09
\end{align*}
```

## Example 3

```{admonition} Amount of an annuity 
:class: tip

A Math 110 student decides to make semiannual payments of \$2,500 into a retirement account paying 2\% interest per year compounded continuously. How much will the student have in their retirement account after 20 years?
```

```{dropdown} **Step 1:** Recall the formula for the amount of an annuity.

$$A = \frac{mP}{r}\left(e^{rT} - 1\right)$$
```

```{dropdown} **Step 2:** Plug in the given values: $m=2$, $P=2500$, $r=0.02$, and $T=20$. 

\begin{align*}
  \frac{(2)(2,500)}{0.02} \left(e^{(0.02)(20)}-1 \right)
  &= \frac{5000}{2/100}\left( e^{0.4}-1\right)\\
  &= \frac{100}{2}\cdot 5000\left( e^{0.4}-1\right)\\
  &= 50\cdot 5000\left( e^{0.4}-1\right)\\
  &= 250000\left( e^{0.4}-1\right)\\
  &\approx \$122,956.17
\end{align*}

Therefore, the student will have approximately \$122,956.17 in their retirement account after 20 years.
```

## Example 4

```{admonition} Present value of an annuity
:class: tip

Determine the present value of an annuity if payments of \$100 are made monthly for the next 10 years and the account earns an interest rate of 10\% per year compounded continuously.
```

```{dropdown} **Step 1:** Recall the formula for the present value of an annuity.

$$PV = \frac{mP}{r}\left(1 - e^{-rT}\right)$$
```

```{dropdown} **Step 2:** Plug in the given values: $m=12$, $P=100$, $r=0.1$, and $T=10$. 

\begin{align*}
  \frac{(12)(100)}{0.1} \left(1-e^{-(0.1)(10)} \right)
  &=\frac{1200}{1/10} \left(1-e^{-1} \right)\\
  &=10\cdot 1200 \left(1-e^{-1} \right)\\
  &=12000\left( 1-e^{-1}\right)\\
  &\approx \$7,585.45
\end{align*}

Therefore, the annuity is worth a single lump sum of money worth approximately \$7,585.45.
```
