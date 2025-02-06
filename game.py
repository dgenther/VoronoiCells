import pygame as pg
from voronoi import Voronoi

resolution = (1920, 1080)

class Game:
    def __init__(self):
        self.display = pg.display.set_mode(resolution)
        self.clock = pg.time.Clock()
        self.tick_rate = 60
        self.is_running = True

        self.voronoi = Voronoi(1, resolution=resolution)

    def draw(self):
        pass

    def run_game_loop(self):
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.is_running = False
                    pg.quit()
                    quit()

            self.draw()

            pg.display.update()
            self.clock.tick(self.tick_rate)