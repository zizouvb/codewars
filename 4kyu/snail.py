def snail(snail_map):
    size = len(snail_map)
    if size==0:
        return []
    elif size==1:
        return snail_map[0]
    snail_list = snail_map[0]
    sub_snail_map = []
    for y in range(1,size-1):
        snail_list.append(snail_map[y][size-1])
        sub_snail_map.append(snail_map[y][1:size-1])    
    snail_list.extend(snail_map[size-1][::-1])
    for y in range(size-2,0,-1):
        snail_list.append(snail_map[y][0])
    return snail_list + snail(sub_snail_map)
