def get_free_neighbors(maze,node,N):
    y,x = node
    
    neighbors_list = []
    if x>0:
        if maze[y][x-1]==".":
            neighbors_list.append([y,x-1])
    if x<N-1:
        if maze[y][x+1]==".":
            neighbors_list.append([y,x+1])
    if y>0:
        if maze[y-1][x]==".":
            neighbors_list.append([y-1,x])
    if y<N-1:
        if maze[y+1][x]==".":
            neighbors_list.append([y+1,x])
    return neighbors_list
    
def path_finder(maze_str):
    maze=[list(line) for line in maze_str.split("\n")]
    N=len(maze)
    node = [N-1,N-1]
    queue = [node]
    while queue:
        node = queue.pop(0)
        y,x = node
        if x==0 and y==0:
            return True
        else:
            maze[y][x]="x"
        queue=get_free_neighbors(maze,node,N)+queue
