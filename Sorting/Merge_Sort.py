import math
A = [3,1,2,4,5]  #p=0,q=2,r=4
def merge(A,p,q,r):
    n1 = q-p+1   #2-0+1=3
    n2 = r-q    #2
#   let L[1..n1+1] and R[1...n2+1] be new array
    L,R = [],[]
    for i in range(n1):     # 0,1,2
        L.append(A[p+i])     #L0:A-1
    for j in range(n2):
        R.append(A[q+1+j])
    L.append('inf')
    R.append('inf')
    i,j=0,0
    for k in range(p,r+1):       #for putting sorted values back into A array 
        if L[i] == "inf":      # Left side is empty, take from Right
            A[k] = R[j]
            j += 1
        elif R[j] == "inf":    # Right side is empty, take from Left
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:      #condition for sorting
            A[k]=L[i]
            i+=1
        else:               #condition for sorting
            A[k]=R[j]
            j+=1      

def sort(A,p,r):
    if p<r:
        q=math.floor((p+r)/2)
        sort(A,p,q)
        sort(A,q+1,r)
        merge(A,p,q,r)
sort(A,0,4)
print(A)
