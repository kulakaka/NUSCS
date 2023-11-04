import random
def rotate(bouquet,step):
    bli = list(bouquet)

    for i in range(step):
        n = bli[0]
        del bli[0]
        bli.append(n)

    return tuple(bli)
        
#print(rotate(("R", "P", "W", "W", "P", "R", "R", "R"), 8))


def flower_I(bouquet,k):
    bli = list(bouquet)
    result = ''
    for i in range(len(bouquet)):
        for i in range(k-1):
            n = bli[0]
            del bli[0]
            bli.append(n)
        x = bli[0]
        del bli[0]
        result += x
        
    return result 


#print(flower_I(("R", "P", "W", "W", "P", "R", "R", "R"), 3))

def flower_R(bouquet,k):
    if not bouquet:
        return ''
    else:
        b = rotate(bouquet,k)

        return b[-1]+flower_R(b[:len(bouquet)-1],k) 
print(flower_R(("R", "P", "W", "W", "P", "R", "R", "R"), 3))

def pink_rose(bouquet):
    counter = 0
    while True:
        if flower_I(bouquet,counter)[-1]=='P':
            
            return counter
        counter +=1

#print(pink_rose(("R", "P", "W", "W", "P", "R", "R", "R")))


flowers_r_us = [("R", 5, 3), ("R", 3, 2), ("W", 4, 3), ("W", 2, 2), ("P", 3, 4)]
def make_bouquet(shop, num):
    num = num-3
    li= []
    for i in shop:
        for n in shop:
            li.append(i[1]+n[1])
    
    if num in li:
        return True
    else:
        return False
    


#print(make_bouquet(flowers_r_us, 2))

def minimum_cost(shop,num):
    num = num-3
    li= []
    costli = []
    for i in shop:
        for n in shop:
            li.append(i[1]+n[1])
            if num == i[1]+n[1]:
                costli.append(i[2]+n[2])
    
    if num in li:
        return min(costli)+4
    else:
        return -1


#print(minimum_cost(flowers_r_us, 14))


def paint_area(S,C,D):
    total_area = S*S
    count =0
    for i in range(10000):
        x = random.uniform(-S/2,S/2)
        y = random.uniform(-S/2,S/2)

     
        if x**2 + y**2 > (C / 2)**2:
            # Check if the point is inside one of the pink petals.
            for (px, py) in [(0, S/2 - D/2), (S/2 - D/2, 0), (0, -S/2 + D/2), (-S/2 + D/2, 0)]:
                if (x - px)**2 + (y - py)**2 <= (D / 2)**2:
                    count+=1
    
    pink_area = count/10000

    return pink_area*total_area
print(paint_area(15, 8, 3) )