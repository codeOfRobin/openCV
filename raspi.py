import cv2
import csv
import sys
# sys.setdefaultencoding("utf8")
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('fabric4.png')

img = cv2.imread('fabric4.png',0)
height, width = img.shape[:2]
print height
print width
crop_img = img[height/4:height/4+height/2, width/4:width/4+width/2]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)

img=crop_img
img=cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

contours, hierarchy = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

idx =0 
centers=[]
defects=0
for cnt in contours:
	if cv2.contourArea(cnt)>15:
		(x,y),radius = cv2.minEnclosingCircle(cnt)
		center = (int(x),int(y))
		radius = int(radius)
		centers=centers+[center]
		cv2.circle(img,center,radius,(0,255,0),2)
		idx+=1
	if cv2.contourArea(cnt)>1000:
		defects+=1
# cv2.imshow('img',img)

rows=0
cols=0
# print(idx)

centers=np.array(centers)
print(centers.shape[0])

for i in range(centers.shape[0]):
	# print i
	if i<centers.size-2:	
		(x1,y1)=centers[i-1]
		(x2,y2)=centers[i]
	if y2-y1>8 or y2-y1<-8:
		rows+=1
	if x2-x1>120 or x2-x1<-120:
		cols+=1

print rows," rows"
print cols," cols"
print defects," defects"

plt.plot(centers,'ro-')
plt.show()

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(img,'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

with open('foobar.csv', 'a') as csvfile:
	spamwriter = csv.writer(csvfile, dialect='excel',quoting=csv.QUOTE_ALL, lineterminator='\n')
	spamwriter.writerow([rows,cols,defects])

