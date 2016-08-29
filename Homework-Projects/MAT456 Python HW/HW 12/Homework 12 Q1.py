import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
from sklearn import manifold
import matplotlib.cbook as cbook
import scipy
from scipy.misc import imread
from scipy import ndimage

#MDS Conversion adapted from Noel O'Blog

def main():
    landmarks = ['American Museum of Natural History',
    'Brooklyn Bridge',
    'Central Park', 
    'Guggenheim Museum',
    'High Line',
    'Rockefeller Center',
    'September 11 Memorial',
    'Statue of Liberty',
    'Times Square',
    'Mystery']
    
    dist = distanceMatrix()
 

    adist = np.array(dist)
    amax = np.amax(dist)
    adist /= amax

    mds = manifold.MDS(n_components=2, dissimilarity="precomputed", random_state=6)
    results = mds.fit(dist)

    coords = results.embedding_
    print coords
    print coords[:,1][0]
    for x in range (len(coords[:,1])):
        coords[:,1][x] = coords[:,1][x]*-1
    #Can comment this out to run without background NYC MAP
    datafile = cbook.get_sample_data('/Users/niqson/5map.png')
    img = imread(datafile)
    plt.scatter(
    coords[:, 0], coords[:, 1], marker = 'o',s=25,color='cyan'
    )
    
    plt.annotate('Museum of Nat. History', coords[0])
    plt.annotate('Brooklyn Bridge', coords[1])
    plt.annotate('Central Park', coords[2],xytext = (-20, 20),textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.2', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    plt.annotate('Guggenheim Museum', coords[3],xytext = (20, 10),textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.2', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    plt.annotate('High Line', coords[4],xytext = (-20, 20),textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.2', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    plt.annotate('Rockefeller Center', coords[5])
    plt.annotate('9/11 Memorial', coords[6])
    plt.annotate('Statue of Liberty', coords[7])
    plt.annotate('Times Square', coords[8],xytext = (-20, 20),textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.2', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    plt.annotate('Mystery', coords[9],size = 20)
    rotated_img = scipy.ndimage.rotate(img, -10)
    plt.imshow(rotated_img, zorder=0, extent=[-32000, 30000, -30000, 19000])
    plt.show()
    
    '''
    themap = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-74.2919219, llcrnrlat=40.4729623,
    urcrnrlon=-73.585905,  urcrnrlat=40.983567)
    themap.drawcounties()
    themap.drawcoastlines()
    themap.drawmapboundary(fill_color='royalblue')
    themap.fillcontinents(color='coral',lake_color='aqua')

    

    plt.show()
    '''
def distanceMatrix():
    f = open('landmarkDistances.txt','r')
    distancemap = [map(float,line.split(' ')) for line in f]
    f.close()
    return distancemap


    
main()
