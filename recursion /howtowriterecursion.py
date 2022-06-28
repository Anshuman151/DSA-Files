def factorial(n):
    assert n>=0 and int(n)==n, "The Number must be an integer"
    if n in[0,1]:
     return 1
    else:
     return n*factorial(n-1)
print(factorial(5))
#print(factorial(-3))                 #  this will show assertion error given in line 2
