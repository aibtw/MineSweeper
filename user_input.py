class UserInput:

    def __init__(self):
        pass

    def dimensions(self):
        rows_num = int(input("Enter the number of rows: "))
        columns_num = int(input("Enter the number of columns: "))

        return [rows_num,columns_num]

    def next_move(self):
        row_in = int(input("\n\n~~~~Enter row index~~~~\n"))
        col_in = int(input("~~~~Enter column index~~~~\n"))
        print("\n\n")
        u_in = [row_in - 1, col_in - 1]
        return u_in


