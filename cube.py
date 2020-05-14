from copy import deepcopy
from typing import List

import numpy as np


class Rotation:

    @staticmethod
    def create_matrix(size: int, indices_list: List[list]) -> np.ndarray:

        # Allocate rotation matrix
        output = np.zeros((size, size), dtype=int)

        # Set off diagonal values for each list of indices
        for indices in indices_list:
            length = len(indices)

            for i in range(length):

                index_1 = indices[i]
                index_2 = indices[(i + 1) % length]

                output[index_1, index_2] = 1    # TODO: THE TRANSPOSITION MIGHT BE CORRECT HERE PLEASE CHECK

        # Set on diagonal values
        for i in range(size):

            for indices in indices_list:
                if i in indices:
                    break
            else:
                output[i, i] = 1

        return output


class Cube:

    # Order of the colored faces on the cube
    color_order = ['W', 'R', 'G', 'Y', 'O', 'B']

    # Number of mobile tiles
    size = 6 * 8

    # Constructor
    def __init__(self):

        # Construct representation of tiles
        self.tiles = np.identity(self.size, dtype=int)

        # Create ordered list of faces for rotation operations
        self.faces = []

        # Create opposite color ordering
        inverse_order = deepcopy(self.color_order)
        inverse_order.reverse()

        for i in range(6):

            new_faces = []

            # Top cycle
            if i < 3:

                for j in range(0, 3):
                    new_faces.append(self.color_order[(i + j) % 3])

                for j in range(1, 3):
                    new_faces.append(self.color_order[(i + j) % 3 + 3])

            # Bot cycle:
            else:

                i = 5 - i

                for j in range(0, 3):
                    new_faces.append(inverse_order[(i + j) % 3])

                for j in range(1, 3):
                    new_faces.append(inverse_order[(i + j) % 3 + 3])

            self.faces.append(new_faces)

    '''
    # Representation
    def __repr__(self):
        return "[---]"
    '''

    # To string
    def __str__(self):

        # Create dedicated output string
        output = "\n"

        # Append facial decomposition
        for i in range(6):
            output += f"Rotating color {self.color_order[i]} with faces {self.faces[i]}\n"

        # Append the tiles
        output += str(self.tiles)

        # Return the grand prize
        return output


if __name__ == "__main__":

    # Print the cube
    yan3 = Cube()
    print(yan3)

    # Print transformation matrix
    print(Rotation.create_matrix(8, [[1, 2, 7], [4, 5, 6, 3]]))
