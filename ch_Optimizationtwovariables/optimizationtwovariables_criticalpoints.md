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

# Critical Points

## Definition

```{admonition} Definition
:class: info

A _**critical point**_ of the function $f(x,y)$ is a point $(a,b)$ in the domain of $f$ such that

$$f_x(a,b) = 0 ~~~~\text{and}~~~~ f_y(a,b) = 0 $$

or at least one of the first-order partial derivatives, $f_x(a,b)$ or $f_y(a,b)$, does not exist.
```


```{admonition} Critical Points versus Relative Extrema
:class: warning
Critical points of $f$ correspond to **possible** locations of relative extrema.  In other words, not all critical points correspond to a relative extrema.  However, every relative extrema must appear at a critical point.
```


### Example - Both partial derivatives are zero

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

u, v = np.mgrid[0:2:50j, 0:2*np.pi:50j]
x = u*np.cos(v)
y = u*np.sin(v)
z = x**2 + y**2
x1, y1 = np.mgrid[-1.5:1.5:50j, -1.5:1.5:50j]
z1 = 0*x + 0*y

fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Contours parallel to yz-plane', 'Contours parallel to xz-plane'],
                    )

fig.add_trace(go.Surface(
    contours = {
        "x": {"show": True, "start": -2, "end": 2, "size": 0.5},
        "y": {"show": True, "start": -2, "end": 2, "size": 0.5}
    },
    x=x, y=y, z=z,
    colorscale='Pinkyl',
    hoverinfo="none",
    showscale=False
    ), 
    1, 1
)

fig.add_trace(go.Surface(
    contours = {
        "x": {"show": True, "start": 0, "end": 0, "size": 0},
        "y": {"show": True, "start": 0, "end": 0, "size": 0}
    }, 
    x=x1, y=y1, z=z1, 
    colorscale=[[0,'black'],[1,'black']], 
    hoverinfo="none",
    showscale=False, 
    opacity=0.5
    ),
    1,1
)



fig.add_trace(go.Surface(
  contours = {
    "x": {"show": True, "start": -2, "end": 2, "size": 0.5},
    "y": {"show": True, "start": -2, "end": 2, "size": 0.5}
  },
  x=x, y=y, z=1-z,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False), 
  1, 2)

fig.add_trace(go.Surface(
  contours = {
      "x": {"show": True, "start": 0, "end": 0, "size": 0},
      "y": {"show": True, "start": 0, "end": 0, "size": 0}
      }, 
      x=x1, y=y1, z=z1 + 1, colorscale=[[0,'black'],[1,'black']], hoverinfo="none",showscale=False, opacity=0.5),
      1,2)

fig.update_traces(
  contours_x=dict(show=True, highlight=False, project_x=False),
  contours_y=dict(show=True, highlight=False, project_y=False),
  contours_z=dict(show=False, highlight=False, project_z=False),
  row=1, col=1
  )

fig.update_traces(
  contours_x=dict(show=True, highlight=False),
  contours_y=dict(show=True, highlight=False, project_y=False),
  contours_z=dict(show=False, highlight=False),
  row=1, col=2
  )


fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=40, r=20, b=50, t=0)
)

fig.update_layout(
  scene2 = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=20, r=40, b=50, t=0)
)

fig.update_layout(title_text="Paraboloid")
fig.show()
```



### Example - Derivatives do not exist

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

u, v = np.mgrid[0:1:100j, 0:2*np.pi:100j]
x = u*np.cos(v)
y = u*np.sin(v)
z = (x**2 + y**2)**0.25


fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Contours parallel to yz-plane', 'Contours parallel to xz-plane'],
                    )

fig.add_trace(go.Surface(
    contours = {
        "x": {"show": True, "start": -2, "end": 2, "size": 0.5},
        "y": {"show": True, "start": -2, "end": 2, "size": 0.5}
    },
    x=x, y=y, z=z,
    colorscale='Pinkyl',
    hoverinfo="none",
    showscale=False
    ), 
    1, 1
)


x2,y2 = np.mgrid[-2:2:101j, -2:2:101j] 
z2 = np.exp(-1*np.abs(x2))

fig.add_trace(go.Surface(
  contours = {
    "x": {"show": True, "start": -2, "end": 2, "size": 0.5},
    "y": {"show": True, "start": -2, "end": 2, "size": 0.5}
  },
  x=x2, y=y2, z=z2,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False), 
  1, 2)


fig.update_traces(
  contours_x=dict(show=True, highlight=False, project_x=False),
  contours_y=dict(show=True, highlight=False, project_y=False),
  contours_z=dict(show=False, highlight=False, project_z=False),
  row=1, col=1
  )

fig.update_traces(
  contours_x=dict(show=True, highlight=False),
  contours_y=dict(show=True, highlight=False, project_y=False),
  contours_z=dict(show=False, highlight=False),
  row=1, col=2
  )


fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=40, r=20, b=50, t=0)
)

fig.update_layout(
  scene2 = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=20, r=40, b=50, t=0)
)

fig.update_layout(title_text="Paraboloid")
fig.show()
```



### Example
```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

x,y = np.mgrid[-2.5:2.5:100j, -2.5:2.5:100j]
z = 2*np.sin(3.14*x/2)*np.cos(3.14*y/2)/np.log(2 + (x-0.25)**2 + (y+0.25)**2) + x/5 + y/6

surface = go.Surface(
  contours = {"z": {"show": True, "start": -2, "end": 2, "size": 0.5}}, 
  x=x, y=y, z=z,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False,
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=False)
)

delta = 0.000
size = 5

max_points = go.Scatter3d(
  x=[0.80,-0.87,-0.82], y=[-0.05,1.95,-1.8], z=[2.40+delta,1.1+delta,0.62+delta], 
  mode='markers',
  marker=dict(size=size,color="black"),
  hoverinfo="none",
  name="Relative maximum"
)

saddle_points = go.Scatter3d(
  x=[-2,-2,-0.04,0.06,2,2], y=[-0.86,0.9,-0.98,1,0.93,-0.98], z=[-0.54,-0.24,-0.14,0.16,0.55,0.23], 
  mode='markers',
  marker=dict(size=size,color="blue"),
  hoverinfo="none",
  name="Saddle points"
)

min_points = go.Scatter3d(
  x=[-0.82,0.88,0.88], y=[-0.08,1.8,-1.89], z=[-1.85-delta,-0.5-delta,-1.32-delta], 
  mode='markers',
  marker=dict(size=size,color="red"),
  hoverinfo="none",
  name="Relative minimum"
)


critical_points = go.Scatter3d(
  x=[0.80,-0.87,-0.82,-2,-2,-0.04,0.06,2,2,-0.82,0.88,0.88], y=[-0.05,1.95,-1.8,-0.86,0.9,-0.98,1,0.93,-0.98,-0.08,1.8,-1.89], z=[2.40+delta,1.1+delta,0.62+delta,-0.54,-0.24,-0.14,0.16,0.55,0.23,-1.85-delta,-0.5-delta,-1.32-delta], 
  mode='markers',
  marker=dict(size=size,color="black"),
  hoverinfo="none",
  name="Critical points"
)

fig = go.Figure(data=[surface,critical_points])


fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  #margin=dict(l=0, r=0, b=25, t=0)
)
fig.show()

```