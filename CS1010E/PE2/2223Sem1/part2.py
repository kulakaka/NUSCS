
def prince_map(filename,prince):
 pass


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
    area = 1
    map = readmap(filename)
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y]==prince:
                r=x
                c=y 

    DFS_island(map,[r,c],stack,visited)

def DFS_island(map,startpoint,stack,visited):
    r,c = startpoint
   
    if [r,c] not in stack and map[r+1][c] =='.':
        stack.append([r+1,c])
        #area+=1
    if [r,c] not in stack and map[r-1][c]=='.':
        stack.append([r-1,c])
        #area+=1
    if [r,c] not in stack and map[r][c+1]=='.':
        stack.append([r,c+1])
        #area+=1
    if [r,c] not in stack and map[r-1][c-1]=='.':
        stack.append([r,c-1])
        #area+=1
    
    visited.append([r,c])

    
    return   DFS_island(map,[i[0],i[1]],stack,visited)



    return len(visited)

print(island_area("map1.txt","B"))

