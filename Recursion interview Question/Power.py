#consider base be a and exponent as n
def power(a,n):
    assert n>=0 and n==int(n),"Base and Exponent should be positive integer !"
    if n==0:
        return 1
    elif n==1:
        return a
    else:
        return a*power(a,n-1)
print(power(-2.5,3))
