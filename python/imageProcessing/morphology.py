import numpy as np
import cv2
from pylab import *



def erodeOperation(dir = dir):
    img = cv2.imread(dir)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))

    erodeImg = cv2.erode(img, element)
    recoverImg = cv2.dilate(erodeImg, element)

    diffOriginAndErode = img - erodeImg
    diffOriginRecover = img - recoverImg

    fig = plt.figure()
    subplot(1, 2, 1)
    imshow(img)
    title('original image')
    #
    # subplot(1,5,2)
    # imshow(erodeImg)
    # title('erode image')
    #
    # subplot(1,5,3)
    # imshow(recoverImg)
    # title('recover image')
    #
    # subplot(1,5,4)
    # imshow(diffOriginAndErode)
    # title('diffOriginAndErode')

    subplot(1, 2, 2)
    imshow(diffOriginRecover)
    title('diffOriginRecover')
    show()

def closeOperation(dir= dir):
    img = cv2.imread(dir)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, element, iterations=1)
    diff = img - opening
    cv2.imshow('original image',img)
    cv2.imshow('closing image',opening)
    cv2.imshow('diff',diff)
    cv2.waitKey(0)
dir = './data/wirebond.tif'
if __name__ == '__main__':
    erodeOperation(dir)