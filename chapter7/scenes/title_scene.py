import pyxel



class TitleScene:

    def __init__(self, game):
        self.game = game
        self.alpha = 0.0


    def start(self):

        self.alpha = 0.0


        self.game.player = None


        self.game.enemies = []


        pyxel.playm(0, loop=True)

    def update(self):

        if self.alpha < 1.0:
            self.alpha += 0.015


        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(
            pyxel.GAMEPAD1_BUTTON_B
        ):
            
            pyxel.dither(1.0)


            self.game.change_scene("play")

    def draw(self):

        pyxel.cls(0)


        pyxel.dither(self.alpha)
        pyxel.bltm(0, 0, 1, 0, 0, 128, 128)
        pyxel.blt(0, 0, 1, 0, 0, 128, 128, 0)


        pyxel.rect(30, 97, 67, 11, 0)
        pyxel.text(34, 100, "PRESS ENTER KEY", 7)