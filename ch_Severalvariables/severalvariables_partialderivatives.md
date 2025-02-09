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

# Partial Derivatives


## Differentiation of Functions of Several Variables


```{admonition} Limit Definition of the First Partial Derivatives of $f(x,y)$

The _**first partial derivative of $f$ with respect to $x$**_, denoted $\dfrac{\partial f}{\partial x}$ or $f_x(x,y)$, is the function defined by

$$\frac{\partial f}{\partial x} = f_x(x,y) = \lim_{h\to 0} \frac{f(x+h,y) - f(x,y)}{h}$$

The _**first partial derivative of $f$ with respect to $y$**_, denoted $\dfrac{\partial f}{\partial y}$ or $f_y(x,y)$, is the function defined by

$$\frac{\partial f}{\partial y} = f_y(x,y) = \lim_{k\to 0} \frac{f(x,y+k) - f(x,y)}{k}$$

```


```{admonition} How to Compute a Partial Derivative

The limit definition of a partial derivative can be extended to functions of three or more variables.  But like derivatives of functions of one variable, we'd prefer not to use the limit definition when it comes time to compute a partial derivative.

Instead, to compute the partial derivative of $f$ with respect to one variable, treat all the other variables as if they are constants, and then apply the usual rules of differentiation.
```



### Example 1

````{admonition} Computing partial derivatives
:class: tip

Consider the function $f(x,y) = \dfrac{1}{2}x^3 - xy^2$.

```{dropdown} Treat $x$ as the variable and $y$ as a constant.

For example, if we let $y=2$, then 

$$z = f(x,2) = \dfrac{1}{2}x^3 - 4x$$ 

is a cubic polynomial in $x$ and $\dfrac{dz}{dx} = \dfrac{3}{2}x^2 - 4$.

In general, if we treat $y$ as a constant, then $f(x,y) = \dfrac{1}{2}x^3 - xy^2$ can be thought of as a function of $x$, and its partial derivative with respect to $x$ is given by

$$f_x(x,y) = \dfrac{3}{2}x^2 - y^2.$$
```

```{dropdown} Treat $y$ as the variable and $x$ as a constant.

For example, if we let $x=-1$, then 

$$z = f(-1,y) = -\dfrac{1}{2} + y^2$$ 

is a quadratic polynomial in $y$ and $\dfrac{dz}{dy} = 2y$.

In general, if we treat $x$ as a constant, then $f(x,y) = \dfrac{1}{2}x^3 - xy^2$ can be thought of as a function of $y$, and its partial derivative with respect to $y$ is given by

$$f_y(x,y) = -2xy.$$
```

````


```{admonition} Vertical Cross Sections
:class: note

For a given function of two variables, $f(x,y)$, when we plug in $y = b$, we can interpret the resulting function of one variable, $z = f(x,b)$, as the intersection of the surface $z=f(x,y)$ and the vertical plane $y=b$.  Similarly, when we plug in $x = a$, we can interpret the resulting function of one variable, $z = f(a,y)$, as the intersection of the surface $z=f(x,y)$ and the vertical plane $x=a$.

Two copies of the graph of the function $z = \dfrac{1}{2}x^3 - xy^2$ are shown below.  On the left, the surface is displayed along with the vertical plane $y = b$ where the value of $b$ can be adjused using the slider below the graph.  The intersection of the suface and the plane is drawn in black and is the graph of the function $z = f(x,b) = \dfrac{1}{2}x^3 - b^2x$, which is a cubic polynomial in $x$. 

On the right, the surface is displayed along with the vertical plane $x = a$ where the value of $a$ can be adjused using the slider below the graph.  The intersection of the suface and the plane is drawn in black and is the graph of the function $z = f(a,y) = \dfrac{1}{2}a^3 - ay^2$, which is a quadratic polynomial in $y$.
```

<style>
table {
    border-collapse: collapse;
}
table, th, td {
   border: none;
   padding: none;
}
blockquote {
    border-left: none;
    padding-left: 0px;
}
tr:hover {background-color: #EEEEEE;}
</style>

<!--cellspacing="0" cellpadding="0" borderspacing="0"-->
<table width=100%  style='border: none; padding: none'>
<tr>
<td width=50%>

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

#u, v = np.mgrid[0:2:50j, 0:2*np.pi:50j]
#x = u*np.cos(v)
#y = u*np.sin(v)
#z = x**2 + y**2
x, y = np.mgrid[-1.5:1.51:50j, -1.5:1.51:50j]
z = x**3/2 - 1*x*y**2

u,v = np.mgrid[-1.5:1.5:50j, -1.9:1.9:50j]

# Create figure
fig = go.Figure()

# Add contours, one for each slider step
for step in np.arange(-1.5,1.6, 0.1):
  fig.add_trace(
    go.Surface(
      contours = {"y": {"show": True, "start": step, "end": step+0.5, "size": 2}},
      x=x, y=y, z=z,
      colorscale='Pinkyl',
      hoverinfo="none",
      visible=False,
      showscale=False)
    )
  fig.add_trace(
    go.Surface(
      x=u, y=step+0*u+0*v, z=v, 
      colorscale=[[0,'lightgray'],[1,'lightgray']], 
      hoverinfo="none",
      showscale=False, 
      visible=False,
      opacity=0.33)
    )



# Make 50th trace visible
fig.data[50].visible = True
fig.data[51].visible = True

# Create and add slider
steps = []
for i in range(int(len(fig.data)/2)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label=str(round(-1.5 + i/10,2))
  )
  step["args"][0]["visible"][2*i] = True  # Toggle i'th trace to "visible"
  step["args"][0]["visible"][2*i+1] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
  y=0.1,
    active=25,
    currentvalue={"prefix": "Current Vertical Cross Section: y = "},
    pad={"t": 50},
    steps=steps
)]


fig.update_traces(
  contours_x=dict(show=False, highlight=False),
  contours_y=dict(show=True, usecolormap=False, highlightcolor="black", project_y=False),
  contours_z=dict(show=False, highlight=False)
  )


fig.update_layout(
  sliders=sliders,
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=40, r=40, b=80, t=0)
)

fig.show()
```

</td>
<td width=50%>

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

#u, v = np.mgrid[0:2:50j, 0:2*np.pi:50j]
#x = u*np.cos(v)
#y = u*np.sin(v)
#z = x**2 + y**2
x, y = np.mgrid[-1.5:1.51:50j, -1.5:1.51:50j]
z = x**3/2 - 1*x*y**2

u,v = np.mgrid[-1.5:1.5:50j, -1.9:1.9:50j]

# Create figure
fig = go.Figure()

# Add contours, one for each slider step
for step in np.arange(-1.5,1.6, 0.1):
  fig.add_trace(
    go.Surface(
      contours = {"x": {"show": True, "start": step, "end": step+0.5, "size": 2}},
      x=x, y=y, z=z,
      colorscale='Pinkyl',
      hoverinfo="none",
      visible=False,
      showscale=False)
    )
  fig.add_trace(
    go.Surface(
      x=step+0*u+0*v, y=u, z=v, 
      colorscale=[[0,'lightgray'],[1,'lightgray']], 
      hoverinfo="none",
      showscale=False, 
      visible=False,
      opacity=0.33)
    )



# Make 50th trace visible
fig.data[50].visible = True
fig.data[51].visible = True

# Create and add slider
steps = []
for i in range(int(len(fig.data)/2)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label=str(round(-1.5 + i/10,2))
  )
  step["args"][0]["visible"][2*i] = True  # Toggle i'th trace to "visible"
  step["args"][0]["visible"][2*i+1] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
  y=0.1,
    active=25,
    currentvalue={"prefix": "Current Vertical Cross Section: x = "},
    pad={"t": 50},
    steps=steps
)]


fig.update_traces(
  contours_x=dict(show=True, usecolormap=False, highlightcolor="black", project_x=False),
  contours_y=dict(show=False, highlight=False),
  contours_z=dict(show=False, highlight=False)
  )


fig.update_layout(
  sliders=sliders,
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=40, r=40, b=80, t=0)
)

fig.show()
```


</td>
</tr>
</table>



<!--

### Example - y is a constant

```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

#u, v = np.mgrid[0:2:50j, 0:2*np.pi:50j]
#x = u*np.cos(v)
#y = u*np.sin(v)
#z = x**2 + y**2
x, y = np.mgrid[-1.5:1.51:50j, -1.5:1.51:50j]
z = x**3/2 - 1*x*y**2

u,v = np.mgrid[-1.5:1.5:50j, -1.9:1.9:50j]

# Create figure
fig = go.Figure()

# Add contours, one for each slider step
for step in np.arange(-1.5,1.6, 0.1):
  fig.add_trace(
    go.Surface(
      contours = {"y": {"show": True, "start": step, "end": step+0.5, "size": 2}},
      x=x, y=y, z=z,
      colorscale='Pinkyl',
      hoverinfo="none",
      visible=False,
      showscale=False)
    )
  fig.add_trace(
    go.Surface(
      x=u, y=step+0*u+0*v, z=v, 
      colorscale=[[0,'lightgray'],[1,'lightgray']], 
      hoverinfo="none",
      showscale=False, 
      visible=False,
      opacity=0.33)
    )



# Make 50th trace visible
fig.data[50].visible = True
fig.data[51].visible = True

# Create and add slider
steps = []
for i in range(int(len(fig.data)/2)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label=str(round(-1.5 + i/10,2))
  )
  step["args"][0]["visible"][2*i] = True  # Toggle i'th trace to "visible"
  step["args"][0]["visible"][2*i+1] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
    active=25,
    currentvalue={"prefix": "Current Vertical Cross Section: y = "},
    pad={"t": 50},
    steps=steps
)]


fig.update_traces(
  contours_x=dict(show=False, highlight=False),
  contours_y=dict(show=True, usecolormap=False, highlightcolor="black", project_y=False),
  contours_z=dict(show=False, highlight=False)
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

-->


<!--
### Example - x is a constant


```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

#u, v = np.mgrid[0:2:50j, 0:2*np.pi:50j]
#x = u*np.cos(v)
#y = u*np.sin(v)
#z = x**2 + y**2
x, y = np.mgrid[-1.5:1.51:50j, -1.5:1.51:50j]
z = x**3/2 - 1*x*y**2

u,v = np.mgrid[-1.5:1.5:50j, -1.9:1.9:50j]

# Create figure
fig = go.Figure()

# Add contours, one for each slider step
for step in np.arange(-1.5,1.6, 0.1):
  fig.add_trace(
    go.Surface(
      contours = {"x": {"show": True, "start": step, "end": step+0.5, "size": 2}},
      x=x, y=y, z=z,
      colorscale='Pinkyl',
      hoverinfo="none",
      visible=False,
      showscale=False)
    )
  fig.add_trace(
    go.Surface(
      contours = {"y": {"show": True, "start": -1.5, "end": 1.5, "size": 0.5, "color": "white"}, "z": {"show": True, "start": -1.9, "end": 1.9, "size": 0.5, "color": "white"}},
      x=step+0*u+0*v, y=u, z=v, 
      colorscale=[[0,'lightgray'],[1,'lightgray']], 
      hoverinfo="none",
      showscale=False, 
      visible=False,
      opacity=0.33)
    )



# Make 50th trace visible
fig.data[50].visible = True
fig.data[51].visible = True

# Create and add slider
steps = []
for i in range(int(len(fig.data)/2)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label=str(round(-1.5 + i/10,2))
  )
  step["args"][0]["visible"][2*i] = True  # Toggle i'th trace to "visible"
  step["args"][0]["visible"][2*i+1] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
    active=25,
    currentvalue={"prefix": "Current Vertical Cross Section: x = "},
    pad={"t": 50},
    steps=steps
)]


fig.update_traces(
  contours_x=dict(show=True, usecolormap=False, highlightcolor="black", project_x=False),
  contours_y=dict(show=False, highlight=False),
  contours_z=dict(show=False, highlight=False)
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

-->


<!--

### Attempt at two sliders


```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

x, y = np.mgrid[-1.5:1.5:50j, -1.5:1.5:50j]
z = x**3/2 - 1*x*y**2

u,v = np.mgrid[-1.5:1.5:50j, -1.75:1.75:50j]

fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Contours parallel to yz-plane', 'Contours parallel to xz-plane'],
                    )


# Add contours, one for each slider step
for step in np.arange(-1.5,1.6, 0.1):
  fig.add_trace(
    go.Surface(
      contours = {"y": {"show": True, "start": step, "end": step+0.5, "size": 2}},
      x=x, y=y, z=z,
      colorscale='Pinkyl',
      hoverinfo="none",
      visible=False,
      showscale=False),1,1
    )
  fig.add_trace(
    go.Surface(
      x=u, y=step+0*u+0*v, z=v, 
      colorscale=[[0,'lightgray'],[1,'lightgray']], 
      hoverinfo="none",
      showscale=False, 
      visible=False,
      opacity=0.33),1,1
    )

# Make 50th trace visible
fig.data[50].visible = True
fig.data[51].visible = True

# Create and add slider
steps = []
for i in range(int(len(fig.data)/2)):
  step = dict(
    method="update",
    args=[{"visible": [False] * len(fig.data)}],
    label=str(round(-1.5 + i/10,2))
  )
  step["args"][0]["visible"][2*i] = True  # Toggle i'th trace to "visible"
  step["args"][0]["visible"][2*i+1] = True  # Toggle i'th trace to "visible"
  steps.append(step)

sliders = [dict(
  xanchor="right",x=0.5,
    active=25,
    currentvalue={"prefix": "Current Vertical Cross Section: y = "},
    pad={"t": 50},
    steps=steps
),dict(x=0.6,active=25,xanchor="left",
    currentvalue={"prefix": "Current Vertical Cross Section: x= "},
    pad={"t": 50},
    steps=steps)]


fig.update_traces(
  contours_x=dict(show=False, highlight=False),
  contours_y=dict(show=True, usecolormap=False, highlightcolor="black", project_y=False),
  contours_z=dict(show=False, highlight=False),
  row=1, col=1
  )


fig.update_layout(
  sliders=sliders,
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=20, r=20, b=50, t=0)
)


fig.add_trace(go.Surface(
  contours = {"x": {"show": True, "start": 1, "end": 1.5, "size": 2}},
  x=x, y=y, z=z,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False), 
  1,2)

fig.add_trace(go.Surface(
    x=1+0*u+0*v, y=u, z=v, 
    colorscale=[[0,'lightgray'],[1,'lightgray']], 
    hoverinfo="none",
    showscale=False, 
    opacity=0.33
    ),
    1,2
)

fig.update_traces(
  contours_x=dict(show=True, usecolormap=False, highlightcolor="black", project_x=False),
  contours_y=dict(show=False, highlight=False, project_y=False),
  contours_z=dict(show=False, highlight=False, project_z=False),
  row=1, col=2
  )


fig.update_layout(
  scene2 = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  )
)


fig.show()
```
-->



<!--
### Example - Two images - no slider



```{code-cell}
:tags: [remove-input]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

#u, v = np.mgrid[0:2:50j, 0:2*np.pi:50j]
#x = u*np.cos(v)
#y = u*np.sin(v)
#z = x**2 + y**2
x, y = np.mgrid[-1.5:1.5:50j, -1.5:1.5:50j]
z = x**3/2 - 1*x*y**2

u,v = np.mgrid[-1.5:1.5:50j, -1.75:1.75:50j]

fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Contours parallel to yz-plane', 'Contours parallel to xz-plane'],
                    )


fig.add_trace(
  go.Surface(
    contours = {"y": {"show": True, "start": 1, "end": 1.5, "size": 2}},
    x=x, y=y, z=z,
    colorscale='Pinkyl',
    hoverinfo="none",
    showscale=False), 
    1, 1)

fig.add_trace(
  go.Surface(
    x=u, y=1+0*u+0*v, z=v, 
    colorscale=[[0,'lightgray'],[1,'lightgray']], 
    hoverinfo="none",
    showscale=False, 
    opacity=0.33),
    1,1)


fig.add_trace(go.Surface(
  contours = {"x": {"show": True, "start": 1, "end": 1.5, "size": 2}},
  x=x, y=y, z=z,
  colorscale='Pinkyl',
  hoverinfo="none",
  showscale=False), 
  1,2)

fig.add_trace(go.Surface(
    x=1+0*u+0*v, y=u, z=v, 
    colorscale=[[0,'lightgray'],[1,'lightgray']], 
    hoverinfo="none",
    showscale=False, 
    opacity=0.33
    ),
    1,2
)


fig.update_traces(
  contours_x=dict(show=False, highlight=False),
  contours_y=dict(show=True, usecolormap=False, highlightcolor="black", project_y=False),
  contours_z=dict(show=False, highlight=False),
  row=1, col=1
  )


fig.update_traces(
  contours_x=dict(show=True, usecolormap=False, highlightcolor="black", project_x=False),
  contours_y=dict(show=False, highlight=False, project_y=False),
  contours_z=dict(show=False, highlight=False, project_z=False),
  row=1, col=2
  )


fig.update_layout(
  scene = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  scene2 = dict(
      xaxis = dict(visible=True,showgrid=True,showspikes=False),
      yaxis = dict(visible=True,showgrid=True,showspikes=False),
      zaxis = dict(visible=True,showgrid=True,showspikes=False)
  ),
  margin=dict(l=40, r=20, b=50, t=0)
)


fig.show()
```
-->


### Example 2
````{admonition} Compute the indicated partial derivatives
:class: tip

Compute each of the following partial derivatives.

1. $\dfrac{\partial}{\partial x} x^3$

```{dropdown} Answer

$$\dfrac{\partial}{\partial x} x^3 = 3x^2$$ 

since $x^3$ is a function of one variable, which means computing its partial derivative is the same as computing its derivative (i.e., $\dfrac{\partial}{\partial x} x^3 = \dfrac{d}{d x} x^3 = 3x^2$).
```

2. $\dfrac{\partial}{\partial y} \sqrt{x}y$

```{dropdown} Answer

$$\dfrac{\partial}{\partial y} \sqrt{x}y = \sqrt{x}$$ 

since computing the partial derivative with respect to $y$ means all other variables are treated as constants.  In particular, $x$ is treated as a constant, and therefore $\sqrt{x}$ is a constant.  And the derivative of a constant times $y$ with respect to $y$ is equal to the constant (i.e., $\frac{d}{dy} cy = c$ where $c$ is a constant).
```

3. $\dfrac{\partial}{\partial y} xe^z$

```{dropdown} Answer

$$\dfrac{\partial}{\partial y} xe^z = 0$$ 

since computing the partial derivative with respect to $y$ means all other variables are treated as constants.  In particular, $x$ and $z$ are treated as constants, and therefore $xe^z$ is a constant, which means its derivative with respect to $y$ is zero.
```

4. $\dfrac{\partial}{\partial x} x^2\ln(y)$

```{dropdown} Answer

$$\dfrac{\partial}{\partial x} x^2\ln(y) = 2x\ln(y)$$ 

since computing the partial derivative with respect to $x$ means all other variables are treated as constants.  In particular, $y$ is treated as a constant, and therefore $\ln(y)$ is a constant.
```
````




### Example 3
````{admonition} Compute all first partial derivatives
:class: tip

Compute all first partial derivatives of $f(x,y) = \dfrac{3x^7}{y^4}$ 

```{dropdown} **Step 1:** &nbsp; Compute $f_x(x,y)$.

Treating $y$ as if it is a constant, we have

\begin{align*}
\frac{\partial}{\partial x} \left(\dfrac{3x^7}{y^4}\right)
&= \frac{\partial}{\partial x} \left(\frac{3}{y^4}x^7 \right) \\
&= \frac{3}{y^4} \frac{\partial}{\partial x} (x^7) && \text{constant multiple rule} \\
&= \frac{3}{y^4} 7x^6 && \text{power rule} \\
&= \frac{21x^6}{y^4} 
\end{align*}

```


```{dropdown} **Step 2:** &nbsp; Compute $f_y(x,y)$.

Treating $x$ as if it is a constant, we have

\begin{align*}
\frac{\partial}{\partial y} \left(\dfrac{3x^7}{y^4}\right)
&= \frac{\partial}{\partial y} (3x^7y^{-4}) \\
&= 3x^7 \frac{\partial}{\partial y} (y^{-4}) && \text{constant multiple rule} \\
&= 3x^7 (-4)y^{-5} && \text{power rule}\\
&= -\frac{12x^7}{y^5} 
\end{align*}
```
````


### Example 4
````{admonition} Compute all first partial derivatives
:class: tip

Compute all first partial derivatives of $f(x,y) = \sqrt{3x^2 - 5y^4}$ 

```{dropdown} **Step 1:** &nbsp; Compute $f_x(x,y)$.

Treating $y$ as if it is a constant, we have

\begin{align*}
\frac{\partial}{\partial x} \sqrt{3x^2 - 5y^4}
&= \frac{\partial}{\partial x} \left(3x^2 - 5y^4 \right)^{1/2} \\
&= \frac{1}{2} \left(3x^2 - 5y^4 \right)^{-1/2} \frac{\partial}{\partial x} (3x^2 - 5y^4 )&& \text{general power rule} \\
&= \frac{1}{2} \left(3x^2 - 5y^4 \right)^{-1/2} (6x-0) \\
&= \frac{3x}{\sqrt{3x^2 - 5y^4}} && \text{simplify} 
\end{align*}

```


```{dropdown} **Step 2:** &nbsp; Compute $f_y(x,y)$.

Treating $x$ as if it is a constant, we have

\begin{align*}
\frac{\partial}{\partial y} \sqrt{3x^2 - 5y^4}
&= \frac{\partial}{\partial y} \left(3x^2 - 5y^4 \right)^{1/2} \\
&= \frac{1}{2} \left(3x^2 - 5y^4 \right)^{-1/2} \frac{\partial}{\partial y} (3x^2 - 5y^4 )&& \text{general power rule} \\
&= \frac{1}{2} \left(3x^2 - 5y^4 \right)^{-1/2} (0-20y^3) \\
&= -\frac{10y^3}{\sqrt{3x^2 - 5y^4}} && \text{simplify} 
\end{align*}
```
````


### Example 5
````{admonition} Compute all first partial derivatives
:class: tip

Compute all first partial derivatives of $f(x,y,z) = z\ln(y) + e^x\ln(z)$ 

```{dropdown} **Step 1:** &nbsp; Compute $f_x(x,y,z)$.

Treating $y$ and $z$ as if they are constants, we have

\begin{align*}
\frac{\partial}{\partial x} \left( z\ln(y) + e^x\ln(z)\right)
&= \frac{\partial}{\partial x} ( z\ln(y)) + \frac{\partial}{\partial x} (e^x\ln(z)) && \text{sum rule} \\
&= 0 + \ln(z)\frac{\partial}{\partial x} (e^x) && \text{derivative of a constant and constant multiple rule} \\
&= \ln(z)e^x && \text{derivative of $e^x$ with respect to $x$} 
\end{align*}

```


```{dropdown} **Step 2:** &nbsp; Compute $f_y(x,y,z)$.

Treating $x$ and $z$ as if they are constants, we have

\begin{align*}
\frac{\partial}{\partial y} \left(z\ln(y) + e^x\ln(z)\right)
&= \frac{\partial}{\partial y} ( z\ln(y)) + \frac{\partial}{\partial y} (e^x\ln(z)) && \text{sum rule} \\
&= z\frac{\partial}{\partial y} (\ln(y)) + 0 && \text{constant multiple rule and derivative of a constant} \\
&= \frac{z}{y} && \text{derivative of $\ln(y)$ with respect to $y$} 
\end{align*}
```


```{dropdown} **Step 3:** &nbsp; Compute $f_z(x,y,z)$.

Treating $x$ and $y$ as if they are constants, we have

\begin{align*}
\frac{\partial}{\partial z} \left(z\ln(y) + e^x\ln(z)\right)
&= \frac{\partial}{\partial z} ( z\ln(y)) + \frac{\partial}{\partial z} (e^x\ln(z)) && \text{sum rule} \\
&= \ln(y)\frac{\partial}{\partial z} (z) + e^x\frac{\partial}{\partial z} (\ln(z)) && \text{constant multiple rule} \\
&= \ln(y) + \frac{e^x}{z} && \text{derivative of $\ln(z)$ with respect to $z$} 
\end{align*}
```
````