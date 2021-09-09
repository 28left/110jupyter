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
# Cost, Revenue, & Profit

## Total Cost & Average Cost Functions

```{admonition} Definition
:class: info

The **total cost function**, $C(x)$ measures the costs incurred from operating a business and is defined by

$$C(x) = F(x) + V(x)$$

where $F(x)$ denotes the fixed costs  (i.e., costs that remain the same regardless of the level of production $x$) and $V(x)$ denotes the variable costs (i.e., costs that vary depending on the level of production $x$) of operating a business.
```


```{admonition} Definition
:class: info

The **average cost function**, $\overline{C}(x)$, measures the average cost per unit produced and is defined by

$$\overline{C}(x) = \frac{C(x)}{x}.$$
```




## Total Revenue & Average Revenue Functions


```{admonition} Definition
:class: info

The **total revenue function**, $R(x)$, measures the amount of money received from the sale of $x$ units and is defined by

$$R(x) = x\cdot p(x)$$

where $x$ is the number of units demanded and $p(x)$ is the unit price.
```


```{admonition} Definition
:class: info

The **average revenue function**, $\overline{R}(x)$, measures the average amount of money received per unit sold and is defined by

$$\overline{R}(x) = \frac{R(x)}{x}.$$
```


## Total Profit & Average Profit Functions


```{admonition} Definition
:class: info

The **total profit function**, $P(x)$ measures the difference between the total revenue and total cost functions and is defined by

$$P(x) = R(x) - C(x)$$

where $R(x)$ is the total revenue function and $C(x)$ is the total cost function.
```

```{admonition} Definition
:class: info

The **average profit function**, $\overline{P}(x)$, measures the average profit earned per unit produced and sold and is defined by

$$\overline{P}(x) = \frac{P(x)}{x}.$$
```


## Example 1

A manufacturer of Robot Tutors has a fixed monthly cost of \$500 and a processing cost 
of \$9 for each robot tutor produced. Assuming each robot sells for \$19, compute the total profit and the average profit per robot when 250 robots are produced and sold.

```{dropdown} **Step 1:** Compute the total cost function, $C(x)$.

Here, $x$ denotes the number of robots produced.

\begin{align*}
C(x) &= F(x) + V(x) && \text{total cost equals fixed costs plus variable costs}\\
&= 500  + 9x && \hbox{\$500 of fixed costs and \$9 for each robot}
\end{align*}
```

```{dropdown} **Step 2:** Compute the total revenue function, $R(x)$.

\begin{align*}
    R(x) &= x \cdot p(x) && \text{revenue equals number of units times price per unit}\\
    &= 19x && \hbox{since each robot sells for \$19}
\end{align*}
```

```{dropdown} **Step 3:** Compute the total profit function, $P(x)$.

\begin{align*}
    P(x) &= R(x) - C(x) && \text{profit equals revenue minus cost}\\
    &= \left( 19x \right) - \left( 500 + 9x\right) && \text{using Steps 1 and 2}\\
    &= 19x - 500 - 9x \\
    &= 10x - 500 && 
\end{align*}
```

```{dropdown} **Step 4:** Plug in $x=250$ into the profit function.

Plug in $x=250$ into the profit function to find the profit associated with the production and sale of 250 robots.

\begin{align*}
    P(250) &= 10(250) - 500 \\
    &= 2500 - 500\\
    &= 2000
\end{align*}
```

```{dropdown} **Step 5:** Plug in $x=250$ into the average profit function.

Plug in $x=250$ into the average profit function to find the average profit associated with each robot when 250 robots are produced and sold.

\begin{align*}
    \overline{P}(250) 
    &= \frac{P(250)}{250} && \hbox{since $\overline{P}(x) = \frac{P(x)}{x}$}\\
    &= \frac{2000}{250} && \hbox{using Step 4}\\
    &= 8
\end{align*}

Therefore, each of the 250 robots produced and sold earns an average profit of \$8.
```