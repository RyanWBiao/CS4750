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


def backtracking(init_state:State):
    # Termination step:
    if init_state.finished():
        return init_state.get_assignments()
    
    # Get the variable with mimimun priority value. It means this variable will be assign at first
    # This step include MRV
    # The conflict values have been removed from the domain when the variables were made. It's equivalent to forward checking.
    variables = init_state.get_variables()
    min_priority_variable = variables[0]
    for variable in variables:
        if variable.var_priority() < min_priority_variable.var_priority():
            min_priority_variable = variable
    
    # Iterate through the domain 
    for value in min_priority_variable.var_domain():
        init_state.add_assignment(min_priority_variable,value) # (1) add assignment to the state
        init_state.board_modify(min_priority_variable.var_coordinate(),value) # (2) change the board:
        result = backtracking(init_state)  
        if result != False:
            return result  # The result is either an assignment or False
        # Unfinied
    # All values lead to failure
    return False

    # print(min_priority_variable.var_coordinate())


print("***********************")
assignments = backtracking(test_state)

if assignments != False:
    for assignment in assignments:
        print(assignment[0][0],end=" ")
        print(assignment[0][1],end=" ")
        print(assignment[1])

test_state.print_board()
