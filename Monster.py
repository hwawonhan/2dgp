from pico2d import *
import random

class Monster:
    def __init__(self):
        self.x, self.y = 800, random.randint(0, 600)
        self.image = load_image('image//M10.png')
        self.frame = 0
        self.imagey = 0
        self.apper = False
        self.speed = 80
    def update(self, current_time, frame_time):
        distance = self.speed * frame_time
        self.frame = (self.frame + 1) % 7
        if self.apper == False:
            if current_time > 10:
                self.apper = True
                print('apper')

        else:
            if(self.x > 400):
                self.x -= distance



    def draw(self):
        if self.apper == True:
            self.image.clip_draw(self.frame * 50, 0 + (50 * self.imagey), 50, 50, self.x, self.y)

