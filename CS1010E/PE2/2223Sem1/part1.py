aphs=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print(aphs.index('c'))

def encode_I(s1,s2,m):
    output=''
    mls = []
    ## for encode
    for i in s2:
        mls.append(int(i)*m)
    #print(mls)
    for i in range(len(s1)):
        ## find s1 index 
        ind = aphs.index(s1[i])
        tind = (ind+mls[i])%26
        output+=aphs[tind]
    return output



def encode_R(s1,s2,m):
    if not s1:
        return ''
    else:
        step = int(s2[0])*m
    return aphs[(aphs.index(s1[0])+step)%26]+encode_R(s1[1:],s2[1:],m)




def encode_U(s1,s2,m):
    return aphs[(aphs.index(s1[0])+int(s2[0])*m)%26]+encode_R(s1[1:],s2[1:],m)


print(encode_U('bye','128',2))
print(encode_U('dcu','128',-2))