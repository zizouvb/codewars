def spin_words(sentence):
    ans=[]
    for word in sentence.split(" "):    
        ans.append(word[::-1] if len(word)>=5 else word)
    return " ".join(ans)
