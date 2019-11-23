#!/usr/bin/env python3
import pyxel


class App:

    def run(self):
        pyxel.run(self.update, self.draw)

    def setup(self):
        pyxel.init(256, 256, title="SPACESHIP OMG!!!")
        pyxel.image(0).load(0, 0, "assets.png")

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        #pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(64, 64, 0, 0, 0, 32, 32)
        pyxel.blt(64, 128, 0, 32, 32, 32, 32)
        pyxel.blt(128, 128, 0, 64, 64, 32, 32)
