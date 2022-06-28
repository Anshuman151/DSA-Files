#Updation in list
myl=[1,2,3,4,5,6,7]
print(myl)
myl[2]=10
print(myl)
# T.C -> O(1)
#S.C -> O(1)

#Insertion in list
num=[10,20,30,40,50]
num.insert(1,15)
print(num)
num.append(60)
print(num)
newlist=[8,16,24,32,48]
num.extend(newlist)
print(num)