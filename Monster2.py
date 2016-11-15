from pico2d import *
from Kirby import Kirby
import random

class Monster2:
    def __init__(self):
        self.x, self.y = 800, 300
        self.image = load_image('image//M6.png')
        self.hpimage = load_image('image//kirbyhp_.png')
        self.frame = 0
        self.imagey = 0
        self.apper = False
        self.speed = 80
        self.crush = False
        self.trance = 0
        self.HP = 100
    def update(self, current_time, frame_time, kirby):
        distance = self.speed * frame_time
        if (self.crush == True):
            self.frame = (self.frame + 1) % 3
            if (self.frame == 0):
                self.crush = False
                self.imagey = 0
        else:
            self.frame = (self.frame + 1) % 5
        if self.apper == True:
            self.coilsion(kirby)
        if self.apper == False:
            if current_time > 30:
                self.apper = True
                print('apper2')

        else:
            if(self.x > 600):
                self.x -= distance

    def coilsion(self, kirby):
        for i in kirby.bullet:
            left_a, right_a, top_a, bottom_a = self.x - 35, self.x + 35, self.y + 35, self.y - 35
            left_b, right_b, top_b, bottom_b = i[0] - 25, i[0] + 25, i[1] - 25, i[1] + 25

            if self.crush == False and i[2] == False and self.HP > 0:
                if left_b < right_a and left_b > left_a:
                    if top_b < top_a and top_b > bottom_a:
                        self.HP -= 10
                        self.trance += 5
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
                    if bottom_b < top_a and bottom_b > bottom_a:
                        self.HP -= 10
                        self.trance += 5
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
                elif right_b < right_a and right_b > left_a:
                    if top_b < top_a and top_b > bottom_a:
                        self.HP -= 10
                        self.trance += 5
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
                    if bottom_b < top_a and bottom_b > bottom_a:
                        self.HP -= 10
                        self.trance += 5
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
    def draw_hp(self):
        self.hpimage.clip_draw(0, 0, self.HP, 10, self.x - self.trance, self.y + 40)

    def draw(self):
        if self.apper == True and self.HP > 0:
            self.image.clip_draw(self.frame * 70, 0 + (70 * self.imagey), 70, 70, self.x, self.y)
            self.draw_hp()
