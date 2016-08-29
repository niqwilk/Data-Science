#3D plot of gradient descent puzzle (class work)
#Data Science, Lehman College, Spring 2016

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #3D plotting
from matplotlib import cm               #Color maps
import numpy as np

#Create a figure:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Set up the X, Y, and Z arrays:
X = np.arange(-10., 10., 0.1)
Y = np.arange(-10., 10., 0.1)
X, Y = np.meshgrid(X, Y)
#There are two minima for this surface:
#    Change the ranges and grid size to see more detail:
Z = (X**2 - 1)**2 + (X**2*Y - X - 1)**2

#Create and show the surface:
surf = ax.plot_surface(X, Y, Z,cmap=cm.BuPu)
fig.show()


def grad(x,y):
    x = (4*x(x**2-1)) + ((4*x*y-2)(y*x**2-x-1))
    y = ((2*x**2)(y*x**2-x-1))
    return (x,y)

def next(prev, stepSize, grFn):
    grx, gry = grFn(prev[0],prev[1])
    nex = prev[0] - stepSize*grx
    ney = prev[1] - stepSize*gry
    return nex, ney
