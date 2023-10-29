class State:
    def __init__(self,row_number,col_number):
        self.row_number = row_number
        self.col_number = col_number
        self.grid = [["_" for _ in range(col_number+2)] for _ in range(row_number+2)] # add two more rows and cols for padding
        for i in range(1,col_number+1):
            self.grid[0][i] = i
        for j in range(1,row_number+1):
            self.grid[j][0] = j
        self.grid[0][0] = " "

    def printState(self):
        for i in range(self.row_number+1):
            for j in range(self.col_number+1):
                print("{} ".format(self.grid[i][j]),end='')
            print("")


