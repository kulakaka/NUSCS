'''
CS1010E
Assignment 4 - Question 3 Codebase and Template
'''
def make_empty_order():
    return ()

def add_item_to_order(order,item):
    return order + (item,)


# This function calls item_price(item) that should be implemented in Q3 feature 1
def print_receipt(order):
    if not order:
        print("You have no item in your order.")
        return
    print("Your orders:")
    for b in order:
        print(f'{b} ${item_price(b)}')
    print("--------------")
    print(f'Total: {total_price(order)}')

# This function calls item_price(item) that should be implemented in Q3 feature 1
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

def enough_money(order, money_in_my_pocket):
    return total_price(order) <= money_in_my_pocket

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

#-------------------Feature 1 Template------------------#

def item_price(item):
    return 0


#-------------------Feature 2 Template------------------#

def total_price_with_set_discount(order):
    return 0


#-------------------Feature 3 Template------------------#

def get_lucky_burger(money_in_pocket, max_burger_size):
    return []


#Example order process
''' 
my_order = make_empty_order()
my_order = add_item_to_order(my_order,'BVPB')
my_order = add_item_to_order(my_order,'BCPCPB')
my_order = add_item_to_order(my_order,'BPCBPCB')
my_order = add_item_to_order(my_order,'DL')
my_order = add_item_to_order(my_order,'FM')
my_order = add_item_to_order(my_order,'FL')
my_order = add_item_to_order(my_order,'DM')
print_receipt(my_order)
print(f"Price after meal set discount: {total_price_with_set_discount(my_order)}")

#Example getting lucky burger

get_lucky_burger(75, 10)
'''
