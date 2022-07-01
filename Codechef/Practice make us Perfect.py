(p1,p2,p3,p4)=map(int,input().split())
sum=0
for i in (p1,p2,p3,p4):
    if i >= 10 :
        sum+=1
    elif i < 10:
        sum+=0
print(sum)