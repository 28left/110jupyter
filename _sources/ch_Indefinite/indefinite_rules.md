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
# Basic Rules of Integration

## The Rules


```{admonition} Formulas of Integration
:class: info

\begin{align*}
&\text{Integral of a Constant, for any real $k$} && \int k ~dx  = kx + C \\ \\ 
&\text{Integral of $x^n$, for any real $n\neq -1$} && \int x^n ~dx  = \frac{x^{n+1}}{n+1} + C \\ \\
&\text{Integral of $1/x$} && \int \frac{1}{x} ~dx = \ln|x| + C \\ \\ 
&\text{Integral of $e^{x}$} && \int e^{x} ~dx = e^{x} + C  \\ \\
&\text{Integral of $e^{ax}$, for any real $a\neq 0$} && \int e^{ax} ~dx = \frac{1}{a}e^{ax} + C  
\end{align*}
```


```{admonition} Rules of Integration
:class: info

\begin{align*}
&\text{Constant Multiple Rule} && \int cf(x) ~dx  = c \int f(x) ~dx \\ \\
&\text{Sum/Difference Rule} && \int f(x) \pm g(x) ~dx = \int f(x) ~dx \pm \int g(x) ~dx\\ \\
&\text{Substitution Rule, $u=g(x)$, $du=g'(x)~dx$} && \int f(g(x)) g'(x) ~dx = \int f(u) ~du 
\end{align*}
```


<!--
```{admonition} Integral of a Constant
:class: info

For any real number $k$,

$$\int k ~dx = kx + C$$
```

```{admonition} The Power Rule
:class: info

For any real number $n\neq -1$,

$$\int x^n ~dx = \frac{x^{n+1}}{n+1} + C$$
```

```{admonition} The Constant Multiple Rule
:class: info

For any real number $k$,

$$\int kf(x) ~dx = k\int f(x) ~dx$$
```

```{admonition} The Sum Rule
:class: info

$$\int f(x)\pm g(x) ~dx = \int f(x) ~dx \pm \int g(x) ~dx$$
```

```{admonition} Integral of $e^x$
:class: info

For any real number $a\neq 0$,

$$\int e^x ~dx = e^x + C ~~~~~ \text{and} ~~~~~ \int e^{ax} ~dx = \frac{e^{ax}}{a} + C$$
```

```{admonition} Integral of $1/x$
:class: info

$$\int \frac{1}{x} ~dx = \ln|x| + C$$
```

```{admonition} The Substitution Rule
:class: info

If $u=g(x)$ and $du = g'(x) ~dx$ then

$$\int f(g(x))g'(x) ~dx = \int f(u) ~du$$
```
-->


### Example 1
````{admonition} Integral of a constant
:class: tip

Compute $\displaystyle \int 13 ~dz$.

```{dropdown} **Step 1:** &nbsp; Notice the differential $dz$.

This indicates that we are looking for a function of $z$, $f(z)$, such that $f'(z) = 13$.
```

```{dropdown} **Step 2:** &nbsp; Recall the formula for the integral of a constant.

$$\int k ~dx = kx + C$$
```

```{dropdown} **Step 3:** &nbsp; Apply the rule with $k = 13$.

Therefore,

$$\int 13 ~dz = 13z + C$$

In other words, every function of $z$ with derivative equal to $13$ can be written in the form $13z + C$ for some constant $C$.
```


```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $13$ is the derivative of $13z$.

$$\frac{d}{dz} 13z = 13$$
```
````

### Example 2
````{admonition} Integral of a power function
:class: tip

Compute $\displaystyle \int  x^7 ~dx$.

```{dropdown} **Step 1:** &nbsp; Recall the power rule.

For any real number $n\neq -1$,

$$\int x^n ~dx = \frac{x^{n+1}}{n+1} + C$$
```

```{dropdown} **Step 2:** &nbsp; Apply the power rule with $n = 7$.

\begin{align*}
  \int x^7  dx 
  &= \frac{x^{7+1}}{7+1} + C \\
  &= \frac{x^8}{8} + C 
\end{align*}
```

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $x^7$ is the derivative of $\dfrac{x^8}{8}$.

\begin{align*}
\frac{d}{dx} \frac{x^8}{8} 
&= \frac{d}{dx} \frac{1}{8}x^8 \\ 
&= \frac{1}{8} \frac{d}{dx} x^8 \\ 
&= \frac{1}{8} 8x^7 \\ 
&= x^7
\end{align*}
```
````

### Example 3
````{admonition} Integral of a power function with rational exponent
:class: tip

Compute $\displaystyle \int \frac{1}{\sqrt{y}} ~dy$.

```{dropdown} **Step 1:** &nbsp; Rewrite the integrand in the appropriate form to apply the power rule.

$$\int  \frac{1}{\sqrt{y}} ~dy = \int  y^{-1/2} ~dy$$
```

```{dropdown} **Step 2:** &nbsp; Apply the power rule with $n = -1/2$.

\begin{align*}
  \int  y^{-1/2} ~dy 
  &=  \frac{y^{-1/2 + 1}}{-1/2 + 1} + C \\
  &=  \frac{y^{1/2}}{1/2} + C \\
  &= 2\sqrt{y} + C
\end{align*}
```

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $\dfrac{1}{\sqrt{y}}$ is the derivative of $2\sqrt{y}$.

\begin{align*}
\frac{d}{dy} 2\sqrt{y}
&= 2 \frac{d}{dy} y^{1/2} \\ 
&= 2 \frac{1}{2} y^{-1/2} \\ 
&= \dfrac{1}{\sqrt{y}} 
\end{align*}
```
````


### Example 4
````{admonition} Integral of a constant multiple of a power function
:class: tip

Compute $\displaystyle \int  4x^{7/3} ~dx$.

```{dropdown} **Step 1:** &nbsp; Recall the constant multiple rule.

For any real number $k$,

$$\int kf(x) ~dx = k\int f(x) ~dx$$
```

```{dropdown} **Step 2:** &nbsp; Apply the constant multiple rule with $k=4$.

\begin{align*}
  \int 4x^{7/3}  ~dx 
  &= 4\int x^{7/3} ~dx \\
  &= 4 \left(\frac{x^{7/3+1}}{7/3+1}\right) + C && \text{power rule with $n=7/3$}\\
  &= 4 \left( \frac{x^{10/3}}{10/3}\right) + C && \hbox{simplify} \\
  &= 4 \cdot \frac{3}{10} x^{10/3} + C \\
  &=  \frac{6}{5} x^{10/3} + C 
\end{align*}
```

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $4x^{7/3}$ is the derivative of $\dfrac{6}{5} x^{10/3}$.

\begin{align*}
\frac{d}{dx} \frac{6}{5} x^{10/3}
&= \frac{6}{5} \frac{d}{dx}  x^{10/3} \\ 
&= \frac{6}{5} \cdot \frac{10}{3}  x^{7/3} \\ 
&= 4x^{7/3} 
\end{align*}
```
````


### Example 5
````{admonition} Integral of a sum of power functions
:class: tip

Compute $\displaystyle \int 5t^3-\frac{10}{t^{6}}+4\sqrt{t} ~dt$.

```{dropdown} **Step 1:** &nbsp; Recall the sum and difference rule.

$$\int f(x)\pm g(x) ~dx = \int f(x) ~dx \pm \int g(x) ~dx$$
```

```{dropdown} **Step 2:** &nbsp; Apply the sum, difference and constant multiple rules.

\begin{align*}
  \int 5t^3-\frac{10}{t^{6}}+4\sqrt{t}  ~dt
  &= \int 5t^3 ~dt - \int \frac{10}{t^{6}} ~dt + \int 4\sqrt{t}  ~dt && \text{sum rule}\\
  &= 5\int t^3 ~dt - 10\int \frac{1}{t^{6}} ~dt + 4\int \sqrt{t}  ~dt && \text{constant multiple rule}\\
  &= 5\int t^3 ~dt - 10\int t^{-6} ~dt + 4\int t^{1/2} ~dt 
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Integrate each term and then simplify.

\begin{align*}
 
5\int t^3 ~dt - 10\int t^{-6} ~dt + 4\int t^{1/2} ~dt 
  &= 5\cdot \frac{t^4}{4} - 10\cdot \frac{t^{-5}}{-5} + 4\frac{t^{3/2}}{3/2} + C  && \hbox{power rule}\\
  &= \frac{5}{4}t^4 + 2t^{-5} + \frac{8}{3}t^{3/2} + C  && \hbox{simplify}
\end{align*}
```

```{dropdown} Check Our Work.
:color: light
:animate: fade-in

We can verify our answer by showing $5t^3-\dfrac{10}{t^{6}}+4\sqrt{t}$ is the derivative of $\dfrac{5}{4}t^4 + 2t^{-5} + \dfrac{8}{3}t^{3/2}$.

\begin{align*}
\frac{d}{dt} \left(\frac{5}{4}t^4 + 2t^{-5} + \frac{8}{3}t^{3/2} \right)
&=  \frac{5}{4}4t^3 + 2(-5)t^{-6} + \frac{8}{3}\cdot \frac{3}{2}t^{1/2} \\ 
&= 5t^3-\frac{10}{t^{6}}+4\sqrt{t}
\end{align*}
```
````





### Example 6
````{admonition} Integral of a polynomial divided by a power function
:class: tip

Compute $\displaystyle \int \frac{4x^9 - 15x^4 + 7x^3}{x^4} ~dx$.

```{dropdown} **Step 1:** &nbsp; Rewrite the integrand as a sum.

\begin{align*}
  \frac{4x^9-15x^4 + 7x^3}{x^4}
  &= \frac{4x^9}{x^4} -  \frac{15x^4}{x^4} + \frac{7x^3}{x^4}\\
  &= 4x^5 - 15 + \frac{7}{x}
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Apply the sum and constant multiple rules.


\begin{align*}
  \int \frac{4x^9 - 15x^4 + 7x^3}{x^4} ~dx 
  &= \int 4x^5 - 15 + \frac{7}{x} ~dx \\ \\
  &= \int 4x^5 ~dx - \int 15 ~dx + \int \frac{7}{x}~dx && \hbox{sum rule}\\ \\
  &= 4\int x^5 ~dx - \int 15 ~dx + 7\int \frac{1}{x}~dx && \hbox{constant multiple rule}
\end{align*}
```

```{dropdown} **Step 3:** &nbsp; Integrate each term and then simplify.

\begin{align*}
 
  4\int x^5 ~dx - \int 15 ~dx + 7\int \frac{1}{x}~dx 
  &= \frac{4x^6}{6} - 15x + 7\ln|x| + C && \text{integrate each term}\\ \\
  &= \frac{2x^6}{3} - 15x + 7\ln|x| + C && \text{simplify}\\
\end{align*}
```
````

### Example 7
````{admonition} Integral of an exponential function
:class: tip

Compute $\displaystyle \int e^{2x/5} ~dx$.

```{dropdown} **Step 1:** &nbsp; Recall the formula for the integral of $e^{ax}$ for $a\neq 0$.

$$\int e^{ax} ~dx = \frac{e^{ax}}{a} + C$$
```

```{dropdown} **Step 2:** &nbsp; Apply the formula for the integral of $e^{ax}$ with $a=2/5$.

\begin{align*}
  \int e^{2x/5} ~dx 
  &= \frac{e^{2x/5}}{2/5} + C\\ \\
  &= \frac{5}{2}e^{2x/5} + C
\end{align*}
```
````


### Example 8
````{admonition} Integral of a sum of functions
:class: tip

Compute $\displaystyle \int 3e^{2x}+\frac{8}{x}+\frac{4}{x^3} ~dx$.

```{dropdown} **Step 1:** &nbsp; Apply the sum and constant multiple rules.

\begin{align*}
  \int 3e^{2x}+\frac{8}{x}+\frac{4}{x^3} ~dx 
  &= \int 3e^{2x} ~dx + \int \frac{8}{x} ~dx + \int 4x^{-3}~dx  && \hbox{sum rule}\\ \\
  &= 3\int e^{2x} ~dx + 8\int \frac{1}{x} ~dx + 4\int x^{-3}~dx  && \hbox{constant multiple rule}
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Integrate each term and then simplify.

\begin{align*}
  
  &= 3\frac{e^{2x}}{2} + 8\int \frac{1}{x} ~dx + 4\int x^{-3}dx && \text{integral of $e^{ax}$}\\ \\
  &= 3\frac{e^{2x}}{2} + 8\ln|x| + 4\int x^{-3}dx && \text{integral of $1/x$}\\ \\
  &= 3\frac{e^{2x}}{2} + 8\ln|x| + \frac{4x^{-2}}{-2}+C && \text{power rule}\\ \\
  &=\frac{3}{2}e^{2x} + 8\ln|x| - \frac{2}{x^{2}}+C && \text{simplify}
\end{align*}
```

````


### Example 9
````{admonition} Integral of a product of functions
:class: tip

Compute $\displaystyle \int (e^{3x} + 1)(e^{-3x} - 1) ~dx$.

```{dropdown} **Step 1:** &nbsp; Rewrite the integrand as a sum.

\begin{align*}
  (e^{3x} + 1)(e^{-3x} - 1)
  &= e^{3x}e^{-3x} + e^{-3x} - e^{3x} - 1 && \hbox{FOIL}\\
  &= e^{3x-3x} + e^{-3x} - e^{3x} - 1 && \hbox{since $e^a e^b = e^{a+b}$}\\
  &= e^{0} + e^{-3x} - e^{3x} - 1\\
  &= 1 + e^{-3x} - e^{3x} - 1 && \hbox{since $e^0 = 1$}\\
  &= e^{-3x} - e^{3x} && \hbox{simplify}
\end{align*}
```

```{dropdown} **Step 2:** &nbsp; Apply the sum rule and then integrate each term.

\begin{align*}
  \int (e^{3x} + 1)(e^{-3x} - 1) ~dx
  &= \int e^{-3x} - e^{3x} ~dx \\
  &= \int e^{-3x} ~dx  - \int e^{3x} ~dx \\
  &= \frac{1}{-3} e^{-3x}  - \frac{1}{3} e^{3x} + C && \text{integral of $e^{ax}$}\\
  &= -\frac{1}{3}(e^{-3x} + e^{3x}) + C && \text{simplify}
\end{align*}
```
````