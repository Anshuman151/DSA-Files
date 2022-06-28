def fibonacci(n):
    assert n>=0 and int(n)==n ,"the no. must be  positive"
    if n in [0,1]:
        return n
    elif n<0:
        return("The no. is invalid , try another no.")
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))