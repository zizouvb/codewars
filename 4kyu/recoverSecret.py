def recoverSecret(triplets):
    next = {}
    for triplet in triplets:
        if triplet[0] in next:
            next[triplet[0]].add(triplet[1])
        else:
            next[triplet[0]]={triplet[1]}
        if triplet[1] in next:
            next[triplet[1]].add(triplet[2])            
        else:
            next[triplet[1]]={triplet[2]}
    ans=""
    while next:
        first_candidate=set()
        not_first_candidate=set()
        for l in next:
            if l not in not_first_candidate:
                first_candidate.add(l)
            for n in next[l]:
                not_first_candidate.add(n)
                if n in first_candidate:
                    first_candidate.remove(n)
        ans+=list(first_candidate)[0]
        if len(next)==1:
            for n,value in next.items():
                ans+=list(value)[0]
        del next[list(first_candidate)[0]]
    return ans
