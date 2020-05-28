'''
一些用于计算图片相关性的函数
'''
from sklearn import metrics as mr
import numpy as np
import cv2


'''
计算结果与sklearn自带函数结算结果一致，但运行时间较长
'''
def MI(x,y):
    sum = 0.0
    x_value_list = np.unique(x)
    y_value_list = np.unique(y)
    Px = np.array([len(x[x == xval]) / float(len(x)) for xval in x_value_list])  # P(x)
    Py = np.array([len(y[y == yval]) / float(len(y)) for yval in y_value_list])  # P(y)

    for i in range(len(x_value_list)):  #对排序好的X进行遍历
        yi = y[x==x_value_list[i]]
        yj = np.unique(yi)
        for j in yj:  #计算与xi对应位置的yj的每个值的概率
            Pxy = len(yi[yi==j])/float(len(yi))*Px[i]
            Pyj = Py[y_value_list==j]
            Pxi = Px[x_value_list == i]
            t = Pxy/Pxi/Pyj
            sum += Pxy*np.log(t)

    return sum


import time
img1 = cv2.imread('./data/woman1.jpg')
img2 = cv2.imread('./data/woman2.jpg')

img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))

img1 = np.reshape(img1, -1)
img2 = np.reshape(img2, -1)
print(img1.size,img2.size)
t1 = time.time()
print('MI is :',MI(img1,img2),'time',time.time()-t1)
t1 = time.time()
mutual_infor = mr.mutual_info_score(img1, img2)

print(mutual_infor,'time',time.time()-t1)

# img1 = [1,2,3,4,5,6,7]
# img2 = [1,2,0,0,0,0,0]
# img1 = np.array(img1)
# img2 = np.array(img2)
# MI(img1,img2)