from typing import List

import numpy as np

CW = 0
HF = 1
CCW = 2


class Rotation:

    @staticmethod
    def get_matrix(indices_list: List[List[int]]) -> np.ndarray:

        # Allocate rotation matrix
        output = np.zeros((48, 48), dtype=int)

        # Set off diagonal values for each list of indices
        for indices in indices_list:
            length = len(indices)

            for i in range(length):

                index_1 = indices[i]
                index_2 = indices[(i + 1) % length]

                output[index_1, index_2] = 1    # TODO: THE TRANSPOSITION MIGHT BE CORRECT HERE PLEASE CHECK

        # Set on diagonal values
        for i in range(48):

            for indices in indices_list:
                if i in indices:
                    break
            else:
                output[i, i] = 1

        return output

    @staticmethod
    def get_indices(face_1: int, face_2: int, face_3: int, face_4: int,
                    index_1: int, index_2: int, index_3: int, index_4: int,
                    rotation_type: int) -> List[List[int]]:

        if rotation_type == CW:       # Clockwise
            return [[face_1 * 6 + index_1, face_2 * 6 + index_2,   face_3 * 6 + index_3, face_4 * 6 + index_4]]
        elif rotation_type == HF:     # Half turn
            return [[face_1 * 6 + index_1, face_3 * 6 + index_3], [face_2 * 6 + index_2, face_4 * 6 + index_4]]
        elif rotation_type == CCW:    # Counter clockwise
            return [[face_4 * 6 + index_4, face_3 * 6 + index_3,   face_2 * 6 + index_2, face_1 * 6 + index_1]]
        else:
            raise ValueError("Rotation type invalid.")

    @staticmethod
    def from_faces(faces: List[int], rotation_type: int) -> np.ndarray:

        # Get ready to store some indices!
        indices_list = []

        # Rotate the front corners
        indices_list.extend(Rotation.get_indices(faces[0], faces[0], faces[0], faces[0],
                                                 0, 2, 7, 5, rotation_type))

        # Rotate the front edges
        indices_list.extend(Rotation.get_indices(faces[0], faces[0], faces[0], faces[0],
                                                 1, 4, 6, 3, rotation_type))

        # Rotate outside 'left' corners
        indices_list.extend(Rotation.get_indices(faces[1], faces[2], faces[3], faces[4],
                                                 7, 2, 5, 0, rotation_type))

        # Rotate outside edges
        indices_list.extend(Rotation.get_indices(faces[1], faces[2], faces[3], faces[4],
                                                 4, 1, 6, 3, rotation_type))

        # Rotate outside 'right' corners
        indices_list.extend(Rotation.get_indices(faces[1], faces[2], faces[3], faces[4],
                                                 2, 0, 7, 5, rotation_type))

        # Return rotation matrix
        return Rotation.get_matrix(indices_list)


class Cube:

    # Order of the colored faces on the cube
    color_order = ['W', 'R', 'G', 'Y', 'O', 'B']

    # Constructor
    def __init__(self):

        # Construct representation of tiles
        self.tiles = Rotation.get_matrix([[]])

        # Create ordered list of faces for rotation operations
        self.faces_list = []
        self.create_faces_list()

        # Create all of the possible rotation matrices
        self.rotations_list = []
        self.create_rotations_list()

    # Create the list of faces
    def create_faces_list(self):

        for i in range(0, 6):

            faces = []

            # Top cycle
            if i < 3:

                for j in range(0, 3):
                    faces.append((i + j) % 3)

                for j in range(1, 3):
                    faces.append((i + j) % 3 + 3)

            # Bot cycle:
            else:

                i = 5 - i

                for j in range(0, 3):
                    faces.append(5 - ((i + j) % 3))

                for j in range(1, 3):
                    faces.append(5 - ((i + j) % 3 + 3))

            self.faces_list.append(faces)

    # Create the list of rotations
    def create_rotations_list(self):

        for i in range(0, 6):
            rotations = []

            for rotation_type in range(0, 3):
                rotations.append(Rotation.from_faces(self.faces_list[i], rotation_type))

            self.rotations_list.append(rotations)

    # Apply rotation
    def apply_rotation(self, face_index: int, rotation_type: int):

        self.tiles = self.rotations_list[face_index][rotation_type] @ self.tiles    # TODO: MAYBE WRONG PLEASE CHECK

    # To string
    def __str__(self):

        # Create dedicated output string
        output = "\n"

        # Append facial decomposition
        for i in range(6):
            output += f"Rotating color {self.color_order[i]} with faces"

            for j in range(5):
                output += f" {self.color_order[self.faces_list[i][j]]}"

            output += "\n"

        # Return the grand prize
        return output


if __name__ == "__main__":

    # Print the cube
    yan3 = Cube()
    yan3.apply_rotation(0, CW)
