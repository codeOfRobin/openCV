import cv2
import numpy as np

img=cv2.imread("lena1.png",cv2.IMREAD_UNCHANGED)
b,g,r=cv2.split(img)

g=np.zeros(b.shape,np.uint8)
r=np.zeros(r.shape,np.uint8)
img=cv2.merge((b,g,r))
print (img.shape)
cv2.imshow('askdjfnkas',img)

cv2.waitKey(0)
cv2.destroyAllWindows()