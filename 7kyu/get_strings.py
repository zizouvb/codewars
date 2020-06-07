def get_strings(city):
    counter = {}
    for c in city.replace(" ","").lower():
        if c in counter:
            counter[c]+="*"
        else:
            counter[c]="*"
    ans=[]
    for key,value in counter.items():
        ans.append(key + ":" +value)
    return ",".join(ans)
