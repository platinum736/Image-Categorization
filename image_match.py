import os
import numpy as np
import cv2
import pandas

#based on paper jcn by Matthew Turk and Alex Pentland 'Eigenfaces for Recognition'

#steps:
#1. Acquire an initial set of face images(training set)
#2. Calculate the eigenfaces from the training set,
#   keeping only the M imges that corespond to the highest eigne values
#3.


os.chdir("C:\\Users\\rishpand\\Desktop\\Backup\\jpgs1\\2009-04-16\\faces\\resized")
src_images=os.listdir(".")
images=[]
avg_image=np.zeros(shape=(256,256),dtype='u1')
M=len(src_images)
for image in src_images:
    #calculate average of all the images
    img=cv2.imread(image)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    images.append(gray)
    avg_image=avg_image+gray

avg_image=avg_image
print avg_image
cv2.imwrite("average Image.jpg",avg_image)
#cv2.waitKey()
#cv2.destroyAllWindows()

    
    
