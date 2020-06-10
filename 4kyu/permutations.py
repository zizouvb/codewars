from collections import Counter
def permutations(string):
    cnt = Counter(string)
    ans = []
    current_perm = [0 for i in range(len(string))]
    
    def helper(cnt,current_perm,depth):
        if (depth == len(current_perm)):
            ans.append("".join(current_perm))
        for key,value in cnt.items():
            if value==0:
                continue
            current_perm[depth]=key
            cnt[key]-=1
            helper(cnt, current_perm, depth+1)
            cnt[key]+=1
    helper(cnt, current_perm, 0)
    return ans
