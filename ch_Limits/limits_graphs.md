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

# Computing Limits from Graphs

## Example 1 

````{admonition} Evaluate limits based on the graph of a function
:class: tip

Let $f(x)$ be defined by the following graph.  

Evaluate $\lim\limits_{x \to a^-} f(x)$, $\lim\limits_{x \to a^+} f(x)$, and $\lim\limits_{x \to a} f(x)$ for $a = -3, 0, 2$.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_limits_graphs_example_1.png
:alt: Graph of a piecewise defined function
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -6, -5, -4, -4, -2, -1, 1, 2, 3, 4, 5, and 6 marked. There is a vertical y-axis with the points -4, -3, -2, -1, 1, 2, 3, and 4. The graph of a discontinuous function is plotted on these axes. From left to right, the function decreases from positive infinity and goes down to negative infinity as x moves right towards 0, the function increases linearly from a filled in point at (0,0) to a hollow point at (2,2), jumps to a filled in point at (2,-2), continues from a hollow point at (2,-4) upward to positive infinity on the right.
```


```{dropdown} **Step 1:** &nbsp; Evaluate the limit as $x$ approaches $-3$

The two one-sided limits both exist and are both equal to 2.

$$\lim_{x\to -3^-} f(x)=2  ~~~~~ \hbox{and} ~~~~~ \lim_{x\to -3^+} f(x)=2$$

Therefore, the limit exists and $\lim\limits_{x\to -3} f(x) = 2.$
```

```{dropdown} **Step 2:** &nbsp; Evaluate the limit as $x$ approaches $0$ 

The limit from the left does not exist and the limit from the right exists and is equal to 0.

$$\lim_{x\to 0^-} f(x) = -\infty ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 0^+} f(x)=0$$

Therefore, $\lim\limits_{x\to 0} f(x)$ does not exist. Observation: If either of the one-sided limits does not exist (DNE) as $x$ approaches $a$, then the $\lim\limits_{x\to a} f(x)$ does not exist.
```

```{dropdown} **Step 3:** &nbsp; Evaluate the limit as $x$ approaches $2$

The two one-sided limits both exist, but are not equal to each other.

$$\lim_{x\to 2^-} f(x)= 2 ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 2^+} f(x)=-4$$

Therefore, $\lim\limits_{x\to 2} f(x)$ does not exist.
```
````

<!--
```{code-cell}
:tags: [remove-cell]

%load_ext itikz
```


```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.5]
\tikzstyle{every node}=[font=\large]

% create a white background, with a black frame
%\draw [fill=white,white] (-7,-5) rectangle (7,5); 

% draw a grid
\draw[step=10mm, lightgray, thin] (-6.49,-4.49) grid (6.49,4.49); 
%\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); 

% draw axes
\draw [->,thick] (-6.5,0) -- (6.5,0) node[below] {$x$}; 
\draw [->,thick] (0,-4.5) -- (0,4.5) node[right] {$y$};

% tick marks
\foreach \x in {-6,-5,...,-1,1,2,...,6} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\foreach \y in {-4,-3,...,-1,1,2,...,4} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\y};

% plot curve
\clip (-7,-4.5) rectangle (7,4.5);
\draw [ultra thick] (-6,10) to [out=-85,in=160] (-3,2) to [out=-20,in=95] (0,-6);
\draw [ultra thick] (0,0) -- (2,2);
\draw [ultra thick] (2,-4) parabola (6,12);

% \plot points
\fill (0,0) circle (3pt);
\draw [fill=white] (2,2) circle (3pt);
\fill (2,-2) circle (3pt);
\draw [fill=white] (2,-4) circle (3pt);

\end{tikzpicture}
\end{document}
```
-->


+++

## Example 2
````{admonition} Evaluate limits based on the graph of a function
:class: tip

Let $f(x)$ be defined by the following graph.  

Evaluate $\lim\limits_{x \to a^-} f(x)$, $\lim\limits_{x \to a^+} f(x)$, and $\lim\limits_{x \to a} f(x)$ for $a = -1, 1, 4, 6$.


::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_limits_graphs_example_2.png
:alt: Graph of a piecewise defined function
```
:::
::::
```{dropdown} Long Text Description
There is a horizontal x-axis with the points -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, and 9 marked. There is a vertical y-axis with the points -2, -2, 1, 2, 3, 4, 5,  and 6 marked. There is a blue dotted vertical line at x = 6. The graph of a discontinuous function is plotted on these axes. From left to right, the function decreases as it comes in from the left, increases from rounded corner at (-2,0) to a hollow point at (-1,1), increases from that point to another hollow point at (1,3), jumps to a filled in point at (1,4), jumps back to the hollow point at (1,3) and decreases from there to a filled in point at (4,1), jumps to a hollow point at (4,4) and increases up to infinity as x approaches the blue dotted line at x = 6 from the left, and comes up from negative infinity to the right of the blue dotted line and increases as it goes off to the right.
```

```{dropdown} **Step 1:** &nbsp; Evaluate the limit as $x$ approaches $-1$

The two one-sided limits both exist and are both equal to 1.

$$\lim_{x\to -1^-} f(x)=1  ~~~~~ \hbox{and} ~~~~~ \lim_{x\to -1^+} f(x)=1$$

Therefore, the limit exists and $\lim\limits_{x\to -1} f(x) = 1$.  Observation: Although $f(-1)$ is not defined, the limit as $x$ approaches $-1$ still exists.
```

```{dropdown} **Step 2:** &nbsp; Evaluate the limit as $x$ approaches $1$

The two one-sided limits both exist and are both equal to 3.

$$\lim_{x\to 1^-} f(x)=3  ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 1^+} f(x)=3$$

Therefore, the limit exists and $\lim\limits_{x\to 1} f(x) = 3$.  Observation: Although $f(1)$ is defined, it is not equal to the value of the limit as $x$ approaches $1$.
```

```{dropdown} **Step 3:** &nbsp; Evaluate the limit as $x$ approaches $4$

The two one-sided limits both exist, but are not equal to each other.

$$\lim_{x\to 4^-} f(x)= 1 ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 4^+} f(x)=4$$

Therefore, $\lim\limits_{x\to 4} f(x)$ does not exist.
```


```{dropdown} **Step 4:** &nbsp; Evaluate the limit as $x$ approaches $6$

Neither one-sided limit exists.

$$\lim_{x\to 6^-} f(x) = \infty ~~~~~ \hbox{and} ~~~~~ \lim_{x\to 6^+} f(x)= -\infty$$

Therefore, $\lim\limits_{x\to 6} f(x)$ does not exist.
```
````

<!--
```{code-cell}
:tags: [remove-input]

%%itikz
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.5]
\tikzstyle{every node}=[font=\large]

% create a white background, with a black frame
%\draw [fill=white,white] (-4,-3) rectangle (10,7); 

% draw a grid
\draw[step=10mm, lightgray, thin] (-3.49,-2.49) grid (9.49,6.49); 
%\draw[step=1cm, gray] (0,-0) grid (6.5,3.5); 

% draw axes
\draw [->,thick] (-3.5,0) -- (9.5,0) node[below] {$x$}; 
\draw [->,thick] (0,-2.5) -- (0,6.5) node[right] {$y$};

% tick marks
\foreach \x in {-3,-2,...,-1,1,2,...,9} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {\x};
\foreach \y in {-2,-1,1,2,...,6} 
	\draw [thick] (2pt,\y cm) -- (-2pt,\y cm) node[left] {\y};


% plot curve
\clip (-3.5,-2.5) rectangle (9.5,6.5);
\draw [ultra thick,blue,dashed] (6,-3) -- (6,7);
\draw [ultra thick] (-4,4) parabola bend (-2,0) (-1,1);
\draw [ultra thick] (-1,1) to [out=63,in=200] (0,2) to [out=20,in=243] (1,3);
\draw [ultra thick] (1,3) to [out=0,in=180] (4,1);
%\draw[ultra thick,domain=3:1,smooth,samples=300] plot (\x,{2+pow((3-\x)/2,0.33)});
%\draw[ultra thick,domain=3:4,smooth,samples=100] plot (\x,{2-pow(\x-3,0.33)});
\draw [ultra thick] (4,4) to [out=25,in=270] (6,10);
\draw [ultra thick] (6,-6) to [out=85,in=200] (10,5);

% \plot points
\draw [fill=white] (-1,1) circle (3pt);
\draw [fill=white] (1,3) circle (3pt);
\fill (1,4) circle (3pt);
\draw [fill=white] (4,4) circle (3pt);
\fill (4,1) circle (3pt);

\end{tikzpicture}
\end{document}
```
-->