def per_cipher_i(s,n):
    output=[]
    pp=''
   
    for i in range(len(s)//n+1):
        output+=reversed(s[:n])
        s=s[n:]
    for i in output:
        pp+=i
    return pp


#print(per_cipher_i('PE Part 1 is supposed to be easy',7))


def per_cipher_r(s,n):
    if not s:
        return ''
    else:
        a = s[:n]
        return a[::-1]+per_cipher_r(s[n:],n)
    
#print(per_cipher_r(per_cipher_r('12345678910',3),3))


def per_cipher_o(s,n):
    return s[:n][::-1]+per_cipher_r(s[n:],n)


print(per_cipher_o('12345678910',3))