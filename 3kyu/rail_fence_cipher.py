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
