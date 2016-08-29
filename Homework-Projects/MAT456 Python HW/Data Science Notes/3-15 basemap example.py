import matplotlib.pyplot as plt 
import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

infile = open('statesSummary.csv','r')
reader = csv.reader(infile)
yearLine = reader.next()
years = [int(w) for w in yearLine[8:]]

stateNames = []
stateTotals = []
netIncrease = []

for row in reader:
     stateNames.append(row[0])
 #    stateTotals.append(int(row[-1]))
     netIncrease.append(int(row[9]) - int(row[8]))
 #    [int(r) for r in row[1:]])

maxCases = float(max(netIncrease))
scaledTotals = [i/maxCases for i in netIncrease]

map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
map.readshapefile('st99_d00', name='states', drawbounds=True)

ax = plt.gca() # get current axes instance

names = []
for shape_dict in map.states_info:
    names.append(shape_dict['NAME'])

for i in range(len(stateNames)):
    # print "Plotting", stateNames[i]
     seg = map.states[names.index(stateNames[i])]
     if((1.0-scaledTotals[i]) > 1.0):
         green = 1.0
     elif((1.0-scaledTotals[i] < 0)):
        green = 0.0
     else:
        green = 1.0-scaledTotals[i]
     c = (1.0,green,1.0)
     poly = Polygon(seg, facecolor=c,edgecolor='black')
     ax.add_patch(poly)
     
plt.show()
