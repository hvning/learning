from numpy import dot
import numpy as np

def guassEliminate(A,b):
    A_ = A.copy()
    b_ = b.copy()
    n = len(b)
    row = len(A_)
    column = len(A_[0])

    if n != row or n != column:
        print('the size of A is wrong')
        return None
    #step1: generate a Lower triangular matrix
    for i in range(0,n):
        for j in range(i+1,n):
            if A_[j][i] != 0:
                m = A_[j][i]/(A_[i][i]*1.0)
                A_[j] = A_[j] - m*A_[i]
                b_[j] = b_[j] - m * b_[i]
    #step2：calculate every x
    for i in range(1,n+1):
        index = n - i
        b_[index] = (b_[index]-dot(A_[index][index+1:n],b_[index+1:n]))/A_[index][index]

    return b_



if __name__ =="__main__":

    A = [[1.0,1.0,1],[0.0,4.0,-1.0],[2,-2,1]]
    b = [6,5,2.0]
    A = np.array(A)

    b = np.array(b)
    x = guassEliminate(A,b)
    print('function solution is ',x)

    bEvaluate = np.sum(A*x,axis=1)
    print('evaluate:',bEvaluate)
    print('expect:',b)