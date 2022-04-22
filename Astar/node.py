from Astar.state import State

class Node:
    def __init__(self, state: State, path_cost: int = 0, parent = None) -> None:
        self.state = state
        self.path_cost = path_cost
        self.parent = parent 
        self.s = set(self.state.queens)

    def __lt__(self, other):
        return (self.path_cost < other.path_cost)
    def __mt__(self, other):
        return (self.path_cost > other.path_cost)
    def __eq__(self, other):
        return self.s == other.s