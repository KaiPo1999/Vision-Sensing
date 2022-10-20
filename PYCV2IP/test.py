import cv2
import cv2IP
import numpy as np
ip = cv2IP.BaseIP


# imgtest = cv2.imread('Imgs\Gojo.png')
# cv2.imshow('mywindows' ,imgtest)
# cv2.waitKey(0)
imgtest = ip.ImRead('Imgs\Gojo.png')
ip.ImWindows('mywindows')
ip.ImShow('mywindows',imgtest)
cv2.waitKey(0)
ip.ImWrtie('Imgs/new gojo.png',imgtest)

