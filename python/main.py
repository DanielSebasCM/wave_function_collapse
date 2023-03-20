import pygame as pg
from config import *
from Tile import Tile
from Grid import WFC


def draw_tiles_test():
    screen.fill((50, 50, 50))
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            index = j * DIM + i
            x = i * CELL_SIZE
            y = j * CELL_SIZE
            if index < len(tiles):
                screen.blit(tiles[index].img, (x, y))


def possible_tile_variations(tiles):
    new_tiles = []
    for tile in tiles:
        if tile.rotations == 1:
            new_tiles.append(tile.copy())
        elif tile.rotations == 4:
            for i in range(4):
                new_tiles.append(tile.copy().rotate(i))
        else:
            new_tiles.append(tile.copy())
            new_tiles.append(tile.copy().rotate(2))

    return new_tiles


pg.init()
screen = pg.display.set_mode((SIZE, SIZE))
clock = pg.time.Clock()

original_tiles = [
    Tile("Tiles/simple/corner.png", [1, 1, 0, 0], 4),
    Tile("Tiles/simple/cross.png", [1, 1, 1, 1]),
    Tile("Tiles/simple/empty.png", [0, 0, 0, 0]),
    Tile("Tiles/simple/straight.png", [0, 1, 0, 1], 2),
    Tile("Tiles/simple/t.png", [1, 1, 0, 1], 4)
]

tiles = possible_tile_variations(original_tiles)

grid = WFC(DIM, DIM, tiles, screen)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    if not grid.is_solved():
        min_cell = grid.lowest_entropy_cell()
        grid.collapse_cell(*min_cell)
        grid.draw()
    # clock.tick(FPS)

    pg.display.update()
