import game_framework
from pico2d import *
import json

import main_state
import title_state

name = "Rankingstate"
image = None
font = None
def enter():
    global image, font
    image = load_image('image//Rank.png')
    font = load_font('ENCR10B.TTF', 40)

def exit():
    global image, font
    del(image)
    del(font)

def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)



def bubble_sort(data):
    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            if data[i]['Time'] < data[j]['Time']:
                data[i], data[j] = data[j], data[i]

def update(frame_time):
    pass

def draw_ranking():
    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)
    score_data = score_data[:10]

    font.draw(300, 550, '[RANKING]', (255, 255, 255))
    y = 0
    for score in score_data:
        font.draw(70, 450 - 40 * y,
                  'Time:%4.1f, X:%3d, Y:%3d' %
                  (score['Time'], score['X'], score['Y']),
                  (255, 255, 255))
        y += 1


def draw(frame_time):
    global image, font
    clear_canvas()
    image.draw(400, 300)
    draw_ranking()
    update_canvas()



