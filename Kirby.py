from pico2d import *


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
        self.charsize = 70
        self.frame = 0
        self.Speed_PPS = 100
        self.power = 2
        self.bullet = []
        self.image = load_image('image//kirby.png')
    def update(self, frame_time):
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

    def handle_event(self, event):
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
                self.keydown = 3
                self.bullet.append((self.x, self.y, False))


        if event.type == SDL_KEYUP:
            #if(kirby.keydown == 1 or kirby.keydown == 2):
                self.keydown = 0
                self.imagey = 0
                self.imagenum = 8



    def draw(self):
        self.image.clip_draw(self.frame * 71, 0 + (73 * self.imagey), self.charsize, self.charsize, self.x, self.y)
        #draw_rectangle(self.x - 30, self.y - 30, self.x + 30, self.y + 25)