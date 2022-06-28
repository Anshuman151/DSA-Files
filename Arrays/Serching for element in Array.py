from array import *
x=array('i',[1,2,3,4,5,6,12,123,3434,83])

def Search(arr,value):
    for i in arr:
        if value == i:
            print(arr.index(value))                         # this function is used to give the index  of element in the array
    return "the element doesnot belong to this array"
Search(x,123)

#We can also try the following one

# from array import *
# x=array('i',[1,2,3,4,5,6])
#
# def Search(arr,element):
#     for index in range(len(arr)):
#          if element == arr[index]:
#             print("Element is stored in ",str(index)," index")
#     return "the element does not belongs to array"
# Search(x,4)
