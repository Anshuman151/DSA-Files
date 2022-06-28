import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])

def search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i

print(search(arr,8))