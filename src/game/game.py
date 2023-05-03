#!/usr/bin/env python3
import pyxel
from copy import copy
from random import randint, random


class Obj:

    def __init__(self, cords):
        self.cords = cords
        self.is_destroyed = False

    def is_alive(self):
        if self.is_destroyed:
            return False
        x, y = self.cords
        return (
            x > 0 and x < 256
            and y > 0 and y < 256
        )

    def has_collision(self, obj):
        obj_x, obj_y = obj.cords
        x, y = self.cords
        w = self.WIDTH_SPRITE
        h = self.HEIGHT_SPRITE

        return (
            obj_x > x - w / 2
            and obj_x < x + w / 2
            and obj_y > y - h / 2
            and obj_y < y + h / 2
        )


class Precious(Obj):
    WIDTH_SPRITE = 1
    HEIGHT_SPRITE = 1

    def __init__(self, cords, factor, size):
        super().__init__(cords)
        self.time = 60
        self.factor = factor
        self.size = size

    def update(self):
        self.time -= 1

    def is_alive(self):
        return not self.is_destroyed and self.time > 0

    def draw(self):
        x, y = self.cords
        pyxel.circ(x, y, self.size, (self.time // 2) % 16)


class BoomPrecious(Precious):

    def draw(self):
        x, y = self.cords
        pyxel.circ(x, y, self.size, 7 if self.time % 16 < 8 else 8)


class Explosion(Obj):

    def __init__(self, cords, score=None, color=7):
        super().__init__(cords)
        self.time = 15
        self.score = score
        self.color = color

    def update(self):
        self.time -= 1

    def is_alive(self):
        return self.time > 0

    def draw(self):
        x, y = self.cords
        if self.score:
            pyxel.text(x, y, str(self.score), 10)

        r = (self.time - 10) / 5 * 20
        if r > 0:
            pyxel.circ(x, y, r, self.color)


class Bullet(Obj):
    WIDTH_SPRITE = 2
    HEIGHT_SPRITE = 2

    def __init__(self, cords, rotate):
        super().__init__(cords)
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

    def draw(self):
        x, y = self.cords
        pyxel.circ(x, y, 2, 10)


class Ship(Obj):
    WIDTH_SPRITE = 32
    HEIGHT_SPRITE = 32
    ROTATE_INDEXES = {
        'u': 0,
        'l': 1,
        'd': 2,
        'r': 3,
    }

    def __init__(self, cords, rotate, speed, img_index):
        super().__init__(cords)
        self.rotate = rotate
        self.img_index = img_index
        self.speed = speed

    def draw(self):
        w = self.WIDTH_SPRITE
        h = self.HEIGHT_SPRITE
        u = self.ROTATE_INDEXES[self.rotate] * w
        v = self.img_index * h
        x = self.cords[0] - w / 2
        y = self.cords[1] - h / 2
        pyxel.blt(x, y, 0, u, v, w, h, 11)

    def move_up(self):
        self.cords[1] -= self.speed
        self.rotate = 'u'

    def move_down(self):
        self.cords[1] += self.speed
        self.rotate = 'd'

    def move_left(self):
        self.cords[0] -= self.speed
        self.rotate = 'l'

    def move_right(self):
        self.cords[0] += self.speed
        self.rotate = 'r'


class Player(Ship):

    def __init__(self, cords):
        super().__init__(cords=cords, rotate='u', speed=5, img_index=0)
        self.score = 0


class EnemyShip(Ship):

    def __init__(self, cords, enemy_type=0, speed_mult=1):
        speed = randint(3, 6) * speed_mult
        super().__init__(cords=cords, rotate='u', speed=speed, img_index=3 + enemy_type)

    def update(self):
        self.move_up()


class App:

    def run(self):
        pyxel.run(self.update, self.draw)

    def setup(self):
        pyxel.init(256, 256, title="SPACESHIP OMG!!!")
        pyxel.image(0).load(0, 0, "assets.png")
        pyxel.image(1).load(0, 0, "background.png")
        pyxel.sound(0).set("a0", "t", "257", "f", 15)
        pyxel.sound(1).set("f0g1f2", "nnn", "373", "fvf", 20)
        pyxel.sound(2).set(
            "f0g1f2 e0f1e2 d0e1d2 d2d2",  # notes
            "s",  # tones
            "777 555 333 21",   # volumes
            "fff nnn vvv vv",   # effects
            30,  # speed
        )
        pyxel.sound(3).set(
            "e0f1e2 f0g1f2 f3",  # notes
            "s",  # tones
            "555 777 7",   # volumes
            "n",   # effects
            20,  # speed
        )
        pyxel.sound(4).set("a2g3f3", "ppp", "252", "fff", 30)
        self.setup_world()

    def setup_world(self):
        self.time = 0
        self.game_over = False
        self.player = Player([128, 128])
        self.bullets = []
        self.enemies = []
        self.animations = []
        self.preciouses = []
        pyxel.play(0, 3)

    def update(self):
        if not self.game_over and pyxel.frame_count % 10 == 0:
            self.time += 1
        self.keyboard()
        self.bullets = self.update_objs(self.bullets)
        self.enemies = self.update_objs(self.enemies)
        self.animations = self.update_objs(self.animations)
        self.preciouses = self.update_objs(self.preciouses)
        self.update_collision()
        self.spawn_enemies()

        if not self.game_over:
            self.spawn_bonus()

    def update_objs(self, objs):
        survived_objs = []
        for obj in objs:
            obj.update()
            if obj.is_alive():
                survived_objs.append(obj)

        return survived_objs

    def update_collision(self):
        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.has_collision(enemy) or enemy.has_collision(bullet):
                    bullet.is_destroyed = True
                    self.kill_enemy(enemy)
                    pyxel.play(0, 1)

        if self.game_over:
            return

        for my_precious in self.preciouses:
            if my_precious.has_collision(self.player) or self.player.has_collision(my_precious):
                self.apply_precious(my_precious)

        for enemy in self.enemies:
            if enemy.has_collision(self.player) or self.player.has_collision(enemy):
                enemy.is_destroyed = True
                self.game_over = True
                self.animations.append(Explosion(enemy.cords))
                self.animations.append(Explosion(self.player.cords))
                pyxel.play(1, 2)

    def apply_precious(self, my_precious):
        my_precious.is_destroyed = True
        score = int(my_precious.factor * (my_precious.time * 2 + my_precious.size * 5))
        self.player.score += score
        self.animations.append(Explosion(my_precious.cords, score, color=15))
        if isinstance(my_precious, BoomPrecious):
            for enemy in self.enemies:
                if enemy.is_destroyed:
                    continue
                self.kill_enemy(enemy)

            pyxel.play(0, 1)
        else:
            pyxel.play(1, 4)

    def kill_enemy(self, enemy):
        enemy.is_destroyed = True
        score = int(100 + self.time * enemy.speed // 50 + enemy.cords[1])
        self.player.score += score
        self.animations.append(Explosion(enemy.cords, score))

    def spawn_enemies(self):
        spawn_rate = max(50 - self.time // 3, 10)
        if pyxel.frame_count % spawn_rate == 5:
            x = randint(20, 200)
            y = 250
            enemy_type = randint(0, 4)
            speed_mult = 1 + min(self.time / 50, 3)
            enemy = EnemyShip([x, y], enemy_type)
            self.enemies.append(enemy)

    def spawn_bonus(self):
        if pyxel.frame_count % 20 == 0 and random() < 0.3:
            player_x, player_y = self.player.cords
            x = randint(32, 224)
            y = randint(32, 224)
            distance = abs(x - player_x) + abs(y - player_y)
            factor = 1 + distance / 128 + self.time / 5
            size = randint(2, 5)
            cls_precious = Precious if random() < 0.7 else BoomPrecious
            my_precious = cls_precious([x, y], factor, size)
            self.preciouses.append(my_precious)

    def keyboard(self):
        if pyxel.btnp(pyxel.KEY_Q) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_BACK):
            pyxel.quit()
            return

        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_START):
                self.setup_world()
            return

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.player.move_up()
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.player.move_down()
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.player.move_left()
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player.move_right()
        if pyxel.btnp(pyxel.KEY_SPACE, 0, 10) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y, 0, 10):
            if len(self.bullets) > 3:
                return
            bullet = Bullet.from_player(self.player)
            self.bullets.append(bullet)
            pyxel.play(1, 0)

    def draw(self):
        pyxel.cls(2 if self.game_over else 1)
        pyxel.blt(0, 0, 1, 0, 0, 256, 256, 0)
        if self.game_over:
            pyxel.text(80, 40, "GAME OVER", pyxel.frame_count % 16)
            pyxel.text(80, 50, "Total score: %d" % self.player.score, 8)
            pyxel.text(80, 60, "Press Q / BACK / SELECT to quit", 8)
            pyxel.text(80, 70, "Press R / START to restart", 8)
        else:
            pyxel.text(0, 0, "Score: %d" % self.player.score, 7)
            pyxel.text(0, 8, "Time: %d" % self.time, 7)
            self.player.draw()

        self.draw_objs(self.bullets)
        self.draw_objs(self.enemies)
        self.draw_objs(self.animations)
        self.draw_objs(self.preciouses)

    def draw_objs(self, objs):
        for obj in objs:
            obj.draw()
