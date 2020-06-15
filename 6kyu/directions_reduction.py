def dirReduc(arr):
    i=0
    while i<len(arr)-1:
        if (arr[i]=="NORTH" and arr[i+1]=="SOUTH"):
            del arr[i-1:i+1]
            i=0
        elif arr[i]=="SOUTH" and arr[i+1]=="NORTH":
            del arr[i-1:i+1]
            i=0
        elif arr[i]=="WEST" and arr[i+1]=="EAST":
            del arr[i-1:i+1]
            i=0
        elif arr[i]=="EAST" and arr[i+1]=="WEST":
            del arr[i-1:i+1]
            i=0
        else:    
            i+=1
    return arr
