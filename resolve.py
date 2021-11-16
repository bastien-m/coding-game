class Node:
    def __init__(self, value, parent = None, children = None):
        self.value = value
        self.parent = parent
        self.children = children or []

def resolve(cars):
    train = []
    graph = Node(None) # first node of the graph
    while len(cars) > 0:
        current_car = cars.pop(0) # get the first train
        first_node = graph
        possible_leaf = [first_node]
        # browse graph using deep path
        to_browse = graph.children
        if len(to_browse) > 0:
            


    