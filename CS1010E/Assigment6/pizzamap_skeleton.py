############################################
## DO NOT MODIFY THIS PORTION OF CODE!!!! ##
############################################

def create_zero_matrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

def m_tight_print(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)

############################################
########### End of do not modify ###########
############################################

############
##  Task  ##
############

def pd_map(r,c,sites):
    
    map = create_zero_matrix(r,c)
    for rx in range(r):
        for cx in range(c):
            map[rx][cx] = cal_dis([rx,cx],sites)
    return map


def cal_dis(point,sites):
    li = []
    for i in sites:
        li.append(((i[0]-point[0])**2+(i[1]-point[1])**2))
    li2 = li.copy()  
    li2.sort()  
    if li2[0] == li2[1]:
        return 'X'
    else:
        return li.index(min(li))

# m_tight_print(pd_map(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
m_tight_print(pd_map(10,10,[[2,3],[4,9],[7,2]]))
# m_tight_print(pd_map(60,70,[[10,20],[30,20],[40,50]]))
# ex = pd_map(60,70,[[10,20],[30,20],[40,50]])
    
#print(cal_dis(point,sites))
#print(pd_map(7,8,[[1,3],[4,7],[7,2]]))

	
