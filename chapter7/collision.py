

import pyxel
from constants import TILE_NONE, TILE_TO_TILETYPE,TILE_WALL



def get_tile_type(x, y):
    tile = pyxel.tilemaps[0].pget(x // 8, y // 8)
    return TILE_TO_TILETYPE.get(tile, TILE_NONE)



def in_collision(x, y):
    return get_tile_type(x, y) == TILE_WALL



def is_character_colliding(x, y):

    x1 = pyxel.floor(x) // 8
    y1 = pyxel.floor(y) // 8
    x2 = (pyxel.ceil(x) + 7) // 8
    y2 = (pyxel.ceil(y) + 7) // 8


    for yi in range(y1, y2 + 1):
        for xi in range(x1, x2 + 1):
            if in_collision(xi * 8, yi * 8):
                return True
            
    return False



def push_back(x, y, dx, dy):

    for _ in range(pyxel.ceil(abs(dy))):
        step = max(-1, min(1, dy))
        if is_character_colliding(x, y + step):
            break
        y += step
        dy -= step


    for _ in range(pyxel.ceil(abs(dx))):
        step = max(-1, min(1, dx))
        if is_character_colliding(x + step, y):
            break
        x += step
        dx -= step

    return x, y 



