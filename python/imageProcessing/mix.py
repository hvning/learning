
import numpy as np
import cv2
# Read images : obj image will be cloned into im
obj = cv2.imread("./data/car.jpg")
objMask = cv2.imread('./data/carMask.jpg')
backGround = cv2.imread('./data/plane.jpg')
H,W = obj.shape[:2]
obj = cv2.resize(obj,(W//2,H//2))
objMask = cv2.resize(objMask,(W//2,H//2))

mask = 255 * np.ones(obj.shape, obj.dtype)

# # The location of the center of the obj in the im
width, height, channels = backGround.shape

center = (int(height/2-10), int(height/2-10))

# Seamlessly clone obj into im and put the results in output
normal_clone = cv2.seamlessClone(obj, backGround, objMask, center, cv2.NORMAL_CLONE)
mixed_clone = cv2.seamlessClone(obj, backGround, objMask, center, cv2.MIXED_CLONE)

cv2.imshow('normal',normal_clone)
cv2.imshow('mixed',mixed_clone)
cv2.waitKey(0)

