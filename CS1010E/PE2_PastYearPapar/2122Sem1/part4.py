def child_DNA(d):
    if d == 0:
        return 1
    else:
        out = d%10
        return out*child_DNA((d-out)//10)
    
print(child_DNA(16632))


def parent_mutated_DNA(d):
    li = []
    age = child_DNA(d)
    for i in range(1,10):
        if age%i!=0:
            continue
        else:
            s1=age//i
            li.append((len(str(s1)))*10*i+s1)
    
    return min(li)

print(parent_mutated_DNA(16632))


def isMartian(d):
    pl = [2,3,5,7]
    for i in pl:
        while d%i==0:
            d = d/i
    if d>9:
        return False
    else:
        return True


print(isMartian(24))