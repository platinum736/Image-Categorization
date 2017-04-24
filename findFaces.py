import cv2
import numpy as np
import os

#This would find all faces from all the images in a directory and saved the croped face images
face_cascade = cv2.CascadeClassifier("C:\\Users\\rishpand\\Desktop\\Self Projects\\Image categorization\\haarcascade_frontalface_default.xml")
src_dir = "C:\\Users\\rishpand\\Desktop\\Backup\\jpgs1\\2009-04-16"
os.chdir(src_dir)
files=os.listdir(".")
#img = cv2.imread("C:\\Users\\rishpand\\Desktop\\Backup\\jpgs1\\2004-01-01\\1 (8138).jpg")
for src_img in files:
    img = cv2.imread(src_dir+"\\"+src_img)
#cv2.imshow('img',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    i=0
    for (x,y,w,h) in faces:
        #cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
        crop_image=img[y:y+h,x:x+w]    
        #cv2.imshow('crop',crop_image)
        #k = cv2.waitKey() & 0xff
        #if k==26:
        #   break
        name="faces\\"+src_img+"_"+str(i)+".jpg"
        cv2.imwrite(name,crop_image)
        i=i+1

