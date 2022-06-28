mylist=[2,4,3,5,6,-2,4,7,8,9]
def pairSum(myList, sum):
    a=[]
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i] + myList[j] == sum:
                a.append(str(myList[i])+'+'+str(myList[j]))
    return a
print(pairSum(mylist,7))