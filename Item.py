from pico2d import *
from Kirby import Kirby
import random

class Monster1:
    def __init__(self, i):
        self.x, self.y = 800, (i+1) * 200
        self.image = load_image('./image/item.png')
        self.life_time = 0.0
        self.apper = False
        self.speed = 80
        self.crush = False
        self.remove = False

    def update(self, current_time, frame_time, kirby):
        self.life_time += frame_time
        distance = self.speed * frame_time

        if self.apper == False:
            if self.life_time > 20:
                self.apper = True
        else:
            if(self.x > 600):
                self.x -= distance


    def draw(self):
        self.image.clip_draw(self.frame * 60, 0 + (60 * self.imagey), 60, 60, self.x, self.y)
