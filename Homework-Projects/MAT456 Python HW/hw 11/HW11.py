import numpy as np
from mpl_toolkits.basemap import Basemap
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import csv

def main():
    
    lati = coordGrab('Latitude')
    longi = coordGrab('Longitude')
    '''
    map = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-74.359150, llcrnrlat=40.530479,
    urcrnrlon=-73.585905,  urcrnrlat=40.983567)'''
    
    points = zip(lati,longi)
    
    vor = Voronoi(points)
    voronoi_plot_2d(vor)
    
    '''
    x,y = map(longi, lati)
    map.plot(x, y, 'bo', markersize=7, alpha=.7)
  
    map.drawcoastlines()
    map.drawcountries()
    map.drawcounties()
    map.fillcontinents(color = 'red')
    map.drawmapboundary() '''
    plt.title("Location of CUNY campuses in NY")
    
 
    plt.show()

def coordGrab(specific):
    f = open("City_University_of_New_York__CUNY__University_Campus_Locations_Map.csv")
    reader = csv.DictReader(f)
    coord = [float(row[specific]) for row in reader]
    f.close()
    print coord
    return coord

main()
