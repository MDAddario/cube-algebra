import numpy as np
from copy import deepcopy


class Cube:

    # Order of the colored faces on the cube
    color_order = ['W', 'R', 'G', 'Y', 'O', 'B']

    # Constructor
    def __init__(self):

        # Construct representation of tiles
        self.tiles = np.identity(6 * 8)

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

        # Return the grand prize
        return output


if __name__ == "__main__":

    yan3 = Cube()
    print(yan3)
