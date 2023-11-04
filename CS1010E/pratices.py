def stern_brocot(n):
    li = [(0,1),(1,1)]
    inli = []
    isrtli =[]
    for i in range(n):
        idx = 2*n-1
        inli.append(idx)
        #inli.reverse()
        reserinli = inli.reverse()
    for i in range(len(inli)):
        idxs = inli[:i]
        for x in range(len(idxs)):
            isrtdata = (li[inli[i]-1][0]+li[inli[i]][0],li[inli[i]-1][1]+li[inli[i]][1])
            isrtli.insert(0,isrtdata)
        for n in range(len(isrtli)):
            li.insert(reserinli[i],isrtli[n])
    return li
    # for i in range(len(inli)): 
    #     ied = inli[:i]  

    #     for x in range(len(ied)):
    #         xx = ied[x]
    #         re = (li[xx-1][0]+li[xx][0],li[xx-1][1]+li[xx][1])
    #         li.insert(idx,re)
    # return li

print(stern_brocot(2))

