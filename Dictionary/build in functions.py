mydict={'one':'uno','two':'dos','three':'tres','four':'cuarto'}
print('one' in mydict)
print('uno' in mydict.values())
for key in mydict:
    print(key)
print('-------------')
for key in mydict:
    print(mydict[key])
print('-------------')
#all method
mydi={1:True,2:True}
print(all(mydi))
mydi={0:False,1:False}
print(all(mydi))
mydi={0:False,1:False,2:True}
print(all(mydi))
mydi={0:True,1:True,2:False}
print(all(mydi))
mydi={}
print(all(mydi))
print('-------------')
#any method
mydi={1:True,2:True}
print(any(mydi))
mydi={0:False,1:False}
print(any(mydi))
mydi={0:False,1:False,2:True}
print(any(mydi))
mydi={0:True,1:True,2:False}
print(any(mydi))
mydi={}
print(any(mydi))
print('-------------')
#len method
print(len(mydict))
print('-------------')
#sort method
mydict={'e':1,'a':2,'u':3,'o':4,'i':5}
print(sorted(mydict))
print(sorted(mydict,reverse=True))
mydict={'ew1a':1,'ass':2,'ueoddd':3,'sseo':4,'werwi':5}
print(sorted(mydict,key=len))