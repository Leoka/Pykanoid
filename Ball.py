class Ball:

    def __init__(self):
        self.color = (255, 0, 0)
        self.size = 15
        self.x_pos = 100
        self.y_pos = 100
        self.vx = 5
        self.vy = 5

    def move(self):
        self.x_pos += self.vx
        self.y_pos += self.vy