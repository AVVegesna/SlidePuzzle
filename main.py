from heuristic import Heuristic
from neighbours import Neighbour
from node import Node
import heapq


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]  # Reverse the path


def a_star(initial_state, goal_state):
    # Initialize the priority queue and visited set
    start_node = Node(state=initial_state, cost=0, heuristic=Heuristic(initial_state).score)
    frontier = []
    heapq.heappush(frontier, start_node)
    visited = set()

    while frontier:
        current_node = heapq.heappop(frontier)

        # Check if the goal state is reached
        if current_node.state == goal_state:
            return reconstruct_path(current_node)

        # Add current state to visited
        visited.add(tuple(map(tuple, current_node.state)))

        # Expand neighbors
        neighbor_instance = Neighbour(current_node.state)
        for neighbor in neighbor_instance.possible_moves():
            if tuple(map(tuple, neighbor)) not in visited:
                g = current_node.cost + 1  # Increment the cost
                h = Heuristic(neighbor).score  # Heuristic
                neighbor_node = Node(state=neighbor, parent=current_node, cost=g, heuristic=h)
                heapq.heappush(frontier, neighbor_node)

    return None  # No solution found


if __name__ == "__main__":
    initial_state = [
        [2, 3, 6],
        [5, 7, 4],
        [0, 1, 8]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solution_path = a_star(initial_state, goal_state)

    if solution_path:
        print("Solution Found!")
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            for row in state:
                print(row)
            print()
    else:
        print("No solution exists.")
