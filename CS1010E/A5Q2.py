def decode_map(mapfile,ddict,outfile):
    with open(mapfile,'r') as f:
        with open(outfile,'w') as f1:
            for line in f:
                out = decipher_message(line,ddict)
                f1.write(out)
                f1.close

#decode_map('encoded_map2.txt',d1,'decoded_map2.txt')

def find_treasure(mapfile):
    map=[]
    with open(mapfile,'r') as f:
        for line in f:
            row=[]
            for i in line:
                row.append(i)
            map.append(row)
    
    for i in range(1,len(map)-1):
        for x in range(1,len(map[i])-1):
            if map[i][x] =='T':
                if map[i][x-1]=='T' and map[i][x+1]=='T' and map[i-1][x] == 'T' and map[i+1][x]=='T':
                    return (i,x)

                    