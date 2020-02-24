class Board:
    # making a board
    def create_board(self, columns_num, rows_num):
        board = []
        for i in range(rows_num):
            board.append([])
            for j in range(columns_num):
                board[i].append("-")
        return board

    # copying the board to make the hidden version
    def copy_board(self, board):
        hid_board = []
        for i in board:
            temp = []
            for j in i:
                temp.append(j)
            hid_board.append(temp)
        return hid_board

    # printing boards
    def print_board(self, to_print):
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

    def get_adj(self, hid_board, board, next_move):
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
