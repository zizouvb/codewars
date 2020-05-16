from collections import defaultdict
def anagrams(word, words):
    available_letters = defaultdict(int)
    anagrams = []
    for letter in word:
        available_letters[letter]+=1
    for word_candidate in words:
        a_letters = available_letters.copy()
        if len(word_candidate)!=len(word):
            continue
        word_is_in = True
        for i,l in enumerate(word_candidate):
            if a_letters[l]<=0:
                word_is_in = False
                break
            a_letters[l]-=1     
        if word_is_in:
            anagrams.append(word_candidate)   
    
    return anagrams
