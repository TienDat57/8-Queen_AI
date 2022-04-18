from queue import PriorityQueue

def Astar(problem):
    frontier = PriorityQueue()
    expanded = []
    path = []

    frontier.put(problem[0])
