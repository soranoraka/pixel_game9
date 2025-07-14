import pyxel

from .pollen import Pollen



class Flower:

    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.fire_timer = 0


    def update(self):

        if self.fire_timer > 0:
            self.fire_timer -= 1
        else:
            dx = self.game.player.x - self.x
            dy = self.game.player.y - self.y
            sq_dist = dx * dx + dy * dy
            if sq_dist < 60**2:

                dist = pyxel.sqrt(sq_dist)
                self.game.enemies.append(
                    Pollen(self.game, self.x, self.y, dx /dist, dy / dist)
                )


                pyxel.play(2, 4, resume=True)


                self.fire_timer = 90


    def draw(self):

        u = pyxel.frame_count // 8 % 2 * 8 + 8



        pyxel.blt(self.x, self.y, 0, u, 96, 8, 8, 15)

