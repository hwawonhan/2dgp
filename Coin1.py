from pico2d import *

class Coin1:
    global kirby

    def coilsion(self, kirby):
        for i in range(8):
            left_a, right_a, top_a, bottom_a = kirby.x - 30, kirby.x + 30, kirby.y + 30, kirby.y - 25
            left_b, right_b, top_b, bottom_b = self.position[i][0] - self.moveX - 25, self.position[i][0] - self.moveX + 25,\
                                               self.position[i][1] + 25, self.position[i][1] - 25

            if left_b < right_a and left_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    if self.position[i][2] == False:
                        self.position[i] = (self.position[i][0], self.position[i][1], True)
                        kirby.score += 10
                        kirby.coineat()
                if bottom_b < top_a and bottom_b > bottom_a:
                    if self.position[i][2] == False:
                        self.position[i] = (self.position[i][0], self.position[i][1], True)
                        kirby.score += 10
                        kirby.coineat()

            elif right_b < right_a and right_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    if self.position[i][2] == False:
                        self.position[i] = (self.position[i][0], self.position[i][1], True)
                        kirby.score += 10
                        kirby.coineat()

                if bottom_b < top_a and bottom_b > bottom_a:
                    if self.position[i][2] == False:
                        self.position[i] = (self.position[i][0], self.position[i][1], True)
                        kirby.score += 10
                        kirby.coineat()



    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((800 + (i * 50), 300 + (50 * i), False))
            else:
                self.position.append((800 + (i * 50), self.position[3][1] - (50 * (i-4)), False))
        self.moveX = 0
        self.image = load_image('./image/coin_1.png')
        self.imagex = 0
    def update(self, kirby, current_time):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
        self.coilsion(kirby)
        if self.position[0][0] - self.moveX < -790 and current_time < 40:
            self.moveX = 0
            for i in range(8):
                if i < 4:
                    self.position[i] = ((800 + (i * 50), 300 + (50 * i), False))
                else:
                    self.position[i] = ((800 + (i * 50), self.position[3][1] - (50 * (i - 4)), False))

    def draw(self):
        for i in range(8):
            if self.position[i][2] == False:
                self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])