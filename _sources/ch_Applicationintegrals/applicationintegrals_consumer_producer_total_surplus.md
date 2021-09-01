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
# Consumer, Producer, & Total Surplus


## Consumer Surplus

Consumer surplus is the difference between what customers are willing to pay for a product and what they actually pay. 

```{admonition} Definition
:class: info

For a given demand function, $D(x)$, if $\bar{x}$ is the quantity demanded and $\bar{p}$ is unit market price, then **consumer surplus**, $CS$, is given by:

$$CS  = \int^{\bar{x}}_0 D(x)-\bar{p} ~dx = \int_0^{\bar{x}} D(x)~dx - \bar{p}\bar{x}.$$
```

Consumer surplus can also be interpreted as the area of the region between the demand curve and the horizontal line $p=\bar{p}$ on the interval $[0,\bar{x}]$.

```{figure} ../images/pic_applicationintegrals_consumer_producer_total_1.png
---
width: 600px
---
Consumer surplus
```


## Producer Surplus

Producer surplus is the difference between what sellers receive for their product and what they are willing to receive.

```{admonition} Definition
:class: info

For a given supply function, $S(x)$, if $\bar{x}$ is the quantity demanded and $\bar{p}$ is unit market price, then **producer surplus**, $PS$, is given by:

$$PS = \int^{\bar{x}}_0 \bar{p}-S(x) ~dx  =  \bar{p}\bar{x} - \int_0^{\bar{x}} S(x) ~dx.$$
```


Producer surplus can also be interpreted as the area of the region between the supply curve and the horizontal line $p=\bar{p}$ on the interval $[0,\bar{x}]$.

```{figure} ../images/pic_applicationintegrals_consumer_producer_total_2.png
---
width: 600px
---
Producer surplus
```

## Example 1

```{admonition} Determining surplus at market equilibrium using geometry
:class: tip

The demand function for PSL's {\it Calculus on Demand} video series is $p = D(x) = -3x+44$ and the corresponding supply function is $p=S(x) = 4x+2$. Determine the consumer and producer surplus at the market equilibrium values by finding the area of the corresponding region between two curves.
```

```{dropdown} **Step 1:** Find the market equilibrium values.

\begin{align*}
  4x+2 &= -3x+44 && \hbox{Set $S(x) = D(x)$} \\
  4x &= -3x+42 && \hbox{Subtract $2$ from both sides} \\
  7x &= 42 && \hbox{Add $3x$ to both sides} \\
  x &= 6 && \hbox{Divide both sides by $7$} 
\end{align*}

Therefore, the equilibrium quantity is $\bar{x} = 6$ and the equilibrium price is

$$\bar{p} = D(6) = S(6) = 26.$$
```

````{dropdown} **Step 2:** Calculate the consumer surplus.

Consumer surplus at the market equilibrium is the area of the region between the demand curve, $p=-3x+44$, and the horizontal line $p = 26$ on the interval $[0,6]$.

Since the above region is a triangle, its area (i.e., the consumer surplus) can be calculuated using the formula for the area of a triangle (i.e., $\frac{1}{2}\cdot\hbox{base} \cdot \hbox{height}$).

$$CS = \frac{1}{2}\cdot 6\cdot (44-26) = 3\cdot 18 = 54$$

```{image} ../images/pic_applicationintegrals_consumer_producer_total_3.png
---
alt: Consumer surplus as area
width: 500px
align: center
---
```
````

````{dropdown} **Step 3:** Calculate the producer surplus.

Producer surplus at the market equilibrium is the area of the region between the supply curve, $p=4x+2$, and the horizontal line $p = 26$ on the interval $[0,6]$.

Since the above region is a triangle, its area (i.e., the producer surplus) can be calculuated using the formula for the area of a triangle (i.e., $\frac{1}{2}\cdot\hbox{base} \cdot \hbox{height}$).

$$PS = \frac{1}{2}\cdot  6\cdot (26-2) = 3\cdot 24 = 72$$

```{image} ../images/pic_applicationintegrals_consumer_producer_total_4.png
---
alt: Producer surplus as area
width: 500px
align: center
---
```
````

## Total Surplus

Total surplus is the sum of the consumer and the producer surpluses.

```{admonition} Definition
:class: info

For given demand and supply functions, $D(x)$ and $S(x)$, if $\bar{x}$ is the quantity demanded, then **total surplus**, $TS$, is given by:

$$TS = CS + PS = \int_0^{\bar{x}} D(x) - S(x) ~dx$$
```

Total surplus can also be interpreted as the area of the region between the demand curve and the supply curve on the interval $[0,\bar{x}]$.

Total surplus is maximized at the equilibrium quantity.

```{figure} ../images/pic_applicationintegrals_consumer_producer_total_5.png
---
width: 600px
---
Total surplus
```


## Example 2

```{admonition} Determining total surplus
:class: tip

Continuing with Example 1, determine the total surplus at the equilibrium quantity by finding the area of the corresponding region between two curves.
```

````{dropdown} **Step 1:** Calculate the total surplus.

Total surplus at the market equilibrium is the area of the region between the demand curve, $p=-3x+44$, and the supply curve, $p=4x+2$, on the interval $[0,6]$.

Since the above region is a triangle, its area (i.e., the total surplus) can be calculuated using the formula for the area of a triangle (i.e., $\frac{1}{2}\cdot\hbox{base} \cdot \hbox{height}$).

$$TS = \frac{1}{2}\cdot 6 \cdot (44-2) = 3\cdot 42 = 126$$

The total surplus can also be calculated as the sum of the consumer and producer surpluses that were calculated in Example 1.

$$TS = CS + PS = 54 + 72 = 126$$

```{image} ../images/pic_applicationintegrals_consumer_producer_total_6.png
---
alt: Total surplus as area
width: 500px
align: center
---
```
````


## Example 3

```{admonition} Determining surplus using integration
:class: tip

The quantity demanded for computer chips is given by 

$$p = 225-x^2$$

where $x$ is the quantity demanded (in hundreds of chips per week), and $p$ is the price of a single chip (in dollars).  The manufacturer will make $x$ units available to the market each week if 

$$p = 100+\frac{x^2}{4}$$

Determine the consumer and producer surplus at the market equilibrium values.
```

```{dropdown} **Step 1:** Find the market equilibrium values.

\begin{align*}
  100+\frac{x^2}{4} &= 225 -x^2  && \text{Set $S(x) = D(x)$}\\
    \frac{5}{4}x^2 &= 125  && \hbox{Add $x^2$ and subtract $100$ from both sides}\\
  x^2&= 100 && \hbox{Mulitply both sides by $4/5$}\\ 
  x&= 10 && \text{Take the square root of both sides,  $x\geq 0$} 
\end{align*}

Therefore, the equilibrium quantity is $\bar{x} = 10$ and the equilibrium price is

$$\bar{p} = D(10) = S(10) = 125.$$
```

```{dropdown} **Step 2:** Calculate the consumer surplus.

Recall the formula for consumer surplus:

$$CS  = \int^{\bar{x}}_0 D(x)-\bar{p} ~dx = \int_0^{\bar{x}} D(x)~dx - \bar{p}\bar{x}$$


\begin{align*}
  CS &= \int_0^{\bar{x}} D(x) ~dx-\bar{p}\bar{x} && \text{Use the formula for consumer surplus}\\
  &= \int^{10}_0 225-x^2 ~dx - 10\cdot 125\\
  &= \left(225x-\frac{x^3}{3}\right)\Biggr|^{10}_0-1250\\
  &= \left(2250 - \frac{1000}{3}\right) - (0-0) - 1250\\
  &= 2000/3
\end{align*}

Since the units of $x$ are *hundreds* of chips and $p$ is the price of a single chip we need to multiply this result by $100$ to correctly interpret the consumer surplus in dollars. Therefore, the consumer surplus is 

$$100\cdot \frac{2000}{3} \approx \$66,666.67.$$
```

```{dropdown} **Step 3:** Calculate the producer surplus.

Recall the formula for producer surplus.

$$PS = \int^{\bar{x}}_0 \bar{p}-S(x) ~dx  =  \bar{p}\bar{x} - \int_0^{\bar{x}} S(x) ~dx$$

\begin{align*}
  PS 
  &=\bar{p}\bar{x}- \int^{\bar{x}}_0S(x)~dx && \text{Use the formula for producer surplus}\\
  &= 10\cdot 125 - \int^{10}_0 100+\frac{x^2}{4} ~dx \\
  &= 1250 - \left(100x+\frac{x^3}{12}\right)\Biggr|^{10}_0\\
  &= 1250 - \left[\left(1000 + \frac{1000}{12}\right) - (0+0)\right] \\
  &= 500/3
\end{align*}

Since the units of $x$ are *hundreds* of chips and $p$ is the price of a single chip we need to multiply this result by $100$ to correctly interpret the producer surplus in dollars. Therefore, the producer surplus is 

$$100\cdot \frac{500}{3} \approx \$16,666.67.$$
```

## Example 4

```{admonition} Determining surplus using integration
:class: tip

The supplier of a custom pen will make $x$ units of pens available to the market when the wholesale unit price is $p = \sqrt{9+2x}$ where $p$ is in dollars. Determine the producer surplus when the market unit price is set to \$5 a unit.
```

```{dropdown} **Step 1:** Determine the quantity supplied when the market price is \$$5$.

\begin{align*}
  \sqrt{9+2x} &= 5  && \text{Find the units supplied at \$5 a unit}\\
  9+2x &= 25 && \hbox{Square both sides}\\
  2x&= 16 && \hbox{Subtract 9 from both sides}\\
  x&= 8 && \hbox{Divide both sides by 2}
\end{align*}
```

```{dropdown} **Step 2:** Setup the producer surplus as a definite integral.

\begin{align*}
  PS &= \bar{p}\bar{x}- \int^{\bar{x}}_0 S(x) ~dx\\
  &= 5 \cdot 8 - \int_0^{8} \sqrt{9+2x} ~dx\\
  &= 40 - \int_0^{8} (9+2x)^{1/2} ~dx\\
\end{align*}
```

```{dropdown} **Step 3:** Evaluate $\displaystyle \int_0^{8} (9+2x)^{1/2} ~dx$ using substitution.

Use $u-$substitution

\begin{align*}
  u &= 9+2x \\
  du &= 2~dx &&  \left(\hbox{or equivalently, } \frac{1}{2} du = dx\right)
\end{align*}

Compute the new limits of integration using the equation $u = 9+2x$.

\begin{align*}
  x=8 ~~&\Longrightarrow~~ u = 9 + 2(8) = 25\\
  x=0 ~~&\Longrightarrow~~ u = 9 + 2(0) = 9
\end{align*}

Evaluate the integral.
\begin{align*}
  \int_0^{8} (9+2x)^{1/2} ~dx
  &= \int_{9}^{25} u^{1/2}\frac{1}{2} ~du && \hbox{Apply the substitution}\\
  &= \frac{1}{2}\int_{9}^{25} u^{1/2} ~du && \hbox{Constant multiple rule}\\
  &= \frac{1}{2} \cdot \frac{2}{3} u^{3/2}\Biggr|_{9}^{25} && \hbox{Power rule}\\
  &= \frac{1}{3} u^{3/2}\Biggr|_{9}^{25} && \hbox{Simplify}\\
  &= \frac{1}{3} \left(25^{3/2} - 9^{3/2}\right) && \hbox{Plug in limits of integration}\\
  &= \frac{1}{3} \left(5^{3} - 3^{3}\right) && \hbox{Simplify}\\
  &= \frac{1}{3} \left(125 - 27\right)\\
  &= 98/3
\end{align*}
```

```{dropdown} **Step 4:** Complete the computations for the producer surplus.

\begin{align*}
  PS 
  &= 40 - \int_0^{8} (9+2x)^{1/2} ~dx\\
  &= 40 - \frac{98}{3} && \hbox{Using result from Step 3}\\
  &= 22/3  \\
  &\approx \$7.33
\end{align*}

Therefore, the producer surplus is approximately \$7.33 when the unit price is \$5.
```