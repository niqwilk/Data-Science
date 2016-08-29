from numpy import *
import numpy as np  
import matplotlib.pyplot as plt 


#Code adapted from Linear Regression example by MATT NEDRICH and adjusted for overflow

Year = [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
Bronx = [1781, 1755, 2267, 2782, 3023, 5346, 8032, 23593, 37393, 51980, 88908, 200507, 430980, 732016, 1265258, 1394711, 1451277, 1424815, 1471701, 1168972, 1203789, 1332650, 1385108]
Total = [49447, 79215, 119734, 152056, 242278, 391114, 696115, 1174779, 1478103, 1911698, 2507414, 3437202, 4766883, 5620048, 6930446, 7454995, 7891957, 7781984, 7894862, 7071639, 7322564, 8008278, 8175133]
Bronx1 = [i/10000 for i in Bronx]
Total1 = [i/10000 for i in Total]
yolo = zip(Total,Bronx)
print yolo
# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]/10000
        y = points[i, 1]/10000
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]/10000
        y = points[i, 1]/10000
        b_gradient += -(2/N) * float((y - ((m_current * x) + b_current)))
        m_gradient += -(2/N) * x * float((y - ((m_current * x) + b_current)))
    new_b = b_current - float((learningRate * b_gradient))
    new_m = m_current - float((learningRate * m_gradient))
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)
    colors = np.random.rand(20)
    plt.scatter(Bronx1, Total1, alpha=0.5)
    plt.axis([-20,160,-20,900])
    plt.title("Bronx Pop. Plotted Against NYC Pop. 1790 - 2010")
    plt.xlabel("Bronx Population in Ten Thousands")
    plt.ylabel("Total NYC Pop. in Ten Thousands")
    plt.show()

def run():
    points = genfromtxt("data7hw.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    num_iterations = 10000
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))
    print "Running..."
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points))
    print points
    graph(' (5.32198645218*x+62.0605224532)*1',np.arange(-20,160,1))
    
    
          
if __name__ == '__main__':
    run()
