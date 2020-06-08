from collections import Counter
def is_letter(c):
    return c.isalpha()
def string_letter_count(s):
    return "".join([str(occ)+c for c,occ in Counter(sorted(filter(is_letter,list(s.lower())))).items()])
