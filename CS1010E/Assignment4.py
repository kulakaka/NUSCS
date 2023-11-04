def calc_poly(const_seq,var_poly):
    result = 0
    counter = 0
    for i in range(len(const_seq)):
        result = result+const_seq[i]*var_poly**counter

        counter +=1
    return round(result,2)


# cs = [0, -1, 0, 0, 2]
# vp = 3
# print(calc_poly(cs, vp))

def matchResistorss(R,n):
    result= []
    for i in range(len(R)):
        for x in range(i+1,len(R)):
            if R[i]+R[x] == n:
                result.append((R[i],R[x]))
    
    return result
#print(matchResistors(R,152))

from random import shuffle
longList = [i for i in range(1,100000)]
shuffle(longList)
def matchResistors(R,n):
    result = []
    resistor_dic = {}
    for resistor in R:
        target_resis = n-resistor
        
        if target_resis in resistor_dic and resistor_dic[target_resis] >0:
            result.append((resistor,target_resis))
            
            resistor_dic[target_resis]-=1
            if resistor_dic[target_resis] ==0:
                del resistor_dic[target_resis]
        else:
            resistor_dic[resistor] = resistor_dic.get(resistor,1)

    return result

R = (75,80,90,77,88,91,60,74,73,70,55,93,59)

R1 = (23,75,80,90,77,88,91,60,1,74,73,4,70,55,7,9,93,59,12,43)
R2 = (10,12,40,12,10)
R3 = (1,5,5,9,1)
#print(matchResistors(R3,10))

dict_item = {}
dict_item["FS"] = 4
dict_item["DS"] = 3
dict_item['FM'] = dict_item["FS"] +1
dict_item['FL'] = dict_item["FS"] +2
dict_item['DM'] = dict_item['DS'] +1
dict_item['DL'] = dict_item['DS'] +2
def burger_price(burger):
    price = 0
    for char in burger:
        if char == 'B':
            price += 5
        elif char == 'C':
            price += 8
        elif char == 'P':
            price += 9
        elif char == 'V':
            price += 6
        elif char == 'O':
            price += 5
        elif char == 'M':
            price += 7
    return price

def item_price(item):
    price = 0
    for i in item:
        if i == "B":
            return burger_price(item)
        if i == "D" or i =="F":
            return dict_item.get(item)

def total_price(order):
    total = 0
    for i in order:
        total += item_price(i)
    return total

def remove_order(order,item):
    orderl = list(order)
    if item in orderl:
        orderl.remove(item)
        return tuple(orderl)
    else:
        print(f'The item {item} is not in the order.')
        return None

def total_price_with_set_discount(order):
    price = 0
    bcounter= 0
    dcounter=0 
    fcounter=0
    ol = []
    for item in order:
        if item[0] == "B":
            bcounter +=1
        elif item[0] == "F":
            fcounter +=1
        elif item[0] =="D":
            dcounter +=1
    ol.append(bcounter)
    ol.append(dcounter)
    ol.append(fcounter)
    ol.sort()
    ds_n = ol[0]
    price = ds_n*10
    return total_price(order)-price


# def get_lucky_burger(money_in_pocket,max_burger_size):
#     ingredients = "BCPVOM"
#     burger_dic={}
#     #after discount and two slices of bread
#     price = money_in_pocket+3-10
#     acutal_bs = max_burger_size-2
#     for iteralit in range(len(ingredients)):
#         for iternum in range(acutal_bs):


def filter_wave(wave,n):
    new_wave = []
    L = len(wave)
    for i in range(n):
        for num in range(len(wave),1,-2):
          
            if num-1 == -1:
                new_wave[num] = wave[num-1] * 0 + wave[num]*0.6 + wave[num+1]*0.2
            elif L == num:
                new_wave[num] = wave[num-1] * 0.2 + wave[num]*0 + wave[num+1]*0.2
            else:
                new_wave[num] = wave[num-1] * 0.2 + wave[num]*0.6 + wave[num+1]*0.2



    return new_wave

wave = [12,24,34,451,5,4,1,861,1,2]

print(filter_wave(wave,1))



