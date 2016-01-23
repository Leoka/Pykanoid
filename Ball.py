class Ball:

    def __init__(self):
        self.ball_color = (255, 0, 0)
        self.ball_size = 20
        self.x_pos_ball = 100
        self.y_pos_ball = 100
        self.vx_ball = 3
        self.vy_ball = 3

    def move(self):
        self.x_pos_ball += self.vx_ball
        self.y_pos_ball += self.vy_ball