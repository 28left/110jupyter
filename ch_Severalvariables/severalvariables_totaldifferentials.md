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

# Total Differentials

## Definition

### Example



### Tangent Plane


```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

x, y = np.mgrid[0:0.5:50j, 0:0.5:50j]
z = x**2 + y**2

a = 0.2
b = 0.3
c = a**2 + b**2
z1 = c + 2*a*(x - a) + 2*b*(y-b)

fig = go.Figure(data = [
  go.Surface(
    contours = {
      "x": {"show": True, "start": 0, "end": 0.5, "size": 0.1},
      "y": {"show": True, "start": 0, "end": 0.5, "size": 0.1}
      }, 
      x=x, y=y, z=z, colorscale='Pinkyl', hoverinfo="none", showscale=False, opacity=1.0),
  go.Surface(contours = {
      "x": {"show": True, "start": 0, "end": 0.5, "size": 0.1},
      "y": {"show": True, "start": 0, "end": 0.5, "size": 0.1}
      }, 
      x=x, y=y, z=z1, colorscale=[[0,'black'],[1,'black']], hoverinfo="none",showscale=False, opacity=0.5)
  ])


fig.update_traces(
  contours_z=dict(show=False, highlight=False, project_z=False)
  )

fig.update_layout(
  scene = dict(
    xaxis = dict(visible=True,showgrid=True,showspikes=False),
    yaxis = dict(visible=True,showgrid=True,showspikes=False),
    zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  scene_camera_eye=dict(x=-1.5, y=-1.5, z=0.25),
  margin=dict(l=0, r=0, b=25, t=0)
)


fig.update_layout(title_text="Tangent Plane")
fig.show()

```


### Total Differential


```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

a = 0.2
b = 0.3
x, y = np.mgrid[a:0.5:50j, b:0.5:50j]
z = (x**2 + y**2)/2


c = (a**2 + b**2)/2
z1 = c + a*(x - a) + b*(y-b)

fig = go.Figure(data = [
  go.Surface(
    contours = {
      "x": {"show": True, "start": 0, "end": 0.5, "size": 0.1},
      "y": {"show": True, "start": 0, "end": 0.5, "size": 0.1}
    }, 
    x=x, y=y, z=z, colorscale='Pinkyl', hoverinfo="none", showscale=False, opacity=1.0),
  go.Surface(
    contours = {
      "x": {"show": True, "start": 0, "end": 0.5, "size": 0.1},
      "y": {"show": True, "start": 0, "end": 0.5, "size": 0.1}
    },
    x=x, y=y, z=z1, colorscale=[[0,'black'],[1,'black']], hoverinfo="none",showscale=False, opacity=0.5)
  ])


fig.update_traces(
  contours_z=dict(show=False, highlight=False, project_z=False)
  )

fig.update_layout(
  scene = dict(
    xaxis = dict(visible=True,showgrid=True,showspikes=False),
    yaxis = dict(visible=True,showgrid=True,showspikes=False),
    zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  scene_camera_eye=dict(x=1, y=-2, z=0.2),
  margin=dict(l=0, r=0, b=25, t=0)
)


fig.show()

```




