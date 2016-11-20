from pico2d import *
from Kirby import Kirby
import random

class Monster:
    def __init__(self):
        self.x, self.y = 800, random.randint(100, 500)
        self.image = load_image('image//M10.png')
        self.bulletimage = load_image('image//monsterbullet.png')
        self.hpimage = load_image('image//kirbyhp_.png')
        self.frame = 0
        self.imagey = 0
        self.life_time = 0.0
        self.updownkey = 0
        self.apper = False
        self.crush = False
        self.HP = 30
        self.trance = 0
        self.speed = 80
        self.bullet = []
        self.shoutAngle = 0
        self.shoutAngleRate = 20
        self.shoutSpeed = 1
        self.Anglerate = 0.02
        self.Speedra1te = 0.01
        self.Speedrate = 0.1
    def update(self, current_time, frame_time, kirby):
        self.life_time += frame_time
        distance = self.speed * frame_time
        if(self.crush == True):
            self.frame = (self.frame + 1) % 6
            if(self.frame == 0):
                self.crush = False
                self.imagey = 0
        else:
            self.frame = (self.frame + 1) % 7
            if self.frame % 6 == 0 and self.apper == True and self.HP > 0:
                self.bullet.append([self.x, self.y, False])
        if self.updownkey == 0:
            self.y -= 5
            if self.y < 50:
                self.updownkey = 1
        else:
            self.y += 5
            if self.y > 550:
                self.updownkey = 0
        if self.apper == True:
            self.coilsion(kirby)
            if (self.x > 600):
                self.x -= distance


        if self.apper == False:
            if self.life_time > 10:
                self.apper = True
                print('apper')

    def coilsion(self, kirby):
        for i in kirby.bullet:
            left_a, right_a, top_a, bottom_a = self.x - 25, self.x + 25, self.y + 25, self.y - 25
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
        self.hpimage.clip_draw(0, 0, self.HP, 10,self.x - self.trance, self.y + 30)

    def draw_bullet(self, bx, by, on):
        if on == False and self.HP >  0:
            self.bulletimage.clip_draw(0, 0, 20, 20, bx, by)

    def draw(self):
        if self.apper == True and self.HP > 0:
            self.image.clip_draw(self.frame * 50, 0 + (50 * self.imagey), 50, 50, self.x, self.y)
            self.draw_hp()
        if len(self.bullet) != 0:
            for i, bxy in enumerate(self.bullet):
                bxy[0] -= 50
                self.bullet[i][0] = bxy[0]
                self.draw_bullet(bxy[0], bxy[1], bxy[2])
                if bxy[0] >= 800:
                    self.bullet.remove(bxy)
