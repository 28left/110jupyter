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

# Review of Integration of Functions of One Variable

## Formulas and Rules of Integration


```{admonition} Formulas of Integration
:class: info

\begin{align*}
&\text{Integral of a Constant, $k$} && \int k ~dx  = kx + C \\ \\ 
&\text{Integral of $x^n$, $n\neq -1$} && \int x^n ~dx  = \frac{x^{n+1}}{n+1} + C ~~~ \text{if $n\neq -1$}\\ \\
&\text{Integral of $1/x$} && \int \frac{1}{x} ~dx = \ln|x| + C \\ \\ 
&\text{Integral of $e^{ax}$, $a\neq 0$} && \int e^{ax} ~dx = \frac{1}{a}e^{ax} + C ~~~ \text{if $a\neq 0$} 
\end{align*}
```


```{admonition} Rules of Integration
:class: info

\begin{align*}
&\text{Constant Multiple Rule} && \int cf(x) ~dx  = c \int f(x) ~dx \\ \\
&\text{Sum/Difference Rule} && \int f(x) \pm g(x) ~dx = \int f(x) ~dx \pm \int g(x) ~dx\\ \\
&\text{Substitution Rule for Indefinite Integrals} && \int f(g(x)) g'(x) ~dx = \int f(u) ~du \\ \\
&\text{Substitution Rule for Definite Integrals} && \int_{x=a}^{x=b} f(g(x)) g'(x) ~dx = \int_{u=g(a)}^{u=g(b)} f(u) ~du \\ \\
&\text{Integration by Parts} && \int u ~dv = uv - \int v ~du\\ \\
\end{align*}
```


```{admonition} More Practice
:class: important

- {ref}`indefinite:substitution`
- {ref}`definite:substitution`
- {ref}`parts:integration`

```




### Example