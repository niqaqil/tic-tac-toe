# write your code here
def win(symbol):
    cells_ = cell_list
    if ((cells_[0][0] == cells_[0][1] == cells_[0][2] == symbol)
            or (cells_[1][0] == cells_[1][1] == cells_[1][2] == symbol)
            or (cells_[2][0] == cells_[2][1] == cells_[2][2] == symbol)
            or (cells_[0][0] == cells_[1][0] == cells_[2][0] == symbol)
            or (cells_[0][1] == cells_[1][1] == cells_[2][1] == symbol)
            or (cells_[0][2] == cells_[1][2] == cells_[2][2] == symbol)
            or (cells_[0][0] == cells_[1][1] == cells_[2][2] == symbol)
            or (cells_[0][2] == cells_[1][1] == cells_[2][0] == symbol)):
        return True
    return False


def check():
    count_x = 0
    count_o = 0
    x_win = False
    o_win = False
    game_finish = True
    for x in range(len(cell_list)):
        for y in range(len(cell_list[x])):
            if cell_list[x][y] == ' ':
                game_finish = False

    x_win = win('X')
    o_win = win('O')

    if game_finish and not (x_win or o_win):
        print("Draw")
        return True
    else:
        if x_win:
            print("X wins")
            return True
        elif o_win:
            print("O wins")
            return True
    return False


def print_cell():
    print("---------")
    for i in range(len(cell_list)):
        line = ' '.join(cell_list[i])
        print('|', line, '|')
    print("---------")


coordinate = ''


def check_int():
    global coordinate
    check_inte = False
    while not check_inte:
        for i in coordinate:
            if i.isdigit():
                check_inte = True
            else:
                print("You should enter numbers!")
                coordinate = input("Enter the coordinates: ").split()
                check_inte = False
    if check_inte:
        coordinate = [int(i) for i in coordinate]


def check_range():
    check_int()
    global coordinate
    check_num = False
    while not check_num:
        for j in range(len(coordinate)):
            if coordinate[j] >= 1 and coordinate[j] <= 3:
                check_num = True
            else:
                print("Coordinates should be from 1 to 3!")
                coordinate = input("Enter the coordinates: ").split()
                check_int()
                check_num = False


def check_cell(turn):
    check_range()
    global coordinate
    check_cell = False
    while not check_cell:
        if cell_list[coordinate[0] - 1][coordinate[1] - 1] == ' ':
            cell_list[coordinate[0] - 1][coordinate[1] - 1] = turn
            check_cell = True
        else:
            print("This cell is occupied! Choose another one!")
            coordinate = input("Enter the coordinates: ").split()
            check_int()
            check_range()


def turn(t):
    global coordinate
    coordinate = input("Enter the coordinates: ").split()
    check_cell(t)


cells = '         '
cell_list = [[cells[0], cells[1], cells[2]],
             [cells[3], cells[4], cells[5]],
             [cells[6], cells[7], cells[8]]]
print_cell()

check_win = False
step = ['X', 'O']
while not check_win:
    for i in range(len(step)):
        turn(step[i])
        print_cell()
        check_win = check()
        if check_win:
            break
    if check_win:
        break

