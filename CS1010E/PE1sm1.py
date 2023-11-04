def sum_digit_square_I(n):
    nli=[]
    nstr = str(n)
    for i in nstr:
        nli.append(int(i))
    result = 0
    for i in range(len(nli)):
        
        result += int(nli[i])**2

    return result

def sum_digit_square(n):
    while n !=0:
        if n>0 and n<10:
            s += n**2
            break
        s = n//10
        s +=s**2
        n = (n-s)//10
    return s



print(sum_digit_square(123456))
#print(sum_digit_square_I(999988887777666655554444333322221111))

def sum_digit_square_R(n):
    if n == 0:
        return 0
    else:
        nli = list(str(n))
        new_n = n-(int(nli[0])*(10**(len(nli)-1)))

        return int(nli[0])**2+sum_digit_square_R(new_n)
#print(sum_digit_square_R(999988887777666655554444333322221111))


def is_happy_number(n):
    if n>=0 and n<10:
        if n == 1 or n == 7:
            return True
        else:
            return False
    else:
        return is_happy_number(sum_digit_square_R(n))
        
        
#print(is_happy_number(100093))


def all_happy_number(n,m):
    sample = []
    result = []
    for i in range(n,m+1):
        sample.append(i)

    sample.sort()
    for i in sample:
        if is_happy_number(i) == True:
            result.append(i)
    result.sort()
    return result
            
#print(all_happy_numbers(1, 70))



def is_unique1(seq):
    if seq is str:
        seq = list(seq)
    for i in range(len(seq)):
        for j in seq[i+1:]:
            if seq[i]==j:
              
                return False
    return True

def is_unique(seq):
    if seq is str:
        seq = list(seq)
    for i in seq:
        n = seq.index(i)
        for j in seq[n+1:]:
            if i==j:
              
                return False
    return True
#print(is_unique((['aaa', 'bbb', (1,1), 1])))




