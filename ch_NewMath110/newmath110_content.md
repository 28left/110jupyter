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

# Possible New Interactive Content


## Secant Lines

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np

#Function

delta = 0.1
x=np.arange(-3.5, 5.5+delta, delta)
y = np.sin( x )
y = (x-1)*(x-2)*(x-5)*(x+3)/50 + 0.5



# Create figure
fig = go.Figure()

fig.add_trace(
  go.Scatter(
    visible=False,
    line=dict(color="black", width=2),
    hoverinfo="none",
    showlegend=False,
    x=x,
    y=y
    ))



# Add secant lines, one for each slider step
for step in np.arange(-4, 0, delta):
  fig.add_trace(
    go.Scatter(
      visible=False,
      line=dict(color="red", width=2),
      name="",
      hoverinfo="none",
      showlegend=False,
      x=x,
      y = ((step)*(step-1)*(step-4)*(step+4)/50)*(x-1)/step +  0.5
    )
  )
  fig.add_trace(
    go.Scatter(
      visible=False,
      showlegend=False,
      hoverinfo="none",
      #x=[step], y=[np.sin(step)],
      x=[1,step+1], y=[0.5,(step)*(step-1)*(step-4)*(step+4)/50 + 0.5],
      mode='markers',
      marker_color="red",
       marker_size=8
    )
  )


fig.add_trace(
  go.Scatter(
    visible=False,
    showlegend=False,
    hoverinfo="none",
    x=[1], y=[0.5],
    mode='markers',
    marker_color="red",
    marker_size=8
  )
)
fig.add_trace(
  go.Scatter(
    visible=False,
    showlegend=False,
    hoverinfo="none",
    x=[1], y=[0.5],
    mode='markers',
    marker_color="red",
    marker_size=8
  )
)


for step in np.arange(delta, 4+delta, delta):
  fig.add_trace(
    go.Scatter(
      visible=False,
      line=dict(color="red", width=2),
      name="",
      hoverinfo="none",
      showlegend=False,
      x=x,
      y = ((step)*(step-1)*(step-4)*(step+4)/50)*(x-1)/step +  0.5
    )
  )
  fig.add_trace(
    go.Scatter(
      visible=False,
      showlegend=False,
      hoverinfo="none",
      #x=[step], y=[np.sin(step)],
      x=[1,step+1], y=[0.5,(step)*(step-1)*(step-4)*(step+4)/50 + 0.5],
      mode='markers',
      marker_color="red",
       marker_size=8
    )
  )


# Make 10th trace visible
fig.data[0].visible = True
fig.data[91].visible = True
fig.data[92].visible = True

# Create and add slider
steps = []
for i in range(int(len(fig.data)/2-0.5)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label= str(round(-4 + i*delta,1))
  )
  step["args"][0]["visible"][0] = True
  step["args"][0]["visible"][2*i+1] = True  # Toggle i'th trace to "visible"
  step["args"][0]["visible"][2*i+2] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
    active=45,
    currentvalue={"prefix": "h = "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    xaxis=dict(gridcolor='white'),
    yaxis=dict(gridcolor='white',range=[-2, 2]),
    #plot_bgcolor='white'
)
#fig.update_xaxes({'gridcolor': 'grey', 'zerolinecolor': 'black', 'linecolor': 'black', 'linewidth': 2})
#fig.update_yaxes({'gridcolor': 'grey', 'zerolinecolor': 'black'})

fig.show()

```




## Tangent Lines



```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np

#Function

delta = 0.05
x=np.arange(-3.5, 5.5+delta, delta)
y = np.sin( x )
y = (x-1)*(x-2)*(x-5)*(x+3)/50 + 0.5



# Create figure
fig = go.Figure()

fig.add_trace(
  go.Scatter(
    visible=False,
    line=dict(color="black", width=2),
    hoverinfo="none",
    showlegend=False,
    x=x,
    y=y
    ))



# Add tangent lines, one for each slider step
for step in np.arange(-3, 5+delta, delta):
  fig.add_trace(
    go.Scatter(
      visible=False,
      line=dict(color="grey", width=2),
      name="",
      hoverinfo="none",
      showlegend=False,
      x=x,
      y = (4*(step-1)**3 - 3*(step-1)**2 - 32*(step-1) + 16)*(x-step)/50 + (step-1)*(step-2)*(step-5)*(step+3)/50 + 0.5
    )
  )
  fig.add_trace(
    go.Scatter(
      visible=False,
      showlegend=False,
      hoverinfo="none",
      x=[step], y=[(step-1)*(step-2)*(step-5)*(step+3)/50 + 0.5],
      mode='markers',
      marker_color="red",
       marker_size=8
    )
  )


# Make 10th trace visible
fig.data[0].visible = True
fig.data[81].visible = True
fig.data[82].visible = True

# Create and add slider
steps = []
for i in range(int(len(fig.data)/2-0.5)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label= str(round(-3 + i*delta,2))
  )
  step["args"][0]["visible"][0] = True
  step["args"][0]["visible"][2*i+1] = True  # Toggle i'th trace to "visible"
  step["args"][0]["visible"][2*i+2] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
    active=40,
    currentvalue={"prefix": "Point of Tangency: x = "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    xaxis=dict(gridcolor='white'),
    yaxis=dict(gridcolor='white',range=[-2, 2]),
    #plot_bgcolor='white'
)
#fig.update_xaxes({'gridcolor': 'grey', 'zerolinecolor': 'black', 'linecolor': 'black', 'linewidth': 2})
#fig.update_yaxes({'gridcolor': 'grey', 'zerolinecolor': 'black'})

fig.show()

```
<!-->
- Equation of Tangent Line
- Example
- Find all points on the curve that have a horizontal tangent line
- Significance of horizontal tangent lines
-->


## Exponential Functions



```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np

#Function

delta = 0.05
x=np.arange(-4.5, 4.5+delta, delta)




# Create figure
fig = go.Figure()





# Add tangent lines, one for each slider step
deltaB = 0.05

for step in np.arange(deltaB, 5, deltaB):
  fig.add_trace(
  go.Scatter(
    visible=False,
    line=dict(color="black", width=2),
    hoverinfo="none",
    showlegend=False,
    x=x,
    y=step**x
    )
  )



# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label= str(round((i+1)*deltaB,2))
  )
  step["args"][0]["visible"][i] = True
  steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Exponential Base: b = "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    xaxis=dict(gridcolor='white'),
    yaxis=dict(gridcolor='white',range=[-0.1, 4]),
    #plot_bgcolor='white'
)
#fig.update_xaxes({'gridcolor': 'grey', 'zerolinecolor': 'black', 'linecolor': 'black', 'linewidth': 2})
#fig.update_yaxes({'gridcolor': 'grey', 'zerolinecolor': 'black'})

fig.show()

```




## Compound Interest


```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
import numpy as np

#Function

delta = 0.01
x=np.arange(0, 10+delta, delta)




# Create figure
fig = go.Figure()

# Add tangent lines, one for each slider step
for step in np.arange(1, 366, 1):
  fig.add_trace(
  go.Scatter(
    visible=False,
    name='Accumulated Amount',
    line=dict(color="black", width=2),
    showlegend=False,
    x=x,
    y=(1 + 0.1/step)**np.floor(step*x)
    )
  )



# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label= str(i+1)
  )
  step["args"][0]["visible"][i] = True
  steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Conversion Periods: m = "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders,
    xaxis=dict(gridcolor='white'),
    yaxis=dict(gridcolor='white',range=[-0.1, 3]),
    #plot_bgcolor='white'
)
#fig.update_xaxes({'gridcolor': 'grey', 'zerolinecolor': 'black', 'linecolor': 'black', 'linewidth': 2})
#fig.update_yaxes({'gridcolor': 'grey', 'zerolinecolor': 'black'})

fig.show()

```



