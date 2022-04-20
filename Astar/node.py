from Astar.state import State

class Node:
    def __init__(self, state: State, path_cost: int = 0, parent = None) -> None:
        self.state = state
        self.path_cost = path_cost
        self.parent = parent 

    def __lt__(self, node):
        return (self.path_cost < node.path_cost)
    def __mt__(self, node):
        return (self.path_cost > node.path_cost)
    def __eq__(self, node):
        return (self.path_cost == node.path_cost)