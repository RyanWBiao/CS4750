import copy
import time
from classes import State

def successor(state : State):
    successors = []
    #iterate through every position:
    for i in range(1,state.row_number):
        for j in range(1,state.col_number):
            if state.grid[i][j] == "x" or state.grid[i][j] == "o": # This position has been occupied.
                continue
            valid_successor = False
            neighbors = [state.grid[i-1][j-1],state.grid[i-1][j],state.grid[i-1][j+1],state.grid[i][j-1],state.grid[i][j+1],state.grid[i+1][j-1],state.grid[i+1][j],state.grid[i+1][j+1]]
            # print(neighbors)
            for neighbor in neighbors:
                if neighbor == 'x' or neighbor == 'o':
                    valid_successor = True  # Only if it's next to an existing piece.
            # print(neighbors,end=" ")
            # print("This is the [{}][{}]".format(i,j),end=' ')
            # print(valid_successor)

            if valid_successor:
                successors.append([i,j])
    return successors

init_state = State(5,6)

init_state.grid[3][4] = "x"

init_state.printState()

print(successor(init_state))



            