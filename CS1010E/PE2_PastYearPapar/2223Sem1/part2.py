

def readmap_n(filename):
    f = open(filename)
    m = []
    for line in f:
        m.append(line.rstrip('\n'))
    return m
def crop_map(filename,minr,maxr,minc,maxc):
    newmap= []
    map = readmap_n(filename)
    afterrowmap = map[minr:maxr]
    for i in afterrowmap:
       newmap.append(i[minc:maxc])
    return newmap
       
def readmap(filename):
    f = open(filename)
    m = []
    for line in f:
        m.append(list(line.rstrip('\n')))
    return m

def island_area(filename,prince):
    stack=[]
    visited=[]
    area = 0
    map = readmap(filename)
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y]==prince:
                r=x
                c=y 
    stack.append([r,c])
    area = DFS_island(map,[r,c],stack,visited)
    return len(area)
def DFS_island(map,startpoint,stack,visited):
    
    r,c = startpoint
    if not stack:
        return visited

    if [r,c] not in visited and map[r+1][c] =='.':
        stack.append([r+1,c])
    if [r,c] not in visited and map[r-1][c]=='.':
        stack.append([r-1,c])
    if [r,c] not in visited and map[r][c+1]=='.':
        stack.append([r,c+1])
    if [r,c] not in visited and map[r][c-1]=='.':
        stack.append([r,c-1])
    
    if[r,c] not in visited:
        visited.append([r,c])
    
    return DFS_island(map,stack[0],stack[1:],visited)
    

def prince_map(filename,prince):
    stack=[]
    visited=[]
    area = 0
    map = readmap(filename)
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y]==prince:
                r=x
                c=y 
    stack.append([r,c])
    area = DFS_island(map,[r,c],stack,visited)
    row=[]
    col=[]
    for i in area:
        row.append(i[0])
        col.append(i[1])
    
    return crop_map(filename,min(row),max(row)+1,min(col),max(col)+1)

#print(prince_map('map1.txt','A'))

