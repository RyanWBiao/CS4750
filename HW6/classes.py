from typing import List
import copy

# Define variable object including:
# 1. Remaining values domain       
# 2. Priority calculated by (constraints count) and (remaining value count)
# 3. Coordinate
class Variable:
    def __init__(self,coordinate:tuple,priority:int,domain:List[int]) -> None:
        self.__coordinate = coordinate
        self.__priority = priority
        self.__domain = domain

    def var_coordinate(self):
        return self.__coordinate
    def var_priority(self):
        return self.__priority
    def var_domain(self):
        return self.__domain

# 1. An array of current distribution
# 2. Variable List
# 3. Assignment function
# 4. Test state Function
# 4. Sort variable function
class State:
    def __init__(self,board:List[List[int]],assginments:List):
        self.board = [[0] * 10 for _ in range(10)]  # Creating a 2D list
        # Add a margin to the board:
        for i in range(9):
            self.board[i + 1] = [0] + board[i]
        self.assignments = assginments
        self.variables = self.get_variables()

    def board_modify(self,coordinate:tuple,value:int):
        x = coordinate[0]
        y = coordinate[1]
        self.board[x][y] = value
    
    def get_assignments(self):
        return self.assignments
    
    def add_assignment(self,coordinate:tuple,value:int):
        # append a (coordinate,value) pair into the assignment list:
        self.assignments.append((coordinate,value))   # e.g [((1,2),5),((3,4),7)]

    # Remove assignment according to variable's coordinate
    def remove_assignment(self,coordinate:tuple):
        for assignment in self.assignments:
            if assignment[0] == coordinate:
                self.assignments.remove(assignment)

    def finished(self)->bool:
        for i in range(1,10):
            for j in range(1,10):
                if self.board[i][j] == 0:
                    return False
        return True

    # The input should be the coordinate of a variable, and this method return its priority
    def get_priority(self,coordinate:tuple):
        board = self.board
        x = coordinate[0]
        y = coordinate[1]
        remain_values = [1,2,3,4,5,6,7,8,9]
        # Exclude all invalid values:
        for i in range(1,10):
            if i!= y and board[x][i] in remain_values:
                remain_values.remove(board[x][i])
        for i in range(1,10):
            if i!= x and board[i][y] in remain_values:
                remain_values.remove(board[i][y])
        block_start_x = ((x-1)//3)*3+1
        block_start_y = ((y-1)//3)*3+1
        for i in range(block_start_x,block_start_x+3):
            for j in range(block_start_y,block_start_y+3):
                if board[i][j] in remain_values:
                    remain_values.remove(board[i][j])
        remain_values_count = len(remain_values)

        # Calculate the degree:
        degree = -3 # Since the following calculation include the degree to the variable itself. We -3 at first
        # 1. The constraint to the valriables in the same row
        for i in range(1,10):
            if board[x][i] == 0:
                degree = degree + 1
        # 2. The constraint to the valriables in the same col
        for i in range(1,10):
            if i != x and board[i][y] == 0:
                degree = degree + 1
        # 3. The constraint to the valriables in the same block
        block_start_x = ((x-1)//3)*3+1
        block_start_y = ((y-1)//3)*3+1
        for i in range(block_start_x,block_start_x+3):
            for j in range(block_start_y,block_start_y+3):
                if board[i][j] == 0:
                    degree = degree + 1
        
        # Return the priority value: (lower value means higher priority)
        return remain_values_count * 10000 + degree * 100 + y*10 + x
    
    # This mehtod get the domain of a variable (maximum domain is [1-9])
    def get_domain(self,coordinate:tuple)->List[int]:
        board = self.board
        x = coordinate[0]
        y = coordinate[1]
        remain_values = [1,2,3,4,5,6,7,8,9]
        for i in range(1,10):
            if board[x][i] in remain_values:
                remain_values.remove(board[x][i])
        for i in range(1,10):
            if board[i][y] in remain_values:
                remain_values.remove(board[i][y])
        block_start_x = ((x-1)//3)*3+1
        block_start_y = ((y-1)//3)*3+1
        for i in range(block_start_x,block_start_x+3):
            for j in range(block_start_y,block_start_y+3):
                if board[i][j] in remain_values:
                    remain_values.remove(board[i][j])
        return remain_values
    
    # Get all the variables that have not been assigned values yet. And put them into a list.
    def get_variables(self) -> List[Variable]:
        # Get the variables according to board
        variables = []
        for i in range(1,10):
            for j in range(1,10):
                if self.board[i][j] == 0:
                    new_variable = Variable((i,j),self.get_priority((i,j)),self.get_domain((i,j)))
                    variables.append(new_variable)
        return variables
    

    def print_board(self):
        for i in range(1,10):
            for j in range(1,10):
                if self.board[i][j] == 0:
                    print(" ",end=" ")
                else:
                    print(self.board[i][j],end=" ")
                if j%3 == 0:
                    print("|",end='')
            if i%3 == 0:
                print("")
                print("---------------------")
            else:
                print("")
    

