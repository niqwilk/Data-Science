import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.mlab import PCA

#Plotting of PCA adapted from nextgenetics blog

def main():
    medianEarly = commaStrip('Median Wage Early Career')
    medianMid = commaStrip('Median Wage Mid-Career')
    shareGrad = commaStrip('Share with Graduate Degree')
    underEmploy = commaStrip('Underemployment Rate')
    unEmploy = commaStrip('Unemployment Rate')
    #print medianEarly,medianMid,shareGrad,underEmploy,unEmploy
    data = np.array([(medianEarly),(medianMid),(shareGrad),(underEmploy),(unEmploy)])
    dataTrans = data.T

    results = PCA(dataTrans) 
    x = []
    y = []
    z = []
    for item in results.Y:
        x.append(item[0])
        y.append(item[1])
        z.append(item[2])
    print x[19]

    plt.close('all') # close all latent plotting windows
    fig1 = plt.figure() # Make a plotting figure
    ax = Axes3D(fig1) # use the plotting figure to create a Axis3D object.
    pltData = [x,y,z]
    ax.scatter(pltData[0][19], pltData[1][19], pltData[2][19], c='r',s=40)
    ax.scatter(pltData[0][52], pltData[1][52], pltData[2][52], c='r',s=40)
    ax.scatter(pltData[0], pltData[1], pltData[2], c='c', alpha=.6)

    xAxisLine = ((min(pltData[0]), max(pltData[0])), (0, 0), (0,0)) # 2 points make the x-axis line at the data extrema along x-axis 
    ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r') # make a red line for the x-axis.
    yAxisLine = ((0, 0), (min(pltData[1]), max(pltData[1])), (0,0)) # 2 points make the y-axis line at the data extrema along y-axis
    ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r') # make a red line for the y-axis.
    zAxisLine = ((0, 0), (0,0), (min(pltData[2]), max(pltData[2]))) # 2 points make the z-axis line at the data extrema along z-axis
    ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'r') # make a red line for the z-axis.

    # label the axes 
 
    ax.set_title("PCA on Employment Data")
    plt.show() # show the plot
    
    

   

    x = np.vstack([unEmploy,underEmploy,shareGrad,medianEarly,medianMid])
    cov = np.cov(x)
    print cov

    

def commaStrip(name):
    f = open("WageData.csv",'r')
    reader = csv.DictReader(f)
    num = [float(row[name].replace(',','')) for row in reader if len(row[name]) != 0]
    
    f.close()
    #print num
    return num

main()

