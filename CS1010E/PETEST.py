def card_game_i(N,start_pos,start_dir,seq):
    np= N-start_pos-1
    if start_dir == 'CCW':
        for i in seq:
            if i=='D':
                np-=1
            elif i == 'R':
                np+=1
            if np == 0:
                np==N
    elif start_dir =='CW':
        for i in seq:
            if i=='D':
                np+=1
            elif i == 'R':
                np-=1
            if np==N:
                np=0
            
    return np


def card_game_r(N,start_pos,start_dir,seq):
    if len(list(seq)) == 0:
        return 0
    else:
        if start_dir == 'CCW':
            if seq[0]=='D':
                np-=1
            elif seq[0]=='R':
                np+=1
        elif start_dir =='CW':
            if seq[0]=='D':
                np+=1
            elif seq[0]=='R':
                np-=1
        return N-start_pos-1+np+ card_game_r(N,start_pos,start_dir,seq[1:])


def card_game_s(N,start_pos,start_dir,seq):
    
    np= N-start_pos-1
    if start_dir == 'CCW':
        for i in seq:
            if i=='D':
                np-=1
            elif i == 'R':
                np+=1
            elif i == 'S':
                np-=2
            if np == 0:
                np==N
            elif np == -2:
                np==N-2
            elif np == -1:
                np==N-1
    elif start_dir =='CW':
        for i in seq:
            if i=='D':
                np+=1
            elif i == 'R':
                np-=1
            elif i == 'S':
                np+=2
            if np==N:
                np=0
            elif np==N+2:
                np==2
            elif np == N+1:
                np==1
    return np



def find_parents(child_dna,dna_dataset):
    ad = {}
    result =[]
    for i in range(len(dna_dataset)):
        ad[i] = dna_dataset[i]
    for x in ad:
        for i in dna_dataset:
            if ad.get(x)+i == child_dna:
                result.append((ad.get(x),i))
    return result



def three_little_pigs_defence(seq):
    re = ''
    li = list(seq)
    for i in range(len(li)):
        if li[i] == 'H':
            if li[i-1]=='W':
                continue
            else:
                continue
        re+=li[i]

    return re

