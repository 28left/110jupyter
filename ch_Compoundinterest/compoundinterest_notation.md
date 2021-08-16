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
# Notation and Terminology

```{admonition} Basic Notation and Terminology
:class: info

- $P = $ Principal (i.e., value of initial deposit)
- $A = $ Accumulated amount (i.e., sum of the principal and interest)
- $r = $ Nominal interest rate
- $m = $ Number of conversion periods per year, (a conversion period is the interval of time between successive interest payments)

|Annually|Semiannually|Quarterly|Monthly|Weekly|Daily
| :---: | :---: | :---: | :---: | :---: | :---:
|$m=1$|$m=2$|$m=4$|$m=12$|$m=52$|$m=365$

- $t = $ Term of investment (in years)
```

```{admonition} Simple Interest
:class: info

Interest is always computed based on the original principal.

|Interest Earned|Accumulated Amount
| :---: | :---: 
|$I = Prt$| $A = P(1 + rt)$
```

```{admonition} Discrete Compound Interest
:class: info

Interest payments are added to the principal at the end of each conversion period and therefore earn interest during future conversion periods.

|Accumulated Amount|Present Value Formula
| :---: | :---: 
|$A = P \left(1 + \frac{r}{m}\right)^{mt}$| $P = A\left(1 + \frac{r}{m}\right)^{-mt}$
```

```{admonition} Continuous Compound Interest
:class: info

Continuous compounding of interest is equivalent to a discrete compounding of interest where $m$, the number of conversion periods per year, goes to infinity.

|Accumulated Amount|Present Value Formula
| :---: | :---: 
|$A = Pe^{rt}$| $P = Ae^{-rt}$
```

```{admonition} Effective Rate of Interest
:class: info

The effective interest rate, $r_{\text{eff}}$, is the simple interest rate that produces the same accumulated amount in 1 year as the nominal rate, $r$, compounded $m$ times a year.

$$r_{\text{eff}}=\left(1+\frac{r}{m}\right)^m-1$$
```


