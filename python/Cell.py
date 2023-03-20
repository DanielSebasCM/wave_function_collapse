import Tile
import math
from config import *
import pygame as pg


class Cell:
    def __init__(self, options) -> None:
        self.options = options
        self.collapsed = False

    def draw(self, screen, tiles, x, y):
        if self.collapsed:
            tile = tiles[self.options[0]]
            screen.blit(tile.img, (x, y))
        # else:
        #     self.draw_options(screen, tiles, x, y)

    def draw_options(self, screen, tiles, x, y):
        pg.draw.rect(screen, 0x282c34, (x, y, CELL_SIZE, CELL_SIZE))
        dim = math.ceil(math.sqrt(len(self.options)))
        sub_tile_size = CELL_SIZE // dim
        sub_margin = sub_tile_size * MARGIN_FACTOR
        sub_draw_size = sub_tile_size - sub_margin * 2
        for i, option in enumerate(self.options):
            tile = tiles[option]
            sub_x = x + (i % dim) * sub_tile_size
            sub_y = y + (i // dim) * sub_tile_size
            thumbnail = pg.transform.scale(
                tile.img, (sub_draw_size, sub_draw_size))
            screen.blit(
                thumbnail, (sub_x + sub_margin, sub_y + sub_margin))
