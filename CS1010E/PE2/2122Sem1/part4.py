def child_DNA(d):
    if d == 0:
        return 1
    else:
        out = d%10
        return out*child_DNA((d-out)//10)
    
print(child_DNA(9786))


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

print(parent_mutated_DNA(3024))


