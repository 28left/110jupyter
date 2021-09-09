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

## The Basic Definitions

```{admonition} Slope of a Tangent Line
:class: info

The **slope of the tangent line** to the graph of $f(x)$ at the point $P(x, f(x))$ is given by 

$$\lim_{h\to 0} \frac{f(x+h) - f(x)}{h},$$ 

if the limit exists.
```

```{admonition} Average and Instantaneous Rate of Change
:class: info

The **average rate of change** of $f(x)$ over the interval $(x, x+h)$ or slope of the secant line to the graph of $f(x)$ through the points $(x,f(x))$ and $(x+h, f(x+h))$ is 

$$ \frac{f(x+h) - f(x)}{h}.$$

The **instantaneous rate of change** of $f(x)$ at $x$ or slope of the tangent line to the graph of $f(x)$ at $(x,f(x))$ is  

$$\lim_{h\to 0} \frac{f(x+h) - f(x)}{h},$$ 

if the limit exists.
```


```{admonition} The Limit Definition of the Derivative
:class: info

The **derivative** of a function $f(x)$ with respect to $x$ is the function $f'(x)$ which is defined as follows 

$$f'(x) = \lim_{h\to 0} \frac{f(x+h) - f(x)}{h},$$

and the domain of $f'(x)$ is the set of all $x$ where the limit exists.
```

```{admonition} Differentiability and Continuity
:class: warning

If a function is differentiable at $x=a$, then it is continuous at $x=a$. If a function is continuous at $x=a$, then it **is not necessarily** differentiable at $x=a$.
```

## Computing Derivatives Using the Limit Definition

### Example 1

Find the slope of the tangent line to the function 

$$f(x)=3x^2+12$$ 

at $x=5$ using the limit definition of the derivative.

```{dropdown} **Step 1:** Write down the limit definition of a derivative.

$$ 
\boxed{f'(x)=\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}}
$$

Remember: $f(x+h)$ means that we take $f(x)$ and replace $x$ with $(x+h)$.  For example, if $f(x) = x^2$, then $f(x+h)=(x+h)^2=x^2+2xh+h^2.$
```

```{dropdown} **Step 2:** Plug $f(x+h)$ and $f(x)$ into definition.

Plug $f(x+h)$ and $f(x)$ into the limit definition of the derivative.
Using brackets will help avoid errors from forgetting to distribute the negative sign:

$$ f'(x)=\lim_{h \to 0} \frac{[3(x+h)^2+12]-[3x^2+12]}{h}$$
```



```{dropdown} **Step 3:** FOIL and Simplify

\begin{align*}
f'(x) &=\lim_{h \to 0} \frac{[3(x+h)^2+12]-[3x^2+12]}{h}\\ \\
&=\lim_{h \to 0} \frac{[3(x^2+2xh+h^2)+12]-[3x^2+12]}{h} && \hbox{FOIL $(x+h)^2$}\\ \\
&=\lim_{h \to 0} \frac{3x^2+6xh+3h^2+12-3x^2-12}{h} && \hbox{Distribute the '3' and the minus sign}\\ \\
&=\lim_{h \to 0} \frac{\cancel{3x^2}+6xh+3h^2+\cancel{12}-\cancel{3x^2}-\cancel{12}}{h} && \hbox{Simplify}\\ \\
&=\lim_{h \to 0} \frac{6xh+3h^2}{h}
\end{align*}
```

```{dropdown} **Step 4:** Factor out $h$ and cancel.

Factor out an $h$ in the numerator and cancel it with the factor of $h$ in the denominator.

$$f'(x)=\lim_{h \to 0} \frac{6xh+3h^2}{h}=\lim_{h \to 0} \frac{h(6x+3h)}{h}=\lim_{h \to 0} 6x+3h$$
```

```{dropdown} **Step 5:** Evaluate the limit.

$$f'(x)=\lim_{h \to 0} 6x+3h=6x+3(0)=6x$$
```

```{dropdown} **Step 6:** Plug $x=5$ into evaluated limit.

We have found that $f'(x) = 6x$ is the derivative of our function and the general form of the slope of the tangent line. All that's left for us to do is to plug in $x=5$. Therefore, the slope of the tangent line when $x=5$ is $30$.
```


### Example 2

Find the derivative of the function 

$$f(x)=3\sqrt{x}$$ 

using the limit definition of the derivative.

```{dropdown} **Step 1:** Write down the limit definition of a derivative.

$$
\boxed{f'(x)=\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}}
$$
```


```{dropdown} **Step 2:** Plug $f(x+h)$ and $f(x)$ into definition.

Plug $f(x+h)$ and $f(x)$ into the limit definition of the derivative.  
\begin{align*}
f'(x) 
= \lim_{h \to 0} \frac{3\sqrt{x+h}-3\sqrt{x}}{h} 
= \lim_{h \to 0} \frac{3(\sqrt{x+h}-\sqrt{x})}{h} 
\end{align*}
```

```{dropdown} **Step 3:** Rationalize, FOIL, and Simplify.

\begin{align*}
f'(x) 
&= \lim_{h \to 0} \frac{3(\sqrt{x+h}-\sqrt{x})}{h}\cdot \frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}} && \hbox{Rationalize} \\ \\
&= \lim_{h \to 0} \frac{3(\sqrt{x+h}-\sqrt{x})(\sqrt{x+h}+\sqrt{x})}{h(\sqrt{x+h}+\sqrt{x})}  \\ \\
&= \lim_{h \to 0} \frac{3(\sqrt{x+h}\sqrt{x+h} + \sqrt{x+h}\sqrt{x}-\sqrt{x}\sqrt{x+h} - \sqrt{x}\sqrt{x})}{h(\sqrt{x+h}+\sqrt{x})} && \hbox{FOIL} \\ \\
&= \lim_{h \to 0} \frac{3(x+h + \cancel{\sqrt{x+h}\sqrt{x}}-\cancel{\sqrt{x}\sqrt{x+h}} - x)}{h(\sqrt{x+h}+\sqrt{x})} && \hbox{Simplify} \\ \\
&= \lim_{h \to 0} \frac{3(\cancel{x}+h-\cancel{x})}{h(\sqrt{x+h}+\sqrt{x})}  \\ \\
&= \lim_{h \to 0} \frac{3 h}{h(\sqrt{x+h}+\sqrt{x})} 
\end{align*}

Notice how making use of the formula $(\sqrt{A} - \sqrt{B})(\sqrt{A} + \sqrt{B}) = A - B$ can help eliminate some of the above computations.
```

```{dropdown} **Step 4:** Cancel the $h$ in the numerator with the $h$ in the denominator.

$$f'(x) = \lim_{h \to 0} \frac{3 \cancel{h}}{\cancel{h}(\sqrt{x+h}+\sqrt{x})} = \lim_{h \to 0} \frac{3}{\sqrt{x+h}+\sqrt{x}} $$
```

```{dropdown} **Step 5:** Evaluate the limit.

$$f'(x) = \lim_{h \to 0} \frac{3}{\sqrt{x+h}+\sqrt{x}} = \frac{3}{\sqrt{x + 0}+\sqrt{x}} = \frac{3}{\sqrt{x}+\sqrt{x}} = \frac{3}{2\sqrt{x}}$$
```

