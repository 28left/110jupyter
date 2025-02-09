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

# The Second Derivative Test

## Using the Second Partial Derivatives to Classify Critical Points

```{admonition} The Second Derivative Test
:class: info

Suppose $(a,b)$ is a critical point of $f(x,y)$ such that $f_x(a,b) = 0$ and $f_y(a,b) = 0$.  Let $D(x,y) = f_{xx}(x,y)f_{yy}(x,y) - f_{xy}^2(x,y)$


1. If $D(a,b) > 0$ and $f_{xx}(a,b) < 0$, then $f(x,y)$ has a relative maximum value at $(a,b)$

2. If $D(a,b) > 0$ and $f_{xx}(a,b) > 0$, then $f(x,y)$ has a relative minimum value at $(a,b)$

3. If $D(a,b) < 0$ then $f(x,y)$ has a saddle point at $(a,b)$

4. If $D(a,b) = 0$ then the test is inconclusive.

```


### Example



