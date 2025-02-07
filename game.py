import pygame as pg
from vec import vec2, get_vector
from voronoi import Voronoi, Cell, POINT_RADIUS

resolution = vec2((1200, 1200))

class Game:
    def __init__(self):
        self.display = pg.display.set_mode(resolution())
        self.clock = pg.time.Clock()
        self.tick_rate = 60
        self.is_running = True

        self.voronoi = Voronoi(2, resolution=resolution)

        self.left_click_pressed = False
        self.point_selected_idx: int = -1
        self.point_selected_offset: vec2 = vec2((0,0))
        self.added_cell_this_click = False

    def draw(self):
        self.display.fill(pg.Color(100, 100, 100))
        self.voronoi.draw(self.display)

    def run_game_loop(self):
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.is_running = False
                    pg.quit()
                    quit()
                elif event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0]:
                    self.left_click_pressed = True
                    mouse_pos = vec2(pg.mouse.get_pos())
                    cell: Cell
                    for i, cell in enumerate(self.voronoi.cells):
                        if get_vector(cell.pos, mouse_pos).magnitude() <= POINT_RADIUS:
                            self.point_selected_idx = i
                            self.point_selected_offset = get_vector(vec2(pg.mouse.get_pos()), self.voronoi.cells[i].pos)
                            break

                elif event.type == pg.MOUSEBUTTONUP and not pg.mouse.get_pressed()[0]:
                    self.left_click_pressed = False
                    self.point_selected_idx = -1
                    self.added_cell_this_click = False
            
            if self.left_click_pressed and self.point_selected_idx != -1:
                self.voronoi.cells[self.point_selected_idx].pos = vec2(pg.mouse.get_pos()) + self.point_selected_offset
            elif self.left_click_pressed and not self.added_cell_this_click:
                self.voronoi.add_cell(vec2(pg.mouse.get_pos()))
                self.added_cell_this_click = True




            self.draw()

            pg.display.update()
            self.clock.tick(self.tick_rate)