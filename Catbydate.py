import exifread
import os
import cv2
import pandas as pd

path="C:\\Users\\rishpand\\Desktop\\Backup\\jpgs1"
os.chdir(path)
files=os.listdir(".")
df=pd.DataFrame(columns=['name','Timestamp'])
index=0
total=len(files)

for cfile in files:
	f=open(cfile,"rb")
	tags=exifread.process_file(f)
	try:
		row=[cfile,str(tags['EXIF DateTimeOriginal'])]
	except KeyError,e:
		row=[cfile,'NA']
	df.loc[index]=row
	index=index+1
	src=path+"\\"+cfile
	dest=path+"\\"+row[1].split(" ")[0].replace(":","-")+"\\"+cfile
	f.close()
	try:
		os.rename(src,dest)
	except:
		os.mkdir(path+"\\"+row[1].split(" ")[0].replace(":","-"))
		os.rename(src,dest)
	print index
	#print(cfile,tags['EXIF DateTimeOriginal'])



imagePath="DSC03570.JPG"
cascPath="haarcascade_frontalface_default.xml"
faceCascade=cv2.CascadeClassifier(cascPath)

image=cv2.imread(imagePath)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 


faces=faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags=cv2.CASCADE_SCALE_IMAGE)  // ERROR   OOM   originally cv2.CV_CASCADE_SCALE_IMAGE
