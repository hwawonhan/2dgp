import random
import json
import os
from pico2d import*
import game_framework
import title_state

name = "MainState"

kirby = None
sky = None
coin1 = None
coin2 = None
coin3 = None
coin4 = None
running = True

class Kirby:
    def __init__(self):
        self.x, self.y = 100, 300
        self.keydown = 0
        self.imagenum = 8
        self.imagey = 0
        self.charsize = 70
        self.frame = 0
        self.power = 2
        self.image = load_image('image//kirby.png')
    def update(self):
        self.frame = (self.frame + 1) % self.imagenum
        if self.keydown == 1:
            if self.y <= 530:
                self.y += 10
        elif self.keydown == 2:
            if self.y >= 70:
                self.y -= 10
        elif self.keydown == 3:
            if self.power == 1:
                self.imagey = 3
                self.imagenum = 6
            else:
                self.imagey = 4
                self.imagenum = 8
        elif (self.imagey == 3 or self.imagey == 4) and self.frame == 0:
            self.imagenum = 8
            self.imagey = 0
            self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 71, 0 + (73 * self.imagey), self.charsize, self.charsize, self.x, self.y)

class Coin1:
    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((800 + (i * 50), 300 + (50 * i)))
            else:
                self.position.append((800 + (i * 50), self.position[3][1] - (50 * (i-4))))
        self.moveX = 0
        self.image = load_image('image//coin_1.png')
        self.imagex = 0
    def update(self):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
    def draw(self):
        for i in range(8):
            self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])

class Coin2:
    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((1200 + (i * 50), 300 - (50 * i)))
            else:
                self.position.append((1200 + (i * 50), self.position[3][1] + (50 * (i-4))))
        self.moveX = 0
        self.image = load_image('image//coin_1.png')
        self.imagex = 0
    def update(self):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
    def draw(self):
        for i in range(8):
            self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])

class Coin3:
    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((1600 + (i * 50), 300 + (50 * i)))
                self.position.append((1600 + (i * 50), 300 - (50 * i)))
            else:
                self.position.append((1600 + (i * 50), 500 - (50 * (i-3))))
                self.position.append((1600 + (i * 50), 100 + (50 * (i-3))))
        self.moveX = 0
        self.image = load_image('image//coin_1.png')
        self.imagex = 0
    def update(self):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
    def draw(self):
        for i in range(16):
            self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])

class Coin4:
    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((2000 + (i * 50), 300 + (50 * i)))
                self.position.append((2000 + (i * 50), 300 - (50 * i)))
            else:
                self.position.append((2000 + (i * 50), 500 - (50 * (i - 3))))
                self.position.append((2000 + (i * 50), 100 + (50 * (i - 3))))
            if i != 0 and i != 7:
                self.position.append((2000 + (i * 50), 300))

        self.moveX = 0
        self.image = load_image('image//coin_1.png')
        self.imagex = 0
    def update(self):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
    def draw(self):
        for i in range(22):
            self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])

class Sky:
    def __init__(self):
        self.image = load_image('image//bg.png')
        self.image2 = load_image('image//bg_1.png')
        self.x, self.y = 400, 300
        self.x2 = 1200
        self.endBG = 0

    def update(self):
        self.x -= 10
        self.x2 -= 10
        if self.x == -400:
            self.x = self.x2 + 800

        if self.x2 == -400:
            self.x2 = self.x + 800

    def draw(self):
         self.image.draw(self.x, self.y)
         self.image2.draw(self.x2, self.y)

class Monster:
    def __init__(self):
         self.x, self.y = 800, random.randint(0, 600)



def enter():
    global kirby, sky, coin1, coin2, coin3, coin4
    kirby = Kirby()
    sky = Sky()
    coin1 = Coin1()
    coin2 = Coin2()
    coin3 = Coin3()
    coin4 = Coin4()


def exit():
    global kirby, sky, coin1, coin2, coin3, coin4
    del(kirby)
    del(sky)
    del(coin1)
    del(coin2)
    del(coin3)
    del(coin4)


def pause():
    pass


def resume():
    pass


def handle_events():
    global kirby
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                kirby.frame = 0
                kirby.keydown = 1
                kirby.imagey = 1
                kirby.imagenum = 5
            elif event.key == SDLK_DOWN:
                kirby.frame = 0
                kirby.keydown = 2
                kirby.imagey = 2
                kirby.imagenum = 5
            elif event.key == SDLK_SPACE:
                kirby.frame = 0
                kirby.keydown = 3


        if event.type == SDL_KEYUP:
            #if(kirby.keydown == 1 or kirby.keydown == 2):
                kirby.keydown = 0
                kirby.imagey = 0
                kirby.imagenum = 8

def update():
    kirby.update()
    sky.update()
    coin1.update()
    coin2.update()
    coin3.update()
    coin4.update()
    delay(0.07)

def draw():
    clear_canvas()
    sky.draw()
    coin1.draw()
    coin2.draw()
    coin3.draw()
    coin4.draw()
    kirby.draw()
    update_canvas()


