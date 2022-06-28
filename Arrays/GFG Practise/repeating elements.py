from collections import Counter
def duplicate(arr):
    frq = Counter(arr)  #frq will be a dictionary here
    for i in frq:
        if frq[i] > 1:
            print(i, end=' ')


a = [2, 10, 2, 10, 10]
n = len(a)
duplicate(a)
