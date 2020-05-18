import math
def is_prime(num):
  if (num<=1): return False
  for i in range(2,math.ceil(math.sqrt(num))+1):
      if (num%i)==0 and num!=i:
          return False
  return True
  
