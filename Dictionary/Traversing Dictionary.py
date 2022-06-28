myDict = {'name':'Edy','age':26,'adress':'London'}
def traversedict(dict):
    for key in dict:       #T.C -> O(n)
        print(key,dict[key])  #S.C -> O(1)
traversedict(myDict)