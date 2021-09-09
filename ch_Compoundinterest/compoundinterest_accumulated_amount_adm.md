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
# Accumulated Amount Examples

## Example 1

Suppose $\$1000$ is deposited into an account with an interest rate of $16 \%$ compounded annually. How much money is in the account after $3$ years?

```{dropdown} **Step 1:** Since interest is compounded annually, use the accumulated amount for discrete compound interest.

$$A=P\left(1+\frac{r}{m}\right)^{mt}$$
```

```{dropdown} **Step 2:** Plug in the given values: $P = 1000$, $r = 0.16$, $m=1$, and $t = 3$.

\begin{align*}
  A
  &= 1000\left(1 + \frac{0.16}{1}\right)^{1\cdot 3} \\  \\
  &= 1000\left(1 + 0.16\right)^{3} \\  \\
  &= 1000\left(1.16\right)^{3} \approx \$1,560.90
\end{align*}
Therefore, after 3 years of accumulating interest, the original investment of \$1,000 is worth \$1,560.90.
```

## Example 2

Suppose $\$1000$ is deposited into an account with an interest rate of $16 \%$ compounded quarterly. How much money is in the account after $3$ years?

```{dropdown} **Step 1:** Since interest is compounded quarterly, use the accumulated amount for discrete compound interest.

$$A=P\left(1+\frac{r}{m}\right)^{mt}$$
```

```{dropdown} **Step 2:** Plug in the given values: $P = 1000$, $r = 0.16$, $m=4$, and $t = 3$.

\begin{align*}
  A
  &= 1000\left(1 + \frac{0.16}{4}\right)^{4\cdot 3} \\  \\
  &= 1000\left(1 + 0.04\right)^{12} \\ \\
  &= 1000\left(1.04\right)^{12} \approx \$1,601.03
\end{align*}

Therefore, after 3 years of accumulating interest, the original investment of \$1,000 is worth \$1,601.03.
```

```{admonition} Observation
:class: warning

Compare the accumulated amounts in the above two examples. Both examples have the same principal, interest rate, and term. But since interest is compounded more frequently in Example 2 (4 times a year) than in Example 1 (1 time a year), the accumulated amount is higher in Example 2.
```

## Example 3

Find the interest rate required for an investment of $ \$3000$ to double in value after 5 years if interest is compounded quarterly.

```{dropdown} **Step 1:** Since interest is compounded quarterly, use the accumulated amount for discrete compound interest.

$$A=P\left(1+\frac{r}{m}\right)^{mt}$$
```

```{dropdown} **Step 2:** Plug in the given values: $P=3000$, $A=6000$ (since the investment is to double in value), $m=4$, and $t=5$.

\begin{align*}
  6000 
  &= 3000\left(1 + \frac{r}{4} \right)^{4\cdot 5}\\
  &= 3000\left(1 + \frac{r}{4} \right)^{20}
\end{align*}
```

```{dropdown} **Step 3:** Solve for the interest rate, $r$.

**Method 1**

Divide both sides by 3000
$$2 = \left(1 + \frac{r}{4} \right)^{20}$$

Take the natural logarithm of both sides.

\begin{align*}
  \ln(2) 
  &= \ln\left[\left(1 + \frac{r}{4} \right)^{20}\right] \\
  &= 20\ln\left(1 + \frac{r}{4} \right) && \hbox{since $\ln(m^n) = n\ln(m)$}
\end{align*}

Divide both sides by 20.

$$\ln(2)/20 = \ln\left(1 + \frac{r}{4} \right)$$

Take the exponential of both sides.

\begin{align*}
  e^{\ln(2)/20} 
  &= e^{\ln\left(1 + \frac{r}{4} \right)} \\
  &= 1 + \frac{r}{4} && \hbox{since $e^{\ln(x)} = x$}
\end{align*}

Subtract 1 from both sides.

$$e^{\ln(2)/20} - 1  = \frac{r}{4} $$

And finally, multiply both sides by 4.

$$r = 4(e^{\ln(2)/20} - 1)  \approx  0.1411.$$

**Method 2**

Here is an alternate method for solving for the interest rate $r$. We start with the following equation.

$$2 = \left(1 + \frac{r}{4} \right)^{20}$$

Instead of taking the natural logarithm of both sides as we did before, now take the 20th root of both sides (i.e., raise both sides to the power of $1/20$).

$$2^{1/20} = 1 + \frac{r}{4}$$

Subtract 1 from both sides.

$$2^{1/20} - 1 = \frac{r}{4}$$

And finally, multiply both sides by 4.

$$r = 4(2^{1/20} - 1) \approx 0.1411$$

Note that this value of $r$ is numerically equal to the value we found previously since 

\begin{align*}
  e^{\ln(2)/20}
  &= e^{\ln(2^{1/20})} && \hbox{since $n\ln(m) = \ln(m^n)$} \\
  &= 2^{1/20} && \hbox{since $e^{\ln(x)} = x$}
\end{align*}

Therefore, an interest rate of approximately 14.11\% compounded quarterly is required for an investment of \$3000 to double in value in 5 years.
```

## Example 4

Find the interest rate required for an investment of $ \$3000$ to double in value after 5 years if interest is compounded continuously.

```{dropdown} **Step 1:** Since interest is compounded continuously, use the accumulated amount for continuous compound interest.

$$A=Pe^{rt}$$
```

```{dropdown} **Step 2:** Plug in the given values: $P=3000$, $A=6000$ (since the investment is to double in value), and $t=5$.

\begin{align*}
  6000 &= 3000e^{5r}
\end{align*}
```

```{dropdown} **Step 3:** Solve for the interest rate, $r$.

Divide both sides by 3000.

$$2 = e^{5r}$$

Take the natural logarithm of both sides.

\begin{align*}
  \ln(2)
  &= \ln(e^{5r}) \\
  &= 5r && \hbox{since $\ln(e^x) = x$}
\end{align*}

Divide both sides by 5.

$$r = \ln(2) / 5 \approx 0.1386$$

Therefore, an interest rate of approximately 13.86\% compounded continuously is required for an investment of \$3000 to double in value in 5 years.
```

```{admonition} Observation
:class: warning

Compare the last two examples. Since continuous compounding of interest earns interest faster than discrete compounding, a lower interest rate is needed for an investment to double in value over a fixed term if interest is compounded continuously. In our examples, an interest rate of 13.86\% was needed for the investment with continuous compound interest to double in value in 5 years, while an interest rate to 14.11\% was needed for the investment with quarterly compound interest.
```

## Example 5

How long will it take for $\$5000 $ to grow to $\$8000 $ if the investment earns interest at 6\% per year compounded monthly?

```{dropdown} **Step 1:** Since interest is compounded monthly, use the accumulated amount for discrete compound interest.

$$A=P\left(1+\frac{r}{m}\right)^{mt}$$
```

```{dropdown} **Step 2:** Plug in the given values: $P=5000$, $A=8000$, $m=12$, and $r=0.06$.

\begin{align*}
  8000 
  &= 5000\left(1 + \frac{0.06}{12} \right)^{12\cdot t}\\
  &= 5000\left(1 + 0.005 \right)^{12t}
\end{align*}
```

```{dropdown} **Step 3:** Solve for the unknown term $t$.

Divide both sides by 5000.

$$8/5 = 1.005^{12t}$$

Take the natural logarithm of both sides.

\begin{align*}
  \ln(8/5) 
  &= \ln(1.005^{12t}) \\ 
  &= 12t\ln(1.005) & \hbox{since $\ln(m^n) = n\ln(m)$}
\end{align*}

Divide both sides by $12\ln(1.005)$.

\begin{align*}
  t &= \frac{\ln(8/5)}{12\ln(1.005)} \approx 7.85
\end{align*}

Therefore, it will take approximately 7.85 years for \$5000 to grow to \$8000 if the investment earns interest at 6\% per year compounded monthly.
```

## Example 6

How long will it take for $\$5000 $ to grow to $\$8000 $ if the investment earns interest at 6\% per year compounded continuously?

```{dropdown} **Step 1:** Since interest is compounded continuously, use the accumulated amount for continuous compound interest.

$$A=Pe^{rt}$$
```

```{dropdown} **Step 2:** Plug in the given values: $P=5000$, $A=8000$, and $r=0.06$.

\begin{align*}
  8000 
  &= 5000e^{0.06t}
\end{align*}
```

```{dropdown} **Step 3:** Solve for the unknown term $t$.

Divide both sides by 5000.

$$8/5 = e^{0.06t}$$

Take the natural logarithm of both sides.

\begin{align*}
  \ln(8/5) 
  &= \ln(e^{0.06t}) \\
  &= 0.06t & \hbox{since $\ln(e^x) = x$}
\end{align*}

Divide both sides by $0.06$.

\begin{align*}
  t &= \frac{\ln(8/5)}{0.06} \approx 7.83
\end{align*}


Therefore, it will take approximately 7.83 years for \$5000 to grow to \$8000 if the investment earns interest at 6\% per year compounded monthly.
```

```{admonition} Observation
:class: warning

Compare the last two examples. Both examples have the same principal, accumulated amount, and interest rate. But since continuous compounding of interest earns interest faster than discrete compounding, it should take less time for the investment to grow to \$8000 if interest is compounded continuously.  
```

## Example 7

Find the effective interest rate corresponding to a nominal interest rate of $10\%$ compounded semiannually.

```{dropdown} **Step 1:** Recall the formula for effective interest rate, $r_{\text{eff}}$.

$$r_{\text{eff}}=\left(1+\frac{r}{m}\right)^m-1$$
```

```{dropdown} **Step 2:** Plug in the given values: $r = 0.1$ and $m=2$.

\begin{align*}
  r_{\text{eff}}
  &= \left(1+\frac{0.1}{2}\right)^2-1 \\
  &= 1.05^2 - 1 \\
  &= 0.1025
\end{align*}

Therefore, an investment earning interest compounded semiannually at 10\% earns the same amount of interest after 1 year as an investment earning simple interest at 10.25\%.
```

## Example 8

Suppose you have $\$12,000$ in the bank earning interest at a rate of $12\%$ compounded quarterly. Your cousin calls you and needs $\$12,000$ to buy a new car. You are willing him to loan him the money, but you'd hate to lose out on the interest you would gather by simply leaving your money alone. If you charge your cousin an interest rate compounded continuously, what rate should you charge in order to earn the same amount of interest you otherwise would have?

```{dropdown} **Step 1:** Assume your cousin is prepared to pay you back after $t$ years.

We'll use $t$ as the term in each of the following calculations. Eventually, we'll see that the interest rate you charge does not depend on the specific value of $t$.
```

```{dropdown} **Step 2:** Compute the accumulated amount of the $\$12,000$ after $t$ years assuming you leave your money in the bank.

\begin{align*}
  A 
  &= P\left(1 + \frac{r}{m}\right)^{m\cdot t} \\
  &= 12000 \left( 1 + \frac{0.12}{4} \right)^{4t}  \\
  &= 12000 \left( 1.03 \right)^{4t}
\end{align*}
```

```{dropdown} **Step 3:** Compute the accumulated amount of the $\$12,000$ after $t$ years assuming you let your cousin borrow the money.

This would be the amount that your cousin repays you after $t$ years.

\begin{align*}
  A 
  &= Pe^{rt}\\
  &= 12000e^{rt}
\end{align*}
```

```{dropdown} **Step 4:** Equate the two accumulated amounts and solve for $r$.

$$12000\left(1.03\right)^{4t} = 12000e^{rt}$$

Divide both sides by $12000$.

$$1.03^{4t} = e^{rt}$$

Take the natural logarithm of both sides.

$$\ln(1.03^{4t}) = \ln(e^{rt})$$

Simplify using properties of logarithms ($\ln(m^n) = n\ln(m)$ and $\ln(e^x) = x$).

$$4t\ln(1.03) = rt$$

And finally, divide both sides by $t$. Here is where we see that the time it would take your cousin to repay you does not affect the interest rate you would charge.

$$r = 4\ln(1.03) \approx 0.1182$$

Therefore, charging your cousin 11.82\% interest compounded continuously earns the same amount of interest as leaving your money in the bank earning interest at a rate of 12\% compounded quarterly.
```