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



````{admonition} Computing the Area between Two Curves
:class: info

Suppose $f$ and $g$ are continuous functions with $f(x) \geq g(x)$ on $[a,b]$.

```{figure} ../images/pic_applicationintegrals_area_between_curves_1.png
---
width: 600px
---
Area between two curves
```
```{dropdown} Long Text Description

There is a horizontal x axis with the points a and b labeled, and a vertical y axis with no points labeled. The graphs of two functions are plotted. One, labeled f(x), is above the other, labeled g(x). The curve representing f(x) goes up and down with its concavity downward and then upward moving from left to right. The curve representing g(x) goes down and then up, with its concavity always up. The region between the curves, starting at x value a and ending at x value b, is shaded yellow and labeled R.
```

Then the area of the region, $R$, bounded above by $y=f(x)$ and below by $y=g(x)$ on $[a,b]$ is given by

$$\int_a^b f(x)-g(x) ~dx.$$
````


```{admonition} How to Find the Area Between Two Curves
:class: note

It's extremely important to draw the region in question to make sure the above formula is applied correctly. While it's not necessary to draw each curve using all of the techniques built up in the section on {ref}`cur:sketching`, the curves should be drawn with enough detail to clearly identify the top and bottom functions and the corresponding boundaries.

The following guidelines should be applied to make sure the area of the region is computed correctly.

- Find all points of intersection of $f(x)$ and $g(x)$ on $[a,b]$.
- Use the points of intersection and the values of $f(x)$ and $g(x)$ at the endpoints to help sketch the region.
- Break up the given interval at the points of intersection.
- Determine which function is larger on each subinterval.
- Calculate the area of each subregion using the formula above.
- Combine the areas of the different subregions.
```


### Example 1

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
```{dropdown} Long Text Description
There is a horizontal x-axis with points labeled one, two, six, and seven, and a y axis with no points labeled. Parts of the graphs of two functions are plotted. One, labeled f(x), begins at x=1 above the other, labeled g(x), the two meet at x = 2, g(x) is above f(x) until the two meet again at x=6, after which f(x) is once again above g(x). The region between both curves, starting at x=1 and ending at x=7 is shaded yellow.
```


```{dropdown} **Step 1:** &nbsp; Find the points of intersection.

Notice that the functions intersect each other at $x=2$ and $x=6$. Therefore, we need to break up the original interval, $[1,7]$, into the following subintervals

$$[1,2], ~[2,6], ~\hbox{and} ~[6,7].$$
```

```{dropdown} **Step 2:** &nbsp; Determine which function is larger on each subinterval and calculate the area of each subregion.
 
- $[1,2]$: On this interval, $f(x) \geq g(x)$.  Therefore, the area of the region bounded by $f(x)$ and $g(x)$ on $[1,2]$ is 
    
    $$\int_1^2 f(x) - g(x) ~dx.$$

- $[2,6]$: On this interval, $g(x) \geq f(x)$.  Therefore, the area of the region bounded by $f(x)$ and $g(x)$ on $[2,6]$ is 

    $$\int_2^6 g(x) - f(x) ~dx.$$

- $[6,7]$: On this interval, $f(x) \geq g(x)$. Therefore, the area of the region bounded by $f(x)$ and $g(x)$ on $[6,7]$ is 

  $$\int_6^7 f(x) - g(x) ~dx.$$
```

```{dropdown} **Step 3:** &nbsp; Combine the areas of the different subregions.


The area of the region described above is given by

$$\int_1^2 f(x) - g(x)~dx + \int_2^6 g(x) - f(x) ~dx + \int_6^7 f(x)-g(x)~dx.$$
```
````


### Example 2

`````{admonition} Area between two curves on given interval
:class: tip

Find the area of the region bounded by $y = x^2-x$ and $y = 2$ on the interval $[0, 3]$.



```{dropdown} **Step 1:** &nbsp; Find the points of intersection.

The two curves intersect each other when $x^2-x = 2$, or equivalently when

$$x^2 - x - 2 = (x-2)(x+1)$$

equals zero, which happens when $x=2$ and $x=-1$. Notice that $x=-1$ is not relevant since it is not on the interval $[0,3]$.

```

````{dropdown} **Step 2:** &nbsp; Use the points of intersection to help sketch the region.

```{image} ../images/pic_applicationintegrals_area_between_curves_3.png
---
alt: Point of intersection of the two curves
width: 500px
align: center
---
```
```{dropdown} Long Text Description
There is a horizontal x axis with points labeled one, two, and three, and a vertical y axis with no points labeled. The graphs of two functions are plotted. The first is the constant function y = 2, which begins above the second which is y=x^2-x. The second, quadratic, function begins below the first function, dips below the x axis, and meets the second function at x = 2, and is above it to the right of x=2. The region where x^2-x < 2, beginning at x=0 and ending at x=2, is shaded yellow and labeled R_1, and the region where x^2-x > 2, beginning at x=2 and ending at x=3, is shaded yellow and labeled R_2.
```
````



```{dropdown} **Step 3:** &nbsp; Calculate the area of each subregion.

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

```{dropdown} **Step 4:** &nbsp; Combine the areas of the different subregions.

The area of the region bounded by $y = x^2-x$ and $y = 2$ on $[0, 3]$ is 

$$\frac{10}{3} + \frac{11}{6} = 31/6.$$
```

```{admonition} Caution
:class: warning

Because the relative position of the curves change at the point of intersection, the area of the region cannot be computed via a single definite integral like the following:

$$\displaystyle \int_0^3 2 - (x^2-x) ~dx  = 3/2.$$ 

This underscores the importance of drawing the region **before** setting up the integral.
```
`````


### Example 3

`````{admonition} Area enclosed by three curves
:class: tip

Find the area of the bounded region enclosed by $y=\dfrac{2}{\sqrt{x}}$, $y= \dfrac{2}{x^3}$, and $x=2$.

```{dropdown} **Step 1:** &nbsp; Find the points of intersection.

\begin{align*}
  \frac{2}{\sqrt{x}} &= \frac{2}{x^3} && \text{set the equations equal to each other}\\
  2x^3 &= 2\sqrt{x} && \text{cross multiply}\\
  x^3&=\sqrt{x} && \text{divide both sides by 2}\\
  x^\frac{5}{2} &= 1 && \text{divide both sides by }\sqrt{x}\\
  x&=1 && \hbox{raise both sides to the power of $2/5$}
\end{align*}

Therefore, the curves intersect only when $x=1$.  And since only one vertical line, $x=2$, was given that bounds the region, we must use the point of intersection at $x=1$ as the other vertical line that bounds the region.

```


````{dropdown} **Step 2:** &nbsp; Use the points of intersection to help sketch the region.


```{image} ../images/pic_applicationintegrals_area_between_curves_4.png
---
alt: Point of intersection at $x=1$
width: 500px
align: center
---
```
```{dropdown} Long Text Description
There is a horizontal x-axis with the points 1 and 2 labeled, and a vertical y-axis with no points labeled. The graphs of two decreasing, concave up functions are plotted. The first function, y=2/x^3, begins above the second, 2/sqrt(2). The two meet at x=1 and to the right of x=1 y=2/sqrt(x) is above y=2/x^3. The region between the two functions from x=1 and x=2 is shaded yellow and is not labeled.

```
````

```{dropdown} **Step 3:** &nbsp; Calculate the area of the region.

Note that $\dfrac{2}{\sqrt{x}} \geq \dfrac{2}{x^3}$ on $[1,2]$ and therefore the area of the region is given by $\displaystyle \int_1^2 \frac{2}{\sqrt{x}} - \frac{2}{x^3} ~dx$.

\begin{align*}
  \int_1^2 \frac{2}{\sqrt{x}} - \frac{2}{x^3} ~dx
  &= \int_1^2 2x^{-1/2} - 2x^{-3} ~dx \\
  &= \left(2\frac{x^{1/2}}{1/2} - 2 \frac{x^{-2}}{-2} \right) \Biggr|_1^2 && \text{power rule}\\
  &= \left(4\sqrt{x} + \frac{1}{x^2} \right) \Biggr|_1^2 && \text{simplify}\\
  &= \left(4 \sqrt{2} + \frac{1}{4}\right) - (4 + 1) \\
  &= 4 \sqrt{2} - \frac{19}{4}
\end{align*}

Therefore, the area of the region bounded by $y=12\sqrt{x}$, $y=2/x^3$, and $x=2$ is $4 \sqrt{2} - 19/4$.
```
`````

### Example 4

`````{admonition} Area enclosed by two curves with two points of intersection
:class: tip

Find the area of the bounded region enclosed by $y=x$ and $y=x^2$.


```{dropdown} **Step 1:** &nbsp; Find the points of intersection.

\begin{align*}
  x&=x^2 && \text{set the two functions equal to each other}\\
  0&=x^2-x && \text{move everything to one side}\\
  0&=x(x-1) && \text{factor}
\end{align*}

Therefore, the curves intersect when $x=0$ and when $x=1$.

Notice that the points of intersection will be used as the left and right boundaries of our region.
```



````{dropdown} **Step 2:** &nbsp; Use the points of intersection to help sketch the region.

```{image} ../images/pic_applicationintegrals_area_between_curves_5.png
---
alt: Points of intersection at $x=0$ and $x=1$
width: 500px
align: center
---
```
```{dropdown} Long Text Description
There is a horizontal x axis with the point 1 labeled and a vertical y axis with no points labeled. The graphs of two functions are plotted. The first function, the increasing linear function y=x is above the other function, the increasing quadratic function y=x^2, from the y axis to x=1. The region between the two functions from the y axis to x=1 in shaded yellow and is not labeled.
```
````

```{dropdown} **Step 3:** &nbsp; Calculate the area of the region.

Note that $x \geq x^2$ on $[0,1]$ and therefore the area of the region is given by $\displaystyle \int_0^1 x-x^2 ~dx$.

\begin{align*}
  \int^1_0 x-x^2 ~dx
  &= \left(\frac{x^2}{2} - \frac{x^3}{3}\right)\Biggr|^1_0 && \text{compute the antiderivative}\\
  &= \left(\frac{1^2}{2} - \frac{1^3}{3}\right)-\left(\frac{0^2}{2} + \frac{0^3}{3}\right) && \text{plug in the limits of integration}\\
  &= \frac{1}{2} - \frac{1}{3} \\
  &= 1/6
\end{align*}

Therefore, the area of the region bounded by $y=x$ and $y=x^2$ is $1/6$.
```
`````



### Example 5

`````{admonition} Area enclosed by two curves with three points of intersection
:class: tip

Find the area of the bounded region enclosed by $y = x^3$ and $y = 4x$.



```{dropdown} **Step 1:** &nbsp; Find the points of intersection.

\begin{align*}
  x^3 &= 4x && \text{set the functions equal to each other}\\
  x^3 - 4x &= 0 && \text{subtract $4x$ from both sides}\\
  x(x^2-4) &= 0 && \text{factor out an }x\\
  x(x-2)(x+2) &= 0 && \text{factor } x^2 - 4
\end{align*}

Therefore, the curves intersect when $x=-2$, when $x=0$, and when $x=2$.  
```



````{dropdown} **Step 2:** &nbsp; Use the points of intersection to help sketch the region.


```{image} ../images/pic_applicationintegrals_area_between_curves_6.png
---
alt: Points of intersection at $x=-2$, $x=0$, and $x=2$
width: 500px
align: center
---
```
```{dropdown} Long Text Description
There is a horizontal x axis with the points -2 and 2 labeled and a vertical y axis with no points labeled. The graphs of two functions are plotted. The increasing linear function 4x is below the increasing cubic function y=x^3 from x=-2 to the y-axis, and it is above the cubic function from the y-axis to x=2. The area between the curves from x=-2 to the y axis is labeled R_1 and is shaded yellow. The area between the curves from the y axis to x=2 is labeled R_2 and is shaded yellow.
```
````



```{dropdown} **Step 3:** &nbsp; Calculate the area of each subregion.


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

```{dropdown} **Step 3:** &nbsp; Combine the areas of the different subregions.

The area of the region bounded by the curves $y = x^3$ and $y = 4x$ is 

$$4 + 4 = 8.$$
```
`````