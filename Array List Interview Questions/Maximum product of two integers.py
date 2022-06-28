import numpy as np
arr=np.array([1,2,3,4,5,6,10,11,31,23,4,59])
def maxproarr(array):
    maxproduct = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j]>maxproduct:
                maxproduct=array[i]*array[j]
                pairs=str(array[i])+','+str(array[j])
    print(pairs)
    print(maxproduct)
maxproarr(arr)