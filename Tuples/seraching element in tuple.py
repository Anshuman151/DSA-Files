newtuple=('a','b','c','d','e')
print('b' in newtuple)


# def search(tup,target):
#     if target in tup:
#         return tup.index(target)
#     else:
#         return 'element doesnot exist in tuple'
# print(search(newtuple,'c'))


def search(tup,target):
    for i in tup:              #O(n)
        if i == target:
            return tup.index(i)    #O(1)
    return 'element doesnot exist in tuple'  #O(1)

print(search(newtuple,'d'))