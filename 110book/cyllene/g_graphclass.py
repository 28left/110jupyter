import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
import numpy as np
import cyllene.f_functionclass as f_funct
import sympy as sp



''' 
A lot of problems need to be resolved:
	1)Can we keep a record of the graphs graphed? this can be done by just keeping the numpy arrays ? 
	2)we need to be able to deal with poles of functions ( for example 1/x at x = 0, 1/(x^2-1) at x = -1, 1 ...etc)


''' 
class graph():

	def __init__(self):
		self.fig = plt.figure(1)
		self.ax = SubplotZero(self.fig,111)
		self.fig.add_subplot(self.ax)

		for direction in ["xzero","yzero"]:
			self.ax.axis[direction].set_axisline_style("-|>")
			self.ax.axis[direction].set_visible(True)

		for direction in ["left","right","bottom","top"]:
			self.ax.axis[direction].set_visible(False)

		

	def make_graph(self, f):
		I = f.behaviour("largest interval")

		ps = float(I.args[0])
		pe = float(I.args[1])
		t = np.arange(ps, pe, 0.01)

		self.ax.plot(t, f.eval_np(t))


	def make_graphs(self, *functions,Interval=None):
		if(Interval == None):
			f = functions[0]
			I = f.behaviour("largest interval")
			l,r = float(I.args[0]), float(I.args[1]) 
			for f in functions:
				I = f.behaviour("largest interval")
				l,r = min(l,float(I.args[0])), max(r,float(I.args[1]))
		else:
			l,r = float(Interval.args[0]), float(Interval.args[1]) 

		self.Interval = sp.Interval(l,r)
		
		

		t = np.arange(l,r,.01)

		for f in functions:
			self.ax.plot(t,f.eval_np(t))



	def make_secent(self,f,x1,x2):
		I = f.behaviour("largest interval")

		ps = float(I.args[0])
		pe = float(I.args[1])
		t = np.arange(ps, pe, 0.01)

		sec = f.secent_line(x1,x2)
		self.ax.plot(t, sec.eval_np(t))
		self.plot_point(x1, sec.eval_np(x1))
		self.plot_point(x2,sec.eval_np(x2))



	def make_tangent(self,f,x):
		I = f.behaviour("largest interval")
		ps = float(I.args[0])
		pe = float(I.args[1])
		t = np.arange(ps, pe, 0.01)

		tan = f.tangent_line(x)
		self.ax.plot(t, tan.eval_np(t))
		self.plot_point(x, tan.eval_np(x))



	def plot_point(self, x, y):
		self.ax.plot(np.array([x]), np.array([y]), 'ro')


	def zoom_y(self, f, I):
		self.zoom_x(I)
		self.zoom_y(f.range(I))

	def zoom_x(self,I):
		ps = float(I.args[0])
		pe = float(I.args[1])

		self.ax.set_xlim(ps,pe)

	def zoom_y(self,I):
		ps = float(I.args[0])
		pe = float(I.args[1])

		self.ax.set_ylim(ps,pe)
	def show(self):
		return self.fig