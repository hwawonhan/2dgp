from pico2d import *
import game_framework
import title_state


class Kirby:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)


    def __init__(self):
        self.x, self.y = 100, 300
        self.keydown = 0
        self.imagenum = 8
        self.imagey = 0
        self.life_time = 0
        self.charsize = 70
        self.frame = 0
        self.Speed_PPS = 150
        self.power = 2
        self.bullet = []
        self.bulletkey = False
        self.hp = 700
        self.trancehp  = 0
        self.image = load_image('image//kirby.png')
        self.bulletimage = load_image('image//kirbybullet.png')
        self.hpimage = load_image('image//kirbyhp.png')
        self.hpimage_1 = load_image('image//kirbyhp_.png')
        self.gameoverimage = load_image('image//gameover.png')
        self.bulletframe = 0
        self.bulletimagey = 0
    def update(self, frame_time):
        self.life_time += frame_time
        distance = self.Speed_PPS * frame_time
        self.frame = (self.frame + 1) % self.imagenum
        if self.keydown == 1:
            if self.y <= 530:
                self.y += distance
        elif self.keydown == 2:
            if self.y >= 70:
                self.y -= distance
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
        elif self.imagey == 5 and self.frame == 0:
            self.imagenum = 8
            self.imagey = 0
            self.frame = 0
        if self.bulletkey == True:
            bulletx = self.x + 20
            bullety = self.y
            self.bullet.append([bulletx, bullety, False])

    def coilsion(self, monster):
        for i in monster.bullet:
            left_a, right_a, top_a, bottom_a = self.x - 25, self.x + 25, self.y + 25, self.y - 25
            left_b, right_b, top_b, bottom_b = i[0] - 10, i[0] + 10, i[1] - 10, i[1] + 10

            if i[2] == False and monster.HP > 0:
                if left_b < right_a and left_b > left_a:
                    if top_b < top_a and top_b > bottom_a:
                        self.imagey = 5
                        self.imagenum = 5
                        self.imageframe = 1
                        self.hp -= 10
                        self.trancehp += 5
                        i[2] = True
                    if bottom_b < top_a and bottom_b > bottom_a:
                        self.imagey = 5
                        self.imagenum = 5
                        self.imageframe = 1
                        self.hp -= 10
                        self.trancehp += 5
                        i[2] = True
                elif right_b < right_a and right_b > left_a:
                    if top_b < top_a and top_b > bottom_a:
                        self.imagey = 5
                        self.imagenum = 5
                        self.imageframe = 1
                        self.hp -= 10
                        self.trancehp += 5
                        i[2] = True
                    if bottom_b < top_a and bottom_b > bottom_a:
                        self.imagey = 5
                        self.imagenum = 5
                        self.imageframe = 1
                        self.hp -= 10
                        self.trancehp += 5
                        i[2] = True




    def handle_event(self, event):
        if self.hp > 0:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_UP:
                    self.frame = 0
                    self.keydown = 1
                    self.imagey = 1
                    self.imagenum = 5


                elif event.key == SDLK_DOWN:
                    self.frame = 0
                    self.keydown = 2
                    self.imagey = 2
                    self.imagenum = 5
                elif event.key == SDLK_SPACE:
                    self.frame = 0
                    if self.keydown == 1:
                        self.bulletkey = True
                    elif self.keydown == 2:
                        self.bulletkey = True
                    else:
                        self.keydown = 3
                        self.bulletkey = True
                elif event.key == SDLK_i:
                    self.bulletimagey = 1
        else:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.change_state(title_state)

        if event.type == SDL_KEYUP:
            if event.key == SDLK_SPACE:
                self.bulletkey = False
                self.keydown = 0
                #if(kirby.keydown == 1 or kirby.keydown == 2):
            else:
                self.keydown = 0
                self.imagey = 0
                self.imagenum = 8

    def draw_hp(self):
        if self.hp > 300:
            self.hpimage.clip_draw(0, 0,  self.hp, 30, 400 - self.trancehp, 50)
        else:
            self.hpimage_1.clip_draw(0, 0,  self.hp, 30, 400 - self.trancehp, 50)

    def draw_bullet(self, bx, by, crush):
        if crush == False:
            self.bulletimage.clip_draw(self.bulletframe* 50, 0 + (50*self.bulletimagey), 50, 50, bx, by)
    def draw(self):
        if self.hp > 0:
            self.image.clip_draw(self.frame * 71, 0 + (73 * self.imagey), self.charsize, self.charsize, self.x, self.y)
            self.draw_hp()
            #draw_rectangle(self.x - 30, self.y - 30, self.x + 30, self.y + 25)
            if len(self.bullet) != 0:
                for i, bxy in enumerate(self.bullet):
                    bxy[0] += 30
                    self.bulletframe = 3
                    self.bullet[i][0] = bxy[0]
                    self.draw_bullet(bxy[0], bxy[1], bxy[2])
                    if bxy[0] >= 800:
                        self.bullet.remove(bxy)
        else:
            self.gameoverimage.clip_draw(0, 0, 800, 600, 400, 300)


