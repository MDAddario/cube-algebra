from tkinter import *
from cube import Cube
from copy import deepcopy
import numpy as np


class Display:

	# Constructor
	def __init__(self):

		# Create the tkinter window
		self.root = Tk()

		# Create a cube instance
		self.cube = Cube()

		# Setup all of the tkinter elements
		self.frames = []
		self.face_buttons = []
		self.rotation_buttons = []
		self.action_button = None
		self.face_label = None
		self.rotation_label = None
		self.face = 0
		self.rotation = 0
		self.setup_graphics()

		# Setup the cube printing elements
		self.cube_grid = []
		self.setup_grid()

		# Print the cube
		self.print_cube()

	# Rotation command for the cube
	def rotate_cube(self):

		self.cube.apply_rotation(self.face, self.rotation)
		self.print_cube()

	def set_face(self, index):
		self.face = index
		self.face_label.config(text=self.cube.color_order[index])

	def set_rot(self, index):
		self.rotation = index
		self.rotation_label.config(text=self.cube.rotations[index])

	@staticmethod
	def widget_config(widget, alt=False):
		if not alt:
			widget.config(height=4, width=16, relief='raised', fg='white', bg='black')
		else:
			widget.config(height=4, width=8, relief='flat', fg='black', bg='grey')

	# Create tkinter buttons and radios, frames, etc..
	def setup_graphics(self):

		# Setup the frames
		for _ in range(5):
			self.frames.append(Frame(self.root))
			self.frames[-1].pack()

		# Setup face buttons
		for i in range(6):
			self.face_buttons.append(Button(self.frames[1], text=self.cube.color_order[i], command=lambda i=i: self.set_face(i)))
			self.face_buttons[-1].pack(side=LEFT)
			Display.widget_config(self.face_buttons[-1])

		# Setup rotation radios
		for i in range(3):
			self.rotation_buttons.append(Button(self.frames[2], text=self.cube.rotations[i], command=lambda i=i: self.set_rot(i)))
			self.rotation_buttons[-1].pack(side=LEFT)
			Display.widget_config(self.rotation_buttons[-1])

		# Setup labels
		self.face_label = Label(self.frames[3], text=self.cube.color_order[self.face])
		self.face_label.pack(side=LEFT)
		Display.widget_config(self.face_label, alt=True)
		self.rotation_label = Label(self.frames[3], text=self.cube.rotations[self.rotation])
		self.rotation_label.pack(side=LEFT)
		Display.widget_config(self.rotation_label, alt=True)

		# Setup rotate button
		self.action_button = Button(self.frames[4], text="Rotate!", command=self.rotate_cube)
		self.action_button.pack()
		Display.widget_config(self.action_button)

	# Setup the cube grid
	def setup_grid(self):

		# Allocate room for the grid
		for i in range(9):
			self.cube_grid.append([])
			for j in range(12):
				self.cube_grid[-1].append(None)

		# Create the label objects
		for i in range(9):
			for j in range(12):

				# Create new label
				self.cube_grid[i][j] = Label(self.frames[0], bg="grey")
				self.cube_grid[i][j].grid(row=i, column=j)
				Display.widget_config(self.cube_grid[i][j], alt=True)

		# Color the centers
		self.cube_grid[4][4].config(bg="white")
		self.cube_grid[4][7].config(bg="red")
		self.cube_grid[7][4].config(bg="green")
		self.cube_grid[4][10].config(bg="yellow")
		self.cube_grid[4][1].config(bg="orange")
		self.cube_grid[1][4].config(bg="blue")

	# Color a face
	def color_face(self, face, rotation, i_start, j_start):

		color_map = ["white", "red", "green", "yellow", "orange", "blue"]

		# Create duplicate cube
		temp = deepcopy(self.cube)

		# Rotate face if necessary
		if rotation != -1:
			temp.apply_rotation(face, rotation)

		# Span all columns
		# TODO: MAYBE WE NEED TO SPAN THE ROWS
		colors = []
		for col in range(face * 8, face * 8 + 8):
			color_code = np.argmax(self.cube.tiles[:, col])
			colors.append(color_map[color_code // 8])

		# Paint the cube
		ptr = 0
		for i in range(3):
			for j in range(3):

				if i == 1 and j == 1:
					continue

				self.cube_grid[i + i_start][j + j_start].config(bg=colors[ptr])
				ptr += 1

		# Clear the cube
		del temp

	# Print the cube
	def print_cube(self):

		# Color the faces
		self.color_face(0, 0, 3, 3)
		self.color_face(1, 1, 3, 6)
		self.color_face(2, -1, 6, 3)
		self.color_face(3, -1, 3, 9)
		self.color_face(4, 2, 3, 0)
		self.color_face(5, 2, 0, 3)

	# Activate the main loop
	def mainloop(self):
		self.root.mainloop()


if __name__ == "__main__":

	display = Display()
	display.mainloop()
