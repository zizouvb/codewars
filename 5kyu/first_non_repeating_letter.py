def first_non_repeating_letter(string):
    letters = {}
    for i,l in enumerate(string):
        if l.lower() not in letters:
            letters[l.lower()]=i
        else:
            letters[l.lower()]=-1
    for l in letters.keys():
        i=letters[l.lower()]
        if letters[l.lower()]>-1:
            return string[i]
    return ""
