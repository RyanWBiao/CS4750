from typing import List,Tuple
import copy
import time
from classes import State,Variable

test_puzzle = [
    [1,0,0,2,5,0,6,0,8],
    [0,4,0,0,8,0,0,5,0],
    [5,0,8,0,0,0,0,0,2],
    [0,0,0,0,4,0,8,0,0],
    [4,0,0,8,0,1,0,6,0],
    [0,5,0,0,2,6,0,0,0],
    [7,0,4,1,6,2,5,0,0],
    [6,0,5,4,7,0,1,2,3],
    [2,0,0,5,3,8,7,0,0]
]

test_state = State(test_puzzle,[])

test_state.print_board()

for variable in test_state.get_variables():
    print(variable.var_coordinate(),end=" ")
    print(variable.var_domain(),end=" ")
    print(variable.var_priority())

