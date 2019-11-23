#!/usr/bin/env python3
import pyxel


class Player:
    WIDTH_SPRITE = 32
    HEIGHT_SPRITE = 32

    def __init__(self, cords):
        self.score = 0
        self.cords = cords

    def draw(self):
        x, y = self.cords
        pyxel.blt(x, y, 0, 0, 0, self.WIDTH_SPRITE, self.HEIGHT_SPRITE)


class App:

    def run(self):
        pyxel.run(self.update, self.draw)

    def setup(self):
        pyxel.init(256, 256, caption="SPACESHIP OMG!!!", border_color=0)
        pyxel.image(0).load(0, 0, "assets.png")

        self.player = Player([128, 128])

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, "Score: %d" % self.player.score, 7)
        self.player.draw()


if __name__ == "__main__":
    app = App()
    app.setup()
    app.run()
