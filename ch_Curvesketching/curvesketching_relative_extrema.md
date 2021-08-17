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
# Relative Extrema

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

```{admonition} Definition
:class: info

The relative extrema of a function $f$:

- A function $f$ has a **relative maximum** at $x=c$ if there exists an open interval $(a,b)$ containing $c$ such that $f(c) \geq f(x)$ for all $x$ in $(a,b)$.
- A function $f$ has a **relative minimum** at $x=c$ if there exists an open interval $(a,b)$ containing $c$ such that $f(c) \leq f(x)$ for all $x$ in $(a,b)$.
```

## Example 1

The relative extrema are highlighted on the following graph. Observe how the relative extrema appear at points on the curve where the increasing/decreasing behavior of the function changes. 

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\usetikzlibrary{arrows}
\usetikzlibrary{arrows.meta}

\begin{document}

\begin{tikzpicture}[scale = 1.2]

  \draw[white,fill=white] (-1,-1) rectangle (12.5,7.5);
  \draw[->] (-0.5,0) -- (12,0) node[below] {$x$};
  \draw[->] (0,-0.5) -- (0,7) node[right] {$y$};
      
  % draw curve
  \draw [ultra thick] 
  (1,1) parabola bend (2.5,4) (4,2) 
  .. controls (5.5,5) and (7,2) .. (8.5,5) 
  parabola bend (10,3) (11.5,6);

  % draw points
  \draw [black,fill=red] (2.5,4) circle (2.5pt);
  \draw [black,fill=green] (4,2) circle (2.5pt);
  \draw [black,fill=red] (8.5,5) circle (2.5pt);
  \draw [black,fill=green] (10,3) circle (2.5pt);

  % label extrema
  \draw [<-, >=stealth', shorten <=3pt] (2.5,4) -- (3.25,6) node[right] {\bf \large Relative Maxima}; 
  \draw [<-, >=stealth', shorten <=3pt] (8.5,5) -- (7,6);
  \draw [<-, >=stealth', shorten <=3pt] (4,2) -- (5,1) node[right] {\bf \large Relative Minima}; 
  \draw [<-, >=stealth', shorten <=3pt] (10,3) -- (8.7,1);
\end{tikzpicture}
\end{document} 
```

In other words, relative extrema appear at points on the graph of the function where the derivative changes sign.

## How To Find Relative Extrema

The relative extrema of a function appear where $f'(x)$ changes from positive to negative or from negative to positive. Since $f'(x)$ changes sign when there is a relative extrema, it must be the case that either $f'(x)=0$ or $f'(x)$ does not exist at the relative extrema.
