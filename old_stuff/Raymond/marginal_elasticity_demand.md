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
# Elasticity of Demand

```{admonition} Definition
:class: info

The **price elasticity of demand** measures how sensitive customer demand is to a small percentage change in the price of a good.  Intuitively, elasticity is computed by the following ratio:

$$-\frac{\text{\% Change in Quantity Demanded}}{\text{\% Change in Price}}$$

Recall that the Law of Demand implies that a positive percent change in price will result in a negative percent change in demand.  Consequently, the negative sign appears in the formula for elasticity only to make sure that the final result will be a positive value.\\

If the price of the good is $p$ and the corresponding quantity demanded is $f(p)$, then the elasticity of demand at price $p$, $E(p)$, is defined by

\begin{align*}
  E(p) = -\frac{pf'(p)}{f(p)} %\label{elasticity}
\end{align*}
```

## Example 5

A store has determined that the demand for used lamps is given by

$$f(p) = 500 - 15p$$

where $p$ is the price (in dollars) of a lamp.  Find the price elasticity of demand, $E(p)$.

```{dropdown} **Step 1:** Compute $f'(p)$.

\begin{align*}
  f'(p) 
  &= \frac{d}{dp}(500 - 15p)\\ \\
  &= -15
\end{align*}
```

```{dropdown} **Step 2:** Compute $E(p)$.

\begin{align*}
  E(p) 
  &= -\frac{pf'(p)}{f(p)} \\ \\
  &= -\frac{p(-15)}{500 - 15p}\\ \\
  &= \frac{15p}{500 - 15p}    
\end{align*}
```

## Inelastic, Elastic, & Unitary Demand

Suppose $E(100) = 1/2$. This means that when the price is \$100, a 1\% increase in price (i.e., the price increases to \$101), will result in a 0.5\% decrease in demand. Or similarly, a 1\%  decrease in price (i.e., the price decreases to \$99), will result in a 0.5\% increase in demand. In this situation, the incentive is for the producer to increase their price.

```{admonition} Definition
:class: info

If $E(p) < 1$ (i.e., a percent change in price results in a smaller percent change in demand), then demand is said to be **inelastic**. 
```

Suppose $E(100) = 3$. This means that when the price is \$100, a 1\% increase in price will result in a 3\% decrease in demand. Or similarly, a 1\% decrease in price will result in a 3\% increase in demand. In this situation, the incentive is for the producer to reduce their price.

```{admonition} Definition
:class: info

If $E(p) > 1$ (i.e., a percent change in price results in a larger percent change in demand), then demand is said to be **elastic**. 
```

Suppose $E(100) = 1$. This means that when the price is \$100, a 1\% increase in price will result in a 1\% decrease in demand. Or similarly, a 1\% decrease in price will result in a 1\% increase in demand. In this situation, there is no incentive for the producer to change their price.

```{admonition} Definition
:class: info

If $E(p) = 1$ (i.e., a percent change in price results in the same percent change in demand), then demand is said to be **unitary**. 
```

## Example 6

A store has determined that the demand for used lamps is given by

$$f(p) = 500 - 15p$$

where $p$ is the price of a lamp. Compute $E(10)$ and $E(20)$ and interpret the results.

```{dropdown} **Step 1:** Recall the elasticity of demand found in Example 1.

$$E(p) = \frac{15p}{500 - 15p}$$
```

```{dropdown} **Step 2:** Evaluate $E(10)$ and interpret.

$$E(10) = \frac{150}{500 - 150} = \frac{150}{350} = \frac{3}{7}$$

Since $E(10) < 1$, demand is *inelastic* when the price of a lamp is \$10.
```

```{dropdown} **Step 3:** Evaluate $E(20)$ and interpret.

$$E(20) = \frac{300}{500 - 300} = \frac{300}{200} = \frac{3}{2}$$

Since $E(20) > 1$, demand is *elastic* when the price of a lamp is \$20.
```