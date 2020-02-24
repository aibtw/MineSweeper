# make while loop
# while the nubber of elements in certain list x < 10 then get a two random int, if the two exist in x, continue
# else, add them to list x

import random




row = 2
col = 2
x = [[1,2,3],
     [4,5,6],
     [7,8,9]]
adj = []

ri = 0
ci = 0

incr = [-1, 0, 1]
incc = [-1, 0, 1]

for i in incr:
    for j in incc:
        ri = row + i
        ci = col + j

        if (ri < 0) or (ri >= len(x)) or (ci < 0) or (ci >= len(x[0]))\
            or (i==0 and j==0):
            continue
        else:
            print("HI")



##def make_adj(hid_board, board, next_move):
##    row = next_move[0]
##    col = next_move[1]
##
##    row_index = 0
##    col_index = 0
##    indices = []
##    adj_cells = []
##    inc = [-1,0,1]
##    for i in inc:
##        for j in inc:
##            try:
##                temp = hid_board[row+inc[i]][col+inc[j]]
##                row_index = row+inc[i]
##                col_index = col+inc[j]
##            except IndexError:
##                continue
##            else:
##                if (temp is int) | (i == 0 and j == 0) | (row_index < 0) | (col_index < 0):
##                    continue
##                else:
##                    indices.append([row_index , col_index ])
##                # adj_cells.append(temp)
##    # print(adj_cells)
##    print(indices)
##
