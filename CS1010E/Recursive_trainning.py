def sum_odd_n(n):
    if n == 0:
        return 0
    else:
        result = 2*n-1
        return result+sum_odd_n(n-1)

    
def sum_n_squares(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_n_squares(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)
    
def is_even(n):
    if n==0:
        return True
    else:
        return is_odd(n-1)
    
def female(n):
    if n == 0:
        return 1
    else:
        return n-male(female(n-1))
def male(n):
    if n ==0:
        return 0
    else:
        return n- female(male(n-1))


def conway(n):
    if n ==1 or n==2:
        return 1
    else:
        return conway(conway(n-1))+conway(n-conway(n-1))