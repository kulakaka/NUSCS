
def create_map_file():
    pmap1list = ['0000011111',
    '0000X11111',
    '0000111111',
    '000X111111',
    '0001111111',
    '0222111111',
    '2222211111',
    '2222222111',
    '2222222211',
    '2222222222',
    '2222222222']
    pmap2list = ['000000X22222',
    '00000X222222',
    'XXXXX2222222',
    '111122222222',
    '111122222222',
    '111X22222222',
    '111222222222',
    '111222222222',
    '11X222222222',
    '112222222222']
    f1 = open("pmap1.txt","w")
    for line in pmap1list:
        f1.write(line+'\n')
    f1.close()
    f2 = open("pmap2.txt","w")
    for line in pmap2list:
        f2.write(line+'\n')
    f2.close()
create_map_file()

def buyable_map(filename):
    map=[]
    file= open(filename,'r')
    for i in file:
        for ite in i[:-2]:
            map.append([ite])
    
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] !='X':
            
                if row==0:
                    if col==0:
                        if map[row+1][col] or map[row+1][col+1] or map[row][col+1]  != map[row][col]:
                            map[row][col] == '.'
                    elif col == len(map[row]):
                        if map[row+1][col] or map[row+1][col-1] or map[row][col-1]  != map[row][col]:
                            map[row][col] == '.'
                    else:
                        if map[row+1][col] or map[row+1][col-1] or  map[row+1][col+1] or map[row][col-1]or map[row][col+1]  != map[row][col]:
                            map[row][col] == '.'
                elif row == len(map):
                    if col==0:
                        if map[row-1][col] or map[row-1][col+1] or map[row][col+1]  != map[row][col]:
                            map[row][col] == '.'
                    elif col == len(map[row]):
                        if map[row-1][col] or map[row-1][col-1] or map[row][col-1]  != map[row][col]:
                            map[row][col] == '.'
                    else:
                        if map[row][col-1] or map[row-1][col-1] or  map[row-1][col+1] or map[row-1][col] or  map[row][col+1] != map[row][col]:
                            map[row][col] == '.'
                
                elif row!=0 and row!=len(map) and col == 0:
                    if map[row][col+1] or map[row+1][col+1] or  map[row+1][col-1] or map[row-1][col-1] or  map[row][col-1] != map[row][col]:
                            map[row][col] == '.'
                elif row!=0 and row!=len(map) and col == len(map[row]):
                    if map[row][col-1] or map[row-1][col-1] or  map[row+1][col+1] or map[row-1][col] or  map[row+1][col] != map[row][col]:
                            map[row][col] == '.'

                else:
                    if map[row+1][col] or map[row+1][col-1] or  map[row+1][col+1] or map[row][col-1]or map[row][col+1] or map[row][col-1] or map[row-1][col-1] or  map[row-1][col+1] or map[row-1][col] or  map[row][col+1] != map[row][col]:
                        map[row][col] == '.'
                    
    return map

            


    
print(buyable_map('pmap1.txt'))