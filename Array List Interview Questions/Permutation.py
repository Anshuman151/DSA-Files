list1 = list(map(int,input()))
list2 = list(map(int,input()))

def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False
print(permutation(list1,list2))
