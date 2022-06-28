#Method 1
mylist=[1,2,3,4]
def middle(lst):
    new=lst[1:]
    del new[-1]
    return new
print(middle(mylist))
#Method 2
# def middle(lst):
#     a=list()
#     for i in range(lst[1],lst[-1]):
#          a.append(i)
#     print(a)
# mylist=[1,2,3,4]
# middle(mylist)
#Method 3
# def middle(lst):
#     a=lst[1:-1]
#     print(a)
# middle(mylist)
#print(range(len(mylist)))