import pyxel



class ClearScene:

    def __init__(self,game):
        self.game = game


    def start(self):

        pyxel.stop()
        pyxel.playm(0, loop=True)


    def update(self):
        pass


    def draw(self):

        pyxel.cls(0)


        self.game.draw_field()
        self.game.draw_player()
        self.game.draw_enemies()


        pyxel.rect(6, 49, 116, 30, 0)
        pyxel.rectb(6, 49, 116, 30, 7)
        pyxel.text(19, 57, "YOU ESCAPED THE CAVERN!", 7)
        pyxel.text(17, 66, "BUT YOUR QUEST CONTINUES", 7)






