import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv

def main():
    
    lati = coordGrab('LATITUDE')
    longi = coordGrab('LONGITUDE')
    
    map = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-74.363096, llcrnrlat=40.490535,
    urcrnrlon=-73.585905,  urcrnrlat=40.983567)
 
    x,y = map(longi, lati)
    map.plot(x, y, 'bo', markersize=7, alpha=.7)
  
    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color = 'red')
    map.drawmapboundary()
    plt.title("Accident Locations in the 5 Boroughs, Nov. 7th 2015")
 
    plt.show()

def coordGrab(specific):
    f = open("NYPD_Motor_Vehicle_Collisions.csv")
    reader = csv.DictReader(f)
    coord = [float(row[specific]) for row in reader if len(row[specific]) > 1]
    f.close()
    print coord
    return coord

main()
