import cv2
import cv2IP
import numpy as np
ip = cv2IP.BaseIP


# imgtest = cv2.imread('Imgs\Gojo.png')
# cv2.imshow('mywindows' ,imgtest)
# cv2.waitKey(0)
# imgtest = ip.ImRead('Imgs\Gojo.png')
# ip.ImWindows('mywindows')
# ip.ImShow('mywindows',imgtest)
# cv2.waitKey(0)
# ip.ImWrtie('Imgs/new gojo.png',imgtest)
##########

import cv2
import numpy as np

img = cv2.imread("Imgs\Gojo.png", cv2.IMREAD_UNCHANGED)

print(img.shape)

b_channel, g_channel, r_channel,alpha_channel = cv2.split(img)

alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255

mask = (np.multiply(alpha_channel, 1.0 / 255))[:, :, np.newaxis] 
# 最小值爲0
# alpha_channel[:, :int(alpha_channel.shape[0] / 3)] = 100

img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))

cv2.imwrite("E:\master\Vision-Sensing\Imgs\OUTPUT.png", alpha_channel)