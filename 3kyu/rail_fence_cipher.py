def get_next_line(current_line_dir, nb_rails):
    if (current_line_dir[0]<nb_rails-1 and current_line_dir[1]==1) or (current_line_dir[0]>0 and current_line_dir[1]==-1):
        return [current_line_dir[0]+current_line_dir[1],current_line_dir[1]]
    return [current_line_dir[0]-current_line_dir[1],current_line_dir[1]*-1]
    
def encode_rail_fence_cipher(string, n):
    line_dir=[0,1] 
    my_dict= {}
    for i in range(n):
        my_dict[i]=[]
    for i in range(len(string)):
        my_dict[line_dir[0]].append(string[i])
        line_dir=get_next_line(line_dir, n)
    ans=""
    for key,value in my_dict.items():
        ans+="".join(value)
    return ans  
        
def decode_rail_fence_cipher(string, n):
    w = len(string)
    queue = string
    my_array = [["@" for x in range(w)] for y in range(n)]
    for j in range(n):
        line_dir=[0,1]
        for i in range(w):
            if line_dir[0]==j and i>=j and len(queue)>0:
                my_array[line_dir[0]][i] = queue[0]
                queue = queue[1:]
            line_dir=get_next_line(line_dir, n)
    ans=""
    for i in range(w):
        for j in range(n):
            if my_array[j][i]!="@":
                ans+=  my_array[j][i]
    return ans
            
