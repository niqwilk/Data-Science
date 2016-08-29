#Katherine St. John, Summer 2015
#Uses multiple files from weather underground to graph
#    historical max temperatures.

#Adapted by Nicholas Wilk for HW 2

#The libraries to plot, load webpages, and use regular expressions
import matplotlib.pyplot as plt
import urllib2
import re
import numpy as np
from matplotlib.collections import LineCollection


#A function that takes the kind of temperature ("Max", "Min", "Ave") and
#a URL and returns the temperature from that line.
def getTempFromWeb(kind,url):
     page = urllib2.urlopen(url)
     lines = page.readlines()
     for i in range(len(lines)):
          if lines[i].find(kind+" Temperature") >= 0:
               m = i
               break
     searchObj = re.search('\d+', lines[m+2])
     return int(searchObj.group(0))


def main():
     #The url is made up of the prefix, day, and suffix:
     prefix = "http://www.wunderground.com/history/airport/KLGA/2016/1/"
     suffix = "/DailyHistory"
     days = []          #Sets up a list to store days
     mins = []           #Sets up a list so store min values
     for day in range(1,32): #For each day
          days.append(day)       #Add the day to the list
          url = prefix+str(day)+suffix      #Make the url
          M = getTempFromWeb("Min",url)     #Call the function to extract temp
          mins.append(M) #Add the temp to the list
          print day, M 
 ##    days = [i for i in range(1,32)]   Used for debugging programin
 ##    mins = [36,34,36,15,13,26,32,34,41,42,28,26,24,24,34,42,31,20,18,30,27,22,25,24,30,35,34,29,32,30,37]
     ave = float(sum(mins))/ len(mins)
     print ave
     print len(mins)
     

     
     scaled= [i*100/ave-100 for i in mins]
     
     
   
     plt.plot(days, scaled, color='r', label="Variation of Temp")       #Plot max as red
     plt.axhline(y=0,color='b')
     plt.legend(['% Difference From Avg'], loc='upper left',prop={'size':10})
     plt.title("Variation of January Min Temps from Average Min", y=1.02)       #Title for plot
     plt.xlabel('Days', fontsize=16).set_color("white")                     #Label for x-axis
     plt.ylabel('% Fluctuation from Average', fontsize=16).set_color("white")                   #Label for the y-axis
     plt.axis([0,32,-60,60])
     plt.locator_params(axis = 'x', nbins = 16)
     plt.locator_params(axis = 'y', nbins = 20)

     plt.show()
     

main()
