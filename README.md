# pyxel-prelection

![gameplay](gameplay.gif)

## Web version

[click](https://firemark.github.io/pyxel-prelection)

## Install

Requires `libsdl2-dev` and [`pipx`](https://pypa.github.io/pipx/).

In this directory:

```bash
pipx install -e .
pyxel-prelection-game
```

## Why Pyxel?

1. It's very simple to learn (for pro & newbies) (I've made a game in 4 hours! in pure python!)
2. Has many simple examples to copy&edit
3. Has a nice ascii font
4. 8bit sound generator is amazing
5. It's fast (using opengl, sdl2 in rust)
6. Nice to learn programming in python

## Advantages

* Very simple API - you can learn it in one day
* Documentation is a 1 file (README file in github)
* sprites support
* basic shapes drawing support
* 8 bit music / sound
* tilemaps
* built in sprite / map / music editor (But I haven't used it)

## Limitations (by design or not)

* Documentation doesn't have examples directly
* Documentation doesn't describe arguments and what functions/methods do.
* Supports only 16 colors (image assets too!)
* Has a limited banks with sounds and images
* Doesn't have a collision system
* 256×256 screen size (with autoscalling so don't worry)
* No rotating / mirroring sprites
* No particles system
* Random bugs like segmentation fault or floating point error :-(

## Items

Assets: https://guardian5.itch.io/blue-green-and-red-spacecraft-asset (Thx!!)
Sound: Randomized
Engine: [Pyxel](https://github.com/kitao/pyxel)

## Stages

1. [init game](https://github.com/firemark/pyxel-prelection/commit/6000aff4aea00a51111c17b90ecd84a391432339)
2. [change assets and draw sprites](https://github.com/firemark/pyxel-prelection/commit/8b02c392c5a13cf3cbca3581cb2fcb4376afd28e)
3. [add player object](https://github.com/firemark/pyxel-prelection/commit/61ec52f8996e7e3b7c810173f2b23404027b4362)
4. [add player moving](https://github.com/firemark/pyxel-prelection/commit/13118e9182ed1b5ba7a96f6ffa456e19e2409a3d)
5. [add rotating](https://github.com/firemark/pyxel-prelection/commit/0e6298906852f65b9151e93897c13e2f12ca1169)
6. [add bullets](https://github.com/firemark/pyxel-prelection/commit/59c78dba1a7fa6800f124408521df4c9f292cb6c)
7. [compute better cords of bullet](https://github.com/firemark/pyxel-prelection/commit/788c1423833ef62167b8091a1b777557edf22e15)
8. [add enemies](https://github.com/firemark/pyxel-prelection/commit/323119d14e170e10388f7380980c1d3e5d25c537)
9. [add collision with enemy and bullets](https://github.com/firemark/pyxel-prelection/commit/4c8d9cdba7fb0f9f4ae35f5dfced3e8d3d87d1bc)
10. [add spawning enemies](https://github.com/firemark/pyxel-prelection/commit/1c55dcde554a6b174f89653fc9e294465113acb1)
11. [add music (OMG!)](https://github.com/firemark/pyxel-prelection/commit/3922ace55b2febab7338429400087110c47b44c4)
12. [support game over](https://github.com/firemark/pyxel-prelection/commit/f12b5e084bd12dea8c7a57dde4b8209caf6ea8aa)
13. [add animations](https://github.com/firemark/pyxel-prelection/commit/786faace3cc9c717d8814592ec1265404932601a)
14. [add background](https://github.com/firemark/pyxel-prelection/commit/45b3d132a9e4d521245e991b495091919bab13aa)
15. [support gamepad](https://github.com/firemark/pyxel-prelection/commit/a47d99782ec37681ed76ca99bac4b51456622853)
16. [improving gameplay](https://github.com/firemark/pyxel-prelection/commit/557552956e4ad2c4bc55a260e2cb19e3ef3f09b2)
17. [MY PRECIOUS!](https://github.com/firemark/pyxel-prelection/commit/126afa309efad0ff36c7162e2fd071eca2a9d78c)
18. [MY BOOM PRECIOUS!](https://github.com/firemark/pyxel-prelection/commit/c42ec86d9b632452fa6e1905965546f781632ec4)

## Conclusion

* It's not unreal or unity engine
* It's not game maker too (But is very similar to first versions of game maker)
* It's a lot of fun!
* In short time we can make a nice, simple game
* I love 8 bit so much <3
* A good way to learn python and programming

