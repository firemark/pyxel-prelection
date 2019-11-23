#!/usr/bin/env python3
import pyxel


class Player:
    WIDTH_SPRITE = 32
    HEIGHT_SPRITE = 32

    ROTATE_INDEXES = {
        'u': 0,
        'l': 1,
        'd': 2,
        'r': 3,
    }

    def __init__(self, cords):
        self.score = 0
        self.cords = cords
        self.rotate = 'u'

    def draw(self):
        x, y = self.cords
        w = self.WIDTH_SPRITE
        h = self.HEIGHT_SPRITE
        u = self.ROTATE_INDEXES[self.rotate] * w
        pyxel.blt(x, y, 0, u, 0, w, h, 11)

    def move_up(self):
        self.cords[1] -= 10
        self.rotate = 'u'

    def move_down(self):
        self.cords[1] += 10
        self.rotate = 'd'

    def move_left(self):
        self.cords[0] -= 10
        self.rotate = 'l'

    def move_right(self):
        self.cords[0] += 10
        self.rotate = 'r'


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
