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
# Intervals of Increase & Decrease

```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```

```{admonition} Definition
:class: info

A function $f$ is **increasing** on the interval $(a,b)$ if for any two numbers $c$ and $d$ in $(a,b)$, $f(c) < f(d)$ whenever $c<d$.
```

```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=2.0]
\tikzstyle{every node}=[font=\large]
\draw[white,fill=white] (0,-0.2) rectangle (3,3.8);

% axis
\draw[<->] (0,3) |- (3,0);
     
% dash lines
\draw[dashed,red] (0,1.04) node[left] {\textcolor{black}{$f(c)$}} -| (1.2,0);
\draw[dashed,red] (0,1.94) node[left] {\textcolor{black}{$f(d)$}} -| (1.8,0);

% draw curve
\draw [ultra thick] (0.5,0.5) cos (1.5,1.5) sin (2.5,2.5);

% draw points
\draw [black,fill=red] (1.2,1.04) circle (2.0pt);
\draw [black,fill=red] (1.8,1.94) circle (2.0pt);

\node[rotate=90] at (-0.5,1.5) {$<$};
\node[above] at (0.5,-0.6) {$a$};
\node[above] at (1.2,-0.6) {$c$};
\node[above] at (1.5,-0.6) {$<$};
\node[above] at (1.8,-0.6) {$d$};
\node[above] at (2.5,-0.6) {$b$};

% tick marks
\draw [thick] (0.5 cm,2pt) -- (0.5 cm,-2pt);
\draw [thick] (1.2 cm,2pt) -- (1.2 cm,-2pt);
\draw [thick] (1.8 cm,2pt) -- (1.8 cm,-2pt);
\draw [thick] (2.5 cm,2pt) -- (2.5 cm,-2pt);
\end{tikzpicture}
\end{document}
```

```{admonition} Theorem
:class: warning

If $f'(x) > 0$ for all $x$ in the interval $(a,b)$, then $f$ is increasing on $(a,b)$.
```