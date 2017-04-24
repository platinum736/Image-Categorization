import os
import numpy
import cv2
import PIL
from PIL import Image

# This would load all the face images and transform it to smaller images
src_dir="C:\\Users\\rishpand\\Desktop\\Backup\\jpgs1\\2009-04-16\\faces"
os.chdir(src_dir)

images=os.listdir(".")

for image in images:
    img=Image.open(image)
    img=img.resize((256,256),PIL.Image.ANTIALIAS)
    img.save("resized\\"+image)

    
