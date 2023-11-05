from typing import List,Tuple
import copy
import time
from classes import State,Variable



# for variable in test_state.get_variables():
#     print(variable.var_coordinate(),end=" ")
#     print(variable.var_domain(),end=" ")
#     print(variable.var_priority())


def backtracking(init_state:State):
    global assignment_count
    # Termination step:
    if init_state.finished():
        return init_state.get_assignments()
    
    # Get the variable with mimimun priority value. It means this variable will be assign at first
    # This step include MRV
    # The conflict values have been removed from the domain when the variables were made. It's equivalent to forward checking.
    variables = init_state.get_variables() # The variables are newly generated
    min_priority_variable = variables[0]
    for variable in variables:
        if variable.var_priority() < min_priority_variable.var_priority():
            min_priority_variable = variable
    
    # Iterate through the domain 
    domain = min_priority_variable.var_domain()
    for value in domain:
        init_state.add_assignment(min_priority_variable.var_coordinate(),value) # (1) add assignment to the state
        init_state.board_modify(min_priority_variable.var_coordinate(),value) # (2) change the board:

        # Print assignment section:
        assignment_count = assignment_count + 1
        if assignment_count <= 4:
            print("The {} assignment: ".format(assignment_count))
            print("The variable ({},{}) is selected".format(min_priority_variable.var_coordinate()[0],min_priority_variable.var_coordinate()[1]))
            print("The domain of this variable: {}".format(min_priority_variable.var_domain()))
            print("The domain size: {}".format(len(min_priority_variable.var_domain())))
            print("The degree of this variable is: {}".format(init_state.get_degree(min_priority_variable.var_coordinate())))
            print("The value {} is assigned to it".format(value))
            print("")

        result = backtracking(init_state)  
        if result != False:
            return result  # The result is either an assignment or False
        # If the result is False (This assginment will lead to failure) remove this assignment:
        init_state.remove_assignment(min_priority_variable.var_coordinate())
        init_state.board_modify(min_priority_variable.var_coordinate(),0) # Modify the value back to 0

    # All values lead to failure
    return False

    # print(min_priority_variable.var_coordinate())



from sudoku import test_puzzle,test_puzzle2,instance_1,instance_2,instance_3

print("**************************************")

# 
state = State(instance_3,[])
state.print_board()

# Use a global variable to track the number of assginment:
assignment_count = 0
# Remark: This assginment count is not final assignment, some assignment might be remove in the backtracking step

start_time = time.time()
assignments = backtracking(state)
end_time = time.time()

# if assignments != False:
#     for assignment in assignments:
#         print(assignment[0][0],end=" ")
#         print(assignment[0][1],end=" ")
#         print(assignment[1])

if assignments == False:
    print("Search fail")
else:
    state.print_board()

print("The program takes: {}".format(end_time-start_time))
print("")
