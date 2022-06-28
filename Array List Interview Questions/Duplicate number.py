def removeDuplicates(myList):
    new_list = []
    for i in myList:

        if i not in new_list:
            new_list.append(i)

    return new_list
myList=[1,2,3,3,21,1,2,7,7,7]
print(removeDuplicates(myList))