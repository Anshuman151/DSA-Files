# Recursive
def poweroftwo(n):
    if n==0:
        return 1
    else:
        power=poweroftwo(n-1)
        return power*2
#iterative
def poweroftwoit(n):
    i=0
    power=1
    while i<n:
        power=power*2
        i =i+1
    return power
poweroftwo(5)

poweroftwoit(5)
