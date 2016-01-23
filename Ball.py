class Ball:

    def __init__(self):
        self.color = (255, 0, 0)
        self.size = 20
        self.x_pos = 100
        self.y_pos = 100
        self.vx = 3
        self.vy = 3

    def move(self):
        self.x_pos += self.vx
        self.y_pos += self.vy