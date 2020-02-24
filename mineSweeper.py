import pygame
import random
from user_input import UserInput
# making a board
def create_board(columns_num, rows_num):
    board = []
    for i in range(rows_num):
        board.append([])
        for j in range(columns_num):
            board[i].append("-")
    return board


# copying the board to make the hidden version
def copy_board(board):
    hid_board = []
    for i in board:
        temp = []
        for j in i:
            temp.append(j)
        hid_board.append(temp)
    return hid_board


# printing boards
def print_board(to_print):
    # print upper numbers
    print("\t", end=":")
    for i in range(1,len(to_print[0])+1):
        print(str(i), end="\t ")
    print("\n")

    # print side numbers
    for i in range(0,len(to_print)):
        if i+1 < 10:
            print(str(i+1) + ":", end="\t")
        else:
            print(str(i + 1) + ":", end="\t")
            # print the content of the board
        for j in to_print[i]:
            print(j, end ="\t")
        print("\n")


# Get random numbers and store them as pair of x,y in a list, as bombs locations
def get_bombs_locations(columns_num, rows_num):
    b_locations = []
    while len(b_locations) < 10:
        i = random.randint(0, 7)
        j = random.randint(0, 7)

        temp = [i, j]
        if b_locations:
            if temp not in b_locations:
                b_locations.append(temp)
            else:
                continue
        else:
            b_locations.append(temp)
    return b_locations
    # print(b_locations)


# place the bombs in their places in the giver board
def place_bombs(board_to_place, bombs_locations):
    for i in range(len(bombs_locations)):
        temp_row = bombs_locations[i][0]
        temp_col = bombs_locations[i][1]

        board_to_place[temp_row][temp_col] = "*"


# Input of next move
# def user_in():
#     row_in = int(input("\n\n~~~~Enter row index~~~~\n"))
#     col_in = int(input("~~~~Enter column index~~~~\n"))
#     print("\n\n")
#     u_in = [row_in-1, col_in-1]
#     return u_in


# get the indices of adj cells
def get_adj(hid_board, board, next_move):
    row = next_move[0]
    col = next_move[1]
    indices = []
    inc = [-1, 0, 1]

    for i in inc:
        for j in inc:
            row_index = row + i
            col_index = col + j
            if (row_index < 0) or (row_index >= len(hid_board)) \
                    or (col_index < 0) or (col_index >= len(hid_board[0])) or (i == 0 and j == 0):
                continue
            indices.append([row_index, col_index])
    return indices


def play_game():
    # Class input:
    # rows_num = int(input("Enter the number of rows: "))
    # columns_num = int(input("Enter the number of columns: "))
    dimensions = u_inp.dimensions()

    # making the board
    board = create_board(dimensions[1], dimensions[0])
    # making the hidden board
    hid_board = copy_board(board)
    # print the boards
    print_board(board)
    # print_board(hid_board)

    # get bombs locations
    # get_bombs_locations(columns_num, rows_num)
    place_bombs(hid_board, get_bombs_locations(dimensions[1], dimensions[0]))
    print_board(hid_board)

    next_move = u_inp.next_move()
    print(next_move)

    adj_cells = get_adj(hid_board, board, next_move)
    print(adj_cells)


u_inp = UserInput()
play_game()


