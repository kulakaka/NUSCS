
dd ={'a': 'm', 'b': 'a', 'c': 'c', 'd': 'y', 'e': 't', 'f': 'v', 'g': 'o', 'h':
'u', 'i': 'x', 'j': 'e', 'k': 'j', 'l': 'w', 'm': 'f', 'n': 'z', 'o': 'd', 'p':
'l', 'q': 'i', 'r': 'k', 's': 'h', 't': 'n', 'u': 'g', 'v': 'b', 'w': 'q', 'x':
's', 'y': 'p', 'z': 'r'}


def decipher_message(msg,guide):
    re = ''
    for i in msg:
        if guide.get(i):
            re+=guide.get(i)
        else:
            re+=i
    return re

msg1e = "esbtr dgh abzqg! vhe ghz yzqtcjxx qx qt btgesjz cbxepj!"

#print(decipher_message(msg1e,d1))
d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.',
'2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E',
'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ',
'#': ' '}

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

                    


#print(find_treasure('decoded_map2.txt'))           
# key represent the child
# value represnet the ancestor
parent = {'Amy':'Ben', 'May':'Tom', 'Tom':'Ben',
 'Ben':'Howard', 'Howard':'George', 'Frank':'Amy',
 'Joe':'Bill', 'Bill':'Mary', 'Mary':'Philip', 'Simon':'Bill',
 'Zoe':'Mary'}
#name1 is ancestor
#name2 is child

def is_ancestor(name1,name2,pdict):
    count = 0
    while pdict.get(name2) != name1:
        name2 = pdict.get(name2)
        count+=1
        if count == len(pdict):
            return False
    return True

        
def is_related(name1,name2,pdict):
    if is_ancestor(name1,name2,pdict) or is_ancestor(name2,name1,pdict) or pdict.get(name1)==pdict.get(name2) or is_ancestor(pdict.get(name1),name2,parent) or is_ancestor(name1,pdict.get(name2),parent):
        return True
    else:
        return False
    
#print( is_ancestor('Amy', 'Tom', parent))
    

def count(n):
    cnt=0
    for i in range(n+1):
        print(i)
        # if i%2==0:
        #     if i%6==0:
        #         print(i)
        #         cnt+=1

    return cnt

li=[]
x=li+[5]
print(x)        