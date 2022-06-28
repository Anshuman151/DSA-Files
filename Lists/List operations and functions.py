a = [1, 2, 3]
b = [4, 5, 6]
c = a+b
print(c)
d=[3]
e=d*4
print(e)
print(len(a))
print(max(b))
print(min(b))
print(sum(c))
average=sum(c)/len(c)
print(average)

mylist=list()
while(True):
    inp=input('Enter a number : ')
    if inp=='done': break
    value = float(inp)
    mylist.append(value)
average = sum(mylist)/len(mylist)
print('Average:',average)
