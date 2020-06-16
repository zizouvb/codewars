def halving_sum(n): 
    ans=0
    while (n>0):
        ans+=n;
        n//=2
    return ans
