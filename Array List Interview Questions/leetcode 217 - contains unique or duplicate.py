
myl=[1,2,3,4,5,2,3,5,6,3,2,1,9,7,8,9]
def isunique(li):
    a=list()
    for i in li:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True
print(isunique(myl))
