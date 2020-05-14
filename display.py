from tkinter import *
from cube import Cube


class Display:

	# Constructor
	def __init__(self):

		# Create the tkinter window
		self.root = Tk()

		# Create a cube instance
		self.cube = Cube()

		# Setup all of the tkinter elements
		self.frames = []
		self.face_radios = []
		self.rot_radios = []
		self.button = None
		self.face = 0
		self.rotation = 0
		self.setup_graphics()

		# Print the cube
		self.print_cube()

	# Rotation command for the cube
	def rotate_cube(self):

		self.cube.apply_rotation(self.face, self.rotation)
		self.print_cube()

	# Create tkinter buttons and radios, frames, etc..
	def setup_graphics(self):

		# Setup the frames
		for _ in range(4):
			self.frames.append(Frame(self.root))
			self.frames[-1].pack()

		# Setup face radios
		for i in range(6):
			self.face_radios.append(Radiobutton(self.frames[1], text=str(i), variable=self.face, value=i))
			self.face_radios[-1].pack()

		# Setup rotation radios
		for i in range(3):
			self.rot_radios.append(Radiobutton(self.frames[2], text=str(i), variable=self.rotation, value=i))
			self.rot_radios[-1].pack()

		# Setup rotate button
		self.button = Button(self.frames[3], text="Rotate!", command=self.rotate_cube()).pack()

	# Print the cube
	def print_cube(self):
		pass

	# Activate the main loop
	def mainloop(self):
		self.root.mainloop()


if __name__ == "__main__":

	display = Display()
	display.mainloop()
