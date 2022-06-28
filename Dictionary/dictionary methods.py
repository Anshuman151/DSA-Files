mydict={'name':'edy','age':26,'adress':'london','education':'master'}
# Clear Method
# mydict.clear()
# print(mydict)

#copy method
a= mydict.copy()
print(a)

#fromkeys method
newdict={}.fromkeys([1,2,3],0)
print(newdict)
nd={}.fromkeys([1,2,3])
print(nd)

#get method
print(mydict.get('age',27))

#items method
print(mydict.items())

#keys method
print(mydict.keys())

#popitem method
mydict.popitem()
print(mydict)

#set default method
mydict.setdefault('name1','added')
print(mydict)

#pop  method
mydict={'name':'edy','age':26,'adress':'london','education':'master'}
print(mydict.pop('name1','not'))

#values method
print(mydict.values())

#update method
newdi={'a':1,'b':2,'c':3}
mydict.update(newdi)
print(mydict)
