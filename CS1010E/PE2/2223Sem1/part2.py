
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
  
    map = readmap(filename)
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y]==prince:
                r=x
                c=y 


    return marked

def DFS_island(map,startpoint):
    r,c = startpoint
    stack=[]
    visited=[]
    if map[r+1,c] and [r-1,c] and [r,c+1] and [r,c-1]=='W':
        return 
    if map[r+1][c] =='.':
        stack.append([r+1,c])
    if map[r-1][c]=='.':
        stack.append([r-1,c])
    if map[r][c+1]=='.':
        stack.append([r,c+1])
    if map[r-1][c-1]=='.':
        stack.append([r,c-1])

    for i in stack:
        
   
print(island_area("map1.txt","B"))

