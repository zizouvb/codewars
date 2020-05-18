def binary_array_to_number(arr):
  ans=0
  for i,value in enumerate(arr[::-1]):
      ans+=value*2**i
  return ans
      
