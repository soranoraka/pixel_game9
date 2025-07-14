import pyxel
from collision import get_tile_type, in_collision, push_back
from constants import TILE_EXIT, TILE_GEM, TILE_LAVA, TILE_MUSHROOM, TILE_SPIKE



class Player:

    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.direction = 1
        self.jump_counter = 0


    def update(self):

        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(
            pyxel.GAMEPAD1_BUTTON_DPAD_LEFT
        ):
            self.dx = -2
            self.direction = -1

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(
            pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT
        ):
            self.dx = 2
            self.direction = 1


        if self.jump_counter > 0:
            self.jump_counter -= 1
        else:
            self.dy = min(self.dy + 1, 4)


        for i in [1, 6]:
            for j in [1, 6]:
                x = self.x + j
                y = self.y + i
                tile_type = get_tile_type(x, y)

                if tile_type == TILE_GEM:

                    self.game.score += 10


                    pyxel.tilemaps[0].pset(x // 8, y// 8, (0,0))

                    pyxel.play(3, 1)


                if self.dy >= 0 and tile_type == TILE_MUSHROOM:

                    self.dy = -6
                    self.jump_counter = 6


                    pyxel.play(3, 2)

                if tile_type == TILE_EXIT:
                    self.game.change_scene("clear")
                    return
                
                if tile_type in [TILE_SPIKE, TILE_LAVA]:
                    self.game.change_scene("gameover")
                    return
                

        if(
            self.dy >= 0
            and(
                in_collision(self.x, self.y + 8) or in_collision(self.x + 7, self.y +8)
            )
            and(pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B))
        ):
            

            self.dy = -6
            self.jump_counter = 2
            pyxel.play(3, 0)


        self.x, self.y = push_back(self.x, self.y, self.dx, self.dy)


        self.dx = int(self.dx * 0.8)


    def draw(self):

        u = pyxel.frame_count // 4 % 2 * 8 + 8



        w = 8 if self.direction > 0 else -8


        pyxel.blt(self.x, self.y, 0, u, 64, w, 8, 15)
