import numpy as np
arr=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(arr)
newarr=np.delete(arr,0,axis=0)           #axis=0 for deleting row and axis=1 for deleting column
print(newarr)