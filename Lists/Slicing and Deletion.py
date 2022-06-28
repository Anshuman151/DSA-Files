li=['a','b','c','d','e','f']
print(li[0:2])
print(li[0:])
li[0:2]=['x','y']
print(li)
#deletion
li.pop(1)       # O(1)/O(n)
print(li)
print(li.pop()) #pop function
del li[1]  # delete method
print(li)
li.remove('d')
print(li)
