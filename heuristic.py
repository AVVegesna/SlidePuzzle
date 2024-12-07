class Heuristic:
    def __init__(self, state):
        self.goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        self.score = self.calculate_heuristic(state)

    def calculate_heuristic(self, state):
        manhattan_distance = 0
        for state_row in range(len(state)):
            for state_col in range(len(state[state_row])):
                state_number = state[state_row][state_col]
                if state_number != 0:  
                    goal_row = (state_number - 1) // 3
                    goal_col = (state_number - 1) % 3
                    manhattan_distance += abs(goal_row - state_row) + abs(goal_col - state_col)
        return manhattan_distance


# Example usage
if __name__ == "__main__":
    # Define a current puzzle state
    current_state = [
        [1, 8, 3],
        [4, 5, 6],
        [7, 2, 0]
    ]

    # Create an instance of the heuristic calculator
    heuristic_calculator = Heuristic(current_state)

    # Print the heuristic score
    print("Heuristic Score (Manhattan Distance):", heuristic_calculator.score)
