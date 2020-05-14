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
		self.face_buttons = []
		self.rotation_buttons = []
		self.action_button = None
		self.face_label = None
		self.rotation_label = None
		self.face = 0
		self.rotation = 0
		self.setup_graphics()

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
			widget.config(height=4, width=16, relief='flat', fg='black', bg='white')

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

	# Print the cube
	def print_cube(self):
		pass

	# Activate the main loop
	def mainloop(self):
		self.root.mainloop()


if __name__ == "__main__":

	display = Display()
	display.mainloop()
