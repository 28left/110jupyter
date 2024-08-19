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

````{admonition} Properties
:class: info

Le $c$ be any real number and suppose $\displaystyle \lim_{x\to a} f(x) = L$ and $\displaystyle \lim_{x\to a} g(x) = M$, where both $L$ and $M$ are finite values.

```{admonition} Limit of a Constant
:class: note

$$\lim_{x\to a} c = c $$
```

```{admonition} The Sum & Difference Properties
:class: note

$$\lim_{x\to a} [f(x) \pm g(x)] = \lim_{x\to a} f(x) \pm \lim_{x\to a} g(x)=L \pm M$$
```

```{admonition} The Constant Multiple Property
:class: note

$$\lim_{x\to a} cf(x) = c\lim_{x\to a} f(x) = cL$$
```

```{admonition} Generalized Product Property
:class: note

$$\lim_{x\to a} [f(x)g(x)] = [\lim_{x\to a} f(x)][\lim_{x\to a} g(x)]=LM$$
```

```{admonition} Quotient Property
:class: note

$$\lim_{x\to a} \dfrac{f(x)}{g(x)} = \dfrac{\lim\limits_{x\to a} f(x)}{\lim\limits_{x\to a} g(x)}=\dfrac{L}{M}  ~~~~ \text {if $M\neq 0$}$$
```

```{admonition} The Power Property
:class: note

$$\lim_{x\to a} [f(x)]^c = \left[\lim_{x\to a} f(x)\right]^c = L^c ~~~~ \text {if $L^c$ is defined}$$
```

```{admonition} Polynomial and Rational Functions
:class: note

If $f(x)$ is a polynomial or rational function and $a$ is in the domain of $f(x)$, then

$$\lim_{x\to a} f(x) = f(a)$$
```
````
