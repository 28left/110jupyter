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
  name: python394jvsc74a57bd0085761d8a84a55f3b91b6696b289e6480df59aded311489218ab7e58f5e20cd3
---

# Examples: Computing Limits from Graphs

## Example 1

Let $f(x)$ be defined by the following graph.  

```{image} 110_02_03_lim_graphs_1.png
:alt: A graph defining a function f(x)
:class: bg-primary mb-1
:width: 600px
:align: center
```

Evaluate $\lim\limits_{x \to a^-} f(x)$, $\lim\limits_{x \to a^+} f(x)$, and $\lim\limits_{x \to a} f(x)$ for $a = -3, 0, 2$.


```{admonition} $\mathbf{a=-3} \quad$ (Click to show solution)
:class: tip, dropdown

The two one-sided limits both exist and are both equal to 2.

$$\lim_{x\to -3^-} f(x)=2  ~~~~~ \hbox{and} ~~~~~ \lim_{x\to -3^+} f(x)=2$$

Therefore, the limit exists and $\lim\limits_{x\to -3} f(x) = 2.$
```

```{admonition} $\mathbf{a=0} \quad$ (Click to show solution)
:class: tip, dropdown

The limit from the left does not exist and the limit from the right exists and is equal to 0.

$$\lim_{x\to 0^-} f(x) = -\infty ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 0^+} f(x)=0$$

Therefore, $\lim\limits_{x\to 0} f(x)$ does not exist. Observation: If either of the one-sided limits does not exist (DNE) as $x$ approaches $a$, then the $\lim_{x\to a} f(x)$ does not exist.
```

```{admonition} $\mathbf{a=2} \quad$ (Click to show solution)
:class: tip, dropdown

The two one-sided limits both exist, but are not equal to each other.

$$\lim_{x\to 2^-} f(x)= 2 ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 2^+} f(x)=-4$$

Therefore, $\lim\limits_{x\to 2} f(x)$ does not exist.
```
+++

## Example 2

Let $f(x)$ be defined by the following graph.  

```{image} 110_02_03_lim_graphs_2.png
:alt: A graph defining a function f(x)
:class: bg-primary mb-1
:width: 600px
:align: center
```

Evaluate $\lim\limits_{x \to a^-} f(x)$, $\lim\limits_{x \to a^+} f(x)$, and $\lim\limits_{x \to a} f(x)$ for $a = -1, 1, 4, 6$.


```{admonition} $\mathbf{a=-1} \quad$ (Click to show solution)
:class: tip, dropdown

The two one-sided limits both exist and are both equal to 1.

$$\lim_{x\to -1^-} f(x)=1  ~~~~~ \hbox{and} ~~~~~ \lim_{x\to -1^+} f(x)=1$$

Therefore, the limit exists and $\lim\limits_{x\to -1} f(x) = 1$.  Observation: Although $f(-1)$ is not defined, the limit as $x$ approaches $-1$ still exists.
```

```{admonition} $\mathbf{a=1} \quad$ (Click to show solution)
:class: tip, dropdown

The two one-sided limits both exist and are both equal to 3.

$$\lim_{x\to 1^-} f(x)=3  ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 1^+} f(x)=3$$

Therefore, the limit exists and $\lim\limits_{x\to 1} f(x) = 3$.  Observation: Although $f(1)$ is defined, it is not equal to the value of the limit as $x$ approaches $1$.
```

```{admonition} $\mathbf{a=4} \quad$ (Click to show solution)
:class: tip, dropdown

The two one-sided limits both exist, but are not equal to each other.

$$\lim_{x\to 4^-} f(x)= 1 ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 4^+} f(x)=4$$

Therefore, $\lim\limits_{x\to 4} f(x)$ does not exist.
```


```{admonition} $\mathbf{a=6} \quad$ (Click to show solution)
:class: tip, dropdown

Neither one-sided limit exists.

$$\lim_{x\to 6^-} f(x) = \infty ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 6^+} f(x)= -\infty$$

Therefore, $\lim\limits_{x\to 6} f(x)$ does not exist.
```
