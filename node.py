
class Node:
    def __init__(self, state, parent = None, cost = 0, heuristic = 0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + self.heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost

