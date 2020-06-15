import bisect
from collections import OrderedDict

def dbl_linear(n):
    if n==0:
        return 1
    a=[1]
    i=0
    while len(a) < 2*n:
        bisect.insort(a,2*a[i]+1)
        bisect.insort(a,3*a[i]+1)
        i+=1
    return list(OrderedDict.fromkeys(a))[n]
