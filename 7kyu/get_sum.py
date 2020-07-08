def get_sum(a,b):
    if a==b:return a
    sign = int((b-a)/abs(b-a))
    return sum(range(a,b+sign,sign))
#https://www.codewars.com/kata/55f2b110f61eb01779000053/
