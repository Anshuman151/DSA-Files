#updating element
myDict={'name':'edy','age':26}
myDict['age']=27
print(myDict)     #T.C -> O(1)      S.C -> O(1)
#Adding new element
myDict['address']='London'
print(myDict)    #T.C -> O(1)      S.C -> amortized O(1)