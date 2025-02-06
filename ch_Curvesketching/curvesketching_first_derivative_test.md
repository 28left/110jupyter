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
# The First Derivative Test

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

(curve:first_derivative_test)=
## Using the First Derivative to Classify Critical Points


```{admonition} The First Derivative Test
:class: info

Suppose $c$ is a critical point of the continuous function $f$.

1. If $f'(x)$ changes sign **from positive to negative** at $x=c$, then $f(c)$ is a **relative maximum**.
2. If $f'(x)$ changes sign **from negative to positive** at $x=c$, then $f(c)$ is a **relative minimum**. 
3. If $f'(x)$ **does not change sign** at $x=c$, then $f(c)$ is **not a relative extrema.** 
```

### Example 1
````{admonition} Classify critical points based on graph of the first derivative
:class: tip

The following graph corresponds to $f'(x)$, the first derivative of $f(x)$.  

Using the graph of $f'(x)$, find and classify all critical points of $f(x)$.  You may assume that $f'(x)$ is continuous for all $x$ and $f'(x) = 0$ only when $x=-2$, $x=1$, and $x=3$.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_curvesketching_firstderivativetest_3.png
:alt: Graph of $y = f'(x)$
```
:::
::::
```{dropdown} Long Text Description
The graph of the derivative of a continuous function on the interval (-3,4).  The derivative is equal to zero at x = -2, x = 1, and x = 3.  The derivative decreases on the interval (-3,-1.2), increases on the interval (-1.2,1), decreases on the interval (1,2.4), and increases on the interval (2.4,4).
```

```{dropdown} **Step 1:** &nbsp; Determine the critical points of $f$.

Since $f'(x)$ is continuous for all $x$, and therefore defined for all $x$, the only critical points of $f$ occur where $f'(x) = 0$.  And we were specifically told that the derivative is equal to zero only when $x=-2$, $x=1$, and $x=3$, so these are the three critical points of $f$.
```


```{dropdown} **Step 2:** &nbsp; Classify each critical point.

Since $f'(x)$ changes from positive to negative at $x=-2$, $f$ has a relative maximum at $x=-2$.

Since $f'(x)$ does not change sign at $x=1$, $f$ does not have a relative extrema at $x=1$.

Since $f'(x)$ changes from negative to positive at $x=3$, $f$ has a relative minimum at $x=3$.

```

````


### Example 2
`````{admonition} Classifying critical points using the first derivative test
:class: tip

In [Example 1](curvesketching_critical_points_example_1) of the previous section, we found that the critical points of 

$$f(x) = \sqrt[3]{x^2-1}$$ 

were $x=-1$, $x=0$, and $x=1$.
Classify each critical point using the First Derivative Test. 


````{dropdown} **Step 1:** &nbsp; Break up the domain of &nbsp; $f'$ &nbsp; at each critical point.

Plug in one number from each subinterval into $f'$ to determine the sign of $f'$ on each interval.

We have $f'(x) = \dfrac{2x}{3(x^2 - 1)^{2/3}}$.

```{figure} ../images/pic_curvesketching_firstderivativetest_1.png
---
name: pic_curvesketching_firstderivativetest_1
width: 400px
---
Interval analysis of $f'(x) = \dfrac{2x}{3(x^2 - 1)^{2/3}}$
```
```{dropdown} Long Text Description
A number line with positive and negative signs assigned to intervals, which are negative to the left of negative one, negative between negative one and zero, positive between zero and one, and positive to the right of one.
```
````


```{dropdown} **Step 2:** &nbsp; Classify each critical point.

Since $f'$ changes from negative to positive at $x=0$, $f$ has a relative minimum at $x=0$.  

Since $f'$ does not change sign at $x=-1$ and at $x=1$, $f$ does not have relative extrema at these values of $x$.
```
`````


### Example 3

`````{admonition} Classifying critical points using the first derivative test
:class: tip

In [Example 2](curvesketching_critical_points_example_2) of the previous section, we found that the critical points of 

$$f(x) = x^3 +3x^2 - 24x + 1$$ 

were $x=-4$ and $x=2$. Classify the critical point using the First Derivative Test. 


````{dropdown} **Step 1:** &nbsp; Break up the domain of &nbsp; $f'$ &nbsp; at each critical point.

Plug in one number from each subinterval into $f'$ to determine the sign of $f'$ on each interval.

We have $f'(x) = 3(x+4)(x-2)$.

```{figure} ../images/pic_curvesketching_firstderivativetest_2.png
---
name: pic_curvesketching_firstderivativetest_2
width: 400px
---
Interval analysis of $f'(x) = 3(x+4)(x-2)$.
```
```{dropdown} Long Text Description
A number line with positive and negative signs assigned to intervals, with positive to the left of negative four, negative between negative four and two, and positive to the right of two.
```
````


```{dropdown} **Step 2:** &nbsp; Classify each critical point.

Since $f'$ changes from positive to negative at $x=-4$, $f$ has a relative maximum at $x=-4$.  

Since $f'$ changes from negative to positive at $x=2$, $f$ has a relative minimum at $x=2$.
```
`````


```{admonition} More Practice
:class: important

For more examples of applying the First Derivative Test, see

- Optimization: {ref}`optimization:first_derivative_test`

```

