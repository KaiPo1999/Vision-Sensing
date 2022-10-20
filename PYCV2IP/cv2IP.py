import cv2
import numpy as np
import enum

class BaseIP:

    @staticmethod
    def ImRead(filename):
        return cv2.imread(filename ,cv2.IMREAD_UNCHANGED)
    
    @staticmethod
    def ImWrtie(filename,img):
       cv2.imwrite(filename ,img)

    @staticmethod
    def ImShow(winname,img):
        cv2.imshow(winname,img)
        
    @staticmethod
    def ImWindows(winname):
        cv2.namedWindow(winname ,cv2.WINDOW_NORMAL)



# class AlphaBlend(BaseIP):
#     @staticmethod
#     def SplitAlpha(SrcImg)
#         return

#     def DoBlending(Foreground, Background, Alpha)
#         return