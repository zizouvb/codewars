def disemvowel(string):
    ans = ''
    for c in string:
        if c.lower() not in 'aeiou':
            ans += c
    return ans
