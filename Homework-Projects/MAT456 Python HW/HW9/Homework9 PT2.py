import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv
import shapefile


from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import matplotlib.patches as mpatches




def main():
    

    
    
    map = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-74.2919219, llcrnrlat=40.4729623,
    urcrnrlon=-73.585905,  urcrnrlat=40.983567)


    

    sf = shapefile.Reader('geo_export_96de41b5-636a-40a1-bfe4-6b8ee3fbf259')
    fields = sf.fields
    print fields
       
        
    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color = 'white')
    map.drawmapboundary()
    map.readshapefile('geo_export_3d24c064-cd28-4c46-990a-7990102b9ddd', 'shape1')
    map.readshapefile('geo_export_96de41b5-636a-40a1-bfe4-6b8ee3fbf259', 'shape2')
    map.readshapefile('geo_export_b905aa40-9a2c-4648-9a2f-c96ba35e76df', 'shape3')
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111)


    
    for shapedict,shape in zip(map.shape1_info, map.shape1):
            xx,yy = zip(*shape)
            boro = shapedict['boro']
            
            if boro == 1.:
                poly = Polygon(shape,facecolor='r',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=1, color='k')
            elif boro == 2.:
                poly = Polygon(shape,facecolor='y',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=1, color='k')
            elif boro == 3.:
                poly = Polygon(shape,facecolor='g',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=1, color='k')
            elif boro == 4.:
                poly = Polygon(shape,facecolor='m',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=1, color='k')
            elif boro == 5.:
                poly = Polygon(shape,facecolor='c',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=1, color='k')

    for shapedict,shape in zip(map.shape2_info, map.shape2):
            xx,yy = zip(*shape)
            boro = shapedict['boro']
            if int(boro) == 1:
                poly1 = Polygon(shape,facecolor='r',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=.3, color='k')
            elif int(boro) == 2:
                poly1 = Polygon(shape,facecolor='y',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=.3, color='k')
            elif int(boro) == 3:
                poly1 = Polygon(shape,facecolor='g',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=.3, color='k')
            elif int(boro) == 4:
                poly1 = Polygon(shape,facecolor='m',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=.3, color='k')
            elif int(boro) == 5:
                poly1 = Polygon(shape,facecolor='c',edgecolor='k',alpha=.7)
                ax.add_patch(poly)
                map.plot(xx,yy,linewidth=.3, color='k') 

    for shapedict,shape in zip(map.shape3_info, map.shape3):
            xx,yy = zip(*shape)
            boro = shapedict['boro']
            
            if boro == 'BK':
                map.plot(xx,yy,linewidth=.3, color='k') 
                
            elif boro == 'BX':
                map.plot(xx,yy,linewidth=.3, color='k') 
                
            elif boro == 'MN':
                map.plot(xx,yy,linewidth=.3, color='k') 
                
            elif boro == 'QN':
                map.plot(xx,yy,linewidth=.3, color='k') 
                
            elif boro == 'SI':
                map.plot(xx,yy,linewidth=.3, color='k') 
                
    r_patch = mpatches.Patch(color='r', label='Manhattan')
    y_patch = mpatches.Patch(color='y', label='Bronx')
    m_patch = mpatches.Patch(color='m', label='Queens')
    g_patch = mpatches.Patch(color='g', label='Brooklyn')
    c_patch = mpatches.Patch(color='c', label='Staten Island')
    plt.legend(handles=[r_patch,y_patch,g_patch,m_patch,c_patch],loc='upper left')   
    plt.title("Color Coded School Districts by Borough in NYC", y=1.02)
    plt.show()
        




main()
