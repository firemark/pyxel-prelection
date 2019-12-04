#!/usr/bin/env python3
import pyxel
from math import sin, cos

class App:

    def run(self):
        pyxel.run(self.update, self.draw)

    def setup(self):
        pyxel.init(256, 128)
        pyxel.image(0).load(0, 0, "assets.png")
        self.x = 160
        self.y = 48
        self.u = 32
        self.v = 32

    def update(self):
        x_prim = sin(pyxel.frame_count / 30) * 32
        y_prim = cos(pyxel.frame_count / 30) * 32
        self.x = 160 + x_prim
        self.y = 48 + y_prim

        if pyxel.btnp(pyxel.KEY_LEFT):
            self.u -= 8
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.u += 8
        if pyxel.btnp(pyxel.KEY_UP):
            self.v -= 8
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.v += 8

    def draw(self):
        pyxel.cls(1)
        x = self.x
        y = self.y
        u = self.u
        v = self.v
        w, h = 32, 32

        # background
        pyxel.blt(0, 0, 0, 0, 0, 32 * 4, 32 * 4, 11)

        # info background
        pyxel.rectb(u, v, w, h, 10)
        pyxel.text(u - 16, v - 8, '(U,V)', 10)
        pyxel.text(u + w // 2 - 2, v + h + 2, 'W', 10)
        pyxel.text(u + w + 2, v + h // 2 - 2, 'H', 10)

        # sprite
        pyxel.blt(x, y, 0, u, v, w, h, 11)

        # info sprite
        pyxel.rectb(x, y, w, h, 8)
        pyxel.text(x - 16, y - 8, '(X,Y)', 8)
        pyxel.text(x + w // 2 - 2, y + h + 2, 'W', 8)
        pyxel.text(x + w + 2, y + h // 2 - 2, 'H', 8)

        # function
        pyxel.text(128, 120, 'pyxel.blt(X, Y, U, V, W, H, COL)', 7)

if __name__ == "__main__":
    app = App()
    app.setup()
    app.run()
