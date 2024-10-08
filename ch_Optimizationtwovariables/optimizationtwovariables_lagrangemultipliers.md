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

# Lagrange Multipliers

## How to Optimize a Function Subject to a Constraint




```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np



# Create the figure
fig = go.Figure()


# Add the surface trace
u, v = np.mgrid[0:4:100j, 0:2*np.pi:100j]
x_surface = u*np.cos(v)
y_surface = u*np.sin(v)
z_surface = (x_surface**2 + y_surface**2)**0.5
fig.add_trace(go.Surface(x=x_surface, y=y_surface, z=z_surface, 
  hoverinfo='none', showscale=False, colorscale=[[0,'darkgray'],[1,'lightgray']])
)


# Add the constraint trace
x, z = np.mgrid[-4:4:50j, 0:4:50j]
fig.add_trace(go.Surface(x=x, y=2-x/2, z=z, 
  colorscale=[[0,'red'],[1,'red']], hoverinfo="none", showscale=False, opacity=0.33)
)

# Customize traces
fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=False)
  )


# Add the curve trace
x_curve = np.linspace(-2.4, 4, 100)
y_curve = 2 - x_curve/2
z_curve = (x_curve**2 + y_curve**2)**0.5 # np.cos(x_curve)
fig.add_trace(go.Scatter3d(x=x_curve, y=y_curve, z=z_curve,
  mode='lines', hoverinfo='none', line=dict(color='black', width=5))
)


# Customize layout
fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=0, r=0, b=25, t=0)
)

# Show the plot
fig.show()
```



```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np



# Create the figure
fig = go.Figure()


# Add the surface trace
u, v = np.mgrid[0:4:100j, 0:2*np.pi:100j]
x_surface, y_surface = np.mgrid[-2.5:2.5:100j, -2.5:2.5:100j]
#x_surface = u*np.cos(v)
#y_surface = u*np.sin(v)
z_surface = (x_surface-0.25)**2 + 2*(y_surface-0.25)**2
fig.add_trace(go.Surface(x=x_surface, y=y_surface, z=z_surface, 
  hoverinfo='none', showscale=False, colorscale=[[0,'darkgray'],[1,'white']])
)


# Add the constraint trace
x = np.cos(v)
y = np.sin(v)
z = np.linspace(0, 8, 50)
fig.add_trace(go.Surface(x=x, y=y, z=u, 
  colorscale=[[0,'red'],[1,'red']], hoverinfo="none", showscale=False, opacity=0.33)
)

# Customize traces
fig.update_traces(
  contours_x=dict(show=False, usecolormap=True, highlight=False, project_x=False),
  contours_y=dict(show=False, usecolormap=True, highlight=False, project_y=False),
  contours_z=dict(show=True, usecolormap=False, highlightcolor="black", project_z=False)
  )


# Add the curve trace
t = np.linspace(0, 6.29, 100)
x_curve = np.cos(t)
y_curve = np.sin(t)
z_curve = (x_curve-0.25)**2 + 2*(y_curve-0.25)**2
fig.add_trace(go.Scatter3d(x=x_curve, y=y_curve, z=z_curve,
  mode='lines', hoverinfo='none', line=dict(color='black', width=5))
)


# Customize layout
fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False,range=[-2.5,2.5]),
      yaxis = dict(visible=True,showgrid=True,showspikes=False,range=[-2.5,2.5]),
      zaxis = dict(visible=True,showgrid=True,showspikes=False,range=[0,4])
  ),
  margin=dict(l=0, r=0, b=25, t=0)
)

# Show the plot
fig.show()
```




```{admonition} The Method of Lagrange Multipliers
:class: info


```

### Example 1

```{admonition} Lagrange multipliers
:class: tip

Find the extreme values of $f(x,y) = \sqrt{x^2 + y^2}$ subject to the constraint $x + 2y = 4$.  In other words, find the shortest distance from a point on line to the origin.
```

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np

#Function
delta = 0.1
xrange = np.arange(-8, 8, delta)
yrange = np.arange(-4, 4, delta)
x, y = np.meshgrid(xrange,yrange)
F = (x**2 + y**2)**0.5
C = x + 2*y - 4

# Create figure
fig = go.Figure()

# draw sample contours
fig.add_trace(
  go.Contour(
    z = F,
    x = xrange,
    y = yrange,
    contours_coloring='lines',
    colorscale=[[0,'lightgray'],[1,'lightgray']],
    showscale=False,
    line_width = 2,
    hoverinfo="none",
    contours=dict(
            start=0,
            end=8,
            size=2,
            showlabels = True,
            labelfont = dict( 
                size = 15,
                color = 'black',
            )
        ),
    )
)

# draw constraint function
fig.add_trace(
  go.Contour(
    z = C,
    x = xrange,
    y = yrange,
    contours_coloring='lines',
    colorscale=[[0,'red'],[1,'red']],
    showscale=False,
    line_width = 2,
    hoverinfo="none",
    contours=dict(
            start=0,
            end=0,
            size=2
        ),
    )
)



# Add contours, one for each slider step
for step in np.arange(0, 4, 0.05):
  fig.add_trace(
    go.Contour(
      z = F,
      x = xrange,
      y = yrange,
      visible=False,
      contours_coloring='lines',
      colorscale=[[0,'black'],[1,'black']],
      showscale=False,
      line_width = 2,
      hoverinfo="none",
      contours=dict(
        start=step,
        end=step,
        size=2
      ),
    )
  )

# Make 10th trace visible
fig.data[0].visible = True
fig.data[1].visible = True
fig.data[10].visible = True


# Create and add slider
steps = []
for i in range(len(fig.data)-2):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label=str(round(i*0.05,2))
  )
  step["args"][0]["visible"][0] = True
  step["args"][0]["visible"][1] = True
  step["args"][0]["visible"][i+2] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Current Level Curve: z = "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    yaxis_scaleanchor="x"
)

fig.show()

```



### Example 2

```{admonition} Lagrange multipliers
:class: tip

Find the extreme values of $f(x,y) = (x-0.5)^2 + 2(y-0.5)^2$ subject to the constraint $xy = 1$.  
```

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np

#Function
delta = 0.1
xrange = np.arange(-3.5, 4.5, delta)
yrange = np.arange(-1.5, 2.5, delta)
x, y = np.meshgrid(xrange,yrange)
F = (x - 0.5)**2 + 2*(y - 0.5)**2
C = x*y - 1

# Create figure
fig = go.Figure()


# draw sample contours
fig.add_trace(
  go.Contour(
    z = F,
    x = xrange,
    y = yrange,
    contours_coloring='lines',
    colorscale=[[0,'lightgray'],[1,'lightgray']],
    showscale=False,
    line_width = 2,
    hoverinfo="none",
    contours=dict(
            start=0,
            end=30,
            size=2,
            showlabels = True,
            labelfont = dict( 
                size = 15,
                color = 'black',
            )
        ),
    )
)

# draw constraint function
fig.add_trace(
  go.Contour(
    z = C,
    x = xrange,
    y = yrange,
    contours_coloring='lines',
    colorscale=[[0,'red'],[1,'red']],
    showscale=False,
    line_width = 2,
    hoverinfo="none",
    contours=dict(
            start=0,
            end=0,
            size=2
        ),
    )
)



# Add contours, one for each slider step
for step in np.arange(0, 7, 0.1):
  fig.add_trace(
    go.Contour(
      z = F,
      x = xrange,
      y = yrange,
      visible=False,
      contours_coloring='lines',
      colorscale=[[0,'black'],[1,'black']],
      showscale=False,
      line_width = 2,
      hoverinfo="none",
      contours=dict(
        start=step,
        end=step,
        size=2
      ),
    )
  )

# Make 10th trace visible
fig.data[0].visible = True
fig.data[1].visible = True
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)-2):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label=str(i/10)
  )
  step["args"][0]["visible"][0] = True
  step["args"][0]["visible"][1] = True
  step["args"][0]["visible"][i+2] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Current Level Curve: z = "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    yaxis_scaleanchor="x"
)

fig.show()

```



### Example 3

```{admonition} Lagrange multipliers
:class: tip

Find the extreme values of $f(x,y) = (x-0.25)^2 + 2(y-0.25)^2$ subject to the constraint $x^2 + y^2 = 1$.  
```

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np

#Function
delta = 0.1
xrange = np.arange(-3, 3, delta)
yrange = np.arange(-1.5, 1.5, delta)
x, y = np.meshgrid(xrange,yrange)
F = (x - 0.25)**2 + 2*(y - 0.25)**2
C = x**2 + y**2 - 1

# Create figure
fig = go.Figure()


# draw sample contours
fig.add_trace(
  go.Contour(
    z = F,
    x = xrange,
    y = yrange,
    contours_coloring='lines',
    colorscale=[[0,'lightgray'],[1,'lightgray']],
    showscale=False,
    line_width = 2,
    hoverinfo="none",
    contours=dict(
            start=0,
            end=12,
            size=2,
            showlabels = True,
            labelfont = dict( 
                size = 15,
                color = 'black',
            )
        ),
    )
)


# draw constraint function
fig.add_trace(
  go.Contour(
    z = C,
    x = xrange,
    y = yrange,
    contours_coloring='lines',
    colorscale=[[0,'red'],[1,'red']],
    showscale=False,
    line_width = 2,
    hoverinfo="none",
    contours=dict(
            start=0,
            end=0,
            size=2
        ),
    )
)


# Add contours, one for each slider step
for step in np.arange(0, 4, 0.05):
  fig.add_trace(
    go.Contour(
      z = F,
      x = xrange,
      y = yrange,
      visible=False,
      contours_coloring='lines',
      colorscale=[[0,'black'],[1,'black']],
      showscale=False,
      line_width = 2,
      hoverinfo="none",
      contours=dict(
        start=step,
        end=step,
        size=2
      ),
    )
  )

# Make 10th trace visible
fig.data[0].visible = True
fig.data[1].visible = True
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)-2):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label=str(round(i*0.05,2))
  )
  step["args"][0]["visible"][0] = True
  step["args"][0]["visible"][1] = True
  step["args"][0]["visible"][i+2] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Current Level Curve: z = "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    yaxis_scaleanchor="x"
)

fig.show()

```





