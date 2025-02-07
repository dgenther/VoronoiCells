from vec import vec2
from random import randint, choice, choices

COLORS = ['green', 'red', 'cyan', 'yellow']

class Cell:
		def __init__(self, pos: vec2):
			self.pos = pos
			self.color: str = 'black'

class Voronoi:
	RESOLUTION: vec2
	def __init__(self, num_cells: int, resolution: vec2):
		global RESOLUTION
		self.num_cells: int = num_cells
		self.cells: list[Cell] = []
		RESOLUTION = resolution
		

	def add_cell(pos:vec2 = None):
		cell: Cell

		if not pos:
			pos_x = randint(0, RESOLUTION.x)
			pos_y = randint(0, RESOLUTION.y)
			pos = vec2((pos_x, pos_y))

		cell = Cell(pos)

	def draw(self):
		cell: Cell
		for cell in self.cells:
			if cell:
				pass
