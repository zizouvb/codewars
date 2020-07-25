def max_sequence(arr):
    if len(arr)==0:
        return 0
    sub_sum = [arr[0]]
    for i in range(1,len(arr)):
        sub_sum.append(max(sub_sum[i-1]+arr[i],arr[i],0))
    return max(sub_sum)   
