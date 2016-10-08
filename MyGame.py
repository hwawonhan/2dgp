import random
from pico2d import*

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



def handle_events():
    global running
    global kirby
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False




open_canvas(800,600)
sky = Sky()

running = True


while running:
    handle_events()

    sky.update()
    clear_canvas()
    sky.draw()
    update_canvas()

    delay(0.07)

