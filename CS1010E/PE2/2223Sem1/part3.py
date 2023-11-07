def min_no_of_turns(L):
    lis = list(L)

    count=0
    minu = min(lis)
    while len(lis)!=0:
        
        if minu+1 in lis:
            lis.remove(minu)
            minu=minu+1

        else:
            if minu != min(lis):
                    count+=1
                    lis.remove(minu)
                    minu = min(lis)
            else:
                count+=1
                lis.remove(minu)
                if not lis:
                     return count
                minu = min(lis)

    return count
print(min_no_of_turns ((6,5,4,3,2,1,11,12,13,14,15,16,6,5,16,16)))
