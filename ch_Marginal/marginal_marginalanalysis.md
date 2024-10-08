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
# Marginal Analysis

## Definitions

```{admonition} Definition
:class: info

If $C(x)$ denotes the total cost function, then $C'(x)$ denotes the _**marginal cost function**_, which approximates the extra cost incurred in producing one additional unit

$$C'(x) \approx C(x+1) - C(x)$$

and $\overline{C}'(x)$ denotes the _**marginal average cost function**_.
```



```{admonition} Definition
:class: info

If $R(x)$ denotes the total revenue function, then $R'(x)$ denotes the _**marginal revenue function**_, which approximates the revenue realized from the sale of one additional unit

$$R'(x) \approx R(x+1) - R(x)$$

and $\overline{R}'(x)$ denotes the _**marginal average revenue function**_.
```



```{admonition} Definition
:class: info

If $P(x)$ denotes the total profit function, then $P'(x)$ denotes the _**marginal profit function**_, which approximates the profit generated from the production and sale of one additional unit

$$P'(x) \approx P(x+1) - P(x)$$

and $\overline{P}'(x)$ denotes the _**marginal average profit function**_.
```


```{admonition} Summary of Marginal Analysis Notation
:class: note

| Name    | Function | Average                            | Marginal Function | Marginal Average                                  |
|---------|----------|------------------------------------|-------------------|---------------------------------------------------|
| Cost    | $C(x)$   | $\overline{C}(x) = \dfrac{C(x)}{x}$ | $C'(x)$           | $ \overline{C}'(x) = \dfrac{d}{dx}\overline{C}(x)$ |
| Revenue | $R(x)$   | $\overline{R}(x) = \dfrac{R(x)}{x}$ | $R'(x)$           | $ \overline{R}'(x) = \dfrac{d}{dx}\overline{R}(x)$ |
| Profit  | $P(x)$   | $\overline{P}(x) = \dfrac{P(x)}{x}$ | $P'(x)$           | $\overline{P}'(x) = \dfrac{d}{dx}\overline{P}(x)$  |
```


### Example 1
````{admonition} Marginal revenue
:class: tip

The daily demand for the new PBox5 Game *Dr. Mathematica-Exam Day of Reckoning* is given by

$$p(x) = \frac{125}{x+2} - \frac{1}{2}x$$

where $x$ is the number of video games sold each day and $p$ is in dollars. Using the marginal revenue function, $R'(x)$, approximate the marginal revenue when 3 video games are sold each day and interpret the result.


```{dropdown} **Step 1:** &nbsp; Compute the total revenue function, &nbsp; $R(x)$.

\begin{align*}
    R(x) &= x\cdot p(x) \\
    &= x\left(\frac{125}{x+2} - \frac{1}{2}x \right)\\
    &= \frac{125x}{x+2}-\frac{1}{2}x^2
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Compute the marginal revenue function, &nbsp; $R'(x)$.

\begin{align*}
    R'(x) &= \frac{d}{dx}R(x)\\
    &= \frac{d}{dx}\left( \frac{125x}{x+2}-\frac{1}{2}x^2 \right) \\
    &= \frac{125(x+2) -125x}{(x+2)^2} - \frac{1}{2}\cdot 2x \\
    &=  \frac{125x+250 - 125x}{(x+2)^2} - x \\
    &=  \frac{250}{(x+2)^2} - x \\
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Plug in &nbsp; $x=3$ &nbsp; into the marginal revenue function.

\begin{align*}
    R'(3) &= \frac{250}{(3+2)^2} - 3 \\
    &= \frac{250}{5^2} - 3 \\
    %&= \frac{250}{25} - 3 \\
    &= 10 - 3\\
    &= 7
\end{align*}

Therefore, the total daily revenue would increase by approximately \$7 if sales increased from 3 to 4 units each day.
```
````


### Example 2
````{admonition} Marginal profit
:class: tip

If the demand function for math self-help videos is given by

$$p(x) = 35 - 0.1x$$ 

and the total cost function to manufacture the videos is given by

$$C(x) = 3x + 21$$ 

Evaluate the marginal profit function at $x=20$ and interpret the result.


```{dropdown} **Step 1:** &nbsp; Compute the total revenue function, &nbsp; $R(x)$.

\begin{align*}
    R(x) &=  x\cdot p(x)\\
    &= x(35 - 0.1x)\\
    &= 35x-0.1x^2
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Compute the total profit function, &nbsp; $P(x)$.

\begin{align*}
    P(x) &= R(x) - C(x)\\
    &= (35x-0.1x^2)-(3x+21)\\
    &= 35x-0.1x^2-3x-21\\
    &=-0.1x^2 +32x -21
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Compute the marginal profit function, &nbsp; $P'(x)$.

\begin{align*}
    P'(x) &= \frac{d}{dx}P(x) \\
    &= \frac{d}{dx}(-0.1x^2 +32x -21) \\
    &= -0.1(2x) + 32 \\
    &= -0.2x+32
\end{align*}
```

```{dropdown} **Step 4:** &nbsp; Plug in &nbsp; $x=20$ &nbsp; into the marginal profit function.

\begin{align*}
    P'(20) 
    &= -0.2(20)+32\\
    &= -\frac{2}{10}(20)+32\\
    &=-4+32\\
    &=28
\end{align*}
Therefore, the total profit will increase by approximately \$28 when the 21st video is produced and sold.
```
````

### Example 3
````{admonition} Marginal average cost
:class: tip

The daily cost (in dollars) of producing computer screens is given by 

$$C(x)=9x^3-30x^2+90x+900$$

where $x$ denotes the number of thousands of screens produced each day. Calculate the marginal average cost function when 3000 screens are produced each day and interpret the result.

```{dropdown} **Step 1:** &nbsp; Compute and simplify the average cost function, &nbsp; $\overline{C}(x)$.

\begin{align*}
    \overline{C}(x) 
    &= \frac{9x^3-30x^2+90x+900}{x} && \hbox{since $\overline{C}(x) = C(x)/x$}\\ 
    \\
    &= \frac{9x^3}{x} -\frac{30x^2}{x}+\frac{90x}{x}+\frac{900}{x}&& \text{separate the terms to make differentiation easier}\\ 
    \\
    &=9x^2 -30x+90+900x^{-1} && \text{simplify}\\
\end{align*}
```


```{dropdown} **Step 2:** &nbsp; Compute the marginal average cost function, &nbsp; $\overline{C}'(x)$.

\begin{align*}
    \overline{C}'(x) 
    &= \frac{d}{dx} \overline{C}(x)\\
    &= \frac{d}{dx}\left(9x^2 -30x+90+900x^{-1}\right)\\
    &= 9(2x)-30+ 0 + (-1)900x^{-2}\\
    &=18x-30-\frac{900}{x^2}
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Plug in &nbsp; $x=3$.

We plug in $x=3$, since $x$ denotes the *number of thousands* of screens produced each day.  

\begin{align*}
    \overline{C}'(3)
     &=18(3)-30-\frac{900}{3^2} \\
    &=54-30-100 \\ 
    &= -76
\end{align*}

Therefore, the average cost of producing a thousand screens will decrease by approximately \$76 if the level of production is increased from 3000 to 4000 screens.
```
````