mylist=[1,2,3,4,5]
orig=mylist[:]
mylist.sort()
print(mylist)
mylist=mylist + [69]
print(mylist)
mylist.append(10)
print(mylist)
print(orig)