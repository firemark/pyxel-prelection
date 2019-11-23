#!/usr/bin/env python3
import pyxel
from copy import copy


class Bullet:

    def __init__(self, cords, rotate):
        self.cords = cords
        self.rotate = rotate

    @classmethod
    def from_player(cls, player):
        return cls(copy(player.cords), player.rotate)

    def update(self):
        if self.rotate == 'u':
            self.cords[1] -= 15
        elif self.rotate == 'd':
            self.cords[1] += 15
        elif self.rotate == 'l':
            self.cords[0] -= 15
        elif self.rotate == 'r':
            self.cords[0] += 15

    def is_alive(self):
        x, y = self.cords
        return (
            x > 0 and x < 256
            and y > 0 and y < 256
        )

    def draw(self):
        x, y = self.cords
        pyxel.circ(x, y, 2, 10)


class Ship:
    WIDTH_SPRITE = 32
    HEIGHT_SPRITE = 32
    ROTATE_INDEXES = {
        'u': 0,
        'l': 1,
        'd': 2,
        'r': 3,
    }

    def __init__(self, cords, rotate, img_index):
        self.cords = cords
        self.rotate = rotate
        self.img_index = img_index

    def draw(self):
        w = self.WIDTH_SPRITE
        h = self.HEIGHT_SPRITE
        u = self.ROTATE_INDEXES[self.rotate] * w
        v = self.img_index * h
        x = self.cords[0] - w / 2
        y = self.cords[1] - h / 2
        pyxel.blt(x, y, 0, u, v, w, h, 11)

    def move_up(self):
        self.cords[1] -= 5
        self.rotate = 'u'

    def move_down(self):
        self.cords[1] += 5
        self.rotate = 'd'

    def move_left(self):
        self.cords[0] -= 5
        self.rotate = 'l'

    def move_right(self):
        self.cords[0] += 5
        self.rotate = 'r'


class Player(Ship):

    def __init__(self, cords):
        super().__init__(cords=cords, rotate='u', img_index=0)
        self.score = 0


class EnemyShip(Ship):

    def __init__(self, cords):
        super().__init__(cords=cords, rotate='u', img_index=3)

    def update(self):
        self.move_up()

    def is_alive(self):
        x, y = self.cords
        return (
            x > 0 and x < 256
            and y > 0 and y < 256
        )

class App:

    def run(self):
        pyxel.run(self.update, self.draw)

    def setup(self):
        pyxel.init(256, 256, caption="SPACESHIP OMG!!!")
        pyxel.image(0).load(0, 0, "assets.png")

        self.player = Player([128, 128])
        self.bullets = []
        self.enemies = [
            EnemyShip([20 + 50 * i, 250])
            for i in range(4)
        ]

    def update(self):
        self.keyboard()
        self.bullets = self.update_objs(self.bullets)
        self.enemies = self.update_objs(self.enemies)

    def update_objs(self, objs):
        survived_objs = []
        for obj in objs:
            obj.update()
            if obj.is_alive():
                survived_objs.append(obj)

        return survived_objs

    def keyboard(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            return
        if pyxel.btn(pyxel.KEY_UP):
            self.player.move_up()
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player.move_down()
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.move_left()
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.move_right()
        if pyxel.btnp(pyxel.KEY_SPACE, 0, 10):
            if len(self.bullets) > 3:
                return
            bullet = Bullet.from_player(self.player)
            self.bullets.append(bullet)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, "Score: %d" % self.player.score, 7)
        self.player.draw()
        self.draw_objs(self.bullets)
        self.draw_objs(self.enemies)

    def draw_objs(self, objs):
        for obj in objs:
            obj.draw()


if __name__ == "__main__":
    app = App()
    app.setup()
    app.run()
