from pico2d import *


class Sky:
    def __init__(self):
        self.image = load_image('image//bg.png')
        self.image2 = load_image('image//bg_1.png')
        self.bgm = load_music('image//bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.x, self.y = 400, 300
        self.x2 = 1200
        self.endBG = 0
        self.Speed_PPS = 100
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