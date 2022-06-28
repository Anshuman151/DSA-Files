from array import *
# 1.Creating an array and transverse
print("---Step 1---")
my_array = array('i',[1,2,3,4,5,6])
for i in my_array:
    print(i)
# 2.Accessing individual elements through indexes
print("---Step 2---")
print(my_array[3])
# 3.Append any value to the array using append() method
print("---Step 3---")
my_array.append(7)
print(my_array)
# 4.Insert value in array using insert() method
print("---Step 4---")
my_array.insert(0,8)
print(my_array)
# 5.Extend python array using extend() method
print("---Step 5---")
my_array1 = array('i',[11,12,13,14,15,16])
my_array.extend(my_array1)
print(my_array)
# 6.Add items from list into array using fromlist() method
print("---Step 6---")
templist = [20,21,22]
my_array.fromlist(templist)
print(my_array)
# 7. remove any array element using remove() method
print("---Step 7---")
my_array.remove(13)
print(my_array)
# 8. Remove any array  element using pop() method
print("---Step 8---")
my_array.pop()                                       #this function will delete the last element from the array
print(my_array)
# 9. Fetch any elemt through its index using index() method
print("---Step 9---")
print(my_array.index(21))
# 10. Reverse a python array using reverse() method
print("---Step 10---")
my_array.reverse()
print(my_array)
# 11. Get array buffer information through buffer_info() method
print("---Step 11---")
print(my_array.buffer_info())
# 12. Check for number of occurrences of an element using count() method
print("---Step 12---")
my_array.append(5)
print(my_array.count(5))
# 13. Convert array to string using tostring() method
print("---Step 13---")
strtemp = my_array.tostring()            # converting array into string
print(strtemp)
ints = array('i')                        #converting string into array
ints.fromstring(strtemp)                 #converting string into array
print(ints)
# 14. Convert array to a python list with same elements using tolist() method
print("---Step 14---")
print(my_array.tolist())
# 15. Append a string to char array using fromstring() method
 # Same as done in line 54 to line 56
# 16. Slice Elements from an array
print("---Step 16---")
print(my_array[10:14])