
def find_even_index(arr):
    sum_left = 0 
    sum_right = sum(arr)
    even_index = -1
    for i,num in enumerate(arr):
        if sum_left==sum_right-num:
            return i
        sum_left = sum_left+num
        sum_right = sum_right-num  
    return -1
      
