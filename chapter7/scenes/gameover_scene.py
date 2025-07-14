import pyxel



class GameOverScene:

    def __init__(self, game):
        self.game = game


    def start(self):

        self.player_x = self.game.player.x
        self.player_y = self.game.player.y


        self.display_timer = 110


        pyxel.stop()
        pyxel.play(0, 3)


    def update(self):

        if self.display_timer > 0:
            self.display_timer -= 1
        else:
            self.game.change_scene("title")

    
    def draw(self):

        pyxel.cls(0)


        pyxel.camera()


        self.game.draw_field()


        self.game.draw_enemies()


        pyxel.camera(self.game.screen_x, 0)
        w = 8 if pyxel.frame_count // 2 % 2 == 0 else -8

        pyxel.blt(self.player_x, self.player_y, 0, 8, 64, w, 8, 15)
        pyxel.camera()


        pyxel.rect(6, 49, 116, 30, 0)
        pyxel.rectb(6, 49, 116, 30, 7)
        pyxel.text(47, 62, "GAME OVER", 7)
        