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
# The Concept of the Derivative

## Definitions

```{admonition} The Slope of a Tangent Line
:class: info

The _**slope of the line tangent**_ to the graph of $f(x)$ at the point $(x, f(x))$ is given by 

$$\lim_{h\to 0} \frac{f(x+h) - f(x)}{h},$$ 

if the limit exists.
```

```{admonition} Average and Instantaneous Rate of Change
:class: info

The _**average rate of change**_ of $f(x)$ over the interval $(x, x+h)$, which is also the slope of the secant line to the graph of $f(x)$ through the points $(x,f(x))$ and $(x+h, f(x+h))$, is given by

$$ \frac{f(x+h) - f(x)}{h}.$$

The _**instantaneous rate of change**_ of $f(x)$ at $x$, which is also the slope of the tangent line to the graph of $f(x)$ at $(x,f(x))$, is given by

$$\lim_{h\to 0} \frac{f(x+h) - f(x)}{h},$$ 

if the limit exists.
```


```{admonition} The Limit Definition of the Derivative
:class: info

The _**derivative**_ of a function $f(x)$ with respect to $x$ is the function $f'(x)$ which is defined as follows 

$$f'(x) = \lim_{h\to 0} \frac{f(x+h) - f(x)}{h},$$

and the domain of $f'(x)$ is the set of all $x$ where the limit exists.
```



```{admonition} The Equation of a Tangent Line
:class: info

The equation of the line tangent to $f(x)$ at $x=a$ is given by 

$$y = f'(a)(x-a) + f(a)$$ 

The above equation is equivalent to the point-slope equation of a line (i.e., $y=m(x-a) + b$) where the slope, $m$, is equal to $f'(a)$, and the line goes through the point $(a,b)$, where $b = f(a)$.
```


## Computing Derivatives Using the Limit Definition

```{admonition} Simplify the difference quotient
:class: info

When computing the derivative, $f'(x)$, using its limit definition, it turns out that the limit will most likely be an indeterminate form of type $0/0$.  This means that to evaluate the limit, we'll have to simplify the difference quotient

$$\frac{f(x+h) - f(x)}{h}$$ 

until we can cancel out the factor of $h$ in the denominator.   This simplification will usually consist of some combination of expanding (e.g., FOIL) and/or rationalization.  

Once the factor of $h$ in the denominator has been cancelled out, we can evaluate the limit by plugging in $h=0$.
```


### Example 1
````{admonition} Equation of a tangent line
:class: tip

Compute the slope of the line tangent to $f(x)=3x^2+12$ at $x=5$ using the limit definition of the derivative.  Then write down the equation of the line tangent to $f(x)$ at $x=5$.


```{dropdown} **Step 1:** &nbsp; Write down the limit definition of a derivative.

$$ 
\boxed{f'(x)=\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}}
$$

Remember: $f(x+h)$ means that we take $f(x)$ and replace $x$ with $(x+h)$.  For example, if $f(x) = x^2$, then $f(x+h)=(x+h)^2=x^2+2xh+h^2.$
```

```{dropdown} **Step 2:** &nbsp; Plug &nbsp; $f(x+h)$ &nbsp; and &nbsp; $f(x)$ &nbsp; into definition.

Plug $f(x+h) = 3(x+h)^2 + 12$ and $f(x) = 3x^2 + 12$ into the limit definition of the derivative.
Using brackets will help avoid errors from forgetting to distribute the negative sign:

$$ f'(x)=\lim_{h \to 0} \frac{[3(x+h)^2+12]-[3x^2+12]}{h}$$
```


```{dropdown} **Step 3:** &nbsp; FOIL and Simplify

\begin{align*}
f'(x) &=\lim_{h \to 0} \frac{[3(x+h)^2+12]-[3x^2+12]}{h}\\ \\
&=\lim_{h \to 0} \frac{[3(x^2+2xh+h^2)+12]-[3x^2+12]}{h} && \hbox{FOIL $(x+h)^2$}\\ \\
&=\lim_{h \to 0} \frac{3x^2+6xh+3h^2+12-3x^2-12}{h} && \hbox{distribute the 3 and the minus sign}\\ \\
&=\lim_{h \to 0} \frac{\cancel{3x^2}+6xh+3h^2+\cancel{12}-\cancel{3x^2}-\cancel{12}}{h} && \hbox{simplify}\\ \\
&=\lim_{h \to 0} \frac{6xh+3h^2}{h}
\end{align*}
```


```{dropdown} **Step 4:** &nbsp; Factor out &nbsp; $h$ &nbsp; and cancel.

Factor out an $h$ in the numerator and cancel it with the factor of $h$ in the denominator.

$$f'(x)=\lim_{h \to 0} \frac{6xh+3h^2}{h}=\lim_{h \to 0} \frac{h(6x+3h)}{h}=\lim_{h \to 0} 6x+3h$$
```


```{dropdown} **Step 5:** &nbsp; Evaluate the limit.

\begin{align*}
f'(x)
&=\lim_{h \to 0} 6x+3h \\
&= 6x+3(0) &&\text{plug in $h=0$}\\
&=6x && \text{simplify}
\end{align*}
```


```{dropdown} **Step 6:** &nbsp; Compute $f'(5)$.

We have found that $f'(x) = 6x$ is the derivative of our function and the general form of the slope of the tangent line. All that's left for us to do is to plug in $x=5$. Therefore, the slope of the tangent line when $x=5$ (i.e., $f'(5)$) is equal to $30$.
```

```{dropdown} **Step 7:** &nbsp; Compute $f(5)$.

In order to write down the equation of the tangent line, we also need to know the value $f(5)$.

$$f(5) = 3(5)^2 + 12 = 87$$

```

```{dropdown} **Step 8:** &nbsp; Write down the equation of the tangent line.

Now that we know $f(5) = 87$ and $f'(5) = 30$, the equation of the tangent line is given by

$$y = 30(x-5) + 87$$
```
````

### Example 2
````{admonition} Derivative of a square root function
:class: tip

Compute the derivative of $f(x)=3\sqrt{x}$ using the limit definition of the derivative.


```{dropdown} **Step 1:** &nbsp; Write down the limit definition of a derivative.

$$
\boxed{f'(x)=\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}}
$$
```


```{dropdown} **Step 2:** &nbsp; Plug &nbsp; $f(x+h)$ &nbsp; and &nbsp; $f(x)$ &nbsp; into definition.

Plug $f(x+h) = 3\sqrt{x+h}$ and $f(x) = 3\sqrt{x}$ into the limit definition of the derivative.  
\begin{align*}
f'(x) 
= \lim_{h \to 0} \frac{3\sqrt{x+h}-3\sqrt{x}}{h} 
= \lim_{h \to 0} \frac{3(\sqrt{x+h}-\sqrt{x})}{h} 
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Rationalize, FOIL, and simplify.

\begin{align*}
f'(x) 
&= \lim_{h \to 0} \frac{3(\sqrt{x+h}-\sqrt{x})}{h}\cdot \frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}} && \hbox{rationalize} \\ \\
&= \lim_{h \to 0} \frac{3(\sqrt{x+h}-\sqrt{x})(\sqrt{x+h}+\sqrt{x})}{h(\sqrt{x+h}+\sqrt{x})}  \\ \\
&= \lim_{h \to 0} \frac{3(\sqrt{x+h}\sqrt{x+h} + \sqrt{x+h}\sqrt{x}-\sqrt{x}\sqrt{x+h} - \sqrt{x}\sqrt{x})}{h(\sqrt{x+h}+\sqrt{x})} && \hbox{FOIL} \\ \\
&= \lim_{h \to 0} \frac{3(\cancel{x}+h + \cancel{\sqrt{x+h}\sqrt{x}}-\cancel{\sqrt{x}\sqrt{x+h}} - \cancel{x})}{h(\sqrt{x+h}+\sqrt{x})} && \hbox{simplify} \\ \\
&= \lim_{h \to 0} \frac{3 h}{h(\sqrt{x+h}+\sqrt{x})} 
\end{align*}

Notice how making use of the formula $(\sqrt{A} - \sqrt{B})(\sqrt{A} + \sqrt{B}) = A - B$ can help eliminate some of the above computations.
```

```{dropdown} **Step 4:** &nbsp; Cancel the &nbsp; $h$ &nbsp; in the numerator with the &nbsp; $h$ &nbsp; in the denominator.

$$f'(x) = \lim_{h \to 0} \frac{3 \cancel{h}}{\cancel{h}(\sqrt{x+h}+\sqrt{x})} = \lim_{h \to 0} \frac{3}{\sqrt{x+h}+\sqrt{x}} $$
```

```{dropdown} **Step 5:** &nbsp; Evaluate the limit.

\begin{align*}
f'(x) 
&= \lim_{h \to 0} \frac{3}{\sqrt{x+h}+\sqrt{x}} \\
&= \frac{3}{\sqrt{x + 0}+\sqrt{x}} && \text{plug in $h=0$}\\
&= \frac{3}{\sqrt{x}+\sqrt{x}} && \text{simplify}\\
&= \frac{3}{2\sqrt{x}} && \text{combine like terms}
\end{align*}

Therefore, the derivative of $f(x)$ is equal to $\frac{3}{2\sqrt{x}}$.
```
````
