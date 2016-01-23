import pygame
from Ball import Ball
from Paddle import Paddle

pygame.init()

# Parameters
window_size = (720, 640)

done = False

clock = pygame.time.Clock()
ball = Ball()
paddle = Paddle()
screen = pygame.display.set_mode(window_size)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if (pressed[pygame.K_LEFT]) and (paddle.x_pos >= 0):
        paddle.x_pos -= 3
    if (pressed[pygame.K_RIGHT]) and (paddle.x_pos <= window_size[1]):
        paddle.x_pos += 3

    screen.fill((0, 0, 0))

    if (ball.x_pos <= ball.size) or (ball.x_pos >= window_size[0] - ball.size):
        ball.vx = -ball.vx
    if (ball.y_pos <= ball.size) or (ball.y_pos >= window_size[1] - ball.size):
        ball.vy = -ball.vy
    if (ball.y_pos + ball.size >= paddle.y_pos) and ((ball.x_pos >= paddle.x_pos) and (ball.x_pos <= paddle.x_pos + paddle.size[0])):
        ball.vy = -ball.vy

    ball.move()

    pygame.draw.rect(screen, paddle.color, pygame.Rect(paddle.x_pos, paddle.y_pos, paddle.size[0], paddle.size[1]))
    pygame.draw.circle(screen, ball.color, (ball.x_pos, ball.y_pos), ball.size)
    pygame.display.flip()
    clock.tick(60)
