import pyxel
from collision import in_collision, push_back



class Slime:

    def __init__(self, game, x, y, is_elite):
        self.game = game
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.direction = -1
        self.is_elite = is_elite
        self.is_waiting = is_elite


    def update(self):
        if self.is_waiting:
            if(
                abs(self.game.player.x - self.x) >= 32
                or abs(self.game.player.y - self.y) >= 16
            ):
                return
            

            self.is_waiting = False
            self.direction = 1 if self.game.player.x > self.x else -1
            return
            
            
        self.dx = self.direction
        self.dy = min(self.dy + 1, 3)


        if self.direction < 0 and in_collision(
            self.x - 1, self.y + 4
        ):
            self.direction = 1
        elif self.direction > 0 and in_collision(
            self.x + 8, self.y + 4
        ):
            self.direction = -1


        self.x, self.y = push_back(self.x, self.y, self.dx, self.dy)


    def draw(self):

        u = pyxel.frame_count // 4 % 2 * 8 + 8



        if self.is_elite:
            pyxel.blt(self.x, self.y, 0, u, 80, 8, 8, 15)
        else:
            pyxel.blt(self.x, self.y, 0, u, 72, 8, 8, 15)
