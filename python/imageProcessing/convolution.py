import matplotlib.pyplot as plt
import pylab
import numpy as np

dir = './data/python.png'

if __name__ == '__main__':
    img = plt.imread(dir)
    r,g,b = np.split(img,axis=0)
    print(r,g,b)
    plt.imshow(img)  # 显示读取的图片
    plt.show()