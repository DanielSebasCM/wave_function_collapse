from Cell import Cell
from config import *
import math
import random


directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


class WFC:
    __slots__ = "width", "height", "tiles", "grid", "screen", "collapsed"

    def __init__(self, width, height, options, screen) -> None:
        self.width = width
        self.height = height
        self.tiles = options
        self.grid = [[Cell(range(len(options))) for _ in range(height)]
                     for _ in range(width)]
        self.screen = screen
        self.collapsed = 0

    def draw(self):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                x = i * CELL_SIZE
                y = j * CELL_SIZE
                if len(cell.options) < len(self.tiles):
                    cell.draw(self.screen, self.tiles, x, y)

    def lowest_entropy_cell(self):
        min_entropy = math.inf
        min_positions = []
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if not cell.collapsed:
                    entropy = len(cell.options)
                    if entropy == min_entropy:
                        min_positions.append((i, j))

                    if entropy < min_entropy:
                        min_entropy = entropy
                        min_positions = [(i, j)]

        min_pos = random.choice(min_positions)

        return min_pos

    def collapse_cell(self, x, y):
        cell = self.grid[x][y]
        cell.collapsed = True
        cell.options = [random.choice(cell.options)]

        tile = self.tiles[cell.options[0]]

        for i, (dx, dy) in enumerate(directions):
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                neighbor = self.grid[new_x][new_y]
                if not neighbor.collapsed:
                    new_options = list(filter(lambda o: tile.connects(
                        self.tiles[o], i), neighbor.options))
                    neighbor.options = new_options
        self.collapsed += 1

    def is_solved(self):
        return self.collapsed == self.width * self.height
