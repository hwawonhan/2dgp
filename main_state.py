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
front = None


class Kirby:
    def __init__(self):
        self.x, self.y = 100, 300
        self.keydown = 0
        self.imagenum = 8
        self.imagey = 0
        self.charsize = 70
        self.frame = 0
        self.power = 2
        self.bullet = []
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
        #draw_rectangle(self.x - 30, self.y - 30, self.x + 30, self.y + 25)

class Coin1:
    global kirby

    def coilsion(self):
        for i in range(8):
            left_a, right_a, top_a, bottom_a = kirby.x - 30, kirby.x + 30, kirby.y + 30, kirby.y - 25
            left_b, right_b, top_b, bottom_b = self.position[i][0] - self.moveX - 25, self.position[i][0] - self.moveX + 25,\
                                               self.position[i][1] + 25, self.position[i][1] - 25

            if left_b < right_a and left_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
            elif right_b < right_a and right_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)

    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((800 + (i * 50), 300 + (50 * i), False))
            else:
                self.position.append((800 + (i * 50), self.position[3][1] - (50 * (i-4)), False))
        self.moveX = 0
        self.image = load_image('image//coin_1.png')
        self.imagex = 0
    def update(self):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
        self.coilsion()



    def draw(self):
        for i in range(8):
            if self.position[i][2] == False:
                self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])
                #draw_rectangle(self.position[i][0] - self.moveX - 25, self.position[i][1] - 25, self.position[i][0] - self.moveX + 25, self.position[i][1] + 25)
class Coin2:


    def coilsion(self):
        for i in range(8):
            left_a, right_a, top_a, bottom_a = kirby.x - 30, kirby.x + 30, kirby.y + 30, kirby.y - 25
            left_b, right_b, top_b, bottom_b = self.position[i][0] - self.moveX - 25, self.position[i][
                0] - self.moveX + 25, self.position[i][1] + 25, self.position[i][1] - 25

            if left_b < right_a and left_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
            elif right_b < right_a and right_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)

    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((1200 + (i * 50), 300 - (50 * i), False))
            else:
                self.position.append((1200 + (i * 50), self.position[3][1] + (50 * (i-4)), False))
        self.moveX = 0
        self.image = load_image('image//coin_1.png')
        self.imagex = 0
    def update(self):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
        self.coilsion()

    def draw(self):
        for i in range(8):
            if self.position[i][2] == False:
                self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])
                #draw_rectangle(self.position[i][0] - self.moveX - 25, self.position[i][1] - 25, self.position[i][0] - self.moveX + 25, self.position[i][1] + 25)

class Coin3:


    def coilsion(self):
        for i in range(16):
            left_a, right_a, top_a, bottom_a = kirby.x - 30, kirby.x + 30, kirby.y + 30, kirby.y - 25
            left_b, right_b, top_b, bottom_b = self.position[i][0] - self.moveX - 25, self.position[i][
                0] - self.moveX + 25, \
                                               self.position[i][1] + 25, self.position[i][1] - 25

            if left_b < right_a and left_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
            elif right_b < right_a and right_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)


    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((1600 + (i * 50), 300 + (50 * i), False))
                self.position.append((1600 + (i * 50), 300 - (50 * i), False))
            else:
                self.position.append((1600 + (i * 50), 500 - (50 * (i-3)), False))
                self.position.append((1600 + (i * 50), 100 + (50 * (i-3)), False))
        self.moveX = 0
        self.image = load_image('image//coin_1.png')
        self.imagex = 0
    def update(self):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
        self.coilsion()
    def draw(self):
        for i in range(16):
            if self.position[i][2] == False:
                self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])
                #draw_rectangle(self.position[i][0] - self.moveX - 25, self.position[i][1] - 25, self.position[i][0] - self.moveX + 25, self.position[i][1] + 25)

class Coin4:

    def coilsion(self):
        for i in range(22):
            left_a, right_a, top_a, bottom_a = kirby.x - 30, kirby.x + 30, kirby.y + 30, kirby.y - 25
            left_b, right_b, top_b, bottom_b = self.position[i][0] - self.moveX - 25, self.position[i][
                0] - self.moveX + 25, \
                                               self.position[i][1] + 25, self.position[i][1] - 25

            if left_b < right_a and left_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
            elif right_b < right_a and right_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)

    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((2000 + (i * 50), 300 + (50 * i), False))
                self.position.append((2000 + (i * 50), 300 - (50 * i), False))
            else:
                self.position.append((2000 + (i * 50), 500 - (50 * (i - 3)), False))
                self.position.append((2000 + (i * 50), 100 + (50 * (i - 3)), False))
            if i != 0 and i != 7:
                self.position.append((2000 + (i * 50), 300, False))

        self.moveX = 0
        self.image = load_image('image//coin_1.png')
        self.imagex = 0
    def update(self):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
        self.coilsion()
    def draw(self):
        for i in range(22):
            if self.position[i][2] == False:
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
                kirby.bullet.append((kirby.x, kirby.y, False))


        if event.type == SDL_KEYUP:
            #if(kirby.keydown == 1 or kirby.keydown == 2):
                kirby.keydown = 0
                kirby.imagey = 0
                kirby.imagenum = 8

def update():
    global coin1, coin2, coin3, coin4
    j = 0
    kirby.update()
    sky.update()
    coin1.update()
    coin2.update()
    coin3.update()
    coin4.update()
    if coin1.position[0][0] - coin1.moveX < -790:
        coin1.moveX = 0
        for i in range(8):
            if i < 4:
                coin1.position[i] = ((800 + (i * 50), 300 + (50 * i), False))
            else:
                coin1.position[i] = ((800 + (i * 50), coin1.position[3][1] - (50 * (i - 4)), False))

    if coin2.position[0][0] - coin2.moveX < -790:
        coin2.moveX = 0
        for i in range(8):
            if i < 4:
                coin2.position[i] = ((800 + (i * 50), 300 - (50 * i), False))
            else:
                coin2.position[i] = ((800 + (i * 50), coin2.position[3][1] + (50 * (i - 4)), False))

    if coin3.position[0][0] - coin3.moveX < -790:
        coin3.moveX = 0
        j = 0
        for i in range(8):
            if i < 4:
                coin3.position[i + j] = ((800 + (i * 50), 300 + (50 * i), False))
                j = j + 1
                coin3.position[i + j] = ((800 + (i * 50), 300 - (50 * i), False))
            else:
                coin3.position[i + j] = ((800 + (i * 50), 500 - (50 * (i - 3)), False))
                j = j + 1
                coin3.position[i + j] = ((800 + (i * 50), 100 + (50 * (i - 3)), False))

    if coin4.position[0][0] - coin4.moveX < -790:
        coin4.moveX = 0
        j = 0
        for i in range(8):
            if i < 4:
                coin4.position[i + j] = ((800 + (i * 50), 300 + (50 * i), False))
                j = j + 1
                coin4.position[i + j] = ((800 + (j * 50), 300 - (50 * j), False))
            else:
                coin4.position[i + j] = ((800 + (i * 50), 500 - (50 * (i - 3)), False))
                j = j + 1
                coin4.position[i + j] = ((800 + (j * 50), 100 + (50 * (j - 3)), False))
        for i in range(8):
            if i != 0 and i != 7:
                coin4.position[i + 14] = (800 + (i * 50), 300, False)
        coin4.position[7] = (coin4.position[7][0], coin4.position[7][1] + 50, False)
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


