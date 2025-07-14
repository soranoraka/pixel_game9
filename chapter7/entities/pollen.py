import pyxel



class Pollen:

    def __init__(self, game, x, y, dx, dy):
        self.game = game
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy


    def update(self):

        self.x += self.dx
        self.y += self.dy


    def draw(self):

        u = pyxel.frame_count % 2 * 8 + 8


        pyxel.blt(self.x, self.y, 0, u, 104, 8, 8, 15)

            