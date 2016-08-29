
##x = range(1,1001)
##y1 = []
##for i in x:
##    y = math.log(i)
##    y1.append(y)
##y2 = []
##for i in x:
##    y = math.sqrt(i)
##    y2.append(y)
##plt.plot(x,y1,label='y1 = log(x)')
##plt.plot(x,y2,label='y2 = sqrt(x)')
##plt.legend()
##plt.show()

##years = [2003,2004,2005,2006,2007,2008,2009,2010,2011]
##ny = [5399,5100,5565,4460,4165,5741,4134,2385,3118]
##nj = [2887,2698,3363,2432,3134,3214,4598,3320,3398]
##ct = [1403,1348,1810,1788,3058,2738,2751,1964,2004]
##
##plt.scatter(years, nj)
##plt.show()
import math
import matplotlib.pyplot as plt
import numpy as np

infile = open('statesSummary.csv','r')

yearLine = infile.readline()
yearWords = yearLine.split(",")
years = []
for w in yearWords[1:]:
     years.append(int(w))

for i in range(5):
     line = infile.readline()
     words = line.split(",")
     stateName = words[0]
     stateValues = []
     for w in words[1:]:
          stateValues.append(int(w))
     color = np.random.rand(3,1)   
     plt.scatter(years, stateValues,c=color, label=stateName)

plt.title("Cases of Lyme Disease") 
plt.xlabel('Years')                
plt.ylabel('Number of Cases')      
plt.legend(loc = 2,
           fontsize = 'x-small')
plt.show()
