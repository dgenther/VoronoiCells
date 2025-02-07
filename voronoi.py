from vec import vec2
from random import randint, choice, choices
import pygame as pg

COLORS = ['green', 'red', 'cyan', 'yellow']
POINT_RADIUS = 10

class Cell:
		def __init__(self, pos: vec2):
			self.pos = pos
			self.color: str = 'black'

class Voronoi:
	RESOLUTION: vec2
	def __init__(self, num_cells: int, resolution: vec2):
		self.resolution = resolution
		self.cells: list[Cell] = []

		for _ in range(num_cells):
			self.add_cell()
		

	def add_cell(self, pos:vec2 = None):
		cell: Cell

		if not pos:
			pos_x = randint(0, self.resolution.x)
			pos_y = randint(0, self.resolution.y)
			pos = vec2((pos_x, pos_y))

		cell = Cell(pos)
		self.cells.append(cell)

	def draw(self, display: pg.display):
		for i, cell in enumerate(self.cells):
			if cell:
				pg.draw.circle(display, 'black', cell.pos(), POINT_RADIUS)
				
