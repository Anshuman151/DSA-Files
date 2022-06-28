#find missing no.s between integer array between 1 to n
mylist=[1,2,3,4,5,7,8,9,10]
def findmissing(list,n):
     sum1=n*(n+1)/2
     sum2=sum(list)
     return sum1-sum2
print(findmissing(mylist,10))