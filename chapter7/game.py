import pyxel
from scenes import ClearScene, GameOverScene, PlayScene, TitleScene



class Game:

    def __init__(self):

        pyxel.init(128, 128, title="Cursed Caverns")


        pyxel.load("assets/cursed_caverns.pyxres")
        pyxel.tilemaps[2].blt(0, 0, 0, 0, 0, 256, 16)


        self.player = None
        self.enemies = []
        self.scenes = {
            "title": TitleScene(self),
            "play": PlayScene(self),
            "gameover": GameOverScene(self),
            "clear": ClearScene(self),
        }
        self.scene_name = None
        self.screen_x = 0
        self.score = 0


        self.change_scene("title")


        pyxel.run(self.update, self.draw)


    def change_scene(self, scene_name):
        self.scene_name = scene_name
        self.scenes[self.scene_name].start()


    def draw_field(self):
        pyxel.bltm(0, 0, 0, self.screen_x, 0, 128, 128)


    def draw_player(self):
        
        pyxel.camera(self.screen_x, 0)


        if self.player is not None:
            self.player.draw()


        pyxel.camera()

    
    def draw_enemies(self):

        pyxel.camera(self.screen_x, 0)


        for enemy in self.enemies:
            enemy.draw()


        pyxel.camera()


    def update(self):

        self.scenes[self.scene_name].update()


    def draw(self):

        self.scenes[self.scene_name].draw()


        pyxel.text(45, 4, f"SCORE {self.score:4}", 7)




