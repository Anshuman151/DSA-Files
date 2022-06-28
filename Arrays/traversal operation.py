from array import *
arr1 = array('i',[1,2,3,4,5,6,7,8,9]) # i is used to represent integer
arr2 =  array('d',[1.3,2,3.1,4.0]) # d is used to represent double


def TraverseArray(array):
    for i in array:                   # Time complexity= O(n)---> O(1)
        print(i,end=' ')
TraverseArray(arr1)
