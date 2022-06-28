from array import *
x = array('i', [1, 2, 3, 4, 5, 6])
print(x)
print(len(x))

def accessElement(arr,index):
    if index >= len(arr):
        print("There is not any element in this index")
    else:
        print(arr[index])
accessElement(x,6)
accessElement(x,2)