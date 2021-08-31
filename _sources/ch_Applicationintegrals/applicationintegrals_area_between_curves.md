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
# Area Between Two Curves

## Computing the Area of a Region Bounded by Two Curves


```{figure} ../images/pic_applicationintegrals_area_between_curves_1.png
---
width: 600px
---
Area between two curves
```

```{admonition} Computing the Area between Two Curves
:class: info

Suppose $f$ and $g$ are continuous functions with $f(x) \geq g(x)$ on $[a,b]$.

Then the area of the region, $R$, bounded above by $y=f(x)$ and below by $y=g(x)$ on $[a,b]$ is given by

$$\int_a^b f(x)-g(x) ~dx.$$
```


## When Finding the Area Between Two Curves

It's extremely important to draw the region in question to make sure the above formula is applied correctly. While it's not necessary to draw each curve using all of the techniques built up in the Curve Sketching packet, the curves should be drawn with enough detail to clearly identify the top and bottom functions and the corresponding boundaries.

The following guidelines should be applied to make sure the area of the region is computed correctly.

- Find all points of intersection of $f(x)$ and $g(x)$ on $[a,b]$.
- Use the points of intersection and the values of $f(x)$ and $g(x)$ at the endpoints to help sketch the region.
- Break up the given interval at the points of intersection.
- Determine which function is larger on each subinterval.
- Calculate the area of each subregion using the formula above.
- Combine the areas of the different subregions.

## Example 1

````{admonition} Area between two curves on given interval
:class: tip

Find a sum of integrals that represents the area of the region bounded by $y=f(x)$ and $y=g(x)$ on $[1,7]$ as shown below.

```{image} ../images/pic_applicationintegrals_area_between_curves_2.png
---
alt: Area between $f(x)$ and $g(x)$ on interval $[1,7]$
width: 500px
align: center
---
```
````

```{dropdown} **Step 1:** Find the points of intersection.

Notice that the functions intersect each other at $x=2$ and $x=6$. Therefore, we need to break up the original interval, $[1,7]$, into the following subintervals

$$[1,2], ~[2,6], ~\hbox{and} ~[6,7].$$
```

```{dropdown} **Step 2:** Determine which function is larger on each subinterval and calculate the area of each subregion.
 
- $[1,2]$: On this interval, $f(x) \geq g(x)$.  Therefore, the area of the region bounded by $f(x)$ and $g(x)$ on $[1,2]$ is 
    
    $$\int_1^2 f(x) - g(x) ~dx.$$

- $[2,6]$: On this interval, $g(x) \geq f(x)$.  Therefore, the area of the region bounded by $f(x)$ and $g(x)$ on $[2,6]$ is 

    $$\int_2^6 g(x) - f(x) ~dx.$$

- $[6,7]$: On this interval, $f(x) \geq g(x)$. Therefore, the area of the region bounded by $f(x)$ and $g(x)$ on $[6,7]$ is 

  $$\int_6^7 f(x) - g(x) ~dx.$$
```

```{dropdown} **Step 3:** Combine the areas of the different subregions.


The area of the region described above is given by

$$\int_1^2 f(x) - g(x)~dx + \int_2^6 g(x) - f(x) ~dx + \int_6^7 f(x)-g(x)~dx.$$
```

## Example 2

```{admonition} Area between $y = x^2-x$ and $y = 2$ on given interval
:class: tip

Find the area of the region bounded by $y = x^2-x$ and $y = 2$ on the interval $[0, 3]$.
```


````{dropdown} **Step 1:** Find the points of intersection and use them to help sketch the region.

The two curves intersect each other when $x^2-x = 2$, or equivalently when

$$x^2 - x - 2 = (x-2)(x+1)$$

equals zero, which happens when $x=2$ and $x=-1$. Notice that $x=-1$ is not relevant since it is not on the interval $[0,3]$.

```{image} ../images/pic_applicationintegrals_area_between_curves_3.png
---
alt: Point of intersection of the two curves
width: 500px
align: center
---
```
````

```{dropdown} **Step 2:** Calculate the area of each subregion.

- Area of region $R_1$. Note that $2\geq x^2 - x$ on $[0,2]$. 

\begin{align*}
  \int_{0}^2 2 - (x^2 - x) ~dx
  &= \int_{0}^2 2 - x^2 + x ~dx\\
  &= \left( 2x - \frac{x^3}{3} + \frac{x^2}{2} \right) \Biggr|_{0}^2 \\
  &= \left( 4 - \frac{8}{3} + \frac{4}{2} \right) - \left( 0 - 0 + 0 \right) = 10/3
\end{align*}

- Area of region $R_2$. Note that $x^2 - x\geq 2$ on $[2,3]$. 

\begin{align*}
  \int_{2}^3 (x^2 - x) - 2 ~dx
  &= \int_{2}^3 x^2 - x - 2 ~dx\\
  &= \left( \frac{x^3}{3} - \frac{x^2}{2} - 2x \right) \Biggr|_{2}^3 \\
  &= \left( \frac{27}{3} - \frac{9}{2} - 6\right) - \left(\frac{8}{3} - \frac{4}{2} - 4\right) = 11/6
\end{align*}
```

```{dropdown} **Step 3:** Combine the areas of the different subregions.

The area of the region bounded by $y = x^2-x$ and $y = 2$ on $[0, 3]$ is $\frac{10}{3} + \frac{11}{6} = 31/6.$
```

```{admonition} Observation
:class: warning

Observe that the area of the region is not equal to $\int_0^3 2 - (x^2-x) ~dx  = 3/2$. This underscores the importance of drawing the region **before** setting up the integral.
```

## Example 3

```{admonition} Area enclosed by three curves
:class: tip

Find the area of the bounded region enclosed by $y=\dfrac{2}{\sqrt{x}}$, $y= \dfrac{2}{x^3}$, and $x=2$.
```

````{dropdown} **Step 1:** Find the points of intersection and use them to help sketch the region.

\begin{align*}
  \frac{2}{\sqrt{x}} &= \frac{2}{x^3} && \text{Set the equations equal to each other}\\
  2x^3 &= 2\sqrt{x} && \text{Cross multiply}\\
  x^3&=\sqrt{x} && \text{Divide both sides by 2}\\
  x^\frac{5}{2} &= 1 && \text{Divide both sides by }\sqrt{x}\\
  x&=1 && \hbox{Raise both sides to the power of $2/5$}
\end{align*}

Therefore, the curves intersect only when $x=1$.  And since only one vertical line, $x=2$, was given that bounds the region, we must use the point of intersection at $x=1$ as the other vertical line that bounds the region.

```{image} ../images/pic_applicationintegrals_area_between_curves_4.png
---
alt: Point of intersection at $x=1$
width: 500px
align: center
---
```
````

```{dropdown} **Step 2:** Calculate the area of the region.

Note that $\dfrac{2}{\sqrt{x}} \geq \dfrac{2}{x^3}$ on $[1,2]$ and therefore the area of the region is given by $\int_1^2 \frac{2}{\sqrt{x}} - \frac{2}{x^3} ~dx$.

\begin{align*}
  \int_1^2 \frac{2}{\sqrt{x}} - \frac{2}{x^3} ~dx
  &= \int_1^2 2x^{-1/2} - 2x^{-3} ~dx \\
  &= \left(2\frac{x^{1/2}}{1/2} - 2 \frac{x^{-2}}{-2} \right) \Biggr|_1^2 && \hbox{Power rule}\\
  &= \left(4\sqrt{x} + \frac{1}{x^2} \right) \Biggr|_1^2 && \hbox{Simplify}\\
  &= \left(4 \sqrt{2} + \frac{1}{4}\right) - (4 + 1) \\
  &= 4 \sqrt{2} - \frac{19}{4}
\end{align*}

Therefore, the area of the region bounded by $y=12\sqrt{x}$, $y=2/x^3$, and $x=2$ is $4 \sqrt{2} - 19/4$.
```

## Example 4

```{admonition} Area enclosed by two curves with two points of intersection
:class: tip

Find the area of the bounded region enclosed by $y=x$ and $y=x^2$.
```


````{dropdown} **Step 1:** Find the points of intersection and use them to help sketch the region.

\begin{align*}
  x&=x^2 && \text{Set the two functions equal to each other}\\
  0&=x^2-x && \text{Move everything to one side}\\
  0&=x(x-1) && \text{Factor}
\end{align*}

Therefore, the curves intersect when $x=0$ and when $x=1$.

Notice that the points of intersection are used as the left and right boundaries of our region.


```{image} ../images/pic_applicationintegrals_area_between_curves_5.png
---
alt: Points of intersection at $x=0$ and $x=1$
width: 500px
align: center
---
```
````


```{dropdown} **Step 2:** Calculate the area of the region.

Note that $x \geq x^2$ on $[0,1]$ and therefore the area of the region is given by $\int_0^1 x-x^2 ~dx$.

\begin{align*}
  \int^1_0 x-x^2 ~dx
  &= \left(\frac{x^2}{2} - \frac{x^3}{3}\right)\Biggr|^1_0 && \text{Compute the antiderivative}\\
  &= \left(\frac{1^2}{2} - \frac{1^3}{3}\right)-\left(\frac{0^2}{2} + \frac{0^3}{3}\right) && \text{Plug in the limits of integration}\\
  &= \frac{1}{2} - \frac{1}{3} \\
  &= 1/6
\end{align*}

Therefore, the area of the region bounded by $y=x$ and $y=x^2$ is $1/6$.
```

## Example 5

```{admonition} Area enclosed by two curves with three points of intersection
:class: tip

Find the area of the bounded region enclosed by $y = x^3$ and $y = 4x$.
```



````{dropdown} **Step 1:** Find the points of intersection and use them to help sketch the region.

\begin{align*}
  x^3 &= 4x && \text{Set the functions equal to each other}\\
  x^3 - 4x &= 0 && \text{Subtract $4x$ from both sides}\\
  x(x^2-4) &= 0 && \text{Factor out an }x\\
  x(x-2)(x+2) &= 0 && \text{Factor } x^2 - 4
\end{align*}

Therefore, the curves intersect when $x=-2$, when $x=0$, and when $x=2$.  

```{image} ../images/pic_applicationintegrals_area_between_curves_6.png
---
alt: Points of intersection at $x=-2$, $x=0$, and $x=2$
width: 500px
align: center
---
```
````


```{dropdown} **Step 2:** Calculate the area of each subregion.


- Area of region $R_1$. Note that $x^3\geq 4x$ on $[-2,0]$. 

\begin{align*}
  \int^0_{-2} x^3-4x ~dx
  &= \left(\frac{x^4}{4} - 2x^2\right)\Biggr|^0_{-2} \\
  &= \left(\frac{0^4}{4} - 2(0)^2\right)-\left(\frac{(-2)^4}{4}- 2(-2)^2\right) \\
  &= 0 - (4-8) = 4 
\end{align*}

- Area of region $R_2$. Note that $4x\geq x^3$ on $[0,2]$. 

\begin{align*}
  \int^2_{0} 4x-x^3 ~dx
  &= \left(2x^2 -\frac{x^4}{4} \right)\Biggr|^2_{0} \\
  &= \left(2(2)^2 - \frac{2^4}{4}\right)-\left(2(0)^2 - \frac{0^4}{4}\right) \\
  &= (8-4) - 0 = 4 
\end{align*}
```

```{dropdown} **Step 3:** Combine the areas of the different subregions.

The area of the region bounded by the curves $y = x^3$ and $y = 4x$ on the interval $[-1, 3]$ is 

$$4 + 4 = 8.$$
```