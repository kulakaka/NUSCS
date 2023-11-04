d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.',
'2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E',
'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ',
'#': ' '}

def decipher_message(msg,guide):
    dm = '' #decoded message
    length = len(msg)
    for i in range (length):
        if msg[i]==' ':
           dm = dm+' '
        else:
            dm = dm + str(guide.get(msg[i]))
    return dm

def decode_map(mapfile,ddict,outfile):
    with open(mapfile,'r') as mf:
        with open(outfile,'w') as df: 
            for e_line in mf:
                df.write(decipher_message(e_line,ddict)+'\n')

def find_treasure(mapfile):
    t_list = []
    with open(mapfile,'r') as f:
        for line in f:
            t_list.append(line)
        for i in range (1,len(t_list)-1):
            for j in range(1,len(t_list[i])-1):
                if t_list[i][j] == 'T':
                    if (t_list[i-1][j]=='T'
                    and t_list[i][j-1]=='T'
                    and t_list[i][j+1]=='T'
                    and t_list[i+1][j]=='T'):
                        return (i,j)
                    
print(find_treasure('decoded_map.txt'))




decode_map('encoded_map.txt',d1,'decoded_map.txt')