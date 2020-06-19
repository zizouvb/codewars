from collections import Counter
def mix(s1, s2):
    ans=[]
    s1_c = Counter(''.join(sorted(c for c in s1 if c.islower())))
    s2_c = Counter(''.join(sorted(c for c in s2 if c.islower())))
    s1_f = {x: count for x, count in s1_c.items() if count>1}
    s2_f = {x: count for x, count in s2_c.items() if count>1}
    for c in {**s1_f , **s2_f}:
        if s1_c[c]>s2_c[c]:
            ans.append("1:"+s1_c[c]*c)
        elif s1_c[c]<s2_c[c]:
            ans.append("2:"+s2_c[c]*c)
        else:
            ans.append("=:"+s2_c[c]*c)
    return "/".join(sorted(ans,key=lambda x: (-len(x),x)))
