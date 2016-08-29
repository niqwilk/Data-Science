
import matplotlib.pyplot as plt  
import numpy as np

img = plt.imread('Flood.png') #Read in image from bf1.png
img2 = plt.imread('Flood1.png') 
plt.imshow(img)     #Load image into matplotlib
plt.show()
height = img.shape[0]
width = img.shape[1]
newImage = np.zeros((height,width,3))
print img[1,1,2]





for i in range(height):
  #print "processing row", i 
  for j in range(width):
            if(img2[i,j,2] - img[i,j,2] > .20):
                newImage[i,j,0] = 1
              
            else:
                newImage[i,j,0] = img[i,j,0]
                newImage[i,j,1] = img[i,j,1]
                newImage[i,j,2] = img[i,j,2]
            
plt.imshow(newImage)    #Open window to show image (close to continue)
plt.show() 
plt.imsave('face2.png',newImage)
