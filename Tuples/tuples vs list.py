#Mutable
list1 =[0,1,2,3,4,5,6,7]
print(list1)
list1[1]=9
print(list1)
del list1[1]
print(list1)

tuple1=0,1,2,3,4,5,6,7
#tuple1[1]=9                      returns an error
print(tuple1)
tuple1=7,8,9,0
print(tuple1)
#del tuple1[0]                   return an error
# print(tuple1)
#del tuple1               # return error
# print(tuple1)

#tuple can be stored inn list and list acan be stored in tuples
list1=[(1,2),(9,0),(3,4)]
print(list1)
tuple1=([1,2],[9,0],[3,4])
print(tuple1)
tuple1=((1,2),(9,0),(3,4))


