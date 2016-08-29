from __future__ import division
from collections import Counter
from linear_algebra import sum_of_squares, dot
import math
import matplotlib.pyplot as plt


#Nicholas Wilk Homework 4
#Code adapted from Joel Grus 

#NYC historical data:

Year = [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]

Manhattan = [33131, 60515, 96373, 123706, 202589, 312710, 515547, 813669, 942292, 1164673, 1441216, 1850093, 2331542, 2284103, 1867312, 1889924, 1960101, 1698281, 1539233, 1428285, 1487536, 1537195, 1585873]
Brooklyn = [4549, 5740, 8303, 11187, 20535, 47613, 138882, 279122, 419921, 599495, 838547, 1166582, 1634351, 2018356, 2560401, 2698285, 2738175, 2627319, 2602012, 2230936, 2300664, 2465326, 2504700] 
Queens = [6159, 6642, 7444, 8246, 9049, 14480, 18593, 32903, 45468, 56559, 87050, 152999, 284041, 469042, 1079129, 1297634, 1550849, 1809578, 1986473, 1891325, 1951598, 2229379, 2230722]
Bronx = [1781, 1755, 2267, 2782, 3023, 5346, 8032, 23593, 37393, 51980, 88908, 200507, 430980, 732016, 1265258, 1394711, 1451277, 1424815, 1471701, 1168972, 1203789, 1332650, 1385108]
Staten = [3827, 4563, 5347, 6135, 7082, 10965, 15061, 25492, 33029, 38991, 51693, 67021, 85969, 116531, 158346, 174441, 191555, 221991, 295443, 352121, 378977, 443728, 468730]
Total = [49447, 79215, 119734, 152056, 242278, 391114, 696115, 1174779, 1478103, 1911698, 2507414, 3437202, 4766883, 5620048, 6930446, 7454995, 7891957, 7781984, 7894862, 7071639, 7322564, 8008278, 8175133]

def mean(x): 
    return sum(x) / len(x)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
    
def standard_deviation(x):
    return math.sqrt(variance(x))

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero

def main():
    x = correlation(Bronx,Total)
    print "Correlation between Bronx and Total population: ", x
    y = correlation(Manhattan,Total)
    print "Correlation between Manhattan and Total population: ", y
    z = correlation(Queens,Total)
    print "Correlation between Queens and Total population: ", z
    q = correlation(Staten,Total)
    print "Correlation between Staten Island and Total population: ", q
    p = correlation(Brooklyn,Total)
    print "Correlation between Brooklyn and Total population: ", p

    plt.plot(Year, Brooklyn, color='b', label="NYC Population in Brooklyn", linewidth=2)
    plt.plot(Year, Total, color='r', label="NYC Total Population", linewidth=2)
    plt.legend(loc='upper left',prop={'size':13})
    plt.title("Changes in NYC Population from 1790 - 2010", y=1.02)       #Title for plot
    plt.xlabel('Years', fontsize=16).set_color("white")                     #Label for x-axis
    plt.ylabel('Total Population', fontsize=16).set_color("white")                   #Label for the y-axis
 #  plt.axis([1780,2020,0,150000])
    

    plt.show()
    
    
    
 


main()
    
