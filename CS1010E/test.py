def card_game_i(N,start_pos,start_dir,seq):
    li=[]
    for i in range(N):
        li.append(i)
    newli = li[:start_pos]+li[start_pos:]
    if start_dir =='CCW':
        newli = newli.reverse()
    
    for i in seq:
        if i=="D":
            newli = newli.append(newli[0])
            break
        elif i == "R":
            #newli.append(newli[-1])
            #del newli[-1]
            newli = newli.reverse()
    return newli[0]
    
    
#print(card_game_i(5,2,'CW','DDRDR'))

dd= {1:'a',2:'b',35:'v'}

#print((min(dd.values())))

#print(dd.items())
s1="1234567890"

def circle(f,g):
    return lambda x:g(f(x))

g = lambda x:(x,x)
h = circle(g,g)
#print(h(2))
def foo(a,b):
    return a+b

dd = {'a': 0, 'b': 1, 'c': 2,
 'd': 0, 'e': 1, 'f': 2}

def valKeys(dict,valLst):
    kys = []
    for val in valLst:
        kys.extend([k for (k,val) in dict.items()])
    return kys
#print(valKeys(dd,[0,2]))


x=['a','b','c','d']
print(dict(x))
#print(dict(tuple('x','7')))