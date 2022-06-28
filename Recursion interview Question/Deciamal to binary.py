def dtb(n):
    assert n==int(n),"the value of n should be an integer "
    if n==0:
        return 0
    else:
        return n%2 + 10 *dtb(int(n/2))
print(dtb(13))