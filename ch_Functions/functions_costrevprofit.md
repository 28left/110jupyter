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
# Cost, Revenue, and Profit

## Definitions

```{admonition} Definition
:class: info

The _**total cost function**_, $C(x)$ measures the costs incurred from operating a business and is defined by

$$C(x) = F(x) + V(x)$$

where $F(x)$ denotes the fixed costs  (i.e., costs that remain the same regardless of the level of production $x$) and $V(x)$ denotes the variable costs (i.e., costs that vary depending on the level of production $x$) of operating a business.
```


```{admonition} Definition
:class: info

The _**average cost function**_, $\overline{C}(x)$, measures the average cost per unit produced and is defined by

$$\overline{C}(x) = \frac{C(x)}{x}.$$
```



```{admonition} Definition
:class: info

The _**total revenue function**_, $R(x)$, measures the amount of money received from the sale of $x$ units and is defined by

$$R(x) = x\cdot p(x)$$

where $x$ is the number of units demanded and $p(x)$ is the unit price.
```


```{admonition} Definition
:class: info

The _**average revenue function**_, $\overline{R}(x)$, measures the average amount of money received per unit sold and is defined by

$$\overline{R}(x) = \frac{R(x)}{x}.$$
```



```{admonition} Definition
:class: info

The _**total profit function**_, $P(x)$ measures the difference between the total revenue and total cost functions and is defined by

$$P(x) = R(x) - C(x)$$

where $R(x)$ is the total revenue function and $C(x)$ is the total cost function.
```

```{admonition} Definition
:class: info

The _**average profit function**_, $\overline{P}(x)$, measures the average profit earned per unit produced and sold and is defined by

$$\overline{P}(x) = \frac{P(x)}{x}.$$
```



```{admonition} Definition
:class: info

The _**break-even point**_ refers to the value of $x$ where the total revenue from the sale of $x$ units equals the total cost of producing $x$ units.  In other words, the break-even point is the value of $x$ such that 

$$R(x) = C(x)$$

or equivalently,

$$P(x) = 0.$$
```


### Example 1
````{admonition} Find cost, revenue, profit, and break-even point.
:class: tip

A manufacturer of wireless security cameras has fixed monthly costs of \$10,000 and a processing cost of \$49 for each camera produced. Assuming each camera sells for \$99, compute the break-even point.


```{dropdown} **Step 1:** &nbsp; Compute the total cost function, &nbsp; $C(x)$.
 
Here $x$ denotes the number of cameras produced.

\begin{align*}
C(x) &= F(x) + V(x) && \text{total cost equals fixed costs plus variable costs}\\
&= 10000  + 49x && \hbox{\$10,000 of fixed costs and \$49 for each camera}
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Compute the total revenue function, &nbsp; $R(x)$.

\begin{align*}
    R(x) &= x \cdot p(x) && \text{revenue equals number of units times price per unit}\\
    &= 99x && \hbox{since each camera sells for \$99}
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Compute the total profit function, &nbsp; $P(x)$.

\begin{align*}
    P(x) &= R(x) - C(x) && \text{profit equals revenue minus cost}\\
    &= 99x - ( 10000 + 49x) && \text{using Steps 1 and 2}\\
    &= 99x - 10000 - 49x \\
    &= 50x - 10000 && 
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Compute the break-even point.

\begin{align*}
P(x) = 0 
&~~\rightarrow~~ 50x - 10000 = 0 \\
&~~\rightarrow~~ 50x = 10000 \\
&~~\rightarrow~~ x = \frac{10000}{50} = 200
\end{align*}

Therefore, the break-even point is 200 cameras.
```
````