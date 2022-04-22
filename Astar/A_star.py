from Astar.node import Node
from Astar.state import State
from CNF.solve_CNF import CNF
from queue import PriorityQueue

class astar:
    def __init__(self, size: int = 0, initQueens: list = []) -> None:
        self.size = size
        self.initState = State(initQueens)

    def frontier(self, root: Node) -> list:
        frontier_list = []

        if len(root.state.queens) == self.size:
            return frontier_list

        root.state.init_board(self.size)

        for row in range(self.size):
            for col in range(self.size):
                if (CNF.get_pos(col, row)) not in root.state.queens:
                    queens = root.state.queens.copy()
                    queens.append(CNF.get_pos(col, row))
                    state = State(queens)
                    pathCost = self.cost_function(
                        root.state, state) + root.path_cost
                    childNode = Node(state, pathCost, root)
                    frontier_list.append(childNode)

        return frontier_list

    def is_goal(self, state: State):
        if len(state.queens) != self.size:
            return False
        for i in range(len(state.queens)):         
            for j in range(i + 1, len(state.queens)):
                if self.is_attack(state.queens[i], state.queens[j]):
                    return False
        return True

    def successor(self, node: Node) -> list:
        childs = []
        if len(node.state.queens) == self.size:
            return childs
        
        for row in range(self.size):
            for col in range(self.size):
                if (row * self.size + col + 1) not in node.state.queens:
                    queens = node.state.queens.copy()
                    queens.append(row * self.size + col + 1)
                    state = State(queens)
                    path_cost = self.cost_function() + node.path_cost + self.heuristic(state)
                    childNode = Node(state, path_cost, node)
                    childs.append(childNode)
        return childs
        
    def cost_function(self):
        return 1

    def evaluation(self, node: Node):
        return node.path_cost + self.heuristic(node.state)

    def heuristic(self, state: State):
        num_queen_attack = 0
        for i in range(len(state.queens)):
            for j in range(i + 1, len(state.queens)):
                if self.is_attack(state.queens[i], state.queens[j]):
                    num_queen_attack += 1
        return num_queen_attack + self.size - len(state.queens)

    def solve_astar(self):
        frontier = PriorityQueue()
        expanded = []
        path = []
        current = Node(self.initState)
        if self.is_goal(current.state):
            return current.state.queens, [current.state.queens]

        frontier.put((self.evaluation(current), current))
        
        while not frontier.empty():
            node = frontier.get()[1]
            state = node.state

            if state.queens not in expanded:
                expanded.append(state.queens)

            if self.is_goal(state):
                return state.queens, expanded

            childs = self.successor(node)

            for child in childs:
                state = child.state
                childVal = self.evaluation(child)

                if (child not in path):
                    path.append(child)
                    frontier.put((childVal, child)) 
        
        return [], []


    def is_attack(self, queen1: int, queen2: int):
        colQueen1 = (queen1 - 1) // 8
        rowQueen1 = (queen1 - 1) % 8
        colQueen2 = (queen2 - 1) // 8
        rowQueen2 = (queen2 - 1) % 8

        if rowQueen1 == rowQueen2:
            return True
        if colQueen1 == colQueen2:
            return True
        if (rowQueen1 + colQueen1) == (rowQueen2 + colQueen2): return True
        if (rowQueen1 - colQueen1) == (rowQueen2 - colQueen2): return True
        return False


