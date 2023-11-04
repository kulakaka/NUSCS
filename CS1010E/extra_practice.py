from random import *
def area(x0, y0, x1, y1, x2, y2):
    res = abs((x0 * y1 + x1 * y2 + x2*y0) - (y0 * x1 + y1 * x2 + y2*x0))/2
    return res

#print(area(-1,2,3,3,0,-2))


def convert(C):
    F= C*1.8+32
    return max(F,C)

def hugs_kisses(n):
    result=''
    for i in range(n):
        if i%2==0:
            result+='o'
        else:
            result+='x'
    return result

#print(hugs_kisses(3))

def scramble(S):
    odd=''
    even=''
    ls = list(S)
    for i in range(len(ls)):
        if i%2 == 0:
            even+=ls[i]
        else:
            odd+=ls[i]
    return even+odd

#print(scramble('CS1010E'))


def monty_hall(n):

    win = 0
    for i in range(n):
        car = randint(1,3)
        doors = [1,2,3]
        door = choice(doors)
        if door == car:
             win+=1
        else:
            doors.remove(car)
            doors.remove(door)
            if doors[0] == car:
                win+=1
    return win/n
#print(monty_hall(100000))
        