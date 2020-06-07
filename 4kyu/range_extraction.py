def solution(args):
    n=0
    ans=[]
    while n<len(args):
        i=1
        while (i+n<len(args) and args[n+i]==args[n]+i):
            i+=1
        if i>2:
            ans.append(str(args[n]) + "-" + str(args[n]+i-1))
        else:
            ans.append(str(args[n]))
            if i==2:
                i=1
        n+=i
    return ",".join(ans)
