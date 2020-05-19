def move_zeros(array):
    zero_counter=0
    i=0
    while i < len(array)-1:
        if array[i] == 0 and array[i] is not False:
            del array[i]
            zero_counter +=1
            continue
        i+=1
    return array+[0]*zero_counter
