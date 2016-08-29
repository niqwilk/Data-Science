#Nicholas Wilk Homework 2 part 5/6

#Katherine St. John, Summer 2015
#Uses multiple files from weather underground to graph
#    historical max temperatures.
#Adapted by Nihcolas Wilk for Homework 2

import matplotlib.pyplot as plt
import urllib2
import re
import numpy as np

def getDepthFromWeb(url):
    page = urllib2.urlopen(url)
    lines = page.readlines()
    for i in range(len(lines)):
        if lines[i].find("Snow Depth") >= 0:
            m = i
            break
    searchObj = re.search('\d+', lines[m+2])
    if(searchObj is None):
        return 0
    else:
        return int(searchObj.group(0))

def main():
     #The url is made up of the prefix, day, and suffix:
     prefix = "http://www.wunderground.com/history/airport/KLGA/2016/1/"
     suffix = "/DailyHistory"
     days = []
     depths = []
     mins = [36,34,36,15,13,26,32,34,41,42,28,26,24,24,34,42,31,20,18,30,27,22,25,24,30,35,34,29,32,30,37] #min temps for January 2016
     for day in range(1,32): #For each day
          days.append(day)       #Add the day to the list
          url = prefix+str(day)+suffix      #Make the url
          M = getDepthFromWeb(url)     #Call the function to extract Snow Depth
          
          depths.append(M) #Add the temp to the list
          print day, M 
 #    depths = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,27,20,15,9,6,4,3,2]  DATA USED FOR DEBUGGING
     depthScale = [(8)*((n*(n*.09))+1) for n in depths]
     plt.scatter(days, mins, s = depthScale, color = 'r', alpha=0.5)
     plt.title("Minimum Temps in January with Snow Depths as Point Size", y=1.02)       #Title for plot
     plt.xlabel('Days', fontsize=16).set_color("white")                     #Label for x-axis
     plt.ylabel('Minimum Temperature of the Day', fontsize=16).set_color("white")                   #Label for the y-axis
     plt.axis([0,32,10,50])
     plt.locator_params(axis = 'x', nbins = 16)
     plt.locator_params(axis = 'y', nbins = 20)
     l1 = plt.scatter([],[], s=8, edgecolors='none', color = 'r')
     labels = [" = 0 in. or Trace Amounts of Snow"]
     leg = plt.legend([l1], labels, ncol=4, frameon=True, fontsize=12,
     handlelength=1, loc = 'upper left', borderpad = .5,
     handletextpad=1, title='Size of Points Corresponds to Snow Depth', scatterpoints = 1)
     plt.show()
main()
