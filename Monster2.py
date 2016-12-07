from pico2d import *
from Kirby import Kirby
import random

class Monster2:
    def __init__(self):
        self.x, self.y = 800, 300
        self.image = load_image('image//M6.png')
        self.hpimage = load_image('image//kirbyhp_.png')
        self.frame = 0
        self.life_time = 0.0
        self.imagey = 0
        self.bulletimage = load_image('image//monsterbullet.png')
        self.apper = False
        self.speed = 80
        self.crush = False
        self.trance = 0
        self.HP = 100
        self.bullet = []
        self.bulletframe = 0
        self.shoutAngle = 0
        self.shoutAngleRate = 20
        self.shoutSpeed = 1
        self.Anglerate = 0.02
        self.Speedra1te = 0.01
        self.Speedrate = 0.1
        self.Angle =  0
    def update(self, current_time, frame_time, kirby):
        self.life_time += frame_time
        distance = self.speed * frame_time
        self.bulletframe = (self.bulletframe + 1) % 2
        if (self.crush == True):
            self.frame = (self.frame + 1) % 3
            if (self.frame == 0):
                self.crush = False
                self.imagey = 0
        else:
            self.frame = (self.frame + 1) % 5
            if self.frame % 5 == 0 and self.apper == True and self.HP > 0:
                for i in range(12):
                    self.bullet.append([self.x, self.y, False, i*30])
        if self.apper == True:
            self.coilsion(kirby)
            self.Angle += 10
            self.x += math.cos(self.Angle * 3.141592 / 180) * 10
            self.y += math.sin(self.Angle * 3.141592 / 180) * 10
        if self.apper == False:
            if self.life_time > 30:
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
                        if self.HP == 0:
                            kirby.score += 400
                        self.trance += 5
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
                    if bottom_b < top_a and bottom_b > bottom_a:
                        self.HP -= 10
                        if self.HP == 0:
                            kirby.score += 400
                        self.trance += 5
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
                elif right_b < right_a and right_b > left_a:
                    if top_b < top_a and top_b > bottom_a:
                        self.HP -= 10
                        if self.HP == 0:
                            kirby.score += 400
                        self.trance += 5
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
                    if bottom_b < top_a and bottom_b > bottom_a:
                        self.HP -= 10
                        if self.HP == 0:
                            kirby.score += 400
                        self.trance += 5
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
    def draw_hp(self):
        self.hpimage.clip_draw(0, 0, self.HP, 10, self.x - self.trance, self.y + 40)
    def draw_bullet(self, bx, by, on):
        if on == False and self.HP >  0:
            self.bulletimage.clip_draw(self.bulletframe * 20, 40, 20, 20, bx, by)


    def draw(self):
        if len(self.bullet) != 0:
            for i, bxy in enumerate(self.bullet):
                bxy[0] -= math.cos(bxy[3] * 3.141592 / 180) * 20
                bxy[1] -= math.sin(bxy[3] * 3.141592 / 180) * 20
                self.bullet[i][0] = bxy[0]
                self.draw_bullet(bxy[0], bxy[1], bxy[2])
                if bxy[0] >= 800:
                    self.bullet.remove(bxy)

        if self.apper == True and self.HP > 0:
            self.image.clip_draw(self.frame * 70, 0 + (70 * self.imagey), 70, 70, self.x, self.y)
            self.draw_hp()

