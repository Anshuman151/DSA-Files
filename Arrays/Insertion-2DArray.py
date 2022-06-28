import numpy as np
twoDArray=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
print("----------------------")
newtwoDArray=np.insert(twoDArray,0,[[1,2,3,4]],axis=1)   #axis=1 for column and axis=0 for row
print(newtwoDArray)
print("----------------------")
newtwoDArray1 =np.insert(twoDArray,1,[[9,8,7,6]],axis=0)
print(newtwoDArray1)

