def per_cipher_i(s,n):
    output=[]
    pp=''
   
    for i in range(len(s)//n+1):
        output+=reversed(s[:n])
        s=s[n:]
        print(s)
    for i in output:
        pp+=i
    return pp


print(per_cipher_i('PE Part 1 is supposed to be easy',7))

