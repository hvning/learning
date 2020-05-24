import cv2
import numpy as np
import matplotlib.pyplot as plt
dir = './data/pei.png'


def affineTrans(dir = dir):
    img = cv2.imread(dir)
    H = np.float32([[0, 1, 0], [-1, 0, 100]])
    # print(H)
    # H = [[1,0.1,100],
    #      [0.1,1,100]]
    # H = np.array(H,dtype= float)
    # rows, cols = img.shape[:2]
    # res = cv2.warpAffine(img, H, (cols*2, rows*2))  # 需要图像、变换矩阵、变换后的大小

    rows, cols = img.shape[:2]
    H = np.float32([[0, 1, 0], [-1, 0, cols]])
    # 第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

    res = cv2.warpAffine(img, H, (rows, cols))

    cv2.imshow('raw',img)
    cv2.imshow('tran',res)
    cv2.waitKey(0)
# 在对图像矩阵进行变换时，变换矩阵在齐次坐标下是3X3矩阵，但最后一行基本是固定的，为[0,0,1]，因此在CV2中设置变换矩阵时M直接为2X3
#对图像进行平移
def bias(dir):
    M = np.float32([[1,0,10],
                    [0,1,10]])
    img = cv2.imread(dir)
    h,w = img.shape[:2]
    print(h,w)
    res = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('origin',img)
    cv2.imshow('bias',res)
    cv2.waitKey(0)

def rotation(dir):

    img = cv2.imread(dir)
    h, w = img.shape[:2]
    print(h, w)
    M = np.float32([[0.707, -0.707, w//2],
                    [0.707, 0.707, 0]])
    res = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('origin', img)
    cv2.imshow('rotation', res)
    cv2.waitKey(0)
def scale(dir):
    img = cv2.imread(dir)
    h, w = img.shape[:2]

    M = np.float32([[0.5, 0, 0],
                    [0,0.5, 0]])
    res = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('origin', img)
    cv2.imshow('scale', res)
    cv2.waitKey(0)

#在进行投影变换时，自由度为8，因此要对变换矩阵第三行进行设置，该变换可以用于使拍摄倾斜或变型的文件扫描件摆正
def perspective(dir):
    img = cv2.imread(dir)
    h, w = img.shape[:2]
    pts1 = np.float32([[1, 1], [100, 0], [0, 200], [200, 100]])
    pts2 = np.float32([[1, 1], [100, 0], [0, 200], [200, 240]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    print(M) #其中M是3X3的矩阵，矩阵参数也可以自行计算好之后设置
    res = cv2.warpPerspective(img, M, (w, h))
    cv2.imshow('origin', img)
    cv2.imshow('perspective', res)
    cv2.waitKey(0)

if __name__== '__main__':
    perspective(dir)

