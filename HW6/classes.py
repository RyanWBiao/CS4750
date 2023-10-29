from typing import List,Tuple
import copy

# Define variable object including:
# 1. Remaining values domain       
# 2. Priority calculated by (constraints count) and (remaining value count)
# 3. Coordinate
class Variable:
    def __init__(self,coordinate:Tuple(int,int),priority:int) -> None:
        self.coordinate = coordinate
        self.priority = priority

# 1. An array of current distribution
# 2. Variable List
# 3. Assignment function
# 4. Test state Function
# 4. Sort variable function
class State:
    def __init__(self,board:List[List[int]],Assginments:List):
        self.board = board
        self.assignments = Assginments
        # self.variables = self.get_variables(self)

    def get_block_number(x:int,y:int):
        return ((x//3)*3+(y//3)+1)

    # The input should be the coordinate of a variable and borad, and this method return its priority
    def get_priority(coordinate:Tuple(int,int),board:List[List[int]]):
        x = coordinate[0]
        y = coordinate[1]
        remain_values = [1,2,3,4,5,6,7,8,9]
        for i in range(1,10):
            if i!= y and board[x][i] in remain_values:
                remain_values.remove(board[x][i])
        for i in range(1,10):
            if i!= x and board[i][y] in remain_values:
                remain_values.remove(board[i][y])
        remain_values_count = len(remain_values)

        # Calculate the degree:
        for i in range(1,10):
            if i!= y and board[x][i] in remain_values:
                remain_values.remove(board[x][i])
        for i in range(1,10):
            if i!= x and board[i][y] in remain_values:
                remain_values.remove(board[i][y])

        pass    
    
    # Get all the variables that have not been assigned values yet. And put them into a list.
    def get_variables(self) -> List[Variable]:
        # Get the variables according to board
        variables = []
        for i in range(1,10):
            for j in range(1,10):
                if self.board[i][j] != 0:
                    new_variable = Variable((i,j),self.get_priority((i,j),self.board))
                    variables.append(new_variable)

    def print_board():
        pass
    pass
    

