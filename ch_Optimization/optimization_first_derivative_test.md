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

## Example 6

In [Example 4](optimization_critical_points_example_4), we found that the critical points of 

$$f(x)=2x^3-15x^2+36x+20$$ 

were $x=2$ and $x=3$. Classify each critical point using the First Derivative Test. 

```{admonition} Step 1: Break up the domain of $f'(x)$ at each critical point.
:class: tip, dropdown

Plug in one number from each subinterval into $f'(x)$ to determine the sign of $f'(x)$ on each interval.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

$f'(x) = 6(x-2)(x-3)$\hspace{1cm}
\begin{tikzpicture}[baseline=-0.5ex,scale=1.5]
  \draw[thick,->] (0,0) -- (5,0);

  \node at (1,0.2) {\Large $+$};
  \node at (2.5,0.2) {\Large $-$};
  \node at (4,0.2) {\Large $+$};

  % tick marks
  \foreach \x in {2,3} 
    \draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\end{tikzpicture}
\end{document} 
```

```{admonition} Step 2: Classify each critical point.
:class: tip, dropdown

Since $f'(x)$ changes from positive to negative at $x=2$, $f(x)$ has a relative maximum at $x=2$.

Since $f'(x)$ changes from negative to positive at $x=3$, $f(x)$ has a relative minimum at $x=3$.
```

## Example 7

In [Example 5](optimization_critical_points_example_5), we found that the only critical point of 

$$f(x)=\frac{1}{x^2-1}$$ 

was $x=0$. Classify the critical point using the First Derivative Test. 

```{admonition} Step 1: Break up the domain of $f'(x)$ at each critical point.
:class: tip, dropdown

Plug in one number from each subinterval into $f'(x)$ to determine the sign of $f'(x)$ on each interval.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}

$f'(x) = -\dfrac{2x}{(x^2-1)^2}$\hspace{1cm}
\begin{tikzpicture}[baseline=-0.5ex,scale=1.5]
  \draw[thick,->] (-2.5,0) -- (2.5,0);

  \node at (-1.75,0.2) {\Large $+$};
  \node at (-0.5,0.2) {\Large $+$};
  \node at (0.5,0.2) {\Large $-$};
  \node at (1.75,0.2) {\Large $-$};

  % tick marks
  \foreach \x in {-1,0,1} 
    \draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\end{tikzpicture}
\end{document} 
```

```{admonition} Step 2: Classify each critical point.
:class: tip, dropdown

Since $f'(x)$ changes from positive to negative at $x=0$, $f(x)$ has a relative maximum at $x=0$.
```