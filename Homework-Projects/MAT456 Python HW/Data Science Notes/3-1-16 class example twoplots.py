#Katherine St. John
#Data Science, Spring 2016
#Simple example of two different plots with different scales


from random import random
import matplotlib.pyplot as plt
import math 

#import plotly.plotly as py
'''
#Create some random data to plot:
x = [i for i in range(1,32)]
y1 = [i + random() for i in range(1,32)]
y2 = [-i - random() for i in range(1,32)] 

#Set up a figure
fig = plt.figure()

#The first set of data plotted is blue:
ax1 = fig.add_subplot(111)
ax1.plot(x,y1,'b-')
ax1.set_ylabel("Density", color="b")
for tl in ax1.get_yticklabels():
    tl.set_color('b')

#The second set of data plotted is red:
ax2 = ax1.twinx()
ax2.plot(x,y2, 'ro')
ax2.set_ylabel("Other", color="r")
for tl in ax2.get_yticklabels():
    tl.set_color('r')

#Add in a title and show:
plt.title('Two different plots with different scales')
plt.show()
'''

fig = plt.figure()

y1 = [math.log(i) for i in range (1,30)]
x1 = [i for i in range (1,30)]

y2 = [math.exp(x) for x in range (1,30)]

y3 = [math.sqrt(x) for x in range (1,30)]
y4 = [x**2 for x in range (1,30)]

ax1 = fig.add_subplot(221)
ax1.plot(x1,y1,'b-')

ax2 = ax1.twinx()
ax2.plot(x1,y2, 'r-')
ax2.set_ylabel("Other", color="r")
for tl in ax2.get_yticklabels():
    tl.set_color('r')

ax3 = fig.add_subplot(223)
ax3.plot(x1,y3,'g-')

ax4 = fig.add_subplot(224)
ax4.plot(x1,y4,'y-')
plt.show()

