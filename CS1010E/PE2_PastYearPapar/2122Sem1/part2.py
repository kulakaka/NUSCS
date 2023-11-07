
def create_map_file():
    pmap1list = ['0000011111',
    '0000X11111',
    '0000111111',
    '000X111111',
    '0001111111',
    '0222111111',
    '2222211111',
    '2222222111',
    '2222222211',
    '2222222222',
    '2222222222']
    pmap2list = ['000000X22222',
    '00000X222222',
    'XXXXX2222222',
    '111122222222',
    '111122222222',
    '111X22222222',
    '111222222222',
    '111222222222',
    '11X222222222',
    '112222222222']
    f1 = open("pmap1.txt","w")
    for line in pmap1list:
        f1.write(line+'\n')
    f1.close()
    f2 = open("pmap2.txt","w")
    for line in pmap2list:
        f2.write(line+'\n')
    f2.close()
create_map_file()

def buyable_map(filename):
    # Open and read the input map file
    with open(filename, 'r') as file:
        pmap = [line.strip() for line in file]

    rows, cols = len(pmap), len(pmap[0])
    buyable_map = ''

    # Iterate through each location in the map
    for i in range(rows):
        for j in range(cols):
            if pmap[i][j] == 'X':
                # If the location is 'X', mark it as buyable
                buyable_map += 'X'
            else:
                same_shortest_distance = True
                current_shop = pmap[i][j]

                # Check if any neighbor has a different shortest distance shop
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if 0 <= i + x < rows and 0 <= j + y < cols:
                            neighbor_shop = pmap[i + x][j + y]
                            if neighbor_shop != current_shop:
                                same_shortest_distance = False
                                break

                # Mark the location as unbuyable if all neighbors have the same shortest distance shop
                if same_shortest_distance:
                    buyable_map += '.'
                else:
                    buyable_map += current_shop

        # Add a newline character after each row
        buyable_map += '\n'

    return buyable_map

print(buyable_map('pmap1.txt'))