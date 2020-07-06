#https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def capitalize(word):return word[0].upper() + word[1:]
def to_jaden_case(string):return " ".join(list(map(capitalize,string.split(" "))))
