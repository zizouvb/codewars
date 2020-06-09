def pig_it(text):
    ans = []
    for word in text.split(" "):
        if len(word)>1 or word[0].isalpha():   
            ans.append(word[1:]+word[0]+"ay")
        else: ans.append(word)
    return " ".join(ans)
