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
(lim:prop_lim)=
# Properties of Finite Limits

Suppose $\displaystyle \lim_{x\to a} f(x) = L$ and $\displaystyle \lim_{x\to a} g(x) = M$

```{admonition} (1) Limit of a Constant
:class: info
For any real number $c$, 

$$\lim_{x\to a} c = c $$
```

```{admonition} (2) The Sum & Difference Properties
:class: info

$$\lim_{x\to a} [f(x) \pm g(x)] = \lim_{x\to a} f(x) \pm \lim_{x\to a} g(x)=L \pm M$$
```

```{admonition} (3) The Constant Multiple Property
:class: info

For any real number $c$, 

$$\lim_{x\to a} cf(x) = c\lim_{x\to a} f(x) = cL$$
```

```{admonition} (4) Generalized Product Property
:class: info

$$\lim_{x\to a} [f(x)g(x)] = [\lim_{x\to a} f(x)][\lim_{x\to a} g(x)]=LM$$
```

```{admonition} (5) Quotient Property
:class: info

If $M\neq 0$,

$$\lim_{x\to a} \dfrac{f(x)}{g(x)} = \dfrac{\lim\limits_{x\to a} f(x)}{\lim\limits_{x\to a} g(x)}=\dfrac{L}{M}$$
```

```{admonition} (6) The Power Property
:class: info

$$\lim_{x\to a} [f(x)]^r = \left[\lim_{x\to a} f(x)\right]^r = L^r$$
```

```{admonition} (7) Polynomial and Rational Functions
:class: info

If $f(x)$ is a polynomial or rational function and $a$ is in the domain of $f(x)$, then

$$\lim_{x\to a} f(x) = f(a)$$
```
