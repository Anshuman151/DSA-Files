import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
def sumDiagonal(a):
    abc=0
    for layer in range(len(a)):
        #print(layer)
        abc+=a[layer][layer]
    return abc

print(sumDiagonal(arr))