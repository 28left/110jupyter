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
# Riemann Sums and the Definite Integral

## Area Under a Curve and Riemann Sums

Consider trying to compute the area of a region (below left) between the graph of $y=f(x)$ and the $x$-axis on the interval $[a,b]$.

````{panels}

```{image} ../images/pic_definite_riemann_1.png
:alt: Area under $f(x)$ between a nd b
:align: center
```
---

```{image} ../images/pic_definite_riemann_2.png
:alt: Area under $f(x)$ between a nd b
:align: center
```

````


A *Riemann sum* uses rectangles (above right) to approximate the desired area in the following manner.  Start by selecting a value for $n$, which is the number of rectangles. Then break up the interval $[a,b]$ into $n$ subintervals, each having width $\Delta x = (b-a)/n$.  Each subinterval corresponds to the base of a rectangle where $\Delta x$ is the width of the rectangle. Next, pick one value, $x_i$, from each subinterval, and evaluate $f(x_i)$ to determine the height of the corresponding rectangle.

The total area of the $n$ rectangles is given by

$$[f(x_1) + f(x_2) + \cdots + f(x_n)] \Delta x$$

which is called a {\it Riemann Sum}. It approximates the area of the region between the graph of $y=f(x)$ and the $x$-axis on the interval $[a,b]$.

Here are several different ways to select the values $x_1,\ldots,x_n$.

- **Right Riemann Sum**: $x_1,\ldots, x_n$ are the right endpoints of the $n$ subintervals.
- **Left Riemann Sum**: $x_1,\ldots, x_n$ are the left endpoints of the $n$ subintervals.
- **Midpoint Rule**: $x_1,\ldots, x_n$ are the midpoints of the $n$ subintervals.

In general, a Riemann sum approximates the value of a definite integral (see below).

## The Limit Definition of a Definite Integral

```{admonition} Definition
:class: info

Suppose $f$ is a continuous function on $[a,b]$.  The **definite integral** of $f$ from $a$ to $b$, denoted by $\int_a^b f(x) ~dx$, is defined as

$$\int_a^b f(x) ~dx = \lim_{n\to \infty} [f(x_1) + f(x_2) + \cdots + f(x_n)] \Delta x$$

where the values of $x_1,x_2,\ldots, x_n$ are chosen from the $n$ subintervals of $[a,b]$ of equal width $\Delta x = \dfrac{b-a}{n}$.

The values $a$ and $b$ are referred to as **limits of integration**.
```

## Geometric Interpretation of the Definite Integral

If $f(x)\geq 0$ is continuous on $[a,b]$, then $\int_a^b f(x) ~dx$ is equal to the area of the region between the graph of $f$ and the $x$-axis on $[a,b]$.

```{image} ../images/pic_definite_riemann_3.png
---
alt: The definite integral as area under a curve
align: center
width: 600px
---
```

In general, $\int_a^b f(x) ~dx$ can be interpreted as the area of the regions that are below the graph of $f$ and above the $x$-axis minus the area of the regions that are below the $x$-axis and above the graph of $f$.

```{image} ../images/pic_definite_riemann_4.png
---
alt: Areas above and below the x-axis and their impact on the integral
align: center
width: 600px
---
```

$$\int_a^b f(x) ~dx = \hbox{Area of $R_1$} - \hbox{Area of $R_2$} + \hbox{Area of $R_3$}$$




## Properties of the Definite Integral

```{admonition} Properties of the Definite Integral
:class: info

If $f$ and $g$ are continuous on $[a,b]$ and $c$ is a constant, then

- $\displaystyle \int_a^a f(x) ~dx = 0$
- $\displaystyle \int_a^b f(x) ~dx = -\int_b^af(x) ~dx$
- $\displaystyle \int_a^b cf(x) ~dx = c\int_a^b f(x) ~dx$
- $\displaystyle \int_a^b f(x) \pm g(x) ~dx = \int_a^b f(x) ~dx \pm \int_a^b g(x) ~dx$
- $\displaystyle \int_a^b f(x) ~dx = \int_a^c f(x) ~dx + \int_c^b f(x) ~dx$
```




## Example 1

```{admonition} Computing Riemann sums
:class: tip

Use a right Riemann sum, left Riemann sum, and midpoint rule to approximate the area under the graph of $y=x^2$ on $[1,3]$ using 4 subintervals.
```

````{dropdown} **Step 1:** Find the length of each interval, $\Delta x$, and break up $[1,3]$ into 4 subintervals of length $\Delta x$.
:animate: fade-in


$$\Delta x = \frac{b - a}{n} = \frac{3 - 1}{4} = \frac{1}{2}.$$

The endpoints of the subintervals are labeled below the number line while the midpoints of each subinterval are labeled above the number line. Each midpoint is calculated by computing the average of the two endpoints of the corresponding subinterval.

```{image} ../images/pic_definite_riemann_5.png
---
alt: Riemann partition of the integration interval
align: center
class: bg-light
width: 500px
---
```
````

````{dropdown} **Step 2:** Use a right Riemann sum to approximate the area. 
:animate: fade-in


\begin{align*}
  \hbox{Area} &\approx \left[ f(3/2) + f(2) + f(5/2) + f(3)\right]\Delta x \\
  &= \left[\left(\frac{3}{2}\right)^2 + 2^2 + \left(\frac{5}{2}\right)^2 + 3^2 \right] \frac{1}{2}\\
  &= \left[\frac{9}{4} + \frac{16}{4} + \frac{25}{4} + \frac{36}{4}\right] \frac{1}{2}\\
  % &= \frac{1}{2}\cdot \frac{86}{4} \\
  &= 43/4
\end{align*}

```{image} ../images/pic_definite_riemann_6.png
---
alt: Right Riemann sum
align: center
class: bg-light
width: 300px
---
```

Therefore, the area under the graph of $y=x^2$ on $[1,3]$ is approximately $43/4 = 10.75$.
````



````{dropdown} **Step 3:** Use a left Riemann sum to approximate the area.
:animate: fade-in


\begin{align*}
  \hbox{Area} &\approx \left[ f(1) + f(3/2) + f(2) + f(5/2)\right] \Delta x \\
  &= \left[1^2 + \left(\frac{3}{2}\right)^2 + 2^2 + \left(\frac{5}{2}\right)^2 \right] \frac{1}{2} \\
  &= \left[\frac{4}{4} + \frac{9}{4} + \frac{16}{4} + \frac{25}{4}\right]\frac{1}{2} \\
  %&= \frac{1}{2}\cdot \frac{54}{4} \\
  &= 27/4
\end{align*}

```{image} ../images/pic_definite_riemann_7.png
---
alt: Right Riemann sum
align: center
class: bg-light
width: 300px
---
```

Therefore, the area under the graph of $y=x^2$ on $[1,3]$ is approximately $27/4 = 6.75$.
````


````{dropdown} **Step 4:** Use the midpoint rule to approximate the area.
:animate: fade-in


\begin{align*}
  \hbox{Area} &\approx \left[ f(5/4) + f(7/4) + f(9/4) + f(11/4)\right]\Delta x \\
  &= \left[\left(\frac{5}{4}\right)^2 + \left(\frac{7}{4}\right)^2 + \left(\frac{9}{4}\right)^2 + \left(\frac{11}{4}\right)^2 \right] \frac{1}{2} \\
  &= \left[\frac{25}{16} + \frac{49}{16} + \frac{81}{16} + \frac{121}{16}\right] \frac{1}{2} \\
  %&= \frac{1}{2}\cdot \frac{276}{16} \\
  &= 69/8
\end{align*}

```{image} ../images/pic_definite_riemann_8.png
---
alt: Midpoint rule
align: center
class: bg-light
width: 300px
---
```

Therefore, the area under the graph of $y=x^2$ on $[1,3]$ is approximately $69/8 = 8.625$.
````

