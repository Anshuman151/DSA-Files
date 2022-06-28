def findpairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:       # for distinct pairs
                continue
            elif nums[i]+nums[j]==target:
                print(i,j)
            else:
                print('Not found !')

myl=list(map(int,input('Enter the list: ').split()))
findpairs(myl,10)