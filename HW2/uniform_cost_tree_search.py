from classes import State, Node
from typing import List
import copy
import time
import heapq


def reach_goal(state):
    if len(state.dirt_distribution) == 0:
        return True
    else:
        return False

# The expand function is supposed to generate 5 states following current state
def expand(node: Node):
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

    #(e)Suck:
    node_suck.parent = node
    node_suck.score += 0.6
    node_suck.layer += 1
    for dirt in node_suck.state.dirt_distribution:
        if dirt == node_suck.state.agent_position:
            node_suck.state.dirt_distribution.remove(dirt)
            break
    
    return [node_suck,node_down,node_up,node_right,node_left]


# init_state1 = State([2, 2], [[1, 2], [2, 4], [3, 5]])
# root_node = Node(init_state1, None, 0,0)

init_state2 = State([3, 2], [[1, 2], [2, 1], [2, 4], [3, 3]])
root_node = Node(init_state2,None,0,0)

# init_state_test = State([2,2],[[3,1],[3,3]])
# root_node = Node(init_state_test,None,0,0)


def Tree_Search(root:None):
    #Use a heap to implement the fringe, so we can find the minimun efficiently
    fringe = []
    heapq.heappush(fringe,root)   # It's a min heap by default
    count = 1

    # Search:
    while len(fringe) != 0:
        print("This is the {}th node being checked".format(count))
        print("There are {} nodes in the fringe right now.".format(len(fringe)))
        node = heapq.heappop(fringe) #extract the min node from the heap

        print("The score of this node is {}".format(node.score))
        count += 1

        # if count > 10:   #temp restirction
        #     return None

        print("This is the {}th layer in the tree.".format(node.layer))
        node.state.printState()

        print()

        if reach_goal(node.state):
            print("The final position of agent: {}".format(node.state.agent_position))
            return node
        else:
            successors = expand(node)
            for successor in successors:
                # print(successor.score)
                heapq.heappush(fringe,successor)

    if len(fringe) == 0:
        return None


start_time = time.time()

#Search here:
answer_node = Tree_Search(root_node)

end_time = time.time()
print("The program takes: {}".format(end_time-start_time))

# print("This is the {}th layer".format(answer_node.layer))
answer_node.printPath()




