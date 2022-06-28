#Accesing Elements in List
shoppingList=['Milk','Cheese','Butter']
print(shoppingList[1])
print('Milk' in shoppingList)
print('bread' in shoppingList)
print(shoppingList[-1])
#Traversing List
for i in shoppingList:
    print(i)
list=[0,1,2,3]
print(range(len(list)))
for j in range(len(list)):
    if j<=len(list):
       print(list[j])