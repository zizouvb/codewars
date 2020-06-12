import math
def solve(a, b):
    primes = ["2"]
    for i in range(3,50000):
        for j in range(2, math.ceil(math.sqrt(i))+1):
            if not i % j:
                break
        else:
            primes.append(str(i))
    return "".join(primes)[a:a+b]
