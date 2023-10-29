class State:
    # Constructor method (initializer)
    def __init__(self, agent_position, dirt_distribution):
        self.agent_position = agent_position
        self.dirt_distribution = dirt_distribution

    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            # Compare agent_position
            if self.agent_position != other.agent_position:
                return False
            
            # Convert the dirt_distribution to sets for unordered comparison
            self_dirt_set = {tuple(inner) for inner in self.dirt_distribution}
            other_dirt_set = {tuple(inner) for inner in other.dirt_distribution}

            return self_dirt_set == other_dirt_set
        
        return False

    def printState(self):
        matrix = [['0 ' for _ in range(6)] for _ in range(5)]   #This is a 5*6 matrix, don't use 0 index

        #print the dirt and agent, if the agent and dirt are both in the same position, use 2
        matrix[self.agent_position[0]][self.agent_position[1]] = 'A '
        for dirt in self.dirt_distribution:
            if dirt[0] == self.agent_position[0] and dirt[1] == self.agent_position[1]:
                matrix[dirt[0]][dirt[1]] = "2 " 
            else:
                matrix[dirt[0]][dirt[1]] = "X "


        for i in range(1,5):
            for j in range(1,6):
                print(matrix[i][j],end='')
            print("")


#The Node include state and other info associated with the current state
class Node:
    def __init__(self,state,parent,score,layer):
        self.state = state
        self.parent = parent
        self.score = score
        self.layer = layer

    def __lt__(self,other):
        if self.score != other.score:
            return self.score < other.score
        else: #equal
            if self.state.agent_position[0] != other.state.agent_position[0]:
                return self.state.agent_position[0] < other.state.agent_position[0]
            else:
                return self.state.agent_position[1] < other.state.agent_position[1]
        #Two state have the same score same agent position is not supposed to happen in the search

    def printPath(self):
        if self == None:
            print("Search fails")
        else:
            print("The path of the agent:")
            path = []
            while self != None:
                path = [self.state.agent_position] + path
                self = self.parent

            for i in range(len(path)-1):
                if path[i] == path[i+1]:
                    path[i+1] = "suck"

            for place in path:
                print("->{}".format(place),end="")
            print("")

    # # Instance methods
    # def method1(self):
    #     # Access instance attributes or call other methods
    #     print(f"Method 1: {self.instance_attribute1}")

    # def method2(self, value):
    #     self.instance_attribute1 += value