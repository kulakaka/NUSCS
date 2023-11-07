# def sum_of_3(L,n):
#     li=list(L)

#     for i in (li):
#         for x in (li[li.index(i):]):
#             if i==x:
#                 continue
#             for y in (li[li.index(x):]):
#                 if x==y:
#                     continue
#                 elif n == i+x+y:
#                     print(i,x,y)
#                     return True
                
#     return False
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)
def find(L,n):
    li=list(L)

    for i in (li):
        for x in (li[li.index(i):]):
            if i==x:
                continue
            for y in (li[li.index(x):]):
                if x==y:
                    continue
                elif n == i+x+y:
                    print(i,x,y)
                    return True
                
    return False
def find1(l1,l2,l3,n):

    for i in (l1):
        for x in l2:
            if i==x:
                continue
            for y in (l3):
                if x==y:
                    continue
                if n == i+x+y:
                    print(i,x,y)
                    return True
    return False
def sum_of_3(L,n):
    li=quicksort(list(L))
    divider = len(li)//2
    li1 = li[:divider]
    li2 = li[divider:]
    if li[-1]<n:
        
        for i in li1:
            for x in (li1[li1.index(i):]):
                if i==x:
                    continue
                for y in (reversed(li2)):
                    if x==y:
                        continue
                    elif n == i+x+y:
                        print(i,x,y)
                        return True
                    
        return False
    elif li[-1]*2>n:
        
        for i in li1:
            for x in (reversed(li1[li1.index(i):])):
                if i==x:

                    continue
                for y in (reversed(li2)):
                    if x==y:
                        continue
                    elif n == i+x+y:
                        print(i,x,y)
                        return True
    elif li[-1]*3>n:
        for i in reversed(li1):
            for x in (reversed(li1[li1.index(i):])):
                if i==x:
                    continue
                for y in (reversed(li2)):
                    if x==y:
                        continue
                    elif n == i+x+y:
                        print(i,x,y)
                        return True
                    
        return False

    else:
        return False
print(sum_of_3(tuple(range(1,4000)),11994))




