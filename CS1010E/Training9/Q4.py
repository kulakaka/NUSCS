records = [['Alice', 'A1000000A', 90, 80, 99, 70],
           ['Bob'  , 'A1000009D', 60, 99, 60, 90],
           ['Dave' , 'A1000003C', 80, 80, 70, 90],
           ['Eve'  , 'A1000001B', 99, 70, 80, 80],
           ['John' , 'A1000004Z', 70, 80, 70, 80]]

def calculate_total(records):
    output = []
    for st in records:
        if st[2] >100 or st[3] >100 or st[4] >100 or st[5]>100:
            continue
        mark = (st[2]+st[3]+st[4])*0.15+st[5]*0.3+25
        output.append([st[1],mark])

    return output

print(calculate_total(records))
    
