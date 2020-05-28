pattern = {"a" : "1",
"e" : "2",
"i" : "3",
"o" : "4",
"u" : "5",
"1":"a",
"2":"e",
"3":"i",
"4":"o",
"5":"u"}
def encode_chr(c):
    if c in pattern:
        return pattern[c]
    return c
def decode_chr(c):
    if c.isdigit():
        return pattern[c]
    return c
def encode(st):
    return "".join(map(encode_chr,st))
    
def decode(st):
    return "".join(map(decode_chr,st))
