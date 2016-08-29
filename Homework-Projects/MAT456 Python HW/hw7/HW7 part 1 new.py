from scipy import stats
from numpy import *
import numpy as np  
import matplotlib.pyplot as plt 

Year = [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
Bronx = [1781, 1755, 2267, 2782, 3023, 5346, 8032, 23593, 37393, 51980, 88908, 200507, 430980, 732016, 1265258, 1394711, 1451277, 1424815, 1471701, 1168972, 1203789, 1332650, 1385108]
Total = [49447, 79215, 119734, 152056, 242278, 391114, 696115, 1174779, 1478103, 1911698, 2507414, 3437202, 4766883, 5620048, 6930446, 7454995, 7891957, 7781984, 7894862, 7071639, 7322564, 8008278, 8175133]


slope, intercept, r_value, p_value, std_err = stats.linregress(Bronx,Total)

print slope
print intercept
 
def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    
    plt.plot(x, y)
    
    plt.scatter(Bronx, Total, alpha=0.5)
    plt.axis([-50000,1600000,-200000,9000000])
    plt.title("Bronx Population against Total NYC Population", y=1.02)
    plt.xlabel('# of People Living in the Bronx', fontsize=16).set_color("white")
    plt.ylabel('# of People Living in NYC', fontsize=16).set_color("white") 
    plt.show()

graph('5.05482025527*x+954969.958334',np.arange(-50000,1600000,10000))
