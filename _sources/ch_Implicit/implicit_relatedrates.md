---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3.9.6 64-bit
  language: python
  name: python3
---
# Related Rates

```{admonition} How to Solve a Related Rates Problem
:class: info

Here are a few guidelines to follow when solving a related rates problem.

1. **Assign a variable** to each quantity that changes and state the known and unknown rates of change with respect to time $t$.
    
2. **Find an equation** relating the variables. Don't forget about business models.

3. **Differentiate both sides** of the equation implicitly with respect to $t$. Treat all variables as functions of $t$.

4. **Replace the variables** and their derivatives by the numerical data given. Watch out for words like "increasing" or "decreasing", "rising" or "falling", "away" or "towards", etc. to determine if a derivative is positive or negative.

5. **Solve the equation** for the unknown rate of change.
```

## Example 1

Given $p^2x + 6x = 5$ and $\dfrac{dp}{dt} = 3$. Compute $\dfrac{dx}{dt}$ when $p = 2$.

```{dropdown} **Step 1:** Assign variables and state the known and unknown rates of change.

\begin{align*}
\text{Variables (as functions of $t$): } & x(t) \text{ and } p(t) \\ 
\text{Known rate of change: } & \dfrac{dp}{dt} = 3 \\ 
\text{Unknown rate of change: } & \dfrac{dx}{dt} \text{ when} p=2
\end{align*} 
```

```{dropdown} **Step 2:** Find an equation which relates the variables.

$$p^2x + 6x = 5$$
```

```{dropdown} **Step 3:** Differentiate both sides of the equation implicitly with respect to $t$.

\begin{align*}
\frac{d}{dt}(p^2x + 6x)
&= 2pp'x + p^2x' + 6x' && \hbox{Implicit differentiation & Product Rule}\\
&= 0 && \hbox{since $\dfrac{d}{dt} 5 = 0$}
\end{align*}
```

```{dropdown} **Step 4:** Since $x$ appears in the equation after differentiation, we need to find its value by plugging in $p=2$ into the given equation $p^2x + 6x = 5$.

$$(2)^2x + 6x = 5 ~~~~~\Rightarrow~~~~~ 10x = 5 ~~~~~\Rightarrow~~~~~ x = 1/2$$
```

```{dropdown} **Step 5:** Plug in the known values of the variables and their derivatives into the equation found in Step 3. ($p=2$, $x=1/2$, $\frac{dp}{dt} = 3$)

$$2(2)(3)\frac{1}{2} + (2)^2x' + 6x' = 0  ~~~~~\Rightarrow~~~~~ 6 + 10x' = 0 ~~~~~\Rightarrow~~~~~ x' = -3/5$$

Therefore $\dfrac{dx}{dt} = -3/5$ when $p=2$ and $\dfrac{dp}{dt} = 3$.
```

## Example 2

A company is decreasing the production of energy drinks at a rate of 100 cases per day. All cases produced can be sold. The daily demand function is given by 

$$p(x) = 50 - \frac{x}{200}$$ 

where $x$ is the number of cases produced and sold, and $p(x)$ is the unit price in dollars. Find the rate of change of the revenue with respect to the time in days when daily production is 300 cases.

```{dropdown} **Step 1:** Assign variables and state the known and unknown rates of change.

\begin{align*}

\text{Variables (as functions of $t$): } & x(t) = \text{ the quantity produced and sold per day} \\
& R(t) = \text{ the daily revenue} \\
\text{Known rate of change: } & \dfrac{dx}{dt} = -100 \text{ since production is decreasing} \\ \\
\text{Unknown rate of change: } & \dfrac{dR}{dt} \text{ when } x=300
\end{align*}
```

```{dropdown} **Step 2:** Find an equation which relates the variables.

\begin{align*}
R &= x\cdot p(x) && \text{Revenue Function}\\
&= x \left(50 - \frac{x}{200}\right) && \text{since $p(x) = 50 - \frac{x}{200}$}\\
&= 50x - \frac{1}{200}x^2 && \hbox{Simplify}
\end{align*}
```

```{dropdown} **Step 3:** Find an equation which relates the variables. 

\begin{align*}
R &= x\cdot p(x) && \text{Revenue Function}\\
&= x \left(50 - \frac{x}{200}\right) && \text{since $p(x) = 50 - \frac{x}{200}$}\\
&= 50x - \frac{1}{200}x^2 && \hbox{Simplify}
\end{align*}
```

```{dropdown} **Step 4:** Differentiate both sides of the equation implicitly with respect to $t$.

\begin{align*}
\frac{dR}{dt}
&= \frac{d}{dt}\left(50x - \frac{1}{200}x^2 \right)\\ 
&= 50 \,\frac{dx}{dt} - \frac{1}{200}\,2x\,\frac{dx}{dt} && \text{Implicit differentiation & Power Rule}\\
&= 50 \, \frac{dx}{dt} - \frac{x}{100}\,\frac{dx}{dt} && \text{Simplify}
\end{align*}

Therefore revenue is decreasing at \$4700 per day when the level of production is 300 cases per day and decreasing at 100 cases per day.
```

## Example 3

The weekly demand function is given by 

$$2p + x + 4xp = 22$$

where $x$ is the number of thousands of units demanded weekly and $p$ is in dollars. If the price is increasing at a rate of 25 cents per week when the weekly demand is 4000 units, at what rate is the demand decreasing?

```{dropdown} **Step 1:** Assign variables and state the known and unknown rates of change.

\begin{align*}

\text{Variables (as functions of $t$): } & x(t) = \text{ demand in units of a thousand} \\
&  p(t) = \text{ unit price in dollars}\\ 
\text{Known rate of change: } & \dfrac{dp}{dt} = \dfrac{25}{100} \text{ since price (in dollars) is increasing } \\
\text{Unknown rate of change: } & \dfrac{dx}{dt} \text{ when } x = 4

\end{align*}
```

```{dropdown} **Step 2:** Find an equation which relates the variables.

$$2p + x + 4xp = 22$$
```

```{dropdown} **Step 3:** Differentiate both sides of the equation implicitly with respect to $t$.

\begin{align*}
\frac{d}{dt}(2p + x + 4xp)
&= 2\frac{dp}{dt} + \frac{dx}{dt} + 4\frac{dx}{dt}p + 4x\frac{dp}{dt} && \hbox{Implicit differentiation & Product Rule} \\
&= 0 && \hbox{since $\dfrac{d}{dt}22 = 0$}
\end{align*}
```

```{dropdown} **Step 4:** Since $p$ appears in the equation after differentiation, we need to find its value by plugging in $x=4$ into the given demand equation $2p+x+4xp = 22$.

$$2p + 4 + 4(4)p = 22 ~~~~~\Rightarrow~~~~~ 18p + 4 = 22 ~~~~~\Rightarrow~~~~~ p = 1$$
```

```{dropdown} **Step 5:** Plug in the known values of the variables and their derivatives into the equation found in Step 3. ($x=4$, $p=1$, $\frac{dp}{dt} = 25/100$)

\begin{align*}
0 &= 2\left(\frac{25}{100}\right) + \frac{dx}{dt} + 4\frac{dx}{dt}(1) + 4(4)\left(\frac{25}{100}\right) \\
&= \frac{1}{2} + 5\frac{dx}{dt}  + 4 && \hbox{Simplify} \\
&= \frac{9}{2} + 5\frac{dx}{dt} 
\end{align*}

Therefore

$$\frac{9}{2} + 5\frac{dx}{dt} = 0  ~~~~~\Rightarrow~~~~~ 5\frac{dx}{dt} = -\frac{9}{2} ~~~~~\Rightarrow~~~~~ \frac{dx}{dt} = -\frac{9}{10}$$

and since $x$ is measured in thousands of units, this means that demand is decreasing by $900$ units per week (i.e., $9/10$ of one thousand) when the weekly demand is 4000 units and the price is increasing at 25 cents per week.
```

## Example 4

The wholesale price $p$ of an e-tablet writing stylus in dollars is related to the supply $x$ in thousands by:

$$125p^2 - x^2 = 100$$

If 20,000 styluses are available at the beginning of a week, and the price is falling at 4 cents per week, at what rate is the supply falling?

```{dropdown} **Step 1:** Assign variables and state the known and unknown rates of change.

\begin{align*}

\text{Variables (as functions of $t$): } & x(t) = \text{ supply in units of a thousand} \\
&  p(t) = \text{ unit price in dollars}\\ 
\text{Known rate of change: } & \dfrac{dp}{dt} = -\dfrac{4}{100} \text{ since price (in dollars) is falling} \\
\text{Unknown rate of change: } & \dfrac{dx}{dt} \text{ when } x = 20

\end{align*}
```

```{dropdown} **Step 2:** Find an equation which relates the variables.

$$125p^2 - x^2 = 100$$
```

```{dropdown} **Step 3:** Differentiate both sides of the equation implicitly with respect to $t$.

\begin{align*}
250p\frac{dp}{dt} - 2x\frac{dx}{dt} = 0 && \text{Power Rule}
\end{align*}
```

```{dropdown} **Step 4:** Since $p$ appears in the equation after differentiation, we need to find its value by plugging in $x=20$ into the given supply equation $125p^2 - x^2 = 100$.

$$125p^2 - 20^2 = 100 ~~~~~\Rightarrow~~~~~ 125p^2 = 500 ~~~~~\Rightarrow~~~~~ p^2 = 4~~~~~\Rightarrow~~~~~ p = 2$$
```

```{dropdown} **Step 5:** Plug in the known values of the variables and their derivatives into the equation found in Step 3. ($x=20$, $p=2$, $\frac{dp}{dt} = -4/100$)

\begin{align*}
0 &= 250(2)\left(-\frac{4}{100}\right) - 2(20)\frac{dx}{dt} \\
&= -500\left(\frac{4}{100}\right) - 40 \frac{dx}{dt} && \hbox{Simplify} \\
&= -20 - 40 \frac{dx}{dt} 
\end{align*}

Therefore

$$-20 - 40 \frac{dx}{dt} = 0  ~~~~~\Rightarrow~~~~~ -40 \frac{dx}{dt} = 20 ~~~~~\Rightarrow~~~~~ \frac{dx}{dt} = -\frac{1}{2}$$

and since $x$ is measured in thousands of units, this means that supply is falling by $500$ units per week (i.e., $1/2$ of one thousand) when the weekly demand is 20,000 styluses and the price is falling at 4 cents per week.
```