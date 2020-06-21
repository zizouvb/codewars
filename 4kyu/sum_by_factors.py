from functools import reduce
def compute_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return sorted(list(set(factors)))
def sum_for_list(lst):return list(map(lambda x:[x,sum(filter(lambda y:y%x==0,lst))],compute_prime_factors(reduce(lambda x, y: x * abs(y), lst, 1))))
