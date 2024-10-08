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

# Functions of Two Variables


## Domains

```{admonition} Definition
:class: info

The _**domain**_ of a function of two variables, $f(x,y)$, is the set of all values of $x$ and $y$ for which the function is defined.
```

```{admonition} How to Determine the Domain of a Function
:class: note

When determining the domain of a given function, do not include any value that leads to one or more of the following:

- division by zero
- the square root of a negative number
- the logarithm of zero or a negative number

While there are other functions that lead to restrictions on the domain, we will limit our discussion to division, square roots, and logarithms.
```


### Example 1
`````{admonition} Domain of a square root function
:class: tip

Determine the domain of the function $f(x,y) = \sqrt{2x+5y-10}$

```{dropdown} **Step 1:** &nbsp; Describe all points $(x,y)$ in the domain of $f$.

The domain of $f$ consists of all points $(x,y)$ such that $2x + 5y - 10 \geq 0$ since we cannot take the square root of a negative number.  This includes all points $(x,y)$ on or above the line $2x + 5y = 10$.
```

````{dropdown} **Step 2:** &nbsp; Sketch the domain of $f$.

The domain of $f$ can be represented by the following shaded region.  The line $2x+5y = 10$ is drawn as a solid line since points on the line are included in the domain.  The region above the line is shaded to indicate that all points above the line are also in the domain of $f$.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_severalvariables_functions_example_1.png
:alt: Graph of $Domain of $
```
:::
::::
```{dropdown} Long Text Description
```

````

`````

<!--
%\definecolor{shadecolor}{RGB}{218,235,226} % lightgreen
%\definecolor{shadecolor}{RGB}{245,227,210} % light orange
\definecolor{shadecolor}{RGB}{222,231,250} % light blue


\hspace{-50pt}
\begin{tikzpicture}[scale=1.5]

\draw[black,fill=white] (-2.75,-1.25) rectangle (7.75,5.25);

% shade region
\begin{scope}
\clip (-2.4,-3.7) rectangle (7.4,5);
\fill[color=shadecolor] (-5,4) -- (10,-2) -- (10,6) -- (-5,6);
\end{scope}


\draw[very thin,color=lightgray,step=0.5] (-2.4,-0.9) grid (7.4,4.9);
%\draw[very thin,color=gray,step=2] (-3.5,-1) grid (3.5,5);

\draw[->] (-2.5,0) -- (7.5,0) node[below] {$x$};
\draw[->] (0,-1) -- (0,5) node[right] {$y$};
\draw[domain=-2.4:7.4,smooth,variable=\x,black,ultra thick] plot ({\x},{2 - 2*\x/5});%  node[right] {$y=2 - 2x/5$};

       
\node[right] at (0.9, 0.8){$2x + 5y = 10$};

% tick marks
\foreach \x in {-2,2,4,6} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {2,4} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};
\end{tikzpicture}

-->

<!--
```{code-cell}
:tags: [remove-input]

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2, 2, 0.1)
y = 2 - 0.4*x

fig, ax = plt.subplots()

plt.grid()

ax.plot(x, y, 'k--')

ax.fill_between(x, y, 4, where=None, facecolor='green', alpha=.5)

plt.show()

```
-->

### Example 2
`````{admonition} Domain of a logarithmic function
:class: tip

Determine the domain of the function $f(x,y) = \ln(x^2 + y^2 - 4)$

```{dropdown} **Step 1:** &nbsp; Describe all points $(x,y)$ in the domain of $f$.

The domain of $f$ consists of all points $(x,y)$ such that $x^2 + y^2 - 4 > 0$ since we cannot take the logarithm of zero or a negative number. This includes all points $(x,y)$ outside the circle $x^2 + y^2 = 4$, which is a circle centered at the origin of radius $2$.

```

````{dropdown} **Step 2:** &nbsp; Sketch the domain of $f$.

The domain of $f$ can be represented by the following shaded region.  The circle $x^2 + y^2 = 4$ is drawn as a dashed line since points on the circle are not included in the domain.  The region outside the circle is shaded to indicate that all points in this region are in the domain of $f$.

::::{grid} auto
:::{grid-item-card}
:margin: auto
```{image} ../images/pic_severalvariables_functions_example_2.png
:alt: Graph of $Domain of $
```
:::
::::
```{dropdown} Long Text Description
```

````

`````

<!--
%\definecolor{shadecolor}{RGB}{218,235,226} % lightgreen
%\definecolor{shadecolor}{RGB}{245,227,210} % light orange
\definecolor{shadecolor}{RGB}{222,231,250} % light blue


\begin{tikzpicture}[scale=1.5]

\draw[black,fill=white] (-3.75,-3.75) rectangle (3.75,3.75);

%shade region
\begin{scope}
\clip (-3.5,-3.5) rectangle (3.5,3.5);
\shade [inner color=shadecolor, outer color=shadecolor, even odd rule] circle (6) circle (2);
\end{scope}

\draw[very thin,color=lightgray,step=0.5] (-3.4,-3.4) grid (3.4,3.4);

\draw[->] (-3.5,0) -- (3.5,0) node[below] {$x$};
\draw[->] (0,-3.5) -- (0,3.5) node[right] {$y$};
\draw[domain=0:2,smooth,variable=\x,black,ultra thick] plot ({2*cos(\x)},{2*sin(\x)});%  node[right] {$y=2 - 2x/5$};
\draw[dashed,ultra thick] (0,0) circle (2);
       
\node[right] at (0.1, 0.8){$x^2 + y^2 = 4$};

% tick marks
\foreach \x in {-2,2} 
	\draw [thick] (\x cm,2pt) -- (\x cm,-2pt) node[below] {$\x$};
\foreach \y in {-2,2} 
	\draw [thick] (-2pt,\y cm) -- (2pt,\y cm) node[right] {$\y$};
\end{tikzpicture}

-->




## Level Curves

```{code-cell}
:tags: [remove-input]

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cm as cm

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')

```

```{code-cell}
:tags: [remove-input]

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cm as cm

delta = 0.025
x = np.arange(-2.0, 2.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig, ax = plt.subplots()
ax.set_aspect('equal')
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
#ax.set_title('Simplest default with labels')

```

```{code-cell}
:tags: [remove-input]

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cm as cm

delta = 0.025
x = np.arange(-2.0, 2.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2)**0.5

fig, ax = plt.subplots()
ax.set_aspect('equal')
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
#ax.set_title('Simplest default with labels')

```





### A Plane
```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

x,y = np.mgrid[-1:1:10j, -1:1:10j]
z1 = 1 + x/2 - y
z2 = 1 + 3*x - 6*y

fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['', ''],
                    )

fig.add_trace(go.Surface(
  contours = {"z": {"show": True, "start": -10, "end": 10, "size": 0.5}},
  x=x, y=y, z=z1,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False), 
  1, 1)
fig.add_trace(go.Surface(
  contours = {"z": {"show": True, "start": -10, "end": 10, "size": 0.5}},
  x=x, y=y, z=z2,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False), 
  1, 2)


fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=True),
  row=1, col=1
  )

fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=True),
  row=1, col=2
  )



fig.update_layout(
  scene = dict(
    xaxis = dict(visible=True,showgrid=True,showspikes=False),
    yaxis = dict(visible=True,showgrid=True,showspikes=False),
    zaxis = dict(visible=True,showgrid=True,showspikes=False,nticks=4, range=[-10,10])
  )
)

fig.update_layout(
  scene2 = dict(
    xaxis = dict(visible=True,showgrid=True,showspikes=False),
    yaxis = dict(visible=True,showgrid=True,showspikes=False),
    zaxis = dict(visible=True,showgrid=True,showspikes=False,nticks=4, range=[-10,10])
  )
)


fig.show()

```



### Example - Paraboloid 



```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

u, v = np.mgrid[0:2:50j, 0:2*np.pi:50j]
x = u*np.cos(v)
y = u*np.sin(v)
z = x**2 + y**2

X, Y = np.mgrid[-2:2:50j, -2:2:50j]


# Create figure
fig = go.Figure()

# Add contours, one for each slider step
delta = 0.1
for step in np.arange(0,4, delta):
  fig.add_trace(
    go.Surface(
      contours = {"z": {"show": True, "start": step, "end": step+0.5, "size": 2}},
      x=x, y=y, z=z,
      colorscale='Pinkyl',
      hoverinfo="none",
      visible=False,
      showscale=False)
    )
  fig.add_trace(
    go.Surface(
      x=X, y=Y, z=step + 0*X + 0*Y, 
      colorscale=[[0,'gray'],[1,'gray']], 
      hoverinfo="none",
      showscale=False, 
      visible=False,
      opacity=0.50)
    )



# Make 50th trace visible
fig.data[20].visible = True
fig.data[21].visible = True

# Create and add slider
steps = []
for i in range(int(len(fig.data)/2)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label=str(round(i*delta,2))
  )
  step["args"][0]["visible"][2*i] = True  # Toggle i'th trace to "visible"
  step["args"][0]["visible"][2*i+1] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Current Horizontal Cross Section: z = "},
    pad={"t": 50},
    steps=steps
)]


fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=True)
  )

fig.update_layout(
  sliders=sliders,
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=100, r=100, b=80, t=0)
)


fig.show()
```


```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

u, v = np.mgrid[0:2:50j, 0:2*np.pi:50j]
x = u*np.cos(v)
y = u*np.sin(v)
z = x**2 + y**2

fig = go.Figure(go.Surface(
  contours = {"z": {"show": True, "start": 0, "end": 4, "size": 0.5}}, 
  x=x, y=y, z=z,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False)
  )

fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=True)
  )

fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=0, r=0, b=25, t=0)
)
fig.show()

```






### Cone

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np
a, b, d = 1.32, 1., 0.8
c = a**2 - b**2
u, v = np.mgrid[0:2:50j, 0:2*np.pi:50j]
x = u*np.cos(v)
y = u*np.sin(v)
z = (x**2 + y**2)**0.5

fig = go.Figure(go.Surface(
  contours = {"z": {"show": True, "start": 0, "end": 4, "size": 0.25}}, 
  x=x, y=y, z=z,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False)
  )

fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=True)
  )
#fig.update_layout(title_text="Paraboloid with horizontal contours")
fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=0, r=0, b=25, t=0)
)
fig.show()

```


### Miscellaneous

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

x,y = np.mgrid[-2:5:50j, -2:2:50j]
z = x**2 - 2*x*y**2

fig = go.Figure(go.Surface(
  contours = {"z": {"show": True, "start": -20, "end": 25, "size": 2}}, 
  x=x, y=y, z=z,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False)
  )

fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=True)
  )
#fig.update_layout(title_text="Paraboloid with horizontal contours")
fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=0, r=0, b=25, t=0)
)
fig.show()

```


```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go

delta = 0.025
xrange = np.arange(-2, 5, delta)
yrange = np.arange(-2, 2, delta)
x, y = np.meshgrid(xrange,yrange)
F = x**2 - 2*x*y**2


fig = go.Figure(data =
    go.Contour(
        z = F,
        x = xrange,
        y = yrange,
        contours_coloring='lines',
        line_width = 2,
        contours=dict(
            start=-20,
            end=25,
            size=2,
        ),
    ))
fig.show()
```



```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

x,y = np.mgrid[-2:2:50j, -2:2:50j]
z = x*y / 2.718**(x**2 + y**2) / 2

fig = go.Figure(go.Surface(
  contours = {"z": {"show": True, "start": -0.1, "end": 0.1, "size": 0.02}}, 
  x=x, y=y, z=z,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False)
  )

fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=True)
  )
#fig.update_layout(title_text="Paraboloid with horizontal contours")
fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=0, r=0, b=25, t=0)
)
fig.show()

```



```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

x,y = np.mgrid[-5:5:50j, -5:5:50j]
z = np.log(1 + x**2 + 2*y**2)

fig = go.Figure(go.Surface(
  contours = {"z": {"show": True, "start": 0, "end": 4, "size": 0.5}}, 
  x=x, y=y, z=z,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False)
  )

fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=True)
  )
#fig.update_layout(title_text="Paraboloid with horizontal contours")
fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=0, r=0, b=25, t=0)
)
fig.show()

```

<!--
```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

x,y = np.mgrid[-5:5:50j, 0.001:5:50j]
z = 2*x/y + 1

fig = go.Figure(data = [
  go.Surface(
    contours = {"z": {"show": True, "start": -20, "end": 20, "size": 2}}, 
    x=x, y=y, z=z,
    colorscale='Pinkyl',
    hoverinfo="none",
    showscale=False
  ),
  go.Surface(
    contours = {"z": {"show": True, "start": -20, "end": 20, "size": 2}}, 
    x=x, y=-y, z=-z+2,
    colorscale='Pinkyl',
    hoverinfo="none",
    showscale=False
  )
  ]
)

fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=True)
)
#fig.update_layout(title_text="Paraboloid with horizontal contours")
fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False,range=[-10,10])
  ),
  margin=dict(l=0, r=0, b=25, t=0)
)
fig.show()

```
-->


