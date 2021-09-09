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

## Using the First Derivative to Classify Critical Points


```{admonition} The First Derivative Test
:class: info

Suppose $c$ is a critical point of the continuous function $f$.

1. If $f'(x)$ changes sign **from positive to negative** at $x=c$, then $f(c)$ is a **relative maximum**.
2. If $f'(x)$ changes sign **from negative to positive** at $x=c$, then $f(c)$ is a **relative minimum**. 
3. If $f'(x)$ **does not change sign** at $x=c$, then $f(c)$ is **not a relative extrema.** 
```

## Example 1

In [Example 1](curvesketching_critical_points_example_1), we found that the critical points of 

$$f(x) = \sqrt[3]{x^2-1}$$ 

were $x=-1$, $x=0$, and $x=1$.
Classify each critical point using the First Derivative Test. 

````{dropdown} **Step 1:** Break up the domain of $f'(x)$ at each critical point.

Plug in one number from each subinterval into $f'(x)$ to determine the sign of $f'(x)$ on each interval.

We have $f'(x) = \dfrac{2x}{3(x^2 - 1)^{2/3}}$.

```{figure} ../images/pic_curvesketching_firstderivativetest_1.png
---
name: pic_curvesketching_firstderivativetest_1
width: 400px
---
Interval analysis of $f'(x) = \dfrac{2x}{3(x^2 - 1)^{2/3}}$
```
````


```{dropdown} **Step 2:** Classify each critical point.

Since $f'(x)$ changes from negative to positive at $x=0$, $f(x)$ has a relative minimum at $x=0$.  

Since $f'(x)$ does not change sign at $x=-1$ and $x=1$, $f(x)$ does not have relative extrema at these values of $x$.
```


## Example 2

In [Example 2](curvesketching_critical_points_example_2), we found that the critical points of 

$$f(x) = x^3 +3x^2 - 24x + 1$$ 

were $x=-4$ and $x=2$. Classify the critical point using the First Derivative Test. 

````{dropdown} **Step 1:** Break up the domain of $f'(x)$ at each critical point.

Plug in one number from each subinterval into $f'(x)$ to determine the sign of $f'(x)$ on each interval.

We have $f'(x) = 3(x+4)(x-2)$.

```{figure} ../images/pic_curvesketching_firstderivativetest_2.png
---
name: pic_curvesketching_firstderivativetest_2
width: 400px
---
Interval analysis of $f'(x) = 3(x+4)(x-2)$.
```
````


```{dropdown} **Step 2:** Classify each critical point.

Since $f'(x)$ changes from positive to negative at $x=-4$, $f(x)$ has a relative maximum at $x=-4$.  Since $f'(x)$ changes from negative to positive at $x=2$, $f(x)$ has a relative minimum at $x=2$.
```