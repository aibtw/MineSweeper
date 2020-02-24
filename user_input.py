import sys
class UserInput:

    def __init__(self):
        pass

    def dimensions(self):
        rows_num = input("Enter the number of rows: ")
        if rows_num == "q":
            sys.exit()
        columns_num = input("Enter the number of columns: ")
        if columns_num == "q":
            sys.exit()
        return [int(rows_num), int(columns_num)]

    def next_move(self):
        row_in = input("\n\n~~~~Enter row index~~~~\n")
        if row_in == "q":
            sys.exit()
        col_in = input("~~~~Enter column index~~~~\n")
        if col_in == "q":
            sys.exit()
        print("\n\n")
        u_in = [int(row_in) - 1, int(col_in) - 1]
        return u_in

