def unique_in_order(iterable):
    if len(iterable)==0: return []
    ans = [iterable[0]]
    for i in range(1,len(iterable)):
        if iterable[i]!=iterable[i-1]:
            ans.append(iterable[i])
    return ans
