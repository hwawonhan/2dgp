from pico2d import *
from Kirby import Kirby
import random

class Item:
    def __init__(self):
        self.x, self.y = 800, random.randint(50, 550)
        self.image = load_image('./image/item.png')
        self.eatitem = load_wav('./image/itemeat.wav')
        self.eatitem.set_volume(30)
        self.life_time = 0.0
        self.apper = False
        self.speed = 80
        self.crush = False
        self.remove = False

    def coilsion(self, kirby):
        for i in range(8):
            left_a, right_a, top_a, bottom_a = kirby.x - 30, kirby.x + 30, kirby.y + 30, kirby.y - 25
            left_b, right_b, top_b, bottom_b = self.x - 25, self.x + 25, self.y - 25, self.y + 25

            if left_b < right_a and left_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    if self.crush == False:
                        self.crush = True
                        kirby.bulletimagey = 1
                        self.eatitem.play(1)

                if bottom_b < top_a and bottom_b > bottom_a:
                    if self.crush == False:
                        self.crush = True
                        kirby.bulletimagey = 1
                        self.eatitem.play(1)

            elif right_b < right_a and right_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    if self.crush == False:
                        self.crush = True
                        kirby.bulletimagey = 1
                        self.eatitem.play(1)

                if bottom_b < top_a and bottom_b > bottom_a:
                    if self.crush == False:
                        self.crush = True
                        kirby.bulletimagey = 1
                        self.eatitem.play(1)

    def update(self, frame_time, kirby):
        self.life_time += frame_time
        distance = self.speed * frame_time
        self.coilsion(kirby)
        if self.apper == False:
            if self.life_time > 30:
                self.apper = True
        else:
            if(self.x > -50):
                self.x -= distance



    def draw(self):
        if self.apper == True and self.crush == False:
            self.image.clip_draw(0, 0, 50, 50, self.x, self.y)
