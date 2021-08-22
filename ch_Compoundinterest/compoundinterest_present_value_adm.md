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
# Present Value Examples

## Example 9

How much money should be deposited in a bank paying a yearly interest rate of $6\%$ compounded monthly so that after 3 years, the accumulated amount will be \$20,000?

```{admonition} Step 1: Notice that this is a present value problem since we're given the accumulated amount and we're asked to find the principal.
:class: tip, dropdown

And since interest is compounded monthly, we'll use the present value formula for discrete compounding of interest.

$$P = A\left(1 + \frac{r}{m}\right)^{-mt}$$
```

```{admonition} Step 2: Plug in the given values: $A = 20000$, $r = 0.06$, $m=12$, and $t=3$.
:class: tip, dropdown

\begin{align*}
  P
  &=20000\left(1+\frac{0.06}{12}\right)^{-(12)(3)}\\ \\
  &=20000(1.005)^{-36} \approx \$16,712.90
\end{align*}

Therefore, \$16,712.90 invested at 6\% interest compounded monthly will be worth \$20,000 in 3 years.
```

## Example 10

Use the accumulated amount for discrete compound interest to solve the previous example.

```{admonition} Step 1: Start with the formula for accumulated amount for discrete compounding of interest.
:class: tip, dropdown

$$A = P\left( 1 + \frac{r}{m}\right)^{mt}$$
```

```{admonition} Step 2: Plug in the given values: $A = 20000$, $r = 0.06$, $m=12$, and $t=3$.
:class: tip, dropdown

\begin{align*}
  20000 
  &= P\left(1+\frac{0.06}{12}\right)^{(12)(3)}\\
  &=P(1.005)^{36}
\end{align*}
```

```{admonition} Step 3: Solve for $P$.
:class: tip, dropdown

\begin{align*}
  P  = \frac{20000}{1.005^{36}} \approx \$16,712.90
\end{align*}
```

## Example 11

Parents wish to establish a trust fund for their child's education. If they need \$170,000 in 7 years, how much should they set aside now if the money is invested at $20\%$ compounded continuously?

```{admonition} Step 1: Notice that this is a present value problem since we're given the accumulated amount and we're asked to find the principal.
:class: tip, dropdown

And since interest is compounded continuously, we'll use the present value formula for continuous compounding of interest.

$$P = Ae^{-rt}$$
```

```{admonition} Step 2: Plug in the given values: $A = 170000$, $r = 0.2$, and $t=7$.
:class: tip, dropdown

\begin{align*}
  P 
  &=170,000e^{-(0.2)(7)}\\ \\
  &=170,000e^{-1.4} \approx {\$41,921.48}
\end{align*}

Therefore, \$41,921.48 invested at 20\% interest compounded continuously will be worth \$170,000 in 7 years.
```

## Example 12

Use the accumulated amount for continuous compound interest to solve the previous example.

```{admonition} Step 1: Start with the formula for accumulated amount for continuous compounding of interest.
:class: tip, dropdown

$$A = Pe^{rt}$$
```

```{admonition} Step 2: Plug in the given values: $A = 170000$, $r = 0.2$, and $t=7$.
:class: tip, dropdown

\begin{align*}
  170000 
  &= Pe^{(0.2)(7)}\\
  &= Pe^{1.4}
\end{align*}
```

```{admonition} Step 3: Solve for $P$.
:class: tip, dropdown

\begin{align*}
  P 
  &= \frac{170000}{e^{1.4}} \approx \$41,921.48
\end{align*}
```