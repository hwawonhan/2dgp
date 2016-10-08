import random
from pico2d import*
class Kirby:
    def __init__(self):
        self.x, self.y = 100, 300
        self.keydown = 0
        self.imagenum = 8
        self.imagey = 0
        self.charsize = 70
        self.frame = 0
        self.power = 1
        self.image = load_image('kirby.png')
    def update(self):
        self.frame = (self.frame + 1) % self.imagenum
        if self.keydown == 1:
            self.y += 10
        elif self.keydown == 2:
            self.y -= 10
        elif self.keydown == 3:
            if kirby.power == 1:
                kirby.imagey = 3
                kirby.imagenum = 6
            else:
                kirby.imagey = 4
                kirby.imagenum = 8
        elif (self.imagey == 3 or self.imagey == 4) and self.frame == 0:
            self.imagenum = 8
            self.imagey = 0
            self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 71, 0 + (72 * self.imagey), self.charsize, self.charsize, self.x, self.y)

class Coin:
    def __init__(self):
        self.x, self.y = 800, random.randint(50,550)
        self.image = load_image('coin.png')
        self.imagey = 0
    def update(self):
        self.x -= 10
        self.imagey = (self.imagey + 1) % 3
    def draw(self):
        self.image.clip_draw(0, (self.imagey * 70) + 2, 70, 68, self.x, self.y)



class Sky:
    def __init__(self):
        self.image = load_image('bg.png')
        self.image2 = load_image('bg_1.png')
        self.x, self.y = 400, 300
        self.x2 = 1200
        self.endBG = 0
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

class Monster:
    def __init__(self):
         self.x, self.y = 800, random.randint(0, 600)



def handle_events():
    global running
    global kirby
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                kirby.frame = 0
                kirby.keydown = 1
                kirby.imagey = 1
                kirby.imagenum = 5
            elif event.key == SDLK_DOWN:
                kirby.frame = 0
                kirby.keydown = 2
                kirby.imagey = 2
                kirby.imagenum = 5
            elif event.key == SDLK_SPACE:
                kirby.frame = 0
                kirby.keydown = 3


        if event.type == SDL_KEYUP:
            #if(kirby.keydown == 1 or kirby.keydown == 2):
                kirby.keydown = 0
                kirby.imagey = 0
                kirby.imagenum = 8



open_canvas(800,600)
kirby = Kirby()
sky = Sky()
coins = [Coin() for i in range(1)]
running = True;


while running:
    handle_events()
    kirby.update()
    for coin in coins:
        coin.update()
    sky.update()

    clear_canvas()

    sky.draw()
    kirby.draw()
    for coin in coins:
        coin.draw()
    update_canvas()

    delay(0.1)

