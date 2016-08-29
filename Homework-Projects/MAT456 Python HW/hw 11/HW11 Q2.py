import matplotlib.pyplot as plt  
import numpy as np
import ast
import random
import math

#Adapted user coordinate input function from user 'Blender' on stackoverflow


def main():
    height = 400
    width = 400
    newImage = np.zeros((height,width,3))
    points  = get_coords()
    colorDic = {}
    
    
    for i in points:
        red = random.random()
        green = random.random()
        blue = random.random() 
        colorDic[i] = (red,green,blue)

    for i in range(height):
   
      for j in range(width):
            
                best = closestPoint(points,(i,j))
                newImage[i,j,0] = colorDic[best][0]
                newImage[i,j,1] = colorDic[best][1]
                newImage[i,j,2] = colorDic[best][2]
    plt.imshow(newImage)    #Open window to show image (close to continue)
    plt.title('Points Shaded Based on Proximity')
    plt.show()             
                

def closestPoint(pointList,candidate):
    best = math.sqrt((candidate[0] - pointList[0][0])**2 + (candidate[1] - pointList[0][1])**2)
    keeper = pointList[0]
    for i in pointList:
        distance = math.sqrt((candidate[0] - i[0])**2 + (candidate[1] - i[1])**2)
        if distance < best:
            best = distance
            keeper = i
    return keeper

def get_coords():
    print "Enter a list of points of (x,y) values between 0 and 400. For example (0,0), (20,150), (174,399)"
    points = raw_input()

    while True:
        try:
            return ast.literal_eval(points)
        except SyntaxError:
            print "Please enter the coordinates in the format mentioned"

main()
