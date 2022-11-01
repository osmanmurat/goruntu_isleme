import numpy as np
import cv2

y_boyut=500
x_boyut=500
foto = cv2.resize(cv2.imread("kkk.jpg",0),(x_boyut,y_boyut))

# cv2.imshow("foto",foto)
# cv2.waitKey()

ters_foto = np.zeros([x_boyut,y_boyut],dtype=np.uint8)

for i in range (x_boyut):
    for k in range (y_boyut):
        ters_foto[i,k] = 255 - foto[i,k]

cv2.imshow("foto",ters_foto)
cv2.waitKey()
