from pico2d import *
from Kirby import Kirby
import random

class Boss:
    def __init__(self):
        self.x, self.y = 800, random.randint(100, 500)
        self.image = load_image('./image/Boss.png')
        self.bulletimage = load_image('./image/monsterbullet.png')
        self.hpimage = load_image('./image/kirbyhp_.png')
        self.bossfaceimage = load_image('./image/Bossface.png')
        self.bossclearimage = load_image('./image/bossclear.png')
        self.Apear_sound = load_wav('./image/BossApear.wav')
        self.font = load_font('ENCR10B.TTF')
        self.Apear_sound.set_volume(50)
        self.frame = 0
        self.life_time = 0.0
        self.imagey = 0
        self.updownkey = 0
        self.apper = False
        self.crush = False
        self.HP = 700
        self.trance = 0
        self.speed = 80
        self.imboss = True
        self.bullet = []
        self.bullettype2 = []
        self.bullettype3 = []
    def update(self, current_time, frame_time, kirby):
        self.life_time += frame_time
        distance = self.speed * frame_time
        if(self.crush == True):
            self.frame = (self.frame + 1) % 2
            if(self.frame == 0):
                self.crush = False
                self.imagey = 0
        else:
            self.frame = (self.frame + 1) % 4
            if self.frame % 3 == 0 and self.apper == True and self.HP > 0:
                self.bullet.append([self.x, self.y, False, 0])
            if self.frame % 3 == 1 and self.apper == True and self.HP > 0:
                self.bullettype2.append([self.x, self.y, False, 30, 5])
            if self.frame % 3 == 2 and self.apper == True and self.HP > 0:
                for i in range(12):
                    self.bullettype3.append([self.x, self.y, False, i*30])
        if self.updownkey == 0:
            self.y -= 5
            if self.y < 150:
                self.updownkey = 1
        else:
            self.y += 5
            if self.y > 450:
                self.updownkey = 0
        if self.apper == True:
            self.coilsion(kirby)
            if (self.x > 600):
                self.x -= distance


        if self.apper == False:
            if self.life_time > 45:
                self.apper = True
                self.Apear_sound.play(1)
                print('apper')

    def coilsion(self, kirby):
        for i in kirby.bullet:
            left_a, right_a, top_a, bottom_a = self.x - 30, self.x + 30, self.y + 75, self.y + 25
            left_b, right_b, top_b, bottom_b = i[0] - 25, i[0] + 25, i[1] - 25, i[1] + 25
            draw_rectangle(left_a,top_a,right_a, bottom_a)
            if self.crush == False and i[2] == False and self.HP > 0:
                if left_b < right_a and left_b > left_a:
                    if top_b < top_a and top_b > bottom_a:
                        self.HP -= kirby.damage
                        if self.HP <= 0:
                            kirby.score += 1000
                        self.trance += kirby.damage//2
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
                    if bottom_b < top_a and bottom_b > bottom_a:
                        self.HP -= kirby.damage
                        if self.HP <= 0:
                            kirby.score += 1000
                        self.trance += kirby.damage//2
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
                elif right_b < right_a and right_b > left_a:
                    if top_b < top_a and top_b > bottom_a:
                        self.HP -= kirby.damage
                        if self.HP <= 0:
                            kirby.score += 1000
                        self.trance += kirby.damage//2
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True
                    if bottom_b < top_a and bottom_b > bottom_a:
                        self.HP -= kirby.damage
                        if self.HP <= 0:
                            kirby.score += 1000
                        self.trance += kirby.damage//2
                        self.crush = True
                        self.imagey = 1
                        self.imageframe = 1
                        i[2] = True


    def draw_hp(self):
        self.hpimage.clip_draw(0, 0, self.HP, 30, 400 - self.trance, 550)
        self.bossfaceimage.clip_draw(0, 0, 70, 70, 30, 550)

    def draw_bullet(self, bx, by, on, type):
        if on == False and self.HP > 0:
            if type == 0:
                self.bulletimage.clip_draw(0, 60, 20, 20, bx, by)

    def draw_bullettype2(self, bx, by, on):
        if on == False and self.HP > 0:
            self.bulletimage.clip_draw(0, 20, 20, 20, bx, by)

    def draw_bullettype3(self, bx, by, on):
        if on == False and self.HP > 0:
            self.bulletimage.clip_draw(20, 40, 20, 20, bx, by)

    def getHP(self):
        return self.HP
    def draw(self, score):
        if self.apper == True and self.HP > 0:
            self.image.clip_draw(self.frame * 200, 0 + (200 * self.imagey), 200, 200, self.x, self.y)
            self.draw_hp()
        if self.HP <= 0:
            self.bossclearimage.clip_draw(0, 0, 800, 600, 400, 300)
            self.font.draw(350, 250, 'Score : %3d' % score, (255, 255, 255))
        if len(self.bullet) != 0:
            for i, bxy in enumerate(self.bullet):
                bxy[0] -= 50
                self.bullet[i][0] = bxy[0]
                self.draw_bullet(bxy[0], bxy[1], bxy[2], bxy[3])
                if bxy[0] >= 800:
                    self.bullet.remove(bxy)

        if len(self.bullettype2) != 0:
            for i, bxy in enumerate(self.bullettype2):
                bxy[3] += 10
                if bxy[4] < 10:
                    bxy[4] += 1
                bxy[0] -= math.cos(bxy[3]*math.pi/180) * bxy[4]
                bxy[0] -= 10
                bxy[1] -= math.sin(bxy[3]*math.pi/180) * bxy[4]
                self.bullettype2[i][0] = bxy[0]
                self.draw_bullettype2(bxy[0], bxy[1], bxy[2])
                if bxy[0] >= 800:
                    self.bullettype2.remove(bxy)

        if len(self.bullettype3) != 0:
            for i, bxy in enumerate(self.bullettype3):
                bxy[0] -= math.cos(bxy[3] * 3.141592 / 180) * 20
                bxy[1] -= math.sin(bxy[3] * 3.141592 / 180) * 20
                self.bullettype3[i][0] = bxy[0]
                self.draw_bullettype3(bxy[0], bxy[1], bxy[2])
                if bxy[0] >= 800:
                    self.bullettype3.remove(bxy)
