

def how_many_male(faculty):
    m_counter= 0
    for i in faculty:
        if i == 'M':
            m_counter+=1
        elif i == "F":
            continue
        else:
            return False
        
    return m_counter
def how_many_female(faculty):
    f_counter = 0
    for i in faculty:
        if i == "F":
            f_counter+=1
        elif i == "M":
            continue
        else:
            False
    return f_counter

def gender_balance(faculty):
    m_counter = 0
    f_counter = 0
    for i in faculty:
        if i == 'M':
            m_counter+=1
        elif i == "F":
            f_counter+=1
        else:
            return False
    if m_counter == f_counter:
        return "balanced"
    elif m_counter > f_counter:
        return "male"
    elif f_counter > m_counter:
        return "female"
    else:
        return False


def caterpillar (n):
    pillar = []
    string =''
    for i in range(n-1):
        pillar.append("Q")
    
    pillar.append(6)
    
    for i in pillar:
        string = string + str(i)
    return string


def caterpillar_with_backside (n):
    pillar = []
    string =''
    for i in range(n-1):
        if i == 0:
            pillar.append("c")
        pillar.append("Q")
    
    pillar.append(6)

    for i in pillar:
        string = string + str(i)
    return string

