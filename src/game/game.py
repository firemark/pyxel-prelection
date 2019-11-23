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

    def move_up(self):
        self.cords[1] -= 10

    def move_down(self):
        self.cords[1] += 10

    def move_left(self):
        self.cords[0] -= 10

    def move_right(self):
        self.cords[0] += 10


class App:

    def run(self):
        pyxel.run(self.update, self.draw)

    def setup(self):
        pyxel.init(256, 256, title="SPACESHIP OMG!!!")
        pyxel.image(0).load(0, 0, "assets.png")

        self.player = Player([128, 128])

    def update(self):
        self.keyboard()

    def keyboard(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_UP):
            self.player.move_up()
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.player.move_down()
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.player.move_left()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.player.move_right()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, "Score: %d" % self.player.score, 7)
        self.player.draw()
