import numpy as np
arr=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
def search(x,n):                       #Using linear Search
    for i in range(len(x)):           #O(mn)     m are the rows and n are the columns
        for j in range(len(x[0])):     #O(n)
            if n==x[i][j]:          # O(1)
                return "The value is located at index "+str(i)+","+str(j)
    return "Value not found"
print(search(arr,17))