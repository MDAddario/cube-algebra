from cube import Cube


# Brute force search all scrambles
def brute_force(cube: Cube, max_ply: int, ply: int = 0, last_face: int = 0):

	# Check if cube is solved
	if cube.is_solved():
		print(f"Cube is solved after {ply} moves!")
		return

	# Terminate search
	if ply == max_ply:
		return

	# Rotate all faces
	for face in range(6):

		# Truncate search space based off last rotation
		if face != 0:

			# Avoid rotating same face twice
			if face == last_face:
				continue

			# When rotating opposite faces, set one allowed ordering
			if (face % 3 == last_face % 3) and face < 3:
				continue

			# Perform all types of rotations
			for rotation in range(3):

				# Rotate cube
				cube.apply_rotation(face, rotation)

				# Search new state
				brute_force(cube, max_ply, ply + 1, face)

				# Undo rotation
				cube.apply_inverse(face, rotation)


if __name__ == "__main__":

	# Create a fresh cube
	yan3 = Cube()

	# Perform the sexy move
	yan3.apply_rotation(1, 0)
	yan3.apply_rotation(0, 0)
	yan3.apply_rotation(1, 2)
	yan3.apply_rotation(0, 2)

	# Search for the solution
	max_ply = 4

	# Begin the search
	brute_force(yan3, max_ply)