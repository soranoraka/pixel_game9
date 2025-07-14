import pyxel
from collision import get_tile_type
from constants import (
    SCROLL_BORDER_X,
    TILE_FLOWER_POINT,
    TILE_MUMMY_POINT,
    TILE_SLIME1_POINT,
    TILE_SLIME2_POINT,
)
from entities import Flower, Mummy, Player, Slime



class PlayScene:

    def __init__(self, game):
        self.game = game


    def start(self):

        pyxel.tilemaps[0].blt(0, 0, 2, 0, 0, 256, 16)


        game = self.game
        game.player = Player(game, 0, 0)
        game.screen_x = 0
        game.score = 0


        self.spawn_enemy(0, 127)


        pyxel.stop()
        pyxel.playm(1, loop=True)


    def spawn_enemy(self, left_x, right_x):
        game = self.game
        enemies = game.enemies


        left_x = pyxel.ceil(left_x / 8)
        right_x = pyxel.floor(right_x / 8)


        for tx in range(left_x, right_x + 1):
            for ty in range(16):
                x = tx * 8
                y = ty * 8
                tile_type = get_tile_type(x, y)

                if tile_type == TILE_SLIME1_POINT:
                    enemies.append(Slime(game, x, y, False))
                elif tile_type == TILE_SLIME2_POINT:
                    enemies.append(Slime(game, x, y, True))
                elif tile_type == TILE_MUMMY_POINT:
                    enemies.append(Mummy(game, x, y))
                elif tile_type == TILE_FLOWER_POINT:
                    enemies.append(Flower(game, x, y))
                else:
                    continue




                pyxel.tilemaps[0].pset(tx, ty, (0, 0))


    def update(self):
        game = self.game
        player = game.player
        enemies = game.enemies


        if player is not None:
            player.update()


        player.x = min(max(player.x, game.screen_x), 2040)
        player.y = max(player.y, 0)


        if player.x > game.screen_x + SCROLL_BORDER_X:
            last_screen_x = game.screen_x
            game.screen_x = min(player.x - SCROLL_BORDER_X, 240 * 8)



            self.spawn_enemy(last_screen_x + 128, game.screen_x + 127)


        if player.y >= pyxel.height:
            pyxel.play(3, 4)
            game.change_scene("gameover")


        for enemy in enemies.copy():
            enemy.update()


            if abs(player.x - enemy.x) < 6 and abs(player.y - enemy.y) < 6:
                game.change_scene("gameover")
                return


            if(
                enemy.x < game.screen_x - 8
                or enemy.x > game.screen_x + 160
                or enemy.y > 160
            ):
                if enemy in enemies:
                    enemies.remove(enemy)



    def draw(self):

        pyxel.cls(0)


        self.game.draw_field()


        self.game.draw_player()


        self.game.draw_enemies()

