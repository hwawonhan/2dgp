import random
import json
import os

from pico2d import*
from Kirby import Kirby
from Coin1 import Coin1
from Sky import Sky
import game_framework
import title_state
name = "MainState"


sky = None
kirby = None
coin1 = None
coin2 = None
coin3 = None
coin4 = None
running = True
front = None
current_time = get_time()


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

        if self.position[0][0] - self.moveX < -790:
            self.moveX = 0
            for i in range(8):
                if i < 4:
                    self.position[i] = ((800 + (i * 50), 300 - (50 * i), False))
                else:
                    self.position[i] = ((800 + (i * 50), self.position[3][1] + (50 * (i - 4)), False))

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

        if self.position[0][0] - self.moveX < -790:
            self.moveX = 0
            j = 0
            for i in range(8):
                if i < 4:
                    self.position[i + j] = ((800 + (i * 50), 300 + (50 * i), False))
                    j = j + 1
                    self.position[i + j] = ((800 + (i * 50), 300 - (50 * i), False))
                else:
                    self.position[i + j] = ((800 + (i * 50), 500 - (50 * (i - 3)), False))
                    j = j + 1
                    self.position[i + j] = ((800 + (i * 50), 100 + (50 * (i - 3)), False))

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
        if self.position[0][0] - self.moveX < -790:
            self.moveX = 0
            j = 0
            for i in range(8):
                if i < 4:
                    self.position[i + j] = ((800 + (i * 50), 300 + (50 * i), False))
                    j = j + 1
                    self.position[i + j] = ((800 + (j * 50), 300 - (50 * j), False))
                else:
                    self.position[i + j] = ((800 + (i * 50), 500 - (50 * (i - 3)), False))
                    j = j + 1
                    self.position[i + j] = ((800 + (j * 50), 100 + (50 * (j - 3)), False))
            for i in range(8):
                if i != 0 and i != 7:
                    self.position[i + 14] = (800 + (i * 50), 300, False)
            self.position[7] = (self.position[7][0], self.position[7][1] + 50, False)

    def draw(self):
        for i in range(22):
            if self.position[i][2] == False:
                self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])


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
        else:
            kirby.handle_event(event)

def update():
    global coin1, coin2, coin3, coin4, current_time
    j = 0
    frame_time = get_time() - current_time
    frame_rate = 1.0 / frame_time
    current_time += frame_time
    kirby.update(frame_time)
    sky.update()
    coin1.update(kirby)
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


