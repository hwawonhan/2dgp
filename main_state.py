import random
import json
import os

from pico2d import*
from Kirby import Kirby
from Coin1 import Coin1
from Coin2 import Coin2
from Coin3 import Coin3
from Coin4 import Coin4
from Sky import Sky
import game_framework
import title_state
name = "MainState"


sky = None
kirby = None
coin1 = None
coin2 = None
coin3 = None
coin4 = None
running = True
front = None
current_time = get_time()



class Monster:
    def __init__(self):
         self.x, self.y = 800, random.randint(0, 600)



def enter():
    global kirby, sky, coin1, coin2, coin3, coin4
    kirby = Kirby()
    sky = Sky()
    coin1 = Coin1()
    coin2 = Coin2()
    coin3 = Coin3()
    coin4 = Coin4()


def exit():
    global kirby, sky, coin1, coin2, coin3, coin4
    del(kirby)
    del(sky)
    del(coin1)
    del(coin2)
    del(coin3)
    del(coin4)


def pause():
    pass


def resume():
    pass


def handle_events():
    global kirby
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            kirby.handle_event(event)

def update():
    global coin1, coin2, coin3, coin4, current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    kirby.update(frame_time)
    sky.update()
    coin1.update(kirby)
    coin2.update(kirby)
    coin3.update(kirby)
    coin4.update(kirby)



    delay(0.07)

def draw():
    clear_canvas()
    sky.draw()
    coin1.draw()
    coin2.draw()
    coin3.draw()
    coin4.draw()
    kirby.draw()
    update_canvas()


