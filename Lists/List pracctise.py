arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6):
    print(arr[i], end = " ")
a=[1,2,3,4,5,6,7,8,9]
print(a[::2])
a=[1,2,3,4,5]
print(a[3:0:-1])

def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())

def f(i, values = []):
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)


a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)

