from pico2d import*


class Coin4:

    def coilsion(self,kirby):
        for i in range(22):
            left_a, right_a, top_a, bottom_a = kirby.x - 30, kirby.x + 30, kirby.y + 30, kirby.y - 25
            left_b, right_b, top_b, bottom_b = self.position[i][0] - self.moveX - 25, self.position[i][
                0] - self.moveX + 25, \
                                               self.position[i][1] + 25, self.position[i][1] - 25

            if left_b < right_a and left_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
            elif right_b < right_a and right_b > left_a:
                if top_b < top_a and top_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)
                if bottom_b < top_a and bottom_b > bottom_a:
                    self.position[i] = (self.position[i][0], self.position[i][1], True)

    def __init__(self):
        self.position = []
        for i in range(8):
            if i < 4:
                self.position.append((2000 + (i * 50), 300 + (50 * i), False))
                self.position.append((2000 + (i * 50), 300 - (50 * i), False))
            else:
                self.position.append((2000 + (i * 50), 500 - (50 * (i - 3)), False))
                self.position.append((2000 + (i * 50), 100 + (50 * (i - 3)), False))
            if i != 0 and i != 7:
                self.position.append((2000 + (i * 50), 300, False))

        self.moveX = 0
        self.image = load_image('image//coin_1.png')
        self.imagex = 0
    def update(self, kirby, current_time):
        self.moveX += 10
        self.imagex = (self.imagex + 1) % 7
        self.coilsion(kirby)
        if self.position[0][0] - self.moveX < -790 and current_time < 40:
            self.moveX = 0
            j = 0
            for i in range(8):
                if i < 4:
                    self.position[i + j] = ((800 + (i * 50), 300 + (50 * i), False))
                    j = j + 1
                    self.position[i + j] = ((800 + (j * 50), 300 - (50 * j), False))
                else:
                    self.position[i + j] = ((800 + (i * 50), 500 - (50 * (i - 3)), False))
                    j = j + 1
                    self.position[i + j] = ((800 + (j * 50), 100 + (50 * (j - 3)), False))
            for i in range(8):
                if i != 0 and i != 7:
                    self.position[i + 14] = (800 + (i * 50), 300, False)
            self.position[7] = (self.position[7][0], self.position[7][1] + 50, False)

    def draw(self):
        for i in range(22):
            if self.position[i][2] == False:
                self.image.clip_draw((self.imagex * 50), 0, 50, 50, self.position[i][0] - self.moveX, self.position[i][1])
