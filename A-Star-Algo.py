# This class represent a graph
class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


# This class represent a node
class Node:

    # Initialize the class
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))


# A* search

def A_Star(graph, heuristics, start, end):
    # Create lists for open nodes and closed nodes
    open_list = []
    closed = []
    path = []
    current = start
    # Set g = 0 for the start node

    start_node = Node(start, None)
    start_node.g = 0
    start_node.h = heuristics[start]
    start_node.f = start_node.g + start_node.h
    open_list.append(start_node)

    goal_node = Node(end, None)
    goal_node.h = heuristics[end]


    if not open_list:
        print("Failure")
        return path
    else:
        while open_list:
            open_list.sort(key=lambda x: x.g + x.h) #Evaluation Function
            #  open_list.sort()
            current_node = open_list.pop(0)
            if current_node.name not in closed:
                closed.append(current_node.name)

                # curr = min(open,key=lambda x:x.g + x.h)
                if current_node.name == goal_node.name:
                    while current_node.parent:
                        path.append(current_node)
                        current_node = current_node.parent
                    path.append(current_node)
                    print("Success")
                    return path[::-1]
                else:
                    # Get neighbours
                    neighbors = graph.get(current_node.name)
                    print(current_node)
                    #open_list.remove(current_node)
                    #closed.append(current_node)

                    for key, value in neighbors.items():
                        #print("Node ", key)
                        # Create a neighbor node
                        # key is the name, f is the value
                        neighbor = Node(key, current_node)
                        neighbor.h = heuristics[key]
                        neighbor.g = current_node.g + value
                        #neighbor.f = neighbor.h + neighbor.g

                        if neighbor.name not in closed:
                            neighbor.f = neighbor.h + neighbor.g

                            if In_Open(open_list, neighbor):
                                neighbor.parent = current_node
                                open_list.append(neighbor)


                # Everything is green, add neighbor to open list

    # Create a start node and an goal node

    # Add the start node

    # Loop until the open list is empty

    # Sort the open list to get the node with the lowest cost first

    # Get the node with the lowest cost

    # Add the current node to the closed list

    # Check if we have reached the goal, return the path (From Current Node to Start Node By Node.parent)

    # Return reversed path (Hint: Return Llist of path in this Fashion for Reverse return path[::-1])


# Return None, no path is found

# Check if a neighbor should be added to open list
def In_Open(open_nodes, neighbor):
    for node in open_nodes:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True


# The main entry point for this module
def main():
    # Create a graph
    graph = Graph()

    # Create graph connections (Actual distance)
    graph.connect('Arad', 'Zerind', 75)
    # Add Remaining Links From Example Given in Sides (Romania Map)
    graph.connect('Fugaras', 'Bucharest', 211)
    graph.connect('Pitesti', 'Bucharest', 101)
    graph.connect('Giurgiu', 'Bucharest', 90)

    graph.connect('Arad', 'Timisoara', 118)
    graph.connect('Arad', 'Sibiu', 140)
    graph.connect('Zerind', 'Oradea', 71)
    graph.connect('Oradea', 'Sibiu', 151)
    graph.connect('Timisoara', 'Lugoj', 111)
    graph.connect('Lugoj', 'Mehadia', 70)
    graph.connect('Mehadia', 'Dobreta', 75)
    graph.connect('Dobreta', 'Craiova', 120)
    graph.connect('Craiova', 'Vilcea', 146)
    graph.connect('Craiova', 'Pitesti', 138)
    graph.connect('Sibiu', 'Fagaras', 99)
    graph.connect('Sibiu', 'Vilcea', 80)
    graph.connect('Vilcea', 'Pitesti', 97)

    graph.connect('Bucharest', 'Urziceni', 85)
    graph.connect('Urziceni', 'Hirsova', 98)
    graph.connect('Hirsova', 'Etorie', 85)
    graph.connect('Urziceni', 'Vaslui', 142)
    graph.connect('Vaslui', 'Iasi', 92)
    graph.connect('Iasi', 'Neamt', 87)

    # Make graph undirected, create symmetric connections
    graph.make_undirected()

    # Create heuristics (straight-line distance, air-travel distance) for Destination Bucharest
    heuristics = {}
    heuristics['Arad'] = 366
    # Add Remaining Heuristics From Example Given in Sides (Romania Map)
    heuristics['Bucharest'] = 0
    heuristics['Craiova'] = 160
    heuristics['Dobreta'] = 242
    heuristics['Eforie'] = 161
    heuristics['Fagaras'] = 176
    heuristics['Giurgiu'] = 77
    heuristics['Hirsova'] = 151
    heuristics['Iasi'] = 226
    heuristics['Lugoj'] = 244
    heuristics['Mehadia'] = 241
    heuristics['Neamt'] = 234
    heuristics['Oradea'] = 380
    heuristics['Pitesti'] = 100
    heuristics['Vilcea'] = 193
    heuristics['Sibiu'] = 253
    heuristics['Timisoara'] = 329
    heuristics['Urziceni'] = 80
    heuristics['Vaslui'] = 199
    heuristics['Zerind'] = 374

    # Print Graph Nodes
    print(graph.nodes())
    print('\n')

    # Run search algorithm
    path = A_Star(graph, heuristics, 'Arad', 'Bucharest')
    print('Paths')
    print(path)


# Tell python to run main method
if __name__ == "__main__": main()
