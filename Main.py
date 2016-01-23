import pygame
import sys

pygame.init()

# Parameters
window_size = (720, 640)
# Paddle
paddle_color = (0, 128, 255)
paddle_size = [80, 10]
x_pos_paddle = 310
y_pos_paddle = 620
# Ball
ball_color = (255, 0, 0)
ball_size = 14
x_pos_ball = 100
y_pos_ball = 100
vx_ball = 1
vy_ball = 1

done = False

clock = pygame.time.Clock()

screen = pygame.display.set_mode(window_size)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: x_pos_paddle -= 3
    if pressed[pygame.K_RIGHT]: x_pos_paddle += 3

    screen.fill((0, 0, 0))

    if (x_pos_ball <= 8) or (x_pos_ball >= window_size[0]-8):
        vx_ball = -vx_ball
    if (y_pos_ball <= 8) or (y_pos_ball >= window_size[1]-8):
        vy_ball = -vy_ball

    x_pos_ball += vx_ball
    y_pos_ball += vy_ball

    pygame.draw.rect(screen, paddle_color, pygame.Rect(x_pos_paddle, y_pos_paddle, paddle_size[0], paddle_size[1]))
    pygame.draw.circle(screen, ball_color, (x_pos_ball, y_pos_ball), ball_size)
    pygame.display.flip()
    clock.tick(60)

