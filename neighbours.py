
class Neighbour:
    def __init__(self, state):
        self.state = state
        self.moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        self.null_location = None

    def find_null_location(self):
        for row in range(len(self.state)):
            for col in range(len(self.state[row])):
                if self.state[row][col] == 0:
                    self.null_location = (row, col)
                    return

    def possible_moves(self):
        if self.null_location is None:
            self.find_null_location()

        list_of_moves = []
        blank_row, blank_col = self.null_location

        for direction, (row_offset, col_offset) in self.moves.items():
            new_row = blank_row + row_offset
            new_col = blank_col + col_offset
            if 0 <= new_row < len(self.state) and 0 <= new_col < len(self.state[0]):
                # Create a new state with the blank tile moved
                new_state = [row[:] for row in self.state]  # Deep copy of the state
                # Swap blank with the target tile
                new_state[blank_row][blank_col], new_state[new_row][new_col] = (
                    new_state[new_row][new_col],
                    new_state[blank_row][blank_col],
                )
                list_of_moves.append(new_state)
        return list_of_moves
