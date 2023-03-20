import pygame as pg
from config import *


class Tile:
    def __init__(self, img, sides, rotations=1, x_flip=False, y_flip=False):

        if rotations not in [1, 2, 4]:
            raise Exception("Invalid number of rotations (1, 2, 4)")

        if type(img) == str:
            self.img = pg.transform.scale(
                pg.image.load(img), (CELL_SIZE, CELL_SIZE))
        else:
            self.img = img

        self.sides = sides
        self.rotations = rotations
        self.x_flip = x_flip
        self.y_flip = y_flip

    def copy(self):
        return Tile(self.img, self.sides)

    def rotate(self, n=1):
        if n == 0:
            return self

        self.sides = self.sides[n:] + self.sides[:n]
        self.img = pg.transform.rotate(self.img, 90 * n)

        return self

    def connects(self, tile, dir):
        return self.sides[dir] == tile.sides[(dir + 2) % 4]
