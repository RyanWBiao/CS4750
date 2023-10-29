from classes import State, Node
from typing import List
import copy
import time


def reach_goal(state):
    if len(state.dirt_distribution) == 0:
        return True
    else:
        return False

# The expand function is supposed to generate 5 states following current state
# def expand(node: Node, fringe: List[Node]):
def expand(node:Node):
    # Make 5 copies for node
    node_left = copy.deepcopy(node)
    node_right = copy.deepcopy(node)
    node_up = copy.deepcopy(node)
    node_down = copy.deepcopy(node)
    node_suck = copy.deepcopy(node)

    # (a)Left shift:
    node_left.parent = node
    node_left.score += 1.0
    node_left.layer += 1
    if (node_left.state.agent_position[1] - 1) >= 1:
        node_left.state.agent_position[1] -= 1

    # (b)Right shift:
    node_right.parent = node
    node_right.score += 0.9
    node_right.layer += 1
    if (node_right.state.agent_position[1] + 1) <= 5:
        node_right.state.agent_position[1] += 1

    # (c)Up shift:
    node_up.parent = node
    node_up.score += 0.8
    node_up.layer += 1
    if (node_up.state.agent_position[0] - 1) >= 1:
        node_up.state.agent_position[0] -= 1

    # (d)Down shift:
    node_down.parent = node
    node_down.score += 0.7
    node_down.layer += 1
    if (node_down.state.agent_position[0] + 1) <= 4:
        node_down.state.agent_position[0] += 1

    # (e)Suck:
    node_suck.parent = node
    node_suck.score += 0.6
    node_suck.layer += 1
    for dirt in node_suck.state.dirt_distribution:
        if dirt == node_suck.state.agent_position:
            node_suck.state.dirt_distribution.remove(dirt)
            break

    return [node_suck,node_down,node_up,node_right,node_left]


init_state_test = State([2, 2], [[3, 1], [3, 3]])
root_node_test = Node(init_state_test, None, 0, 0)

init_state1 = State([2, 2], [[1, 2], [2, 4], [3, 5]])
root_node1 = Node(init_state1, None, 0, 0)

init_state2 = State([3, 2], [[1, 2], [2, 1], [2, 4], [3, 3]])
root_node2 = Node(init_state2,None,0,0)

#use count as a global variable
count_test = 0
count1 = 0
count2 = 0


def Iterative_Deepening_Search(root:Node):
    depth = 1
    while True:
        result = Recursive_DLS(root,depth)
        if result != 'cutoff':
            return result
        depth += 1



def Recursive_DLS(node : Node ,limit:int ):
    global count_test  # Declare count_test as a global variable
    cutoff_occurred = False
    count_test += 1 #increment the global count
    print("This is the {}th node being checked".format(count_test))
    node.state.printState()
    if reach_goal(node.state):
        return node
    elif node.layer == limit:
        return 'cutoff' #use this string to represent cutoff happened
    else:
        for successor in expand(node):
            result = Recursive_DLS(successor,limit)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'Failure':
                return result
    if cutoff_occurred:
        return 'cutoff'
    else:
        return 'failure'


# print("Iterative deepenin tree search:")
# print("The result of test node")
# start_time = time.time()
# answer_node_test = Iterative_Deepening_Search(root_node_test)
# end_time = time.time()
# print("The program takes: {}".format(end_time-start_time))
# print("This is the {}th layer".format(answer_node_test.layer))
# answer_node_test.printPath()

# print("Iterative deepenin tree search:")
# print("The result of instance 1")
# start_time = time.time()
# answer_node1 = Iterative_Deepening_Search(root_node1)
# end_time = time.time()
# print("The program takes: {}".format(end_time-start_time))
# print("This is the {}th layer".format(answer_node1.layer))
# answer_node1.printPath()

# print("")

print("Iterative deepenin tree search:")
print("The result of instance 2")
start_time = time.time()
answer_node2 = Iterative_Deepening_Search(root_node2)
end_time = time.time()
print("The program takes: {}".format(end_time-start_time))
print("This is the {}th layer".format(answer_node2.layer))
answer_node2.printPath()
