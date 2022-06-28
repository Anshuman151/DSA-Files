#using linear search
myDict = {'name':'Edy','age':26,'adress':'London'}
def search(dict,value):
     for key in dict:    #T.C -> O(n)
         if dict[key] == value:  O(1)
             return key,value
     return 'The value does not exist'
print(search(myDict,26))
print(search(myDict,'an'))