import pyxel
from collision import in_collision, push_back



class Mummy:

    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.direction = 1


    def update(self):

        self.dx = self.direction
        self.dy = min(self.dy + 1, 3)


        if in_collision(self.x, self.y + 8) or in_collision(
            self.x + 7, self.y + 8
        ):
            if self.direction < 0 and(
                in_collision(self.x - 1, self.y + 4)
                or not in_collision(self.x - 1, self.y + 8)
            ):
                self.direction = 1
            elif self.direction > 0 and (
                in_collision(self.x + 8, self.y + 4)
                or not in_collision(self.x + 8, self.y + 8)
            ):
                self.direction = -1
        
        
        self.x, self.y = push_back(self.x, self.y, self.dx, self.dy)


    def draw(self):

        u = pyxel.frame_count // 4 % 2 * 8 + 8


        w = 8 if self.direction > 0 else -8



        pyxel.blt(self.x, self.y, 0, u, 88, w, 8, 15)
        

