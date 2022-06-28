ml=list()
n=int(input("Enter the no. of days: "))
for i in range(n):
    temp=int(input('Day '+str(i+1)+' temperature : '))
    ml.append(temp)
average=sum(ml)/len(ml)
print('Average temperature: '+str(average))
for j in range(len(ml)):
    if ml[j]>average:
        print("Day "+str(j+1)+" has above average temperature")
