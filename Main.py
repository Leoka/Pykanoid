import pygame
from Ball import Ball

pygame.init()

# Parameters
window_size = (720, 640)
# Paddle
paddle_color = (0, 128, 255)
paddle_size = [80, 10]
x_pos_paddle = 310
y_pos_paddle = 620

done = False

clock = pygame.time.Clock()
ball = Ball()
print(ball.x_pos_ball)
screen = pygame.display.set_mode(window_size)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: x_pos_paddle -= 3
    if pressed[pygame.K_RIGHT]: x_pos_paddle += 3

    screen.fill((0, 0, 0))

    if (ball.x_pos_ball <= 20) or (ball.x_pos_ball >= window_size[0]-20):
        ball.vx_ball = -ball.vx_ball
    if (ball.y_pos_ball <= 20) or (ball.y_pos_ball >= window_size[1]-20):
        ball.vy_ball = -ball.vy_ball

    ball.move()

    pygame.draw.rect(screen, paddle_color, pygame.Rect(x_pos_paddle, y_pos_paddle, paddle_size[0], paddle_size[1]))
    pygame.draw.circle(screen, ball.ball_color, (ball.x_pos_ball, ball.y_pos_ball), ball.ball_size)
    pygame.display.flip()
    clock.tick(60)

