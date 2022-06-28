import numpy as np
myarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(myarray)
def rotatematrix(matrix):

    n=len(matrix)
    for layer in range(n//2):
        #print(layer)
        first=layer
        last=n-layer-1
        for i in range(first,last):
            #print(i)
            #save top element
            top = matrix[layer][i]
            # move left to top
            matrix[layer][i] = matrix[-i-1][layer]
            #move bottom to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            #move right to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer-1]
            #move top to right
            matrix[i][-layer - 1]=top
    return matrix
print('Matrix after Rotation: ')
print(rotatematrix(myarray))
