---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3.9 64-bit
  language: python
  name: python3
---
# Demand and Supply

```{admonition} Definition
:class: info

**Demand** refers to the quantity of goods or services that consumers are willing to purchase at a given price.
```


````{panels}
The Law of Demand assumes
- all factors affecting purchasing except price are held constant,
- if price goes up, then consumers buy less, and
- if price goes down, then consumers (are incentivized) to buy more.

The demand curve, $p = d(x)$, shows the quantity demanded, $x$, at each price, $p$, and the Law of Demand dictates it is a decreasing function.

---

```{image} ../images/pic_functions_demand.png
:alt: Demand function
:width: 300px
:align: center
```

````



```{admonition} Definition
:class: info

**Supply** refers to the amount of goods that producers want to sell at a given price.
```


````{panels}
The Law of Supply assumes
- all factors affecting supply except price are held constant, 
- if price goes up, then suppliers (are incentivized) to produce more, and  
- if price goes down, then suppliers produce less. 

The supply curve, $p = s(x)$, shows the quantity supplied, $x$, at each price, $p$, and the Law of Supply dictates it is an increasing function.

---

```{image} ../images/pic_functions_supply.png
:alt: Supply function
:width: 300px
:align: center
```

````


```{admonition} Domain Considerations
:class: info

For any demand or supply function, the domain should be restricted so that both the quantity $x$ and price $p$ are nonnegative (i.e., $x\geq 0$ and $p\geq 0$).  
```


## Example 1

Determine the appropriate domain for the demand function, $d(x) = 600 - 15x$.

```{dropdown} **Step 1:** Find the values of $x\geq 0$ such that $p = d(x) \geq 0$.

\begin{align*}
600 - 15x \geq 0 
~~&\rightarrow~~ 600 \geq 15x \\ 
~~&\rightarrow~~ 40 \geq x
\end{align*}
```



## Market Equilibrium

```{admonition} Definition
:class: info

A **market equilibrium** exists when the quantity produced is equal to the quantity demanded.
```

The market equilibrium quantity and price can be determined by finding the point of intersection of the demand and supply curves.

```{figure} ../images/pic_functions_equilibrium.png
---
name: illustration-equilibrium
alt: The equilibrium is given where demand and supply curves intersect
width: 600px
---
The market equilibrium is given where demand and supply curves intersect
```



## Example 2

The demand and supply functions for Penn State Berkey Creamery Gift Boxes are: 

\begin{align*}
p = d(x) &= -x^2 - x + 72\\
p = s(x) &= 2x + 32
\end{align*}

where $x$ is the number of thousands of boxes and $p$ is in dollars.  Determine the market equilibrium values.

```{dropdown} **Step 1:** Determine the equilibrium quantity.

Since both demand and supply are written as functions of $x$, we'll first solve for the equilibrium quantity by setting the two functions equal to each other. 

$$-x^2 - x + 72 = 2x + 32$$

Adding $x^2+x-72$ to both sides and factoring yields

\begin{align*}
0 
&= x^2 + 3x -40 \\
&= (x+8)(x-5)
\end{align*}

which is equal to zero when $x=-8$ or when $x=5$.  But since $x$ must be nonnegative, the equilibrium quantity corresponds to $x=5$, which is 5000 boxes.
```



```{dropdown} **Step 2:** Determine the equilibrium price.

Evaluate demand and supply functions at $x=5$ to compute the equilibrium price.

\begin{align*}
d(5) 
&= -5^2 - 5 + 72 \\
&= -25 - 5 + 72 \\
&= 42
\end{align*}

\begin{align*}
s(5) 
&= 2(5) + 32 \\
&= 10 + 32 \\
&= 42
\end{align*}

Therefore, the equilibrium price is 42 dollars.
```
