import numpy as np
from mpl_toolkits.basemap import Basemap
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import csv
from bokeh.plotting import figure, show, output_file, vplot
import datetime as dt
import pandas as pd
import seaborn as sns
import plotly.plotly as py
import plotly.graph_objs as go
from bokeh.io import output_file, show
from bokeh.charts import Bar
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, BoxZoomTool, PanTool, ResizeTool, HoverTool, WheelZoomTool, BoxSelectTool
)



def main():
    
    dates = DataExtract('Date','Tesla Sales')
    sales = DataExtract('Sales','Tesla Sales')
    coords = DataExtract('GPS','Supercharger')
    stalls = DataExtract('Stalls','Supercharger')
    chargerNames = DataExtract('Supercharger','Supercharger')
    opendates = DateGrab()
    color = ColorGrab()
    status = DataExtract('Status', 'Supercharger')
    stateList = DataExtract('State','Supercharger')
    lats, lons = coordGrab(coords)
    sales_tot = np.cumsum(sales)
    x = [dt.datetime.strptime(d,'%m-%d-%Y').date() for d in dates]

    print sum(sales)
    print sum(stalls)
 
    stateCount = {}
    for state in stateList:
            stateCount[state] = stateCount.get(state,0)+1
    print stateCount


    
                                    


    sns.set() 


    date_format = "%Y-%m-%d"
    starter = '2012-11-19'
    loop = 0
    a = dt.datetime.strptime(starter, date_format)
    dayslength = []
    while loop < 264:
        b = dt.datetime.strptime(opendates[loop], date_format)
        dayspend = int((b-a).days)
        dayslength.append(dayspend)
        loop+=1
    dayslength.sort()
    print dayslength

    daydiff = [0]
    test = 0
    while test < 263:
        z = (dayslength[test+1]-dayslength[test])+2
        daydiff.append(z)
        test+=1
    print daydiff
    p = range(1,265)

    

    sortstates = [(k,v) for v,k in sorted(
      [(v,k) for k,v in stateCount.items()],reverse=True
       )
    ]
    
    orderstates = [i[0] for i in sortstates]
    ordernums = [int(i[1]) for i in sortstates]
    statedata = {'State': orderstates,
            'Number of Supercharging Stations': ordernums}

    dff = pd.DataFrame(statedata, columns=['State', 'Number of Supercharging Stations'])
    barchar = sns.barplot(x="State", y='Number of Supercharging Stations', data=dff)
    barchar.set(ylabel='Number of Superchargring Stations', xlabel='State')
    sns.plt.title('United States Supercharger Distribution')
    sns.plt.show()        
        

    data = {'Supercharger Number': p,
            'Days Since First Charger Opened': dayslength}
    df = pd.DataFrame(data,columns = ['Days Since First Charger Opened','Supercharger Number'])
    print df
    g = sns.jointplot(x='Days Since First Charger Opened', y='Supercharger Number', kind="reg",xlim=(-10, 1500), ylim=(-10,500), data=df)
    sns.plt.title('Tesla Supercharger Network Growth')
    sns.plt.show()
            
        


    

##    ax = plt.subplot(111)
##    ax.plot(sales)
##    ax.bar(x, sales, width=10)
##    ax.xaxis_date()
##
##    plt.show()

    p2 = figure(x_axis_type = "datetime") #x_axis_type = "datetime"
    p2.title = "Tesla Car Sales"
    p2.grid.grid_line_alpha=0.3
    p2.xaxis.axis_label = 'Date'
    p2.yaxis.axis_label = 'Sales Numbers'
    p2.line(x, sales_tot, color='#A6CEE3', legend='Tesla Sales',line_width=2)
    window_size = 30
    window = np.ones(window_size)/float(window_size)
    p2.legend.orientation = "top_left"
    output_file("Final Project Test.html", title='Tesla Sales Graph')
    show(p2)

    date_format = "%m/%d/%Y"
    
    
    
    


    map_options = GMapOptions(lat=39.503542,lng=-97.114248, map_type="roadmap", zoom=long(3.99),
    )

    


    plot = GMapPlot(
        x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="Tesla Supercharger Network"
    )
    source = ColumnDataSource(
    data=dict(
        lat=lats,
        lon=lons,
        loc = chargerNames,
        fill = color,
        stat = status,
        dates = opendates
        )
    )

    hover = HoverTool(
        tooltips=[
            ("Location", "@loc"),
            ("Status", "@stat"),
            ("Open Date", "@dates"),
            
            
        ]
    )
    
    circle = Circle(x="lon", y="lat", size=5, fill_color="fill", fill_alpha=0.8, line_color=None)
    plot.add_glyph(source, circle)
    plot.add_tools(PanTool(), hover, WheelZoomTool(), BoxSelectTool(), BoxZoomTool(), ResizeTool())
    output_file("gmap_plot.html")
    show(plot)


 
    




   


    


def datetime(x):
    return np.array(x, dtype=np.datetime64)

def DataExtract(data,filename):
    f = open(filename+'.csv')
    reader = csv.DictReader(f)
    
    thedata = [float(row[data]) if row[data].isdigit() else row[data] for row in reader]
    f.close()
    #print thedata
    return thedata

def coordGrab(array):
    x=0
    lats = []
    lons = []
    while x < len(array):
        lat, lon = array[x].split(',')
        lats.append(lat.strip())
        lons.append(lon.strip())
        x+=1

    return lats, lons

def ColorGrab():
    f = open('Supercharger.csv')
    reader = csv.DictReader(f)
    
    thecolor = ['green' if row['Status'] == 'Open' else 'orange' if row['Status'] == 'Construction' else 'blue' for row in reader]
    f.close()
    #print thedata
    return thecolor

def DateGrab():
    f = open('Supercharger.csv')
    reader = csv.DictReader(f)
    
    opendates = ['Pending' if row['Open Date'] is '' else row['Open Date'] for row in reader]
    f.close()
    #print thedata
    return opendates

        
    

main()
