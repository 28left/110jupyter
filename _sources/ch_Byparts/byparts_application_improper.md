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
# Application of Improper Integrals

## Perpetuity

```{panels}

A **perpetuity** is an annuity (i.e., a sequence of payments made at regular intervals) in which the periodic payments begin at a fixed date and continue indefinitely.

- $P=$ the size of each payment
- $r$ = annual interest rate (compounded continuously)
- $m=$ the number of payments per year

---

|Annually|Semiannually|Quarterly|
| :---: | :---: | :---: |
|$m=1$|$m=2$|$m=4$|

|Monthly|Weekly|Daily|
| :---: | :---: | :---: |
|$m=12$|$m=52$|$m=365$|

```

By taking the present value formula for an income stream (see page 7) with $R(t) = mP$ and letting the term $T$ go to infinity (i.e., evaluating the improper integral $\int_0^\infty mPe^{-rt} ~dt$), we arrive at the following formula for the present value of a perpetuity.

```{admonition} Present Value of a Perpetuity
:class: info

$$PV = \frac{mP}{r}$$
```

## Example 1

```{admonition} Computing the funds necessary for an endowment
:class: tip

A group wishes to provide a semiannual math scholarship in the amount of \$6,000 beginning in six months. If the fund will earn 4\% interest per year compounded continuously, find the amount of the endowment the group is required to make now.
```

```{dropdown} **Step 1:** Recall the formula for the present value of a perpetuity.

$$PV = \frac{mP}{r}$$
```

```{dropdown} **Step 2:** Plug in the given values: $m=2$, $P=6000$, and $r=0.04$. 

\begin{align*}
  PV
  &= \frac{2(6000)}{0.04}\\
  &= \frac{12000}{4/100}\\
  &= \frac{12000(100)}{4}\\
  &= 3000(100) \\
  &= 300000
\end{align*}

Therefore, a single payment of \$300,000 is required to fund the scholarship indefinitely.
```