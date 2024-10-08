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

# Relative & Absolute Extrema


## Definitions
```{admonition} Definition
:class: info

A function $f$ has a _**relative maximum**_ at the point $(a,b)$ if there exists a region $R$ containing $(a,b)$ such that $f(a,b) \geq f(x,y)$ for all $(x,y)$ in $R$.  In this case, $f(a,b)$ is called a  _**relative maximum value**_  of $f$. 
```

```{admonition} Definition
:class: info

A function $f$ has a _**relative minimum**_ at the point $(a,b)$ if there exists a region $R$ containing $(a,b)$ such that $f(a,b) \leq f(x,y)$ for all $(x,y)$ in $R$.  In this case, $f(a,b)$ is called a  _**relative minimum value**_  of $f$. 
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

fig = go.Figure(data=[surface,max_points,min_points])


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