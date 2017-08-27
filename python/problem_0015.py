"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

import numpy as np

class Grid(object):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def generate_matrix(self):
        ret_matrix = []
        for i in range(0, self.rows + 1):
            row = []
            for j in range(0, self.columns + 1):
                row.append([i, j])
            ret_matrix.append(row)
        return ret_matrix

    def get_valid_next_position(self, position):
        positions = []
        if position[0] + 1 <= self.rows:
            positions.append([position[0] + 1, position[1]])
        if position[1] + 1 <= self.columns:
            positions.append([position[0], position[1] + 1])
        return positions

    def get_valid_paths(self, current_position):
        valid_paths = []
        valid_positions = self.get_valid_next_position(current_position)
        if len(valid_positions) == 0:
            return current_position
        else:
            valid_path = []
            for i, vp in enumerate(valid_positions):
                valid_path.append(self.get_valid_paths(vp))
            valid_paths.append(valid_path)
        return valid_paths



if __name__ == "__main__":
    # TODO: Need to finish code
    g = Grid(2, 2)
    mat = g.generate_matrix()
    positions = g.get_valid_next_position([2, 2])
    paths = g.get_valid_paths([0, 0])
    print(paths)