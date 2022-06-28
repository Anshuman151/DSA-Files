import numpy as np
twoDArray=np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9], [1, 2, 3, 4]])
print(twoDArray)
def accessElements(array, rowIndex, colIndex):
    if rowIndex>=len(array) or colIndex>=len(array[0]):    #     O(1)
        print('Incorrect index')                   #O(1)
    else:
        print(array[rowIndex][colIndex])          #O(1)
accessElements(twoDArray,4,1)