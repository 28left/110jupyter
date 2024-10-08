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

# Differential Equations


```{code-cell}
:tags: [remove-input]

import plotly.figure_factory as ff
import numpy as np

x,y = np.meshgrid(np.arange(0, 4, .2), np.arange(0, 2, .2))
u = np.cos(x)
v = np.sin(x)

fig = ff.create_quiver(x, y, u, v)
fig.show()
```



## Slope Field - Exponential Growth & Decay

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np

#Function

delta = 0.2
x,y = np.meshgrid(np.arange(0, 4, .2), np.arange(0, 2, .2))

# Create figure
fig = go.Figure()

# Add slopefields lines, one for each slider step
for step in np.arange(-5, 5.2, 0.2):
  fig.add_trace(
    ff.create_quiver(
      x, y, 
      1 / np.sqrt(1 + step*step*y**2), step*y/ np.sqrt(1 + step*step*y**2),
      visible=False,
      hoverinfo="none").data[0]
  )

# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label= str(round(-5 + i*0.2,2))
  )
  step["args"][0]["visible"][i] = True
  steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Growth factor: k = "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
  sliders=sliders,
  xaxis=dict(gridcolor='white'),
  yaxis=dict(gridcolor='white',range=[-0.1, 2]),
  #plot_bgcolor='white'
)
#fig.update_xaxes({'gridcolor': 'grey', 'zerolinecolor': 'black', 'linecolor': 'black', 'linewidth': 2})
#fig.update_yaxes({'gridcolor': 'grey', 'zerolinecolor': 'black'})

fig.show()

```



## Euler's Method

```{code-cell}
:tags: [remove-input]

import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

b = 1      # the damping coefficient (you can change this value)
m = 1      # the particle mass (you can change this, too)
v0 = 5     # the initial velocity
dt = 0.5   # the time step (you can also change this, if you like)



# Solving exactly gives the equation v(t) = v0 * exp(-b/m t)
# Let's plot the comparison between the Euler’s-method solution and the true function


# Create figure
fig = go.Figure()

x = np.arange(0, 1.05, 0.05)


# plot solution
fig.add_trace(
  go.Scatter(
    x=x, y=v0 * np.exp(-b/m * x),
    mode='lines', name='true',
    marker={'color': 'rgba(0, 0, 255, 0.8)'},
  )
)

# Add Euler's method, one for each slider step
delta = 0.02
for step in np.arange(delta, 0.5+delta, delta):
  v = [v0,]  # initialize an array of velocities
  t = [0, ]  # and an array of times

  while t[-1] < 1:
    dv = -b / m * v[-1] * step  # compute the change in velocity, assumed constant over time interval
    v.append(v[-1] + dv)      # append the new velocity to the growing array of velocities
    t.append(t[-1] + step)      # and append the new time

  fig.add_trace(
    go.Scatter(
      x=t, y=v, 
      name='Euler', 
      visible=False,
      mode='markers', 
      marker_color='rgba(152, 0, 0, 0.8)',
      marker={'size': 8, 'color': 'rgba(152, 0, 0, 0.8)'}
    )
  )

# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)-1):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label= str(round((i+1)*delta,2))
  )
  step["args"][0]["visible"][0] = True
  step["args"][0]["visible"][i+1] = True
  steps.append(step)

sliders = [dict(
    active=9,
    currentvalue={"prefix": "Step size: dt = "},
    pad={"t": 50},
    steps=steps
)]


fig.update_layout(
  sliders=sliders,
  xaxis=dict(title={'text': 't'},range=[-0.1, 1.1]),
  yaxis=dict(title={'text': 'v'},range=[-0.1, 5.1]),
  #font=dict(size=18)
)
fig.show()

```