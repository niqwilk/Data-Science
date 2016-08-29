#Nicholas Wilk Homework 2 part 7,8

import matplotlib.pyplot as plt
import urllib2
import numpy as np

def main():

    Year = [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]

    Manhattan = [33131, 60515, 96373, 123706, 202589, 312710, 515547, 813669, 942292, 1164673, 1441216, 1850093, 2331542, 2284103, 1867312, 1889924, 1960101, 1698281, 1539233, 1428285, 1487536, 1537195, 1585873]
    Brooklyn = [4549, 5740, 8303, 11187, 20535, 47613, 138882, 279122, 419921, 599495, 838547, 1166582, 1634351, 2018356, 2560401, 2698285, 2738175, 2627319, 2602012, 2230936, 2300664, 2465326, 2504700] 
    Queens = [6159, 6642, 7444, 8246, 9049, 14480, 18593, 32903, 45468, 56559, 87050, 152999, 284041, 469042, 1079129, 1297634, 1550849, 1809578, 1986473, 1891325, 1951598, 2229379, 2230722]
    Bronx = [1781, 1755, 2267, 2782, 3023, 5346, 8032, 23593, 37393, 51980, 88908, 200507, 430980, 732016, 1265258, 1394711, 1451277, 1424815, 1471701, 1168972, 1203789, 1332650, 1385108]
    Staten = [3827, 4563, 5347, 6135, 7082, 10965, 15061, 25492, 33029, 38991, 51693, 67021, 85969, 116531, 158346, 174441, 191555, 221991, 295443, 352121, 378977, 443728, 468730]
    Total = [49447, 79215, 119734, 152056, 242278, 391114, 696115, 1174779, 1478103, 1911698, 2507414, 3437202, 4766883, 5620048, 6930446, 7454995, 7891957, 7781984, 7894862, 7071639, 7322564, 8008278, 8175133]

    ManPerc = [(float(Manhattan[i])/Total[i])*100 for i in range(0,23)]
    BroPerc = [(float(Brooklyn[i])/Total[i])*100 for i in range(0,23)]
    QueensPerc = [(float(Queens[i])/Total[i])*100 for i in range(0,23)]
    BronxPerc = [(float(Bronx[i])/Total[i])*100 for i in range(0,23)]
    StatPerc = [(float(Staten[i])/Total[i])*100 for i in range(0,23)]

    plt.plot(Year, ManPerc, color='r', label="% NYC Population in Manhattan", linewidth=2)
    plt.plot(Year, BroPerc, color='b', label="% NYC Population in Brooklyn", linewidth=2)
    plt.plot(Year, QueensPerc, color='g', label="% NYC Population in Queens", linewidth=2)
    plt.plot(Year, BronxPerc, color='m', label="% NYC Population in Bronx", linewidth=2)
    plt.plot(Year, StatPerc, color='y', label="% NYC Population in Staten Island", linewidth=2)

    plt.legend(loc='upper right',prop={'size':13})
    plt.title("Changes in NYC Population Distribution by Borough", y=1.02)       #Title for plot
    plt.xlabel('Years', fontsize=16).set_color("white")                     #Label for x-axis
    plt.ylabel('% of Total NYC Population in each Borough', fontsize=16).set_color("white")                   #Label for the y-axis
    plt.axis([1780,2020,0,100])
    plt.locator_params(axis = 'x', nbins = 15)
    plt.locator_params(axis = 'y', nbins = 25)

    plt.show()


    

main()
