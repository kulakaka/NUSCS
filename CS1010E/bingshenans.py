bouquet = ('R','P','W','W','P','R','R','R')

def rotate(bouquet,k):
    lst = list(bouquet)
    while len(lst) < k:
        lst = lst + list(bouquet)
    lst = lst + list(bouquet)
    return tuple(lst[k:k+len(bouquet)])

def valentino_rec(bouquet,k):
    if not bouquet:
        return ''
    else:
        b = rotate(bouquet,k)
        return b[-1] + valentino_rec(b[:len(bouquet)-1],k)

def pink_rose(bouquet):
    n = 0
    if 'P' not in bouquet:
        return -1
    else: 
        while True:
            if valentino_rec(bouquet,n)[-1] == 'P':
                return n
            n += 1

def is_possible(shop,total):
    def can_form(total,num1,num2): #returns true is it's possible to use num1 and num2 to form total
        big = max(num1,num2)
        small = min(num1,num2)
        count = total//big +1
        output = []
        for i in range(count):
            if int((total - i*big)/small) == (total - i*big)/small:
                output.append((total - i*big)/small) + i
        return output

    return


                

    
print(can_form(22,4,8))
