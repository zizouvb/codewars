def rot13(message):
    ans = ""
    for l in message:
        if l<="m" and l>="a":
            ans+=chr(ord(l)+13)
        elif l>"m" and l<="z":
            ans+=chr(ord(l)-13)
        elif l<="M" and l>="A":
            ans+=chr(ord(l)+13)
        elif l>"M" and l<="Z":
            ans+=chr(ord(l)-13)
        else:
            ans+=l   
    return ans
