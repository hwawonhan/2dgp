import game_framework
import main_state
import ranking_state
from pico2d import *


name = "TitleState"
image = None
imagestart = None
imagestarty = 0
imagerank = None
imageranky = 1
bgm = None
def enter():
    global image, imagestart, imagerank, bgm
    image = load_image('./image/title_.png')
    imagestart = load_image('./image/Start.png')
    imagerank = load_image('./image/Exit.png')
    bgm = load_music('./image/bgm.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
def exit():
    global image, bgm
    del(image)
    del(bgm)

def handle_events():
    global imagestarty, imageranky
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                imagestarty = 0
                imageranky = 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                imagestarty = 1
                imageranky = 0
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if imagestarty == 0:
                    game_framework.change_state(main_state)
                if imageranky == 0:
                    game_framework.change_state(ranking_state)




def draw():
    clear_canvas()
    image.draw(400, 300)
    imagestart.clip_draw(0, 100 * imagestarty, 200, 100, 250, 100)
    imagerank.clip_draw(0, 100 * imageranky, 200, 100, 550, 100)
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass






