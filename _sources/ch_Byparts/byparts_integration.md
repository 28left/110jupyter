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
# Integration by Parts

## How to Integrate Products of Different Types of Functions

```{admonition} Reversing the Product Rule of Differentiation
:class: info

The product rule for differentiating $f(x)g(x)$ (i.e., $\frac{d}{dx}(fg) = f'g + fg'$) can be translated into the following rule for computing the antiderivative of a product:

$$\int fg' ~dx = fg - \int f'g ~dx$$ 

This rule is known as _**integration by parts**_ and its usefulness relies on $f'g$ being easier to integrate than $fg'$. When applying integration by parts to the integral of a product, $fg'$, the first consideration is determining which factor corresponds to $f$ and which factor corresponds to $g'$. This will be addressed below.
```


```{admonition} Notation
:class: info

Integration by parts is often written in the following form

$$\int u ~dv = uv - \int v ~du.$$

where $u = f(x)$, $dv = g'(x) ~dx$, and therefore $du = f'(x)~dx$ and $v = g(x)$.
```


```{admonition} When to Apply Integration by Parts
:class: info

The method of integration by parts is most commonly applied to integrating products of different types of functions. For example, the product of a polynomial and an exponential function or the product of a polynomial and a logarithmic function. Integration by parts can also be used to integrate inverse functions, like $\ln(x)$.
```



```{admonition} LAE: How to Pick $u$ and $dv$
:class: info

When deciding which factor corresponds to $u$ (i.e., $f(x)$), use the acronym *LAE* to help remember the order in which different types of functions are preferred. 

- **L**ogarithmic functions (e.g., $\ln(x)$) 
- **A**lgebraic (including power, polynomial, and rational) functions (e.g., $x^2$, $1/x$, $\sqrt{x}$)
- **E**xponential functions (e.g., $e^x$)


In other words, a logarithmic function is our first choice for $u$, if it appears in the integrand. If not, then our second choice is for an algebraic function, and our last choice would be an exponential function. 

Once $u$ has been selected, set $dv$ to be the remaining factors of the integrand, including the differential $dx$. Furthermore, if $u = f(x)$ and $dv = g(x) ~dx$, then

$$du = f'(x) ~dx ~~~~\text{and} ~~~~ v = \int g(x)~dx  ~~~ \hbox{(no $+ C$ required)}$$  
```


### Example 1
````{admonition} Integrate the product of a power function and an exponential function
:class: tip

Compute $\displaystyle \int 2x e^x ~dx.$

```{dropdown} **Step 1:** &nbsp; Based on the integrand and the preferred LAE order, pick $u$ and $dv$.

Since the integrand is $2xe^x$, the preferred choice for $u$ is $u=2x$ and therefore $dv = e^x ~dx$.
```

```{dropdown} **Step 2:** &nbsp; Compute $du$ and $v$.

\begin{align*}
  u &= 2x & dv &= e^x~dx \\
  du &= \frac{d}{dx}(2x) ~dx = 2~dx & v &= \int e^x~dx = e^x 
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Compute the integral using integration by parts.

\begin{align*}
  \int 2xe^x ~dx
  &= uv -\int v  ~du \\
  &= (2x)e^x - \int (e^x)2 ~dx\\
  &= 2xe^x - 2\int e^x ~dx && \hbox{simplify}\\
  &= 2xe^x - 2e^x + C \\
  &= 2e^x(x-1) + C
\end{align*}
```

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $2x e^x$ is the derivative of $2e^x(x-1)$.

\begin{align*}
\frac{d}{dx} 2e^x(x-1)
&= 2e^x(x-1) + 2e^x && \text{product rule} \\
&= 2xe^x - 2e^x + 2e^x && \text{expand} \\ 
&= 2xe^x && \text{simplify}
\end{align*}
```
````

### Example 2
````{admonition} Integrate the product of a power function and a logarithmic function
:class: tip

Compute $\displaystyle \int x^2 \ln(x) ~dx.$


```{dropdown} **Step 1:** &nbsp; Based on the integrand and the preferred LAE order, pick $u$ and $dv$.

Since the integrand is $x^2 \ln(x)$, the preferred choice for $u$ is $u=\ln(x)$ and therefore $dv = x^2 ~dx$.
```

```{dropdown} **Step 2:** &nbsp; Compute $du$ and $v$.

\begin{align*}
  u &= \ln(x) & dv &= x^2~dx \\
  du &= \frac{d}{dx}(\ln(x)) ~dx = \frac{1}{x}~dx & v &= \int x^2~dx = \frac{1}{3}x^3 
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Compute the integral using integration by parts.

\begin{align*}
  \int x^2\ln(x) ~dx 
  &= uv -\int v ~du \\
  &= \ln(x)\left(\frac{1}{3}x^3\right) - \int \left(\frac{1}{3}x^3\right)\frac{1}{x} ~dx\\
  &= \frac{1}{3}x^3\ln(x) - \frac{1}{3}\int x^2 ~dx && \hbox{simplify}\\
  &= \frac{1}{3}x^3\ln(x) - \frac{1}{3}\cdot \frac{1}{3}x^3 + C\\
  &= \frac{1}{3}x^3\ln(x) - \frac{1}{9}x^3 + C
\end{align*}
```

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $x^2 \ln(x)$ is the derivative of $\dfrac{1}{3}x^3\ln(x) - \dfrac{1}{9}x^3$.

\begin{align*}
\frac{d}{dx} \left(\frac{1}{3}x^3\ln(x) - \frac{1}{9}x^3\right)
&= \frac{1}{3}3x^2\ln(x) + \frac{1}{3}x^3\frac{1}{x} - \frac{1}{9}3x^2 && \text{product and sum rules} \\
&= x^2\ln(x) + \frac{1}{3}x^2 - \frac{1}{3}x^2 && \text{simplify}\\
&= x^2\ln(x) && \text{simplify}
\end{align*}
```
````

### Example 3
````{admonition} Integrating the logarithm
:class: tip

Compute $\displaystyle \int \ln(x) ~dx.$


```{dropdown} **Step 1:** &nbsp; Based on the integrand and the preferred LAE order, pick $u$ and $dv$.

Since the integrand is $\ln(x)$, the preferred choice for $u$ is $u=\ln(x)$ and therefore $dv = dx$.
```

```{dropdown} **Step 2:** &nbsp; Compute $du$ and $v$.

\begin{align*}
  u &= \ln(x) & dv &= 1~dx \\
  du &= \frac{d}{dx}(\ln(x)) ~dx = \frac{1}{x}~dx & v &= \int 1~dx = x 
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Compute the integral using integration by parts.

\begin{align*}
  \int \ln(x) ~dx 
  &= uv -\int v ~du \\
  &= (\ln(x))x - \int x \frac{1}{x} ~dx\\
  &= x\ln(x) - \int 1 ~dx && \hbox{simplify}\\
  &= x\ln(x) - x + C
\end{align*}
```

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $\ln(x)$ is the derivative of $x\ln(x) - x$.

\begin{align*}
\frac{d}{dx} \left(x\ln(x) - x\right) 
&= \ln(x) + x\frac{1}{x} - 1 && \text{product and sum rules} \\
&= \ln(x) + 1 - 1 && \text{simplify}\\
&= \ln(x) && \text{simplify}
\end{align*}
```
````

### Example 4
`````{admonition} Area of a region
:class: tip

Compute the area of the region under the graph of $\displaystyle f(x) = 3xe^{-2x} $ from $x=0$ to $x=4$.


```{dropdown} **Step 1:** &nbsp; Write the area of the region as a definite integral.

$$\hbox{Area} = \int_0^4 3xe^{-2x}~dx$$
```

````{dropdown} **Step 2:** &nbsp; Compute $\displaystyle \int 3xe^{-2x} ~dx $ using integration by parts.

Pick $u$ and $dv$ and compute $du$ and $v$. (Recall $\int e^{ax} ~dx = \frac{1}{a}e^{ax}+C$.) 

\begin{align*}
  u &= 3x & dv &= e^{-2x}~dx \\
  du &= \frac{d}{dx}(3x) ~dx = 3~dx & v &= \int e^{-2x}~dx = -\frac{1}{2}e^{-2x}
\end{align*}

\begin{align*}
  \int 3xe^{-2x} ~dx 
  &= uv - \int v ~du \\
  &= (3x)\left(-\frac{1}{2}e^{-2x}\right) - \int \left(-\frac{1}{2}e^{-2x}\right)3 ~dx\\
  &= -\frac{3}{2}xe^{-2x} + \frac{3}{2}\int e^{-2x} ~dx && \hbox{simplify}\\
  &= -\frac{3}{2}xe^{-2x} + \frac{3}{2}\left(-\frac{1}{2}\right)e^{-2x} + C && \text{using } \int e^{ax}dx = \frac{1}{a}e^{ax}+C \\
  &= -\frac{3}{2}xe^{-2x} - \frac{3}{4}e^{-2x} + C \\
\end{align*}

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $3xe^{-2x}$ is the derivative of $-\dfrac{3}{2}xe^{-2x} - \dfrac{3}{4}e^{-2x}$.

\begin{align*}
\frac{d}{dx} \left(-\frac{3}{2}xe^{-2x} - \frac{3}{4}e^{-2x}\right) 
&= -\frac{3}{2}e^{-2x} - \frac{3}{2}xe^{-2x}(-2) - \frac{3}{4}e^{-2x}(-2) && \text{product and sum rules} \\
&= -\frac{3}{2}e^{-2x} + 3xe^{-2x} + \frac{3}{2}e^{-2x} && \text{simplify}\\
&= 3xe^{-2x} && \text{simplify}
\end{align*}
```
````

```{dropdown} **Step 3:** &nbsp; Evaluate $\displaystyle \int_0^4 3xe^{-2x} ~dx $ using the answer to Step 2.

\begin{align*}
  \hbox{Area} 
  &= \int_0^4 3xe^{-2x}~dx && \hbox{using Step 1}\\
  &= \left(-\frac{3}{2}xe^{-2x} - \frac{3}{4}e^{-2x}\right) \Biggr|_0^4 && \hbox{using Step 2}\\
  &= \left(-\frac{3}{2}(4)e^{-8} - \frac{3}{4}e^{-8}\right) - \left(-\frac{3}{2}(0)e^{0} - \frac{3}{4}e^{0}\right)\\
  &= \left(-6e^{-8} - \frac{3}{4}e^{-8}\right) - \left(0 - \frac{3}{4}\right) && \hbox{since $e^0=1$}\\
  &= \frac{3}{4} - \frac{27}{4}e^{-8} && \hbox{simplify}
\end{align*}
```
`````


### Example 5
`````{admonition} Evaluating a definite integral using integration by parts
:class: tip

Evaluate $\displaystyle \int_1^e (4x+1)\ln(x) ~dx$.


````{dropdown} **Step 1:** &nbsp; Compute $\displaystyle \int (4x+1)\ln(x) ~dx $ using integration by parts.

Pick $u$ and $dv$ and compute $du$ and $v$. 

\begin{align*}
  u &= \ln(x) & dv &= 4x+1 ~dx \\
  du &= \frac{d}{dx}\ln(x) ~dx = \frac{1}{x}~dx & v &= \int 4x+1~dx = 2x^2+x
\end{align*}

\begin{align*}
  \int (4x+1)\ln(x) ~dx 
  &= uv - \int v ~du \\
  &= (\ln(x))(2x^2+x) - \int (2x^2+x)\frac{1}{x} ~dx\\
  &= (2x^2+x)\ln(x) - \int 2x+1 ~dx && \hbox{simplify}\\
  &= (2x^2+x)\ln(x) - (x^2+x) + C \\
  &= (2x^2+x)\ln(x) - x^2 - x + C 
\end{align*}

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $(4x+1)\ln(x)$ is the derivative of $(2x^2+x)\ln(x) - x^2 - x$.

\begin{align*}
\frac{d}{dx} \left((2x^2+x)\ln(x) - x^2 - x\right) 
&= (4x+1)\ln(x) + (2x^2+x)\frac{1}{x} - 2x - 1&& \text{product and sum rules} \\
&= (4x+1)\ln(x) + 2x+1 - 2x - 1 && \text{expand}\\
&= (4x+1)\ln(x) && \text{simplify}
\end{align*}
```
````

```{dropdown} **Step 2:** &nbsp; Evaluate $\displaystyle \int_1^e (4x+1)\ln(x) ~dx$ using the answer to Step 1.

\begin{align*}
  \int_1^e (4x+1)\ln(x) ~dx 
  &= \left((2x^2+x)\ln(x) - x^2 - x\right) \Big|_1^e && \hbox{using Step 1}\\
  &= \left((2e^2+e)\ln(e) - e^2 - e\right) - \left(3\ln(1) - 2\right)\\
  &= \left(2e^2+e - e^2 - e\right) - \left(0 -2\right) && \hbox{since $\ln(e)=1$, $\ln(1)=0$}\\
  &= e^2 + 2 &&\hbox{simplify}
\end{align*}
```
`````

### Example 6

`````{admonition} An integral that requires two applications of integration by parts
:class: tip

Compute $\displaystyle \int 5x^2e^x ~dx$.


```{dropdown} **Step 1:** &nbsp; Use integration by parts to compute $\displaystyle \int 5x^2e^x ~dx$.

Pick $u$ and $dv$ and compute $du$ and $v$.

\begin{align*}
  u &= 5x^2 & dv &= e^x~dx \\
  du &= \frac{d}{dx}(5x^2) ~dx = 10x~dx & v &= \int e^x~dx = e^x
\end{align*}

\begin{align*}
  \int 5x^2e^x ~dx
  &= uv - \int v~du \\ 
  &= 5x^2e^x - \int 10xe^x~dx 
\end{align*}

In order to compute the indefinite integral of $10xe^x$, we need to use integration by parts again.
```

````{dropdown} **Step 2:** &nbsp; Use integration by parts to compute $\displaystyle \int 10xe^x ~dx$.

Pick $u$ and $dv$ and compute $du$ and $v$.

\begin{align*}
  u &= 10x & dv &= e^x~dx \\
  du &= \frac{d}{dx}(10x) ~dx = 10~dx & v &= \int e^x~dx = e^x
\end{align*}

\begin{align*}
  \int 10xe^x ~dx
  &= uv - \int v ~du \\
  &= 10xe^x - \int 10e^x~dx \\
  &= 10xe^x - 10e^x + C \\
  &= (10x - 10)e^x + C
\end{align*}

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $10xe^x$ is the derivative of $(10x - 10)e^x$.

\begin{align*}
\frac{d}{dx} (10x - 10)e^x
&= 10e^x + (10x - 10)e^x && \text{product rule} \\
&= (10 + 10x - 10)e^x && \text{pull out common factor of $e^x$}\\
&= 10xe^x && \text{simplify}
\end{align*}
```
````

```{dropdown} **Step 3:** &nbsp; Use the answer to Step 2 to complete the computations in Step 1.

\begin{align*}
  \int 5x^2e^x ~dx
  &= 5x^2e^x - \int 10xe^x~dx  && \text{using Step 1}\\
  &= 5x^2e^x - (10x - 10)e^x + C && \text{using Step 2}\\
  &= (5x^2 - (10x - 10))e^x + C && \text{pull out common factor of $e^x$}\\
  &= (5x^2 - 10x + 10)e^x + C && \text{simplify}
\end{align*}
```

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $5x^2e^x$ is the derivative of $(5x^2 - 10x + 10)e^x$.

\begin{align*}
\frac{d}{dx} (5x^2 - 10x + 10)e^x
&= (10x - 10)e^x + (5x^2 - 10x +10)e^x && \text{product rule} \\
&= (10x - 10 + 5x^2 - 10x + 10)e^x && \text{pull out common factor of $e^x$}\\
&= 5x^2e^x && \text{simplify}
\end{align*}
```
`````
