import random
import os
import json

from pico2d import*
import game_framework
import title_state
import ranking_state

from Kirby import Kirby
from Coin1 import Coin1
from Coin2 import Coin2
from Coin3 import Coin3
from Coin4 import Coin4
from Monster import Monster
from Monster1 import Monster1
from Monster2 import Monster2
from Boss import Boss
from Sky import Sky

name = "MainState"


sky = None
kirby = None
coin1 = None
coin2 = None
coin3 = None
coin4 = None
running = True
monster = None
monster1 = None
monster2 = None
boss = None
front = None
current_time = get_time()




def enter():
    global kirby, sky, coin1, coin2, coin3, coin4, monster, monster1, monster2, current_time, boss
    kirby = Kirby()
    sky = Sky()
    coin1 = Coin1()
    coin2 = Coin2()
    coin3 = Coin3()
    coin4 = Coin4()
    boss = Boss()
    monster = [Monster() for i in range(1) ]
    monster1 = [Monster1() for i in range(2)]
    monster2 = Monster2()
    game_framework.reset_time()


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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            game_framework.change_state(ranking_state)
        else:
            kirby.handle_event(event)


def update():
    global coin1, coin2, coin3, coin4, current_time, kirby, boss
    frame_time = get_time() - current_time
    current_time += frame_time

    kirby.update(frame_time)
    sky.update()
    for i in range(1):
        monster[i].update(current_time, frame_time, kirby)
    for i in range(2):
        monster1[i].update(current_time,frame_time, kirby)

    monster2.update(current_time, frame_time, kirby)
    boss.update(current_time, frame_time, kirby)
    coin1.update(kirby, current_time)
    coin2.update(kirby, current_time)
    coin3.update(kirby, current_time)
    coin4.update(kirby, current_time)
    for i in range(1):
        kirby.coilsion(monster[i])
    for i in range(2):
        kirby.coilsion(monster1[i])
    kirby.coilsion(monster2)
    kirby.coilsion(boss)
    delay(0.07)

def draw():
    clear_canvas()
    sky.draw()
    coin1.draw()
    coin2.draw()
    coin3.draw()
    coin4.draw()
    for i in range(1):
        monster[i].draw()
    for i in range(2):
        monster1[i].draw()
    monster2.draw()
    boss.draw()
    kirby.draw()
    update_canvas()


