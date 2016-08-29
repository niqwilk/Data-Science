import matplotlib.pyplot as plt
import urllib2
import numpy as np


Total = [49447, 79215, 119734, 152056, 242278, 391114, 696115, 1174779, 1478103, 1911698, 2507414, 3437202, 4766883, 5620048, 6930446, 7454995, 7891957, 7781984, 7894862, 7071639, 7322564, 8008278, 8175133]
Year = [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
Manhattan = [33131, 60515, 96373, 123706, 202589, 312710, 515547, 813669, 942292, 1164673, 1441216, 1850093, 2331542, 2284103, 1867312, 1889924, 1960101, 1698281, 1539233, 1428285, 1487536, 1537195, 1585873]
ManPerc = [(float(Manhattan[i])/Total[i])*100 for i in range(0,23)]
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(Year, ManPerc, 'r')
ax2 = ax1.twinx()
ax2.plot(Year,Total, 'b')
ax2.set_ylabel("Other", color="b")
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.show()
