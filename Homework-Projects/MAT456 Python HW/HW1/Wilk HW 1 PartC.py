#Katherine St. John, Summer 2015
#Uses multiple files from weather underground to graph
#    historical max temperatures.

#Adapted by Nicholas Wilk for HW 1

#The libraries to plot, load webpages, and use regular expressions
import matplotlib.pyplot as plt
import urllib2
import re


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
      
     

     #Makea a histogram of the maximum temps:
     plt.hist(mins)
     plt.title("Minimum Daily NYC Temps in January 2016")
     plt.xlabel("Temperatures")
     plt.ylabel("Frequency")
     plt.show()

     

main()
