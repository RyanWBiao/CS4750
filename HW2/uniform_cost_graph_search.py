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


def expand(node: Node, fringe: List[Node]):
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

    # Insert the new nodes into the fringe:
    fringe.append(node_left)
    fringe.append(node_right)
    fringe.append(node_up)
    fringe.append(node_down)
    fringe.append(node_suck)


# init_state_test = State([2, 2], [[3, 1], [3, 3]])
# root_node = Node(init_state_test, None, 0, 0)

# init_state1 = State([2, 2], [[1, 2], [2, 4], [3, 5]])
# root_node = Node(init_state1, None, 0, 0)

init_state2 = State([3, 2], [[1, 2], [2, 1], [2, 4], [3, 3]])
root_node = Node(init_state2,None,0,0)


def not_in_closed(state, closed):
    for checked_state in closed:
        if state == checked_state:  # This is the method defined in class
            return False  # This state is in the closed
    return True
    

def Graph_Search(root):
    # Insert the initial root into the fringe
    fringe = [root]
    # An empty set to store states that have been checked
    closed = []

    # Count the number of nodes that have been checked
    count = 1

    # Search:
    while len(fringe) != 0:
        # extract the node with min score
        node = min(fringe, key=lambda x: x.score)

        print("This is the {}th node being checked".format(count))
        count += 1
        # if count > 20:   #temp restirction for test
        #     return None
        print("This i the {}th layer in the tree.".format(node.layer))
        node.state.printState()
        print()

        fringe.remove(node)
        if reach_goal(node.state):
            print("The final position of agent: {}".format(
                node.state.agent_position))
            print("The number of states that have been checked: {}".format(len(closed)))
            return node
        if not_in_closed(node.state, closed):
            closed.append(node.state)
            expand(node, fringe)
        # If the node is in the closed set, we just ignore it. It has been removed and will not be expanded

    if len(fringe) == 0:
        return None


start_time = time.time()

answer_node = Graph_Search(root_node)

end_time = time.time()
print("The program takes: {}".format(end_time-start_time))

print("This is the {}th layer".format(answer_node.layer))

answer_node.printPath()
