############################################
## DO NOT MODIFY THIS PORTION OF CODE!!!! ##
############################################

def create_game_matrix(r,c):
    output = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        output.append(row)
    return output

def print_TTT(game):
    for i in range(3):
        print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
        if i !=2:
            print('-----')

def ttt_gameplay():
    game = create_game_matrix(3,3)
    for i in range(3):
        for j in range(3):
            game[i][j] = i*3+j+1
    player = 0

    print_TTT(game)
    for i in range(9): 
        print()
        valid_move = False
        while not valid_move:
            pos = int(input(f'Player {piece[player]} move:'))
            valid_move = check_valid_move(game,pos)
            if not valid_move:
                print(f'Your move {pos} is not valid')
        pos -= 1
        game[pos//3][pos%3] = piece[player]
        winner = check_win(game)
        if winner:
            print(f'Player {winner} won!!! Game over.')
            print_TTT(game)
            return
        player = 1 - player
        print_TTT(game)

    print('No one won. It\'s a tie game.')

piece = ['X','O']
game1 = [[1,2,3],[4,5,6],[7,8,9]]
game2 = [['X',2,3],['X',5,6],['X',8,9]]
game3 = [['O',2,3],[4,'O',6],[7,'O',9]]
game4 = [['X',2,'X'],[4,'O',6],['X','O','X']]
game5 = [['X','X','O'],['X','O','X'],['O','X','X']]

############################################
########### End of do not modify ###########
############################################

############
## Task 1 ##
############

def check_valid_move(game,inp):
    for i in game:
        for x in i:
            if x==inp:
                return True
    return False

# print(check_valid_move(game1, 4))
# print(check_valid_move(game1, 10))
# print(check_valid_move(game2, 4))
# print(check_valid_move(game4, 4))
# print(check_valid_move(game5, 4))
# print(check_valid_move(game2, 1))
# print(check_valid_move(game5, -9))

############
## Task 2 ##
############

def check_win(game):
    for i in range(len(game)):
        if game[i][0] == game[i][1] == game[i][2]:
            return game[i][0]
        elif game[0][i] == game[1][i] == game[2][i]:
            return game[0][i]
    
    if game[0][0] == game[1][1] == game[2][2] or  game[0][2] == game[1][1] == game[2][0]:
        return game[1][1]
    

    else:        
        return ''

# print(check_win(game1))
# print(check_win(game2))
# print(check_win(game3))
# print(check_win(game4))
# print(check_win(game5))

#############################################################
## Uncomment and run ttt_gameplay() below to test the game ##
#############################################################

ttt_gameplay()
